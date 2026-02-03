# Image Guide for Implenia Ahrens Optimate Homepage

## Required Images

### 1. Hero Background (CRITICAL)
- **Location:** `src/assets/images/hero-background.jpg`
- **Size:** 1920x1080px (landscape)
- **Subject:** Swedish infrastructure (tunnel, bridge, construction site)
- **Suggested Unsplash search:** "tunnel construction" or "infrastructure sweden"
- **Direct links:**
  - https://unsplash.com/photos/gray-tunnel-_SMNO4cN9vs
  - https://unsplash.com/photos/a-train-traveling-down-tracks-next-to-a-tunnel-EbuaKnSm8Zw
  - https://unsplash.com/photos/timelapse-photography-of-tunnel-FXFz-sW0uwo

### 2. Team Photos (YOU HAVE THESE)
- **Location:**
  - `src/assets/images/michael-engstrom.jpg` (400x400px)
  - `src/assets/images/lars-diethelm.jpg` (400x400px)
  - `src/assets/images/ulf-christiansson.jpg` (400x400px)
- **Format:** Professional headshots, square format, neutral background

### 3. Problem Section Image
- **Location:** `src/assets/images/problem-section.jpg`
- **Size:** 800x600px
- **Subject:** Office worker with blueprints/construction plans
- **Suggested search:** "construction manager laptop" or "architect reviewing plans"
- **Direct links:**
  - https://unsplash.com/photos/person-holding-pencil-near-laptop-computer-5fNmWej4tAA
  - https://unsplash.com/photos/man-in-white-dress-shirt-sitting-beside-woman-in-black-long-sleeve-shirt-LPZy4da9aRo

### 4. Solution Images (5 images)
All 600x400px:

**a) Bid Analysis**
- `src/assets/images/solution-bid-analysis.jpg`
- Search: "document comparison" or "spreadsheet analysis"
- https://unsplash.com/photos/turned-on-monitoring-screen-hpjSkU2UYSU

**b) Document Extraction**
- `src/assets/images/solution-document-extraction.jpg`
- Search: "documents pdf"
- https://unsplash.com/photos/white-printer-paper-on-brown-wooden-table-505eectW54k

**c) Meeting Notes**
- `src/assets/images/solution-meeting-notes.jpg`
- Search: "business meeting notes"
- https://unsplash.com/photos/three-men-sitting-while-using-laptops-and-watching-man-beside-whiteboard-QckxruozjRg

**d) Invoice Control**
- `src/assets/images/solution-invoice-control.jpg`
- Search: "invoice document"
- https://unsplash.com/photos/person-using-macbook-pro-on-person-s-lap-npxXWgQ33ZQ

**e) Knowledge Assistant**
- `src/assets/images/solution-knowledge-assistant.jpg`
- Search: "AI chatbot interface" or "search interface"
- https://unsplash.com/photos/black-and-white-robot-toy-on-red-wooden-table-Oalh2MojUuk

## How to Add Images

### Option 1: Download from Unsplash (Recommended)
1. Visit the Unsplash links above
2. Click "Download free" button
3. Save to `src/assets/images/` folder with the correct filename
4. Images are automatically optimized by Astro

### Option 2: Use Your Own Images
1. Place images in `src/assets/images/` folder
2. Use exact filenames listed above
3. Recommended: Optimize first with TinyPNG.com (keep under 500KB for hero, 200KB for others)

### Option 3: Quick Script (If you have URLs)
Create a file with URLs and run a download script

## Adding Your Team Photos

1. Get professional headshots of:
   - Michael Engström
   - Lars Diethelm
   - Ulf Christiansson

2. Resize to 400x400px (square)
   - Use https://squoosh.app for resizing and optimization
   - Or Photoshop/GIMP

3. Save as:
   - `src/assets/images/michael-engstrom.jpg`
   - `src/assets/images/lars-diethelm.jpg`
   - `src/assets/images/ulf-christiansson.jpg`

4. The component will automatically use them (no code changes needed)

## Image Optimization Checklist

Before adding images:
- [ ] Hero: <500KB, 1920x1080px
- [ ] Team photos: <100KB each, 400x400px
- [ ] Solution images: <200KB each, 600x400px
- [ ] All JPG format (or WebP if available)
- [ ] Run through TinyPNG.com or Squoosh.app

## After Adding Images

The Astro dev server will automatically:
- ✅ Convert to WebP format
- ✅ Generate responsive sizes
- ✅ Add lazy loading
- ✅ Prevent layout shift

Just refresh your browser to see them!
