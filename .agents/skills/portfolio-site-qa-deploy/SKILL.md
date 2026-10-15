---
name: portfolio-site-qa-deploy
description: >-
  Provides end-to-end verification, quality assurance, local previewing, and safe GitHub deployment procedures for the VDH Solutions portfolio. Use whenever validating changes, testing the site locally, or deploying updates to production.
---

# Portfolio QA, Local Preview & Deployment Workflow

This skill defines the quality assurance and deployment procedure for the VDH Solutions portfolio.

## 1. Automated Validation

Before staging any commit, always run the validation suite:

```bash
python3 tools/validate.py
```

This automated validator checks:
- **HTML Syntax**: Ensures both `index.html` and `nl/index.html` are syntactically well-formed.
- **Link & Asset Integrity**: Ensures every internal link (`/foto.jpeg`, `/logo.png`, `/CV_Jesse_van_den_Hoven_NL.pdf`, `/ENG_Curriculum Vitae_Jesse van den Hoven.pdf`, `/nl/`, `/`) resolves to an existing file on disk.
- **AI Marker Detection**: Ensures no unintended em-dashes (`—`) or en-dashes (`–`) exist in any HTML file.
- **Sitemap XML**: Validates `sitemap.xml` structure and URLs.

## 2. Local Previewing

To preview changes across both English and Dutch versions locally:

```bash
python3 tools/preview.py
```

This starts a zero-dependency server:
- English site: `http://localhost:8000/`
- Dutch site:   `http://localhost:8000/nl/`

Press `Ctrl+C` in your terminal to stop the preview server when finished.

## 3. Safe Deployment to GitHub Pages

Once validation passes, deploy with git:

```bash
git status
git add index.html nl/index.html sitemap.xml
git commit -m "Your descriptive commit message"
git push origin main
```

Or run the automated deployment script:

```bash
./tools/deploy.sh "Your commit message"
```

GitHub Pages will automatically publish the new version to `https://vdhsolutions.nl/` within 30 seconds.
