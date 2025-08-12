#!/usr/bin/env python3
"""Simple sitemap URL checker.

Usage:
    python sitemap_checker.py https://example.com/sitemap.xml

It will:
- Fetch the sitemap (XML or index).
- Extract URLs (handles gzip transparently if server sets headers).
- Request each URL (HEAD by default) and report status code and canonical tag (if GET).
"""
import sys, re, gzip, io, xml.etree.ElementTree as ET
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

def fetch(url):
    r = requests.get(url, timeout=30, headers={"User-Agent":"seo-tools/1.0"})
    r.raise_for_status()
    # Handle gzipped sitemaps served as binary
    if url.endswith(".gz"):
        return gzip.decompress(r.content).decode("utf-8", errors="ignore")
    return r.text

def parse_sitemap(xml_text):
    root = ET.fromstring(xml_text)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = []
    # sitemap index
    for loc in root.findall(".//sm:sitemap/sm:loc", ns):
        urls.append(("index", loc.text.strip()))
    # urlset
    for loc in root.findall(".//sm:url/sm:loc", ns):
        urls.append(("url", loc.text.strip()))
    return urls

def check_url(url):
    try:
        # HEAD first
        h = requests.head(url, timeout=20, allow_redirects=True, headers={"User-Agent":"seo-tools/1.0"})
        code = h.status_code
        final_url = h.url
        canonical = None
        # If 200, optionally GET first 64KB to find canonical
        if 200 <= code < 400:
            g = requests.get(final_url, timeout=20, headers={"User-Agent":"seo-tools/1.0"}, stream=True)
            chunk = next(g.iter_content(chunk_size=65536))
            soup = BeautifulSoup(chunk, "html.parser")
            link = soup.find("link", rel=lambda x: x and "canonical" in x.lower())
            if link and link.get("href"):
                canonical = link["href"]
        return code, final_url, canonical
    except Exception as e:
        return None, None, str(e)

def main():
    if len(sys.argv) < 2:
        print("Provide a sitemap URL")
        sys.exit(1)
    sitemap_url = sys.argv[1]
    print(f"# Checking sitemap: {sitemap_url}\n")
    text = fetch(sitemap_url)
    items = parse_sitemap(text)
    urls = []
    # expand index
    for typ, loc in items:
        if typ == "index":
            try:
                sub = fetch(loc)
                for _, subloc in parse_sitemap(sub):
                    urls.append(subloc)
            except Exception as e:
                print(f"Could not expand index {loc}: {e}")
        elif typ == "url":
            urls.append(loc)
    print(f"Found {len(urls)} URLs.\n")
    print("status_code,final_url,canonical")
    for u in urls:
        code, final, canon = check_url(u)
        print(f"{code},{final},{canon}")
if __name__ == "__main__":
    main()
