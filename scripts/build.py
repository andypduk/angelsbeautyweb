"""Build the static site. Preview is noindex; public indexing is an explicit opt-in."""
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

parser = argparse.ArgumentParser()
parser.add_argument('--site', default=DEFAULT_SITE)
parser.add_argument('--indexable', action='store_true', help='Enable public indexing after approval of final content/domain.')
args = parser.parse_args()
parts = urlsplit(args.site)
if parts.scheme != 'https' or not parts.hostname or parts.path not in ('', '/') or parts.query or parts.fragment or parts.username:
    parser.error('--site must be an HTTPS origin without a path, credentials, query or fragment')
site = args.site.rstrip('/')
if DIST.exists():
    shutil.rmtree(DIST)
DIST.mkdir()
shutil.copytree(SRC / 'assets', DIST / 'assets')
asset_urls = {}
for filename in ('styles.css', 'luxury.css', 'no-js.css', 'site.js'):
    data = (SRC / filename).read_bytes()
    digest = hashlib.sha256(data).hexdigest()[:10]
    path = Path(filename)
    output_name = f'{path.stem}.{digest}{path.suffix}'
    (DIST / output_name).write_bytes(data)
    asset_urls['/' + filename] = '/' + output_name
shutil.copyfile(SRC / '.htaccess', DIST / '.htaccess')

def gallery_markup():
    entries = json.loads((SRC / 'gallery.json').read_text())
    result = []
    for item in entries:
        if not re.fullmatch(r'[\w-]+', item['image']) or not re.fullmatch(r'[\w-]+', item['post']):
            raise ValueError('Invalid gallery entry')
        result.append(f'''<a class="gallery-item" href="{INSTAGRAM}p/{item['post']}/" target="_blank" rel="noopener noreferrer" aria-label="{html.escape(item['alt'])} — view post on Instagram (opens in a new tab)">
          <img src="/assets/images/{item['image']}.webp" width="480" height="640" alt="{html.escape(item['alt'])}" loading="lazy" decoding="async">
          <span class="gallery-overlay" aria-hidden="true">View on Instagram ↗</span>
        </a>''')
    return '\n'.join(result)

schema = {
    '@context': 'https://schema.org', '@type': 'BeautySalon',
    'name': 'Angels Clinic & Beauty', 'url': site + '/',
    'description': 'A private garden salon in West Clandon, Surrey, offering one-to-one nail, lash, brow and beauty appointments.',
    'image': site + '/assets/images/salon.webp',
    'address': {'@type': 'PostalAddress', 'addressLocality': 'West Clandon, Guildford', 'addressRegion': 'Surrey', 'addressCountry': 'GB'},
    'sameAs': [INSTAGRAM, BOOKSY],
    'potentialAction': {'@type': 'ReserveAction', 'target': BOOKSY}
}
schema_text = json.dumps(schema, ensure_ascii=False)
csp_hash = base64.b64encode(hashlib.sha256(schema_text.encode()).digest()).decode()
headers = (DIST / '.htaccess').read_text().replace("script-src 'self'", "script-src 'self' 'sha256-" + csp_hash + "'")
(DIST / '.htaccess').write_text(headers)
for filename in ('index.html', 'privacy.html', '404.html'):
    page = (SRC / filename).read_text()
    path = '/' if filename == 'index.html' else '/' + filename
    page = page.replace('__SITE__', site).replace('__CANONICAL__', site + path)
    page = page.replace('__ROBOTS__', 'index, follow' if args.indexable and filename != '404.html' else 'noindex, follow')
    page = page.replace('__GALLERY__', gallery_markup()).replace('__SCHEMA__', schema_text)
    for old, new in asset_urls.items():
        page = page.replace(old, new)
    if '__' in page:
        raise ValueError('Unresolved template token in ' + filename)
    (DIST / filename).write_text(page)
(DIST / 'robots.txt').write_text('User-agent: *\nAllow: /\n' + (f'Sitemap: {site}/sitemap.xml\n' if args.indexable else '# Temporary preview: HTML pages carry noindex.\n'))
urls = ['/', '/privacy.html'] if args.indexable else []
(DIST / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(f'<url><loc>{html.escape(site + p)}</loc></url>' for p in urls) + '</urlset>\n')
(DIST / 'llms.txt').write_text(f'''# Angels Clinic & Beauty

> A private garden salon in West Clandon, Guildford, Surrey. One-to-one appointments for nails, lashes, brows and beauty treatments.

This is a temporary website preview. Current treatments, prices, availability, booking conditions and confirmations are provided by Booksy. Instagram imagery on this site is a curated selection, not a live feed.

## Pages
- [Homepage]({site}/): Treatments, salon setting, selected work and booking links.
- [Privacy]({site}/privacy.html): Website privacy and third-party links.

## Official profiles
- [Book on Booksy]({BOOKSY}): Current services and appointment booking.
- [Instagram]({INSTAGRAM}): Angels' photographs and updates.
''')
print(f'Built {DIST} for {site} — indexing {"enabled" if args.indexable else "disabled"}.')
