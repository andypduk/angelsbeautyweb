# Angels website — published handoff

18 November 2026. [Live temporary website](https://cheerful-lightsalmon-kudu-31.hostingersite.com/).

## Delivered scope

The original Figma website was implemented as static HTML, CSS and a small navigation script. Andy then requested a luxury editorial rework for the upmarket Surrey location. The final site has a facial-led hero, oversized serif typography, restrained gold accents, alternating treatment stories, a private-salon introduction and a quieter booking section. This website iteration develops the initial Figma composition; the original Figma file remains the earlier design reference.

The standard scope would have refined the original equal-card layout. Andy explicitly selected the Million Dollar direction: more deliberate editorial composition and service storytelling. This is an art-direction ambition, not a claim of revenue, celebrity clients or measured conversion improvement.

The gold identity, supplied salon interior and selected Dominique Rivas photograph remain. The approved Figma logo refinement now replaces the original raster logo. Full-face Instagram photography is excluded. The three gallery tiles show nail work and close-up lash/brow details, with links to their original posts. The old public `assets/images/lashes.webp` URL returns 404.

## Deployment

Hostinger MCP `hosting_deploy`, type `static`, deployed the built `dist/` directory to the exact requested domain. The connector reported `status: deployed`; HTTPS requests and browser inspection verified the new content. No distinct deployment identifier was returned for this static deploy.

The destination initially contained only Hostinger's `default.php` Coming soon page. Its rendered HTML was saved locally at `output/hostinger-before.html`. No provider restore point or automatic rollback is claimed. `.hostinger/site.json` records the site target for future updates. No DNS, account, billing or email settings were changed.

This handoff records manual Hostinger deployments. Consult the Git history for source-control publication; no automatic deployment is configured.

### Approved logo, treatments and local discovery update

Published through Hostinger MCP `hosting_deploy` on 18 November 2026 to the same temporary domain, type `static`, with status `deployed`. The 620,899-byte export contains 33 files including `.htaccess`. No separate deployment identifier was returned. It adds the approved SVG logo, nine treatment/consultation/visit/area pages, Klarna information, crawlable local content, linked entity/service/breadcrumb/FAQ data and an updated llms.txt. Details and sources: [SEO and content review](SEO-AND-CONTENT.md).

Andy confirmed that indexing must wait for a permanent domain. All twelve HTML routes remain noindex. Hostinger serves its own temporary-domain robots.txt that additionally disallows Googlebot; this differs from the exported robots.txt and must be rechecked on the permanent domain. No cache purge, crawler-unblocking or DNS change was performed.

Thirty-one public paths were downloaded over validated HTTPS and matched the built files byte-for-byte. The twelfth HTML page is the real 404 document; unknown URLs, the removed full-face image and the obsolete raster-logo URL all return HTTP 404. Every page's JSON-LD hash matches the public CSP header; SVG MIME type is correct. Evidence: `output/live-seo-verified/verification.json`. The previous live homepage matched the locally saved complete export at `output/before-logo-release/`, which can be redeployed manually if needed; no provider restore point is claimed.

All eleven normal pages were checked in the live browser at 390 and 1440 px: new logos load, no page-wide horizontal overflow, and noindex is present. Local shared-template checks also passed at 320, 768 and 1024 px. The area directory's match, empty and reset states and mobile-menu Escape/focus behaviour were exercised. Consultation-page Lighthouse accessibility/best-practices scores are 100/100; SEO is 69 because indexing is intentionally disabled. Real-device, VoiceOver, separate Safari/Firefox and actual zoom checks remain pending.

Final live performance: Node 26.13.1, Lighthouse 13.5.0, Headless Chrome 158; three cold navigations per route/profile, no warnings, no budget overrides. All six groups pass. Per-metric medians:

| Route | Profile | LCP ms | CLS | TBT ms | Transfer bytes |
| --- | --- | ---: | ---: | ---: | ---: |
| Homepage | Mobile | 1,361 | 0 | 0 | 277,622 |
| Homepage | Desktop | 330 | 0 | 0 | 435,059 |
| Facial treatment | Mobile | 1,385 | 0 | 0 | 118,359 |
| Facial treatment | Desktop | 347 | 0 | 0 | 118,132 |
| Nearby-area directory | Mobile | 1,221 | 0 | 0 | 93,790 |
| Nearby-area directory | Desktop | 296 | 0 | 0 | 93,801 |

One homepage desktop run measured CLS 0.000251; the other seventeen runs measured zero. Performance scores were 100 except that desktop run at 99. Individual values, spreads and settings are in `output/audit-seo-live/`. These are lab navigations, not field Core Web Vitals or INP. The initial local homepage exceeded the LCP budget at 2,627 ms; a 26 KB responsive hero image and route-specific detail stylesheet reduced the final local median to 2,102 ms before publication. Final desktop/mobile live screenshots are saved as `output/website-updated-desktop.jpg` and `output/website-updated-mobile.jpg`.

## Functional and responsive evidence

| Area | Result |
| --- | --- |
| Main journey | Verified: Booksy links navigate to the actual Angels Clinic & Beauty listing in Guildford. No real appointment was created. |
| Gallery | Verified: three local images and their exact source-post URLs. Images load independently of an Instagram sign-in or API connection. No automatic feed refresh is configured. |
| Mobile navigation | Verified: open/close, expanded state, Escape, focus return and anchor navigation. The initial mobile navigation layout shift was fixed; fingerprinted CSS/JS prevents stale files after redeploys. |
| Homepage reflow | Verified in the in-app browser at 320, 390, 768, 1024 and 1440 CSS px, with no page-wide horizontal overflow. The final public site was checked at 390 and 1440 px. |
| Supporting routes | Verified: privacy page at mobile/desktop and 320 px reflow; real HTTP 404 response with a useful recovery page; public llms.txt, robots.txt and sitemap.xml return correct content types. |
| Browser errors | No website console errors or warnings observed in the in-app browser. |
| Accessibility | Local Lighthouse 13.5.0 accessibility and best-practices categories scored 100. Visible labels/accessible names were corrected; body text and tiny secondary text were enlarged. The initial tiny-text warning was fixed. Subsequent Stop-hook findings were reviewed and narrowly scoped design exceptions were recorded as described below. Manual keyboard/menu checks passed. This is not a WCAG conformance claim. |
| Missing coverage | Physical devices, VoiceOver, dedicated Safari/Firefox checks, 200% text enlargement and an actual 400% browser zoom remain unverified. The 320 px reflow sample does not replace these checks. |

## Performance evidence

Node 26.13.1, Lighthouse 13.5.0, Headless Chrome 158. Each result below is the per-metric median of three cold navigations on the actual built site. No budget overrides. No Lighthouse run warnings in the final live audit. TBT is a lab diagnostic, not field INP.

| Build/profile | LCP | CLS | TBT | Transfer | Budgets |
| --- | --- | --- | --- | --- | --- |
| Final local, mobile | 2,403 ms | 0 | 0 ms | 285,230 B | Passed |
| Final local, desktop | 542 ms | 0 | 0 ms | 442,227 B | Passed |
| Final live, mobile | 1,810 ms | 0 | 0 ms | 267,696 B | Passed |
| Final live, desktop | 410 ms | 0 | 0 ms | 425,180 B | Passed |

Raw reports retain individual run values, range, settings and timing evidence in `output/audit-luxury-local/` and `output/audit-luxury-live/`. The initial live audit of the first layout detected a mobile CLS failure caused by navigation collapsing after first paint. The final audit passes after that correction and the subsequent redesign. Earlier reports are retained as diagnostic history, not final evidence.

The final export is approximately 470 KB across all public files; local font payload is about 59 KB and the navigation script about 1.6 KB before compression. There are no npm runtime dependencies, third-party embeds, analytics requests or background videos. Individual image files are under 160 KB. Field Core Web Vitals and real-user performance are not measured.

Live Lighthouse screenshots are saved as `output/website-desktop.jpg` and `output/website-mobile.jpg`.

## Marketing, discovery and privacy

The audience is local clients considering personal beauty appointments. The page explains the one-to-one garden-salon experience, treatment categories and booking destination. Prices, available appointments, terms and confirmation remain on Booksy. There are no invented testimonials, qualifications, celebrity associations, scarcity messages or discounts.

Unique page metadata, canonical URLs, social metadata, factual BeautySalon JSON-LD and llms.txt are included. The temporary domain's HTML deliberately carries `noindex, follow`; its sitemap contains no indexable URLs. The Lighthouse SEO score is therefore reduced by the intentional crawlability exclusion. Enabling indexing on a final domain is an explicit build option, not an indexing submission or a ranking guarantee.

No tracking, newsletter, enquiry form, customer account, cookies or browser storage was added. The privacy page explains local images/fonts, outbound Booksy/Instagram links and hosting logs. Public headers include CSP, nosniff, referrer and permissions policies. The JSON-LD script is allowed by its exact CSP hash. Only `dist/` was deployed; no source, Git metadata, reports or credentials were uploaded.

## Million Dollar design validation

| Category | Status and observation |
| --- | --- |
| Animations | Verified: restrained image/link hover effects; reduced-motion rules disable transitions. Content does not wait for animation. |
| Images | Verified: authentic nail/brow work, supplied interior/logo and explicitly illustrative licensed stock. No full-face Instagram asset in the export. Provenance is recorded in `docs/ASSETS.md`. |
| Copy | Verified: specific services, personal care and a clear Booksy action. No fabricated celebrity proof or prohibited buzzwords. |
| Layout | Verified: asymmetric service narratives, gallery rhythm, generous space, meaningful mobile reading order and five-width reflow checks. |
| Performance | Verified: final local and live mobile/desktop lab budgets pass; field performance remains unmeasured. |
| Typography | Verified: local Cormorant Garamond and DM Sans, responsive scale, contrast checked by automated accessibility audit. |
| Interactions | Verified: Booksy destination, menu keyboard/focus behaviour, source-post links, privacy route and real 404. No fake booking success state. |

Future work: an owner-authorised Instagram integration is needed only if automatic gallery refresh is desired. Confirm the final public domain before enabling indexing. A Booksy click is not tracked as a confirmed booking, and no campaign or audience measurement has been activated.


## Stop-hook triage

Reviewed all 16 findings after publication: three uppercase-label warnings, four padding warnings, six section-label warnings and three palette warnings. No new UI defect was verified, so no further visual change or redeployment was made.

- Uppercase matches are short masthead/location/section labels; paragraph copy remains sentence case.
- Panel spacing is provided by 64–112px section padding and nested 24–96px horizontal gutters. The footer’s inherited top border is explicitly removed in the theme. The detector did not resolve those relationships.
- Section labels and the ivory/aubergine palette are deliberate parts of the established Figma-led brand, including the supplied gold logo.

Exceptions were persisted through `impeccable hooks ignore-value` in `.impeccable/config.json`, limited to the affected rules and the three named HTML files. No whole-file or project-wide rule suppression was used. The confirmation detector pass returned no remaining findings. Unrelated UI and the live site were unchanged.
