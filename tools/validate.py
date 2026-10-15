#!/usr/bin/env python3
"""
VDH Solutions - Website Validator
Checks HTML syntax, broken internal links, missing assets (images, PDFs),
sitemap structure, and ensures no unwanted AI em-dashes (— or –) are present.
Zero external dependencies (Python standard library only).
"""

import os
import re
import sys
from html.parser import HTMLParser
import xml.etree.ElementTree as ET

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML_FILES = ["index.html", "nl/index.html"]
SITEMAP_FILE = "sitemap.xml"

# Terminal color helpers
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"

errors_found = 0
warnings_found = 0

def log_pass(msg):
    print(f"  {GREEN}✔{RESET} {msg}")

def log_fail(msg):
    global errors_found
    errors_found += 1
    print(f"  {RED}✖ {msg}{RESET}")

def log_warn(msg):
    global warnings_found
    warnings_found += 1
    print(f"  {YELLOW}⚠ {msg}{RESET}")


class StrictHTMLParser(HTMLParser):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def error(self, message):
        log_fail(f"HTML parse error in {self.filename}: {message}")


def check_html_syntax():
    print(f"\n{BOLD}1. Checking HTML Syntax...{RESET}")
    for rel_path in HTML_FILES:
        full_path = os.path.join(REPO_ROOT, rel_path)
        if not os.path.exists(full_path):
            log_fail(f"File missing: {rel_path}")
            continue

        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()

        parser = StrictHTMLParser(rel_path)
        try:
            parser.feed(content)
            log_pass(f"{rel_path}: Syntax valid ({len(content)} bytes)")
        except Exception as e:
            log_fail(f"{rel_path}: Syntax error: {e}")


def check_em_dashes():
    print(f"\n{BOLD}2. Checking for AI markers (em-dashes '—' and en-dashes '–')...{RESET}")
    dash_patterns = [
        ("\u2014", "em-dash (—)"),
        ("\u2013", "en-dash (–)")
    ]

    for rel_path in HTML_FILES:
        full_path = os.path.join(REPO_ROOT, rel_path)
        if not os.path.exists(full_path):
            continue

        with open(full_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        found_in_file = False
        for idx, line in enumerate(lines, start=1):
            for char, name in dash_patterns:
                if char in line:
                    found_in_file = True
                    log_fail(f"{rel_path}:{idx}: Found {name}: {line.strip()[:70]}...")

        if not found_in_file:
            log_pass(f"{rel_path}: No AI em-dashes found")


def check_assets_and_links():
    print(f"\n{BOLD}3. Checking Asset and Internal Links...{RESET}")
    link_regex = re.compile(r'(?:src|href)=["\']([^"\']+)["\']')

    for rel_path in HTML_FILES:
        full_path = os.path.join(REPO_ROOT, rel_path)
        if not os.path.exists(full_path):
            continue

        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()

        targets = link_regex.findall(content)
        checked_count = 0

        for target in targets:
            # Skip external links, mailto, and anchor jumps
            if target.startswith(("http://", "https://", "mailto:", "tel:", "#", "javascript:")):
                continue

            checked_count += 1
            clean_target = target.split("#")[0].split("?")[0].strip()

            # Handle root '/' pointing to index.html
            if clean_target == "/" or clean_target == "":
                target_disk_path = os.path.join(REPO_ROOT, "index.html")
            elif clean_target.startswith("/"):
                subpath = clean_target.lstrip("/")
                if subpath.endswith("/") or os.path.isdir(os.path.join(REPO_ROOT, subpath)):
                    target_disk_path = os.path.join(REPO_ROOT, subpath, "index.html")
                else:
                    target_disk_path = os.path.join(REPO_ROOT, subpath)
            else:
                base_dir = os.path.dirname(full_path)
                target_disk_path = os.path.join(base_dir, clean_target)

            if not os.path.exists(target_disk_path):
                log_fail(f"{rel_path}: Broken link or missing asset: '{target}' (resolved to '{os.path.relpath(target_disk_path, REPO_ROOT)}')")

        log_pass(f"{rel_path}: Verified {checked_count} internal assets and links")


def check_sitemap():
    print(f"\n{BOLD}4. Checking sitemap.xml...{RESET}")
    sitemap_path = os.path.join(REPO_ROOT, SITEMAP_FILE)
    if not os.path.exists(sitemap_path):
        log_fail(f"Missing {SITEMAP_FILE}")
        return

    try:
        tree = ET.parse(sitemap_path)
        root = tree.getroot()
        log_pass(f"{SITEMAP_FILE}: Valid XML structure")

        locs = [elem.text for elem in root.iter() if elem.tag.endswith("loc")]
        for loc in locs:
            log_pass(f"  Indexed URL: {loc}")
    except Exception as e:
        log_fail(f"{SITEMAP_FILE} XML parsing error: {e}")


def main():
    print(f"{BOLD}=== VDH Solutions Portfolio Validation ==={RESET}")
    check_html_syntax()
    check_em_dashes()
    check_assets_and_links()
    check_sitemap()

    print("\n" + "=" * 45)
    if errors_found == 0:
        print(f"{GREEN}{BOLD}✔ All checks passed cleanly! Site is ready for production.{RESET}\n")
        sys.exit(0)
    else:
        print(f"{RED}{BOLD}✖ {errors_found} error(s) found. Please resolve them before deploying.{RESET}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
