# Website assets

The website uses exact local originals already uploaded to the approved Figma file. Figma's generated asset download endpoint returned zero-byte payloads during implementation; those payloads were discarded. The original files below supplied the same approved photographs and artwork. WebP versions preserve the image content; CSS applies the Figma crops.

| Website asset | Original in `docs/design/assets/` | Placement |
| --- | --- | --- |
| `angels-logo-gold.svg` | `docs/design/logo-refinement/angels-logo-gold.svg` | Header, footer and privacy header; approved Figma vector refinement |
| `nails.webp` | `7289f59011fc7599.jpg` | Hero, nails card, first Instagram tile |
| `brows.webp` | `66cd454b817c574b.jpg` | Brows card, second Instagram tile |
| `facial.webp` | `dominique-rivas-facial-massage.jpg` | Editorial hero and skin treatment story; illustrative stock |
| `facial-800.webp` | `dominique-rivas-facial-massage.jpg` | 800 px responsive variant for smaller displays; same illustrative photograph |
| `salon.webp` | `salon-interior.jpg` | Experience section |
| `brown-nails.webp` | `2b81ed4e3872d756.jpg` | Third Instagram tile |

The full-face Instagram photograph formerly exported as `lashes.webp` has been removed from both the gallery and public export at Andy's request. Only nail work and tight eye/brow detail photographs are included in the website gallery. The original design source remains an archival asset, not a published website image.

Image provenance and source posts: [design handoff](design/README.md). The stock photograph is by [Dominique Rivas on Unsplash](https://unsplash.com/photos/a-woman-getting-a-facial-massage-on-her-face-rWwuf8yKw4Y), under the free Unsplash License checked on 18 November 2026. It is illustrative service imagery, not an Angels client or result.

Cormorant Garamond Regular and DM Sans (400/500) are local Latin WOFF2 files downloaded from Google Fonts. Their SIL Open Font License texts are included in `src/assets/fonts/`. No external font requests are needed at runtime.

Optimised image files were produced using the installed `cwebp -q 85 -metadata none` command. Original images remain unchanged in the design directory. The favicon is a simple gold A on aubergine; it is not a vector reconstruction of the supplied logo.

The refined logo was approved on 18 November 2026. It preserves the layered uppercase/script/descriptor format in richer gold, with stronger Cinzel Bold lettering and a DM Sans SemiBold descriptor. Its lettering is outlined in the SVG; the editable text and three colourways remain in Figma. The SVG is transparent and needs no extra web fonts or raster cropping. The original JPEG remains archived in the design source.
