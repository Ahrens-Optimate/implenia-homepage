#!/usr/bin/env python3
"""
Image management for the Implenia homepage.
Currently using Envato PhotoDune preview images (watermarked).

IMPORTANT: The hero and problem section images are currently WATERMARKED PREVIEWS.
To purchase the full versions without watermarks:

1. Hero Background - Öresund Bridge:
   https://photodune.net/item/the-oresund-bridge-between-denmark-and-sweden/39405216
   Price: $7.00 | Resolution: 7211x4800px (34.6MP)

2. Problem Section - Engineers with Blueprints:
   https://photodune.net/item/engineer-and-construction-site-manager-dealing-with-blueprints-and-plans/24002134
   Price: $5.00 | Resolution: 5472x3648px (20MP)

Total cost for professional images: $12.00

Run: python download_images.py
"""

import os
import urllib.request
from pathlib import Path

# Create images directory if it doesn't exist
images_dir = Path("src/assets/images")
images_dir.mkdir(parents=True, exist_ok=True)

# Placeholder images for solution cards (free Unsplash)
# These are less critical and can remain as placeholders
IMAGES = {
    # Solution 1: Bid analysis - spreadsheet/documents
    "solution-bid-analysis.jpg": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&q=80",

    # Solution 2: Document extraction - papers/documents
    "solution-document-extraction.jpg": "https://images.unsplash.com/photo-1568667256549-094345857637?w=600&q=80",

    # Solution 3: Meeting notes - business meeting
    "solution-meeting-notes.jpg": "https://images.unsplash.com/photo-1552664730-d307ca884978?w=600&q=80",

    # Solution 4: Invoice control - laptop/documents
    "solution-invoice-control.jpg": "https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?w=600&q=80",

    # Solution 5: Knowledge assistant - AI/robot
    "solution-knowledge-assistant.jpg": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&q=80",
}

def download_image(url, filename):
    """Download an image from URL to the images directory."""
    filepath = images_dir / filename

    if filepath.exists():
        print(f"[OK] {filename} already exists, skipping")
        return

    try:
        print(f"[>>] Downloading {filename}...")
        # Add User-Agent to avoid 403 errors
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            with open(filepath, 'wb') as out_file:
                out_file.write(response.read())
        print(f"[OK] Downloaded {filename}")
    except Exception as e:
        print(f"[ERROR] Failed to download {filename}: {e}")

def main():
    print("Downloading images for Implenia Ahrens Optimate homepage...")
    print(f"Saving to: {images_dir.absolute()}\n")

    for filename, url in IMAGES.items():
        download_image(url, filename)

    print("\n" + "="*60)
    print("Download complete!")
    print("\nNext steps:")
    print("1. Add your team photos to src/assets/images/:")
    print("   - michael-engstrom.jpg")
    print("   - lars-diethelm.jpg")
    print("   - ulf-christiansson.jpg")
    print("2. Refresh your browser to see the images!")
    print("="*60)

if __name__ == "__main__":
    main()
