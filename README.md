# Angels Clinic & Beauty

Website project for Angels Clinic & Beauty.

## Website

The responsive website began with the approved [Figma design](https://www.figma.com/design/WKseG6Qlc8DgpR1ERlWAZB?node-id=2-350). Andy's subsequent luxury editorial rework adds a facial-led hero, alternating treatment stories and a three-image gallery. It preserves the supplied gold logo and salon interior, Booksy booking links and the ivory/aubergine palette. Full-face Instagram photographs are excluded. [Design notes and asset provenance](docs/design/README.md) record the original image sources; [current asset mapping](docs/ASSETS.md) records the website placements.

Temporary site: [cheerful-lightsalmon-kudu-31.hostingersite.com](https://cheerful-lightsalmon-kudu-31.hostingersite.com/). Public indexing remains disabled on this temporary domain.

## Local development

Requires Python 3.10+; npm is a convenience wrapper. No npm dependencies or install step.

```sh
npm run build
npm run preview
```

Open `http://127.0.0.1:4321/`. Source lives in `src/`; the build generates `dist/`. You can also run `python3 scripts/build.py` and `python3 scripts/serve.py` directly. Use `npm run preview -- --port 4322` for another local port.

The static export includes a homepage, privacy page, real 404 page, local fonts, compressed WebP images, structured data, robots.txt, sitemap.xml and llms.txt. Deploy only `dist/`, never this repository root. Hostinger reads the included `.htaccess` for headers, compression and 404 handling.

## Content and integrations

- Booking links use Angels' official `https://angels9.booksy.com/a/` link. Booksy owns prices, availability, booking terms and confirmation. No appointments are created by this site.
- Edit `src/gallery.json` to change the Instagram selection. Images are local files in `src/assets/images/`; each gallery tile links to its original post. No Instagram embed, API credentials, background refresh, analytics or tracking is installed.
- The facial image is illustrative stock by Dominique Rivas, credited on the page and in the design notes. The salon and Instagram images are supplied/original Angels material.
- Font files are self-hosted with their OFL license texts. The logo remains the original raster artwork, cropped with CSS as in Figma.

## Publishing

`npm run build` produces the temporary preview export with `noindex`. To prepare a future approved, indexable release on a final domain:

```sh
python3 scripts/build.py --site https://YOUR-CONFIRMED-DOMAIN --indexable
```

This changes only local output; it does not publish or submit a sitemap. The default temporary preview sitemap intentionally has no indexable URLs. Retain noindex until the final domain and public content are approved.

See [verification and deployment notes](docs/WEBSITE-HANDOFF.md) for actual checks, audit evidence and remaining limitations.

## Repository

[andypduk/angelsbeautyweb](https://github.com/andypduk/angelsbeautyweb)
