# Local discovery and treatment coverage

18 November 2026. Andy authorised the refined logo, treatment/Klarna coverage, local SEO and AI discovery work, and Hostinger publication. He explicitly chose to wait for a permanent domain before search indexing and approved applying the Botox/B12 advertising guidance.

## Treatment review

Sources: Andy’s latest supplied offerings artwork and the [Angels Booksy menu](https://booksy.com/en-gb/142395_angels-clinic-beauty_nail-salon_959268_west-clandon), checked 18 November 2026. Booksy remains authoritative for live prices, appointment lengths, policies and availability. Older dated offers were not copied.

| Source offering | Website coverage |
| --- | --- |
| Nails | BIAB natural nails, short BIAB extensions, full-cover extensions, rebalance/infills, gel manicure and nail art levels 1–3; soak-off with/without a new set and removal of other work. |
| Brows | Tint, wax/tint, wax, lamination package and maintenance; lip/chin waxing; combined brows/lashes package. |
| LVL/lashes | LVL from supplied artwork; lash lift/tint, Korean lift, eyelash tint and extension removal from Booksy. Clear booking-name explanation and 48-hour patch-test requirement. |
| Facials | Express Facial and Ultimate BB Glow; listed treatment components described without guaranteed outcomes. |
| Dermal fillers | Lip, nasolabial fold, cheek, chin, jaw, contour and profile-balancing options, led by consultation. No promotional before/after images or results guarantees. |
| Skin boosters | Individual appointment and course of three; suitability, product and aftercare questions before commitment. |
| Botox | All Booksy area/package variants addressed through the general consultation route. No public product-name advertising, indirect promotional euphemisms, medicine price list, medicine keywords or injection-result claims. |
| B12 | The general assessment/consultation route handles enquiries. No public promotion of the injectable medicine or energy, metabolism or wellness claims. |
| Klarna | Plain payment-method identification and a visit FAQ. Availability, eligibility and arrangements must be confirmed directly with Macy. No instalment, interest-free, universal-approval or Booksy-checkout promise. |

This is a content review, not a legal-compliance certification. The supplied promotional image is not published as a banner because it names prescription medicines and includes benefit claims. Qualifications/insurance badges, celebrity associations and review totals have not been invented or added.

The implementation follows [ASA guidance for prescription medicines on websites](https://www.asa.org.uk/advice-online/health-prescription-only-medicines-websites.html), [ASA vitamin-shot guidance](https://www.asa.org.uk/resource/enforcement-notice-advertising-vitamin-shots.html) and [NHS advice on choosing a practitioner](https://www.nhs.uk/tests-and-treatments/cosmetic-procedures/advice/choosing-who-will-do-your-procedure/). Klarna wording identifies the payment method without inviting credit, following [Klarna’s UK marketing guidance](https://d3tn1kidxl5adl.cloudfront.net/platform/shopify/resources/marketing-tools/partner-marketing-legal-guidelines/united-kingdom/). [Booksy UK payment guidance](https://help.booksy.com/hc/en-gb/articles/21619656357266-What-payment-methods-are-accepted-on-Booksy) does not establish a Klarna integration for this salon, so none is claimed.

## Page architecture

The homepage links to a treatment index, five treatment-family pages, a personal-consultation page, visit/payment information and a nearby-area directory. Each has its own title, description, canonical, social metadata, visible headings, descriptive links, business/service entities and breadcrumbs. FAQs are rendered in HTML and included in matching structured data. No separate pages target medicine names.

No cloned town-by-treatment pages were created. All services take place at the single West Clandon salon. The area directory is a practical distance lookup, not a claim of a branch or mobile treatment service in each town.

## Ten-mile coverage

`src/areas.json` records 179 populated places and selected local districts within a calculated ten-mile radius of West Clandon village centre, including Clandon, Guildford, Merrow, Burpham, Woking, the Horsleys, Ripley, Send, Cobham, Godalming, Leatherhead, Dorking and Weybridge.

Coordinates are from the [GeoNames GB extract](https://download.geonames.org/export/dump/GB.zip), downloaded 18 November 2026, under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The centre is GeoNames ID 2634469, 51.26063, -0.50323. A great-circle calculation uses Earth radius 3958.7613 miles and filters unrounded distances to at most ten miles. Display distances are rounded to one decimal place. The directory credits GeoNames and explains that distances are between place centres, not from the salon’s private address, driving distances or journey times. Two differently located Effingham records were reconciled to the village record 2650195. Data carries GeoNames’ accuracy limitations; this is approximate planning information.

## Search and AI

Important content is delivered as HTML. JSON-LD links BeautySalon, WebSite, WebPage/FAQPage, Service, OfferCatalog and BreadcrumbList entities. The business identity includes the approved SVG logo, actual social/booking profiles, locality and a ten-mile GeoCircle. Private street-address information, unverified phone numbers, ratings, credentials and opening hours are omitted. Schema syntax and visible-FAQ alignment are checked locally; rich-result eligibility is not certified.

`/llms.txt` provides a concise linked site guide and factual booking/location/payment context. This is supplemental documentation, not an AI ranking mechanism. [Google’s AI search guidance](https://developers.google.com/search/docs/appearance/ai-features) says normal SEO practices apply and no special AI schema or file is required. The site avoids [doorway pages](https://developers.google.com/search/docs/essentials/spam-policies#doorway-abuse). [OpenAI crawler guidance](https://developers.openai.com/api/docs/bots) distinguishes search crawling from training. Existing wildcard crawler permissions are preserved; no additional training opt-in is introduced.

## Permanent-domain release gate

The actual Hostinger export remains `noindex, follow`. Its sitemap contains no indexable URLs. A crawler may fetch HTML to read that directive; robots.txt is not used as a substitute for noindex.

`--indexable` is rejected for temporary `*.hostingersite.com` domains. After the actual permanent domain is confirmed, use `python3 scripts/build.py --site https://CONFIRMED-DOMAIN --indexable`. This sets all canonical/social/schema/llms links consistently and creates the eleven-URL indexable sitemap; 404 remains noindex. An isolated `.example` fixture verified this branch without publishing it.

Permanent-domain/DNS/HTTPS configuration, verified Google Business Profile consistency, Search Console/Bing ownership and sitemap submission, live index status and field performance remain launch tasks. No domain, Business Profile, webmaster account or analytics settings have been changed. Rankings, indexing and AI citations are not guaranteed.

## Verification

`python3 scripts/check_site.py` checks all 12 routes, unique metadata, all local links/fragments/assets, JSON-LD/CSP hashes, visible FAQ parity, medicine-promotion exclusions, outlined SVG, llms links and preview/sitemap policy. Isolated future-domain export passes the indexable policy checks. Browser checks cover all eleven normal pages at 390/1440 px and shared templates at 320/768/1024 px, with loaded header logos and no page-wide horizontal overflow. Nearby-area matching, no-result and clearing states, plus mobile-menu Escape/focus return, were exercised.

Performance and deployment-specific evidence is recorded in WEBSITE-HANDOFF.md. Physical-device, VoiceOver, separate Safari/Firefox and actual browser-zoom checks remain unverified.
