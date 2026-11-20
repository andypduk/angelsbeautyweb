"""Build static pages; indexing requires an approved permanent-domain release."""
import argparse
import base64
import hashlib
import html
import json
import re
import shutil
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent.parent
SRC, DIST = ROOT / 'src', ROOT / 'dist'
BOOKSY = 'https://angels9.booksy.com/a/'
INSTAGRAM = 'https://www.instagram.com/angels.surrey/'
DEFAULT_SITE = 'https://cheerful-lightsalmon-kudu-31.hostingersite.com'
e = html.escape
parser = argparse.ArgumentParser()
parser.add_argument('--site', default=DEFAULT_SITE)
parser.add_argument('--indexable', action='store_true', help='Enable indexing after permanent-domain approval.')
args = parser.parse_args()
parts = urlsplit(args.site)
if parts.scheme != 'https' or not parts.hostname or parts.path not in ('', '/') or parts.query or parts.fragment or parts.username:
    parser.error('--site must be an HTTPS origin without a path, credentials, query or fragment')
if args.indexable and parts.hostname.endswith('.hostingersite.com'):
    parser.error('Temporary Hostinger previews must stay noindex. Confirm a permanent domain first.')
site = args.site.rstrip('/')
pages = json.loads((SRC / 'pages.json').read_text())
areas = json.loads((SRC / 'areas.json').read_text())
paths = [p['path'] for p in pages]
if len(paths) != len(set(paths)) or any(not re.fullmatch(r'/(?:[a-z0-9-]+/)+', p) for p in paths):
    raise ValueError('Page paths must be unique, slash-terminated local paths')
if DIST.exists():
    shutil.rmtree(DIST)
DIST.mkdir()
shutil.copytree(SRC / 'assets', DIST / 'assets')
asset_urls = {}
for filename in ('styles.css', 'luxury.css', 'pages.css', 'no-js.css', 'site.js'):
    data = (SRC / filename).read_bytes()
    digest = hashlib.sha256(data).hexdigest()[:10]
    path = Path(filename)
    output_name = f'{path.stem}.{digest}{path.suffix}'
    (DIST / output_name).write_bytes(data)
    asset_urls['/' + filename] = '/' + output_name


def gallery_markup():
    result = []
    for item in json.loads((SRC / 'gallery.json').read_text()):
        if not re.fullmatch(r'[\w-]+', item['image']) or not re.fullmatch(r'[\w-]+', item['post']):
            raise ValueError('Invalid gallery entry')
        result.append(f'<a class="gallery-item" href="{INSTAGRAM}p/{item["post"]}/" target="_blank" rel="noopener noreferrer" aria-label="{e(item["alt"])} — view post on Instagram (opens in a new tab)"><img src="/assets/images/{item["image"]}.webp" width="480" height="640" alt="{e(item["alt"])}" loading="lazy" decoding="async"><span class="gallery-overlay" aria-hidden="true">View on Instagram ↗</span></a>')
    return '\n'.join(result)


coverage = {'@type': 'GeoCircle', 'geoMidpoint': {'@type': 'GeoCoordinates', 'latitude': areas['centre']['latitude'], 'longitude': areas['centre']['longitude']}, 'geoRadius': 16093.44}
business = {
    '@type': 'BeautySalon', '@id': site + '/#salon', 'name': 'Angels Clinic & Beauty', 'url': site + '/',
    'description': 'A private garden beauty salon in West Clandon, near Guildford, Surrey. One-to-one appointments with Macy.',
    'logo': {'@type': 'ImageObject', 'url': site + '/assets/images/angels-logo-gold.svg', 'width': 1000, 'height': 330},
    'image': site + '/assets/images/salon.webp',
    'address': {'@type': 'PostalAddress', 'addressLocality': 'West Clandon', 'addressRegion': 'Surrey', 'addressCountry': 'GB'},
    'areaServed': coverage, 'sameAs': [INSTAGRAM, BOOKSY], 'potentialAction': {'@type': 'ReserveAction', 'target': BOOKSY},
    'hasOfferCatalog': {'@type': 'OfferCatalog', 'name': 'Beauty appointments', 'itemListElement': [
        {'@type': 'Offer', 'itemOffered': {'@type': 'Service', 'name': p['service_name'], 'url': site + p['path']}}
        for p in pages if p.get('service_name')
    ]}
}


def schema_for(page):
    path = page['path']
    web = {'@type': 'WebPage', '@id': site + path + '#page', 'url': site + path, 'name': page['title'], 'description': page['description'], 'inLanguage': 'en-GB', 'isPartOf': {'@id': site + '/#website'}, 'about': {'@id': site + '/#salon'}}
    graph = [business, {'@type': 'WebSite', '@id': site + '/#website', 'url': site + '/', 'name': 'Angels Clinic & Beauty', 'inLanguage': 'en-GB', 'publisher': {'@id': site + '/#salon'}}, web]
    if path != '/':
        crumbs = [{'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': site + '/'}]
        if path.startswith('/treatments/') and path != '/treatments/':
            crumbs.append({'@type': 'ListItem', 'position': 2, 'name': 'Treatments', 'item': site + '/treatments/'})
        crumbs.append({'@type': 'ListItem', 'position': len(crumbs) + 1, 'name': page['label'].split(' · ')[0], 'item': site + path})
        graph.append({'@type': 'BreadcrumbList', 'itemListElement': crumbs})
    if page.get('service_name'):
        graph.append({'@type': 'Service', '@id': site + path + '#service', 'name': page['service_name'], 'url': site + path, 'provider': {'@id': site + '/#salon'}, 'areaServed': coverage})
    if page.get('faqs'):
        web['@type'] = 'FAQPage'
        web['mainEntity'] = [{'@type': 'Question', 'name': f['q'], 'acceptedAnswer': {'@type': 'Answer', 'text': f['a']}} for f in page['faqs']]
    return json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False).replace('<', '\\u003c')


hashes = set()


def emit(text, path, schema=None):
    target = DIST / ('index.html' if path == '/' else path.lstrip('/') + ('index.html' if path.endswith('/') else ''))
    target.parent.mkdir(parents=True, exist_ok=True)
    if schema:
        text = text.replace('__SCHEMA__', schema)
        hashes.add(base64.b64encode(hashlib.sha256(schema.encode()).digest()).decode())
    text = text.replace('__SITE__', site).replace('__CANONICAL__', site + path)
    text = text.replace('__ROBOTS__', 'index, follow' if args.indexable and path != '/404.html' else 'noindex, follow')
    for old, new in asset_urls.items():
        text = text.replace(old, new)
    if '__' in text:
        raise ValueError('Unresolved template token: ' + path)
    target.write_text(text)


home = (SRC / 'index.html').read_text()
home_meta = {'path': '/', 'title': 'Beauty salon in West Clandon, near Guildford | Angels', 'description': 'BIAB nails, lash lifts, brows and facials at Angels, a private beauty salon in West Clandon, near Guildford, Surrey.'}
hours = (SRC / 'hours.html').read_text().strip()
emit(home.replace('__GALLERY__', gallery_markup()).replace('__HOURS__', hours), '/', schema_for(home_meta))
header = re.search(r'<header\b.*?</header>', home, re.S).group(0)
header = re.sub(r'href="#([^"]+)"', r'href="/#\1"', header)
footer = re.search(r'<footer\b.*?</footer>', home, re.S).group(0)
template = (SRC / 'page.html').read_text()


def directory():
    services = [p for p in pages if p.get('service_name')]
    return '<nav class="service-directory" aria-label="Treatment pages">' + ''.join(f'<a href="{p["path"]}"><span class="service-number" aria-hidden="true">0{i}</span><span><h2>{e(p["label"].split(" · ")[0])}</h2><p>{e(p.get("directory_summary", p["service_name"]))}</p></span><span aria-hidden="true">↗</span></a>' for i, p in enumerate(services, 1)) + '</nav>'


def local_directory():
    blocks = []
    for lower, upper, label in [(0, 3, 'Up to 3 miles'), (3, 6, 'Over 3 to 6 miles'), (6, 10, 'Over 6 to 10 miles')]:
        places = [p for p in areas['places'] if lower < p['miles'] <= upper or lower == 0 and p['miles'] == 0]
        rows = ''.join(f'<li data-place="{e(p["name"].lower())}"><span>{e(p["name"])}</span><span>{p["miles"]:.1f} miles</span></li>' for p in places)
        blocks.append(f'<details class="area-band"><summary>{label}<span>{len(places)} places</span></summary><ul class="area-list">{rows}</ul></details>')
    return '<section class="area-directory" aria-labelledby="areas-heading"><h2 id="areas-heading">Find your nearby town or village</h2><p>Approximate straight-line distances from West Clandon village centre. Driving routes and journey times will differ. All appointments take place at the West Clandon salon.</p><div class="area-search" hidden><label for="area-search">Find a town, village or local area</label><input type="search" id="area-search" placeholder="For example: Guildford" aria-describedby="area-count"><p id="area-count" role="status"></p></div><div class="area-bands">' + ''.join(blocks) + '</div><p class="small muted">Place coordinates: <a href="https://www.geonames.org/">GeoNames</a>, <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>. Populated-place records and selected local districts checked 18 November 2026. Distances calculated between place centres; not a promise of travel time.</p></section>'


for page in pages:
    body = ''
    for section in page['sections']:
        body += '<section class="detail-section"><h2>' + e(section['heading']) + '</h2>'
        body += ''.join('<p>' + e(p) + '</p>' for p in section.get('paragraphs', []))
        if section.get('items'):
            body += '<ul class="service-list">' + ''.join('<li>' + e(i) + '</li>' for i in section['items']) + '</ul>'
        body += '</section>'
    if page.get('kind') == 'directory':
        body += directory()
    if page.get('kind') == 'areas':
        body += local_directory()
    if page['path'] == '/your-visit/':
        body += '<section class="detail-section"><h2>Opening hours</h2>' + hours + '</section>'
    if page.get('image') == 'facial.webp':
        body += '<p class="photo-credit">Illustrative facial photograph by <a href="https://unsplash.com/photos/a-woman-getting-a-facial-massage-on-her-face-rWwuf8yKw4Y">Dominique Rivas / Unsplash</a>.</p>'
    if page['faqs']:
        body += '<section class="detail-faq"><h2>Before you book</h2>' + ''.join('<div class="faq"><h3>' + e(f['q']) + '</h3><p>' + e(f['a']) + '</p></div>' for f in page['faqs']) + '</section>'
    crumbs = '<a href="/">Home</a><span aria-hidden="true">/</span>'
    if page['path'].startswith('/treatments/') and page['path'] != '/treatments/':
        crumbs += '<a href="/treatments/">Treatments</a><span aria-hidden="true">/</span>'
    crumbs += '<span aria-current="page">' + e(page['label'].split(' · ')[0]) + '</span>'
    image = ''
    if page.get('image'):
        responsive = ' srcset="/assets/images/facial-800.webp 800w, /assets/images/facial.webp 1600w" sizes="(max-width: 639px) calc(100vw - 48px), 45vw"' if page['image'] == 'facial.webp' else ''
        width, height = (1600, 2399) if page['image'] == 'facial.webp' else (480, 640)
        image = f'<img class="detail-photo" src="/assets/images/{page["image"]}"{responsive} alt="{e(page["image_alt"])}" width="{width}" height="{height}" decoding="async">'
    label, _, location = page['label'].partition(' · ')
    hero_label = location if location and label == page['heading'] else page['label']
    values = {'TITLE': e(page['title']), 'DESCRIPTION': e(page['description']), 'HEADER': header, 'FOOTER': footer, 'BREADCRUMBS': crumbs, 'HERO_CLASS': 'with-photo' if image else '', 'LABEL': e(hero_label), 'HEADING': e(page['heading']), 'INTRO': e(page['intro']), 'BOOKING_LABEL': 'View appointments on Booksy', 'IMAGE': image, 'BODY': body}
    rendered = template
    for key, value in values.items():
        rendered = rendered.replace('__' + key + '__', value)
    emit(rendered, page['path'], schema_for(page))
for filename in ('privacy.html', '404.html'):
    emit((SRC / filename).read_text(), '/' + filename)
headers = (SRC / '.htaccess').read_text().replace("script-src 'self'", "script-src 'self' " + ' '.join("'sha256-" + h + "'" for h in sorted(hashes)))
(DIST / '.htaccess').write_text(headers)
(DIST / 'robots.txt').write_text('User-agent: *\nAllow: /\n' + (f'Sitemap: {site}/sitemap.xml\n' if args.indexable else '# Temporary preview: all HTML pages carry noindex.\n'))
urls = ['/', *paths, '/privacy.html'] if args.indexable else []
(DIST / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(f'<url><loc>{e(site + p)}</loc></url>' for p in urls) + '</urlset>\n')
links = '\n'.join(f'- [{p["label"].split(" · ")[0]}]({site}{p["path"]}): {p["description"]}' for p in pages)
(DIST / 'llms.txt').write_text(f'''# Angels Clinic & Beauty

> A private garden beauty salon in West Clandon, near Guildford, Surrey. One-to-one appointments with Macy. All visits take place at the West Clandon salon.

{'Temporary preview: public indexing is disabled until the permanent domain is confirmed.' if not args.indexable else 'Official website for Angels Clinic & Beauty.'}

Booksy holds current service descriptions, prices, availability, policies and confirmation. Klarna acceptance is advertised by the salon; arrangements and eligibility must be confirmed directly with Macy. No payment is processed here.

## Pages
- [Homepage]({site}/): Salon introduction and treatment overview.
{links}
- [Privacy]({site}/privacy.html): Website privacy and third-party links.

## Official profiles
- [Booksy]({BOOKSY}): Current appointments and booking terms.
- [Instagram]({INSTAGRAM}): The salon’s photographs and updates. Website imagery is curated, not an automatic feed.

## Local coverage
Nearby places include West and East Clandon, Guildford, Merrow, Burpham, Woking, Ripley, Send, East and West Horsley, Godalming, Cobham, Leatherhead, Dorking and Weybridge. The areas page lists approximate straight-line distances from West Clandon village centre using GeoNames records, not driving distances or branch locations.
''')
print(f'Built {len(pages) + 3} HTML pages for {site} — indexing {"enabled" if args.indexable else "disabled"}.')
