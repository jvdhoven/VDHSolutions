#!/usr/bin/env bash
# VDH Solutions - Safe Deploy Script
# Validates the site first, then commits and pushes to GitHub.

set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$DIR"

echo "=== 1/3 Running Pre-Deploy Validation ==="
python3 tools/validate.py

echo ""
echo "=== 2/3 Checking Git Status ==="
git status --short

if [ -z "$(git status --porcelain)" ]; then
  echo "Geen wijzigingen om te committen. Alles is al up-to-date."
  exit 0
fi

echo ""
MESSAGE="$1"
if [ -z "$MESSAGE" ]; then
  read -r -p "Geef een commit message op (bijv. 'Update cv en werkervaring'): " MESSAGE
fi

if [ -z "$MESSAGE" ]; then
  echo "Fout: Commit message mag niet leeg zijn."
  exit 1
fi

echo ""
echo "=== 3/3 Staging, Committing and Pushing to GitHub ==="
git add index.html nl/index.html sitemap.xml tools/ README.md AGENTS.md 2>/dev/null || git add -A
git commit -m "$MESSAGE"
git push origin main

echo ""
echo "✔ Succesvol gepusht naar GitHub! De wijzigingen staan binnen enkele seconden live."
