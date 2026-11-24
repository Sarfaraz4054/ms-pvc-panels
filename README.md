# MS PVC Panels website (static: HTML, CSS, JS)

Open `index.html` in a browser (or use the VS Code "Live Server" extension). Upload the whole folder to any hosting.

## Replace product images
1. Open the folder for the category, e.g. `images/pvc-panels/`. `README.txt` there lists the exact file names.
2. Copy your photo into the folder with that exact name (e.g. `pvc-panel-001.jpg`). It shows up automatically. Until then a placeholder is shown.
3. Use square photos about 800x800 px, under 150 KB. Home banner: `images/banners/hero-banner.jpg`.

## Edit product names, codes and sizes
Each product is one `<article class="card" ...>` block in its category page. Change `data-name`, `data-code`, `data-dims` and the `<h3>` / code text. Sizes live in `data-dims`, e.g. `Size=10 Feet|12 Feet;Width=1 Foot` (the visible size text and the WhatsApp message are both built from it). WPC uses `Height=1.5 Feet;Width=6 Inches`. Use VS Code Find & Replace (Ctrl+H) to change many at once. To add a product, copy a whole `<article>` block and edit it.

## WhatsApp numbers
Edit `js/config.js` (enquiry form numbers). Call/WhatsApp links in the HTML contain the numbers too: use Find & Replace for `919848487800` and `919935064878`.

## SEO checklist
1. Replace `https://www.mspvcpanels.com` with your real domain in all files (Find & Replace across the folder).
2. Add the site to Google Search Console, paste the verification tag where marked in each page's `<head>`, and submit `sitemap.xml`.
3. Create and verify a Google Business Profile, then add its link/map in `contact-us.html` (comment marks the spot). Add the full street address to the LocalBusiness schema when you have it.
4. Add real photos with descriptive alt text, and real product names. Rankings are never guaranteed; fresh content, reviews and a good Business Profile help over time.

## Optional: regenerate everything
`python tools/build.py` rewrites all pages from one script. It overwrites hand edits, so use it OR edit HTML directly.

## Logo
Put your logo in `images/logo.png` (square or nearly square, about 200x200 px, under 50 KB; a transparent PNG looks best). It appears to the left of the site name in the header on every page. Until then a dashed "LOGO" box is shown. To use another file name, change `images/logo.png` in `tools/build.py` and run `python tools/build.py`.

## Product image in WhatsApp enquiries
WhatsApp does not allow a website to attach a photo automatically. So each enquiry includes a link to the product photo; WhatsApp shows it as a picture preview in the chat. This works once the website is live online (not when opened from your computer), and only for products whose photo you have added to `images/`. Products still showing the placeholder send no image link.
