"""Check built routes, links, metadata, preview policy, schemas and CSP together."""
import argparse
import base64
import hashlib
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
from xml.etree import ElementTree as ET


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.meta, self.canonical, self.links, self.ids = {}, [], [], set()
        self.h1, self.titles, self.text, self.scripts = 0, [], [], []
        self.in_title = self.in_schema = False
        self.schema = ''
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get('id'):
            self.ids.add(a['id'])
        if tag == 'meta':
            self.meta[a.get('name', a.get('property'))] = a.get('content', '')
        if tag == 'link' and a.get('rel') == 'canonical':
            self.canonical.append(a['href'])
        for attr in ('href', 'src'):
            if a.get(attr):
                self.links.append(a[attr])
        if tag == 'h1':
            self.h1 += 1
        self.in_title = self.in_title or tag == 'title'
        if tag == 'script' and a.get('type') == 'application/ld+json':
            self.in_schema, self.schema = True, ''

    def handle_data(self, data):
        self.text.append(data)
        if self.in_title:
            self.titles.append(data)
        if self.in_schema:
            self.schema += data

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
        if tag == 'script' and self.in_schema:
            self.scripts.append(self.schema)
            self.in_schema = False


parser = argparse.ArgumentParser()
parser.add_argument('--dist', type=Path, default=Path(__file__).resolve().parent.parent / 'dist')
parser.add_argument('--indexable', action='store_true')
args = parser.parse_args()
root = args.dist
parsed = {p.relative_to(root).as_posix(): Page(p.read_text()) for p in root.rglob('*.html')}
expected_pages = {
    'index.html', 'privacy.html', '404.html', 'areas/index.html', 'your-visit/index.html',
    'treatments/index.html', 'treatments/nails/index.html', 'treatments/lashes-brows/index.html',
    'treatments/facials/index.html', 'treatments/skin-consultation/index.html',
}
assert set(parsed) == expected_pages, ('Unexpected website routes', set(parsed) ^ expected_pages)
headers = (root / '.htaccess').read_text()
titles, canonicals = set(), set()
for name, page in parsed.items():
    assert page.h1 == 1, (name, 'Expected exactly one H1')
    title = ''.join(page.titles)
    assert title and title not in titles, (name, 'Missing/duplicate title')
    titles.add(title)
    assert page.meta.get('description'), (name, 'Missing description')
    if name != '404.html':
        assert len(page.canonical) == 1 and page.canonical[0] not in canonicals, (name, 'Invalid canonical')
        canonicals.add(page.canonical[0])
    robots = 'index, follow' if args.indexable and name != '404.html' else 'noindex, follow'
    assert page.meta['robots'] == robots, (name, 'Indexing gate failed')
    excluded = r'botox|botulinum|\bb12\b|inject(?:ion|able)|skin[- ]boosters?|dermal[- ]fillers?'
    assert not re.search(excluded, (root / name).read_text(), re.I), (name, 'Excluded treatment')
    for link in page.links:
        u = urlsplit(link)
        if u.scheme or u.netloc:
            assert u.scheme in ('https', 'mailto', 'tel'), (name, 'Non-HTTPS link', link)
            continue
        destination = unquote(u.path.lstrip('/'))
        if not destination:
            destination = name if not u.path else 'index.html'
        elif u.path.endswith('/'):
            destination += 'index.html'
        assert (root / destination).is_file(), (name, 'Broken internal link', link)
        if u.fragment:
            assert destination in parsed and u.fragment in parsed[destination].ids, (name, 'Missing anchor', link)
    for script in page.scripts:
        data = json.loads(script)
        digest = base64.b64encode(hashlib.sha256(script.encode()).digest()).decode()
        assert "'sha256-" + digest + "'" in headers, (name, 'JSON-LD blocked by CSP')
        assert data['@context'] == 'https://schema.org'
        visible = ' '.join(page.text)
        for node in data['@graph']:
            if node['@type'] == 'FAQPage':
                for faq in node['mainEntity']:
                    assert faq['name'] in visible and faq['acceptedAnswer']['text'] in visible, (name, 'Schema/visible FAQ mismatch')
    assert '__' not in (root / name).read_text(), (name, 'Template token remains')
sitemap = ET.fromstring((root / 'sitemap.xml').read_text())
urls = [n.text for n in sitemap.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
expected = {c for c in canonicals if not c.endswith('/404.html')} if args.indexable else set()
assert set(urls) == expected, 'Sitemap/indexability mismatch'
assert ('Sitemap:' in (root / 'robots.txt').read_text()) == args.indexable
llms = (root / 'llms.txt').read_text()
for canonical in canonicals:
    if not canonical.endswith('/404.html'):
        assert canonical in llms, ('Missing llms.txt page', canonical)
assert 'Klarna' in (root / 'your-visit/index.html').read_text()
assert not re.search(excluded, llms, re.I), 'Excluded treatment in AI summary'
svg = ET.fromstring((root / 'assets/images/angels-logo-gold.svg').read_text())
assert svg.attrib['viewBox'] == '0 0 1000 330'
assert not svg.findall('.//{http://www.w3.org/2000/svg}image')
print(f'PASS: {len(parsed)} routes; metadata, internal links/anchors, schemas/CSP, SVG, payment copy and indexing policy.')
