# Angels Clinic & Beauty

Website project for Angels Clinic & Beauty.

## Website

The local champagne rebrand uses the previously approved gold ANGELS wordmark, botanical artwork from Macy’s campaign and opening hours from her supplied hours card. The website features nails, brows, lashes and facials, Booksy bookings and a curated three-image Instagram gallery. The editable [desktop design](https://www.figma.com/design/WKseG6Qlc8DgpR1ERlWAZB/?node-id=51-64) and [mobile design](https://www.figma.com/design/WKseG6Qlc8DgpR1ERlWAZB/?node-id=51-65) share the original gold logo component. The treatment exclusions apply to the static website and its search metadata. Booksy manages its own catalogue.

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
- Font files are self-hosted with their OFL license texts. The approved logo refinement is a transparent outlined SVG exported from editable Figma artwork.
- Dedicated treatment, visit/payment and nearby-area pages provide crawlable HTML and linked structured data. [SEO and treatment coverage](docs/SEO-AND-CONTENT.md) records the Botox/B12 guidance, Klarna wording, ten-mile place data and permanent-domain indexing gate.

## Publishing

`npm run build` produces the temporary preview export with `noindex`. To prepare a future approved, indexable release on a final domain:

```sh
python3 scripts/build.py --site https://YOUR-CONFIRMED-DOMAIN --indexable
```

This changes only local output; it does not publish or submit a sitemap. The default temporary preview sitemap intentionally has no indexable URLs. Retain noindex until the final domain and public content are approved.

Run `python3 scripts/check_site.py` after building to verify routes, metadata, links, structured-data hashes and indexing policy. Temporary Hostinger domains cannot be built with `--indexable`.

See [verification and deployment notes](docs/WEBSITE-HANDOFF.md) for actual checks, audit evidence and remaining limitations.

## Repository

[andypduk/angelsbeautyweb](https://github.com/andypduk/angelsbeautyweb)
