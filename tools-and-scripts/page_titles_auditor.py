#!/usr/bin/env python3
"""Audit page titles for length and pixel width approximation.

Usage:
    python page_titles_auditor.py urls.txt

Input:
    urls.txt — one URL per line.
Output:
    CSV to stdout: url,title,length,approx_pixels
"""
import sys, math, requests
from bs4 import BeautifulSoup

def approx_pixels(s):
    # Roughly estimate based on average glyph widths; it's not perfect but useful.
    widths = { "wide": set("MW@#%&"), "narrow": set("il.,'|:;") }
    px = 0
    for ch in s:
        if ch in widths["wide"]:
            px += 10
        elif ch in widths["narrow"]:
            px += 5
        else:
            px += 8
    return px

def fetch_title(url):
    r = requests.get(url, timeout=20, headers={"User-Agent":"seo-tools/1.0"})
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    title = soup.title.string.strip() if soup.title and soup.title.string else ""
    return title

def main():
    if len(sys.argv) < 2:
        print("Usage: python page_titles_auditor.py urls.txt")
        sys.exit(1)
    with open(sys.argv[1], "r") as f:
        urls = [line.strip() for line in f if line.strip()]
    print("url,title,length,approx_pixels")
    for u in urls:
        try:
            t = fetch_title(u)
            print(f"{u},{t.replace(',', ' ')},{len(t)},{approx_pixels(t)}")
        except Exception as e:
            print(f"{u},ERROR: {e},,")
if __name__ == "__main__":
    main()
