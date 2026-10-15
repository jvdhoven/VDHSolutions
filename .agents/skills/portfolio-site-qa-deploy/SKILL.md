---
name: portfolio-site-qa-deploy
description: >-
  Provides end-to-end verification, quality assurance, local previewing, and safe GitHub deployment procedures for the VDH Solutions portfolio. Use whenever validating changes, testing the site locally, or deploying updates to production.
---

# Portfolio QA, Local Preview & Deployment Workflow

This skill defines the quality assurance and deployment procedure for the VDH Solutions portfolio.

## 1. Quality Assurance

Before committing any changes:
- Verify that both `index.html` and `nl/index.html` open directly and render cleanly in a browser.
- Verify that all internal links, images (`/foto.jpeg`, `/logo.png`), and CV downloads (`/CV_Jesse_van_den_Hoven_NL.pdf`, `/ENG_Curriculum Vitae_Jesse van den Hoven.pdf`) work properly.
- Verify that no em-dashes (`—`) or en-dashes (`–`) have been introduced.
- Verify that reciprocal `hreflang` tags and `sitemap.xml` are in sync.

## 2. Deployment to GitHub Pages

Deploy directly with Git:

```bash
git status
git add index.html nl/index.html sitemap.xml
git commit -m "Beschrijvende commit message"
git push origin main
```

GitHub Pages automatically serves the updated website at `https://vdhsolutions.nl/`.
