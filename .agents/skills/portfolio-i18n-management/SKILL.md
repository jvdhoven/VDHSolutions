---
name: portfolio-i18n-management
description: >-
  Manages the dual-language architecture of the VDH Solutions portfolio, keeping English (index.html) and Dutch (nl/index.html) synchronized with clean subpath routing, hreflang tags, anchor preservation, and language switcher consistency. Use whenever updating content in one language that must be mirrored to the other, adding new pages, or modifying navigation and language switching.
---

# Portfolio Bilingual (i18n) Architecture & Workflow

This skill guides the agent in maintaining the two localized versions of the static website without frameworks or server-side build steps.

## Architecture Overview

- **English Version**: `index.html` (served at `/`)
- **Dutch Version**: `nl/index.html` (served at `/nl/`)
- **Hosting**: GitHub Pages with custom domain `vdhsolutions.nl` (both paths resolve natively).

## Synchronization Checklist

Whenever any section (Hero, About, Experience, Education, Expertise, Contact) is modified:

1. **Dual Update**: Update both `index.html` (English) and `nl/index.html` (Dutch). Never leave one language behind.
2. **Root-Relative Assets**: Always use root-relative paths for assets so they load identically from both `/` and `/nl/`:
   - Images: `/logo.png`, `/foto.jpeg`
   - Dutch CV: `/CV_Jesse_van_den_Hoven_NL.pdf`
   - English CV: `/ENG_Curriculum Vitae_Jesse van den Hoven.pdf`
3. **SEO & Hreflang Tags**: Ensure both files have matching reciprocal alternate links in `<head>`:
   ```html
   <link rel="alternate" hreflang="en" href="https://vdhsolutions.nl/">
   <link rel="alternate" hreflang="nl" href="https://vdhsolutions.nl/nl/">
   <link rel="alternate" hreflang="x-default" href="https://vdhsolutions.nl/">
   ```
4. **Language Switcher Consistency**:
   - In `index.html`: `EN` is active (`<span class="lang-btn active">EN</span>`), `NL` links to `/nl/`.
   - In `nl/index.html`: `NL` is active (`<span class="lang-btn active">NL</span>`), `EN` links to `/`.
   - The embedded JavaScript automatically preserves current anchor hashes (e.g. `#experience` $\rightarrow$ `/nl/#experience`) and records choice in `localStorage`.
5. **Sitemap**: Keep [sitemap.xml](../../sitemap.xml) updated with `<xhtml:link>` hreflang entries for both URLs.

## Verification

After making updates across languages, verify in a browser that both pages render properly and all links/downloads work cleanly.
