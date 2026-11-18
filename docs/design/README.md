# Angels website design

Created 18 November 2026 using Figma and the superweb skill.

[Open the editable Figma file](https://www.figma.com/design/WKseG6Qlc8DgpR1ERlWAZB?node-id=2-350).

## Delivered

- Desktop homepage, 1440 px: frame `2:350`.
- Mobile homepage, 390 px: frame `2:465`.
- Mobile menu concept: frame `2:569`.
- Design and integration handoff: frame `2:586`.
- Native text, auto-layout, reusable booking/navigation/treatment components, and shared colour/spacing variables.
- Cormorant Garamond display typography and DM Sans body text; ivory, aubergine and warm neutral surfaces.
- Booksy booking actions and Instagram source-post links configured in the prototype.
- Six authentic Instagram photographs; no generated client imagery or invented testimonials.
- User-supplied salon interior photograph added to the experience section on desktop and mobile; both section crops visually checked.

The audience is local clients considering nails, lashes, brows, facials and aesthetic appointments. The primary action is viewing treatments and booking through Booksy. Instagram visitors and local search are the proposed entry routes. Booking confirmation, current pricing, availability and booking policies remain with Booksy. No conversion target or commercial uplift is claimed.

## Preview files

- `desktop.png`: desktop composition export.
- `mobile.png`: mobile composition export.
- `create-figma.js`: construction source, tied to the image hashes and uploaded asset node IDs in this Figma file. This creates new compositions; do not rerun it blindly against an existing design.
- `assets/salon-interior.jpg`: the interior image supplied by Andy, originally named `639471611_18005394668848080_3708456548039809037_n.jpg`.

## Unsplash shortlist

Searched and visually reviewed on 18 November 2026. Dominique Rivas’s photograph has been selected and placed in the desktop and mobile Skin & aesthetics cards as illustrative service imagery. It is not presented as an Angels client or result. The other two photographs remain shortlist options. Each source page identifies the image as free under the Unsplash License.

1. [Facial massage — Dominique Rivas](https://unsplash.com/photos/a-woman-getting-a-facial-massage-on-her-face-rWwuf8yKw4Y). Recommended: warm, softly lit close-up suits the existing ivory/aubergine direction.
2. [Facial mask application — kimia kazemi](https://unsplash.com/photos/woman-receiving-a-facial-treatment-with-a-brush-wYrnlhDQaIA). Warm, atmospheric portrait format; includes embroidery on the towel, so consider placement carefully.
3. [Spa mask treatment — engin akyurt](https://unsplash.com/photos/woman-lying-on-blue-towel-with-white-cream-on-face-g-m8EDc4X6Q). Bright landscape composition; useful for a service banner, though its turquoise/green accents are less aligned with the current palette.

[Unsplash License](https://unsplash.com/license). Retain photographer/source attribution in the asset register for whichever images are chosen. No paid Unsplash+ images were downloaded or purchased.

## Sources and imagery

Business context: [public Instagram profile](https://www.instagram.com/angels.surrey/) and [Booksy listing](https://booksy.com/en-gb/142395_angels-clinic-beauty_nail-salon_959268_west-clandon).

The Instagram profile directly links to [angels9.booksy.com/a](https://angels9.booksy.com/a/). On 18 November 2026, following that link returned HTTP 200 at `https://cdl.booksy.com/1kfslWZji6b`. A booking was not made or tested.

| Local source image | Original Instagram post |
| --- | --- |
| `assets/525a8b0b8df2d74b.jpg` | [15 November](https://www.instagram.com/angels.surrey/p/De9M1ogNXQu/) |
| `assets/7289f59011fc7599.jpg` | [13 November](https://www.instagram.com/angels.surrey/p/De9Mv5Vt4PZ/) |
| `assets/054be962f4ef4ebc.jpg` | [11 November](https://www.instagram.com/angels.surrey/p/DfmbrOSDVE7/) |
| `assets/2083fe19fb96fa63.jpg` | [9 November](https://www.instagram.com/angels.surrey/p/De9MhopNGll/) |
| `assets/2b81ed4e3872d756.jpg` | [7 November](https://www.instagram.com/angels.surrey/p/De9McDVNCyf/) |
| `assets/66cd454b817c574b.jpg` | [5 November](https://www.instagram.com/angels.surrey/p/De9MUv7tsN-/) |

All images were taken from the public profile for this design. Confirm the business's permission to republish identifiable client photos before public release. The official gold logo was supplied by Andy as `angels logo.jpg` and is preserved at `assets/angels-logo-original.jpg`. A shared logo component replaces all five provisional wordmarks across headers, footers and the mobile menu. The artwork is cropped non-destructively in Figma; Multiply blending makes its white JPEG background blend with light surfaces. This remains raster JPEG artwork, not a vector or genuinely transparent logo. Desktop and mobile mastheads were visually checked.

## Instagram feed implementation

The current gallery is a curated snapshot of real posts. An automatically updating feed is not connected. During implementation, choose an owner-authorised integration, confirm its current supported account types and permissions against Meta documentation, refresh/cache on the server, and keep credentials out of frontend code. Never rely on expiring Instagram CDN URLs as permanent production assets.

Design the loading, empty, disconnected and refresh-failure states. Preserve the last authorised gallery on refresh failure; retain a working Instagram link. Prefer cached authorised images and lightweight post links to loading third-party scripts on every visit. Decide any required consent behaviour once the actual integration is selected. No analytics, pixels, mailing lists or account permissions have been activated.

## Evidence and remaining work

| Area | Status and evidence |
| --- | --- |
| Design | Passed: desktop and mobile screenshots visually reviewed; content remains editable. |
| Desktop/mobile | Passed for Figma compositions at 1440 and 390 px. A component sizing defect was corrected and the mobile design rechecked. Actual browser checks at 320, 768, intermediate widths and zoom remain pending implementation. |
| Layout bounds | Passed: text bounds checked; no horizontal text overflow in the corrected desktop/mobile designs. |
| Functionality | Booksy and individual Instagram URLs configured and read back from the prototype. Booksy share link resolves. Manual prototype interaction testing, especially mobile menu navigation, remains pending. No end-to-end booking verification. |
| Accessibility | Readable hierarchy, 48px+ booking actions and high-contrast primary palette designed. Keyboard, focus, screen-reader, computed contrast and browser reflow checks remain pending implementation. |
| Performance | Not applicable to the Figma artifact. No web runtime exists yet; production-build Lighthouse, image/font budgets and physical-device checks are pending implementation. |
| Marketing/discovery | Audience and booking action defined. Metadata, sitemap, staging noindex, public crawler configuration, local structured data and `/llms.txt` are implementation tasks; no indexing or conversion results claimed. |
| Security/privacy | No credentials, forms or active tracking added. Feed authorisation and image permissions remain production dependencies. |
| Deployment | No website was published during the design phase. The later implementation and Hostinger publication are recorded in ../WEBSITE-HANDOFF.md. |

Before production, confirm final business copy and image permissions, implement the responsive website and authorised feed, and complete the browser/accessibility/performance checks above.

Selected stock asset: `assets/dominique-rivas-facial-massage.jpg` — Dominique Rivas, Unsplash image `rWwuf8yKw4Y`. Source and license recorded above; attribution also saved in the Figma handoff.
