# Agent Guidelines for VDH Solutions Portfolio

These instructions apply to all AI agents working within this repository.

## 1. Pure Static HTML Stack
- The website is 100% static: vanilla HTML5, modern CSS3, and lightweight vanilla JS.
- Do NOT introduce build tools, Webpack, Vite, Node servers, or heavy frameworks (React, Vue, Next.js).
- Keep all files directly readable and runnable in any browser.

## 2. Bilingual Architecture (English & Dutch)
- **English version**: [index.html](file:///Users/jesse/Hobby_projects/Portfolio/VDHSolutions/index.html) (`/`)
- **Dutch version**: [nl/index.html](file:///Users/jesse/Hobby_projects/Portfolio/VDHSolutions/nl/index.html) (`/nl/`)
- Whenever updating content (roles, bio, certifications, projects), **always update both files in sync**.
- Keep root-relative paths for all assets (`/logo.png`, `/foto.jpeg`, `/CV_Jesse_van_den_Hoven_NL.pdf`, `/ENG_Curriculum Vitae_Jesse van den Hoven.pdf`).
- Keep reciprocal `hreflang` links in `<head>` and in [sitemap.xml](file:///Users/jesse/Hobby_projects/Portfolio/VDHSolutions/sitemap.xml).

## 3. Human Writing Voice & Zero-Dash Policy
- **NO em-dashes (`—`) or en-dashes (`–`)**: Never use them. Use commas, colons, parentheses, or clear separate sentences.
- **Tone**: Down-to-earth, pragmatic, hands-on, and authentic, matching Jesse van den Hoven's real voice from his motivation letter and CV.
- Avoid robotic AI buzzwords like *"aanjagen van"*, *"use-case discovery"*, *"Adoption, not demos"*, *"cruciale synergie"*.

## 4. Skills & Validation
Before submitting any work or pushing commits, activate and follow the workspace skills:
- **`portfolio-human-voice`**: `.agents/skills/portfolio-human-voice/SKILL.md`
- **`portfolio-i18n-management`**: `.agents/skills/portfolio-i18n-management/SKILL.md`
- **`portfolio-site-qa-deploy`**: `.agents/skills/portfolio-site-qa-deploy/SKILL.md`

Always verify that the validator passes cleanly:
```bash
python3 tools/validate.py
```
