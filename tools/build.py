"""Regenerates every page of the MS PVC Panels site. Optional: you can also edit the .html files directly.
WARNING: running this overwrites hand-edits made to the .html files, css/ and js/ it generates."""
import os, json
from urllib.parse import quote
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
URL = 'https://www.mspvcpanels.com'   # change to your real domain
P1, P2 = '919848487800', '919935064878'
T1, T2 = '+91 9848487800', '+91 9935064878'
DATE = '2026-11-24'

ADDR1 = 'Balaji Nagar Rd, Ambedkar Nagar, Dammaiguda'
ADDR = ADDR1 + ', Hyderabad, Telangana'
LAT, LNG = 17.507814940597928, 78.57741187859003
DIRS = f'https://www.google.com/maps/search/?api=1&query={LAT},{LNG}'
MAPSRC = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3616.7257672661776!2d78.57741187859003!3d17.507814940597928!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bcb9d4ed145914b%3A0xc70d1280aa5a5a9!2sPVC%2C%20WPC%2C%20Fluted%20Panel%20Shop%20%26%20Works!5e1!3m2!1sen!2sin!4v1795497866993!5m2!1sen!2sin"
MAP = f'<div class="map"><iframe src="{MAPSRC}" title="MS PVC Panels location on Google Maps" width="600" height="450" style="border:0" allowfullscreen loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe></div>'
AREAS = ['Hyderabad', 'Secunderabad', 'Medchal', 'Ranga Reddy', 'Sangareddy', 'Siddipet', 'Warangal', 'Karimnagar', 'Nizamabad', 'Khammam', 'Nalgonda', 'Mahabubnagar', 'Adilabad']

def w(p, s):
    p = os.path.join(ROOT, p); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(s)

def wa(text, n=P1): return f'https://wa.me/{n}?text={quote(text)}'
GEN = wa('Hello MS PVC Panels, I would like to know more about your PVC panels and accessories.')
WAI = '<svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15L2 22l5.2-1.4A10 10 0 1 0 12 2zm4.9 14c-.2.6-1.2 1.1-1.7 1.2-.4.1-1 .1-1.6-.1-3-1.2-4.9-4.2-5.1-4.4-.1-.2-1.2-1.600-1.200-3s.7-2.100 1-2.400c.2-.3.500-.3.700-.3h.5c.2 0 .4 0 .6.500l.8 1.900c.1.200 0 .4-.1.600l-.4.500c-.1.100-.3.300-.1.600.5.800 1.200 1.500 2 2 .3.200.5.100.6-.1l.7-.9c.2-.2.400-.2.600-.1l1.800.9c.2.100.4.200.4.300.1.200.1.800-.1 1.300z"/></svg>'
TEL = '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15 15 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11 11 0 0 0 3.6.6 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11 11 0 0 0 .6 3.6 1 1 0 0 1-.25 1z"/></svg>'

CATS = [
 dict(slug='pvc-panels', title='PVC Panels', single='PVC Panel', code='PVC', n=8, models=[('81201',),('HE GOLDEN PVC','HE Golden PVC Panel'),('N-027',),('N-065',),('105',),('60561',),('60352',),('60701',)], dims='Size=10 Feet|12 Feet;Width=1 Foot', prices='10 Feet=260|12 Feet=320', nav='PVC Panels',
      desc='Clean, durable PVC wall and ceiling panels in a wide range of designs.',
      mt='PVC Panels in Hyderabad | PVC Wall & Ceiling Panels | MS PVC Panels',
      md='Browse 8 PVC panel designs in 10 ft and 12 ft lengths at MS PVC Panels, Hyderabad. PVC wall and ceiling panels for homes and offices across Telangana. Enquire on WhatsApp.',
      intro='Our PVC wall and ceiling panels are available in 8 designs, in 10 feet and 12 feet lengths with a 1 foot width. Choose a design, tap Enquire on WhatsApp, and we will share details for your Hyderabad or Telangana project.'),
 dict(slug='fluted-panels', title='Fluted PVC Panels', single='Fluted Panel', code='FLT', n=13, models=[(m,) for m in ['HY-24','HK-2012','GFP-606','GFP-504','HK-123','GFP-506','GFP-514','IS 18-1G','HK-102','GPF-500','GFP-800','HK-202','07(2G)']], dims='Size=10 Feet|12 Feet;Width=1 Foot', prices='10 Feet=350|12 Feet=420', nav='Fluted Panels',
      desc='Modern ribbed fluted PVC panels for feature walls and interiors.',
      mt='Fluted PVC Panels in Hyderabad | Decorative Wall Panels | MS PVC Panels',
      md='Explore 13 fluted PVC panel designs in 10 ft and 12 ft lengths at MS PVC Panels, Hyderabad. Decorative wall panels for feature walls, TV units and interiors. Enquire on WhatsApp.',
      intro='Fluted PVC panels give feature walls, TV units and entrances a clean, ribbed finish. We stock 13 varieties in 10 feet and 12 feet lengths with a 1 foot width, available for customers in Hyderabad and across Telangana.'),
 dict(slug='bahubali-panels', title='Bahubali Fluted Panels', single='Bahubali Panel', code='BAH', n=4, models=[(m,) for m in ['HE-20 GOLD','HE-19 GOLD','HE-18 GOLD','BHF-009']], dims='Size=10 Feet;Width=1 Foot', prices='10 Feet=420', nav='Bahubali Panels',
      desc='Bold decorative Bahubali fluted panels that make a statement.',
      mt='Bahubali Fluted Panels Hyderabad | Decorative PVC Panels | MS PVC Panels',
      md='Bahubali fluted panels in Hyderabad: 4 decorative designs in 10 ft length at MS PVC Panels. Statement wall panels for homes, shops and offices. Enquire on WhatsApp.',
      intro='Bahubali fluted panels are our most decorative range, made for statement walls in living rooms, bedrooms, shops and offices. 4 designs are available in 10 feet length with a 1 foot width.', deco=1),
 dict(slug='wpc-panels', title='WPC Panels', single='WPC Panel', code='WPC', n=5, models=[(m,) for m in ['WPC-403','WPC-410','WPC-409','RVP-402','WPC-413']], dims='Height=9.5 Feet;Width=6 Inches', prices='all=360', nav='WPC Panels',
      desc='Sturdy WPC wall panels with a natural, textured look.',
      mt='WPC Panels in Hyderabad | WPC Wall Panels | MS PVC Panels',
      md='WPC panels in Hyderabad: 5 designs at MS PVC Panels. Sturdy, stylish wall panels for interiors across Telangana. Enquire on WhatsApp for sizes and availability.',
      intro='Our WPC panels come in 5 designs, each 9.5 feet in height and 6 inches wide. They suit accent walls and interior decoration in Hyderabad and across Telangana.'),
]
HW = [('Gypsum Channels', 'Metal channels used for false ceilings and partition framing.'),
      ('Gypsum Screws', 'Fixing screws for gypsum channels and board installation.'),
      ('PVC Clips', 'Clips used to fix PVC panels neatly to the wall or ceiling frame.'),
      ('PVC L Trims', 'L-shaped trims that finish corners and edges of PVC panels.'),
      ('PVC U Trims', 'U-shaped trims that cap and protect panel edges.')]
HWC = dict(slug='hardware', title='Hardware & Accessories', nav='Hardware & Accessories', file='hardware-accessories.html',
      desc='Gypsum channels, screws, PVC clips, L trims, U trims and more.')
for c in CATS: c['file'] = c['slug'] + '.html'
ALLC = CATS[:3] + [CATS[3], HWC]
NAV = [('Home', 'index.html'), ('About Us', 'about-us.html'), ('Products', 'products.html'), ('PVC Panels', 'pvc-panels.html'),
       ('Fluted Panels', 'fluted-panels.html'), ('WPC Panels', 'wpc-panels.html'), ('Hardware & Accessories', 'hardware-accessories.html'), ('Contact Us', 'contact-us.html')]
QL = NAV[:4] + [('Fluted Panels', 'fluted-panels.html'), ('Bahubali Panels', 'bahubali-panels.html'), ('WPC Panels', 'wpc-panels.html'), ('Hardware & Accessories', 'hardware-accessories.html'), ('Contact Us', 'contact-us.html')]
def price_html(pr):
    if not pr: return ''
    items = [p.split('=') for p in pr.split('|')]
    if items[0][0] == 'all': return f'<div class="price"><b>&#8377;{items[0][1]}</b></div>'
    return '<ul class="price">' + ''.join(f'<li>{k}: <b>&#8377;{v}</b></li>' for k, v in items) + '</ul>'
def slugn(c, i): return f"{c['single'].lower().replace(' ', '-')}-{i:03d}"
def specs(d): return ''.join(f"<li><b>{'Available Sizes' if k == 'Size' else k}:</b> {' &amp; '.join(v.split('|'))}</li>" for k, v in (p.split('=') for p in d.split(';') if p))

LB = {"@context": "https://schema.org", "@type": "LocalBusiness", "name": "MS PVC Panels", "url": URL, "image": URL + "/images/banners/hero-banner.jpg",
      "telephone": ["+919848487800", "+919935064878"], "parentOrganization": {"@type": "Organization", "name": "MS Traders"},
      "address": {"@type": "PostalAddress", "streetAddress": ADDR1, "addressLocality": "Hyderabad", "addressRegion": "Telangana", "addressCountry": "IN"},
      "geo": {"@type": "GeoCoordinates", "latitude": LAT, "longitude": LNG}, "hasMap": DIRS,
      "areaServed": [{"@type": "State", "name": "Telangana"}] + [{"@type": "City", "name": a} for a in AREAS[:2]] + [{"@type": "AdministrativeArea", "name": a} for a in AREAS[2:]],
      "description": "PVC panels, fluted panels, Bahubali fluted panels, WPC panels and interior hardware in Hyderabad, supplied across Telangana."}

def page(fn, title, desc, body, schema=None, crumbs=None, cls=''):
    sch = list(schema or [])
    bc = ''
    if crumbs:
        items = [('Home', 'index.html')] + crumbs
        bc = '<nav class="crumbs" aria-label="Breadcrumb">' + ' &rsaquo; '.join(f'<a href="{u}">{n}</a>' for n, u in items[:-1]) + f' &rsaquo; <span aria-current="page">{items[-1][0]}</span></nav>'
        sch.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": k + 1, "name": n, "item": f"{URL}/{'' if u == 'index.html' else u}"} for k, (n, u) in enumerate(items)]})
    canon = URL + '/' + ('' if fn == 'index.html' else fn)
    ld = ''.join(f'<script type="application/ld+json">{json.dumps(s)}</script>' for s in sch)
    nav = ''.join(f'<a href="{u}"{" class=on" if u == fn else ""}>{n}</a>' for n, u in NAV)
    ql = ''.join(f'<li><a href="{u}">{n}</a></li>' for n, u in QL)
    html = f'''<!DOCTYPE html>
<html lang="en-IN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="canonical" href="{canon}"><meta name="theme-color" content="#0b2545">
<!-- Google Search Console: paste your verification meta tag here -->
<meta property="og:type" content="website"><meta property="og:site_name" content="MS PVC Panels"><meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}"><meta property="og:url" content="{canon}"><meta property="og:image" content="{URL}/images/banners/hero-banner.jpg"><meta property="og:locale" content="en_IN">
<link rel="icon" href="images/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="css/styles.css">{ld}</head>
<body class="{cls}"><a class="skip" href="#main">Skip to content</a>
<header><div class="wrap bar"><a class="logo" href="index.html" aria-label="MS PVC Panels home"><img class="logo-img" src="images/logo.png" alt="MS PVC Panels logo" width="44" height="44" onerror="this.onerror=null;this.src='images/logo-placeholder.svg'"><span class="lt">MS <i>PVC</i> Panels</span></a>
<button class="burger" type="button" aria-label="Open menu" aria-expanded="false">&#9776;</button>
<nav class="nav" aria-label="Main">{nav}</nav>
<a class="btn btn-wa hdr-wa" href="{GEN}" target="_blank" rel="noopener">{WAI} WhatsApp Enquiry</a></div></header>
<main id="main">{bc}{body}</main>
<footer><div class="wrap fgrid"><div><div class="logo flogo"><span class="lt">MS <i>PVC</i> Panels</span></div><p>(A unit of MS Traders)<br>PVC panels, WPC panels and interior hardware in Hyderabad, supplied across Telangana.</p></div>
<div><h3>Quick Links</h3><ul>{ql}</ul></div>
<div><h3>Contact</h3><ul><li><a href="tel:+919848487800">{TEL} {T1}</a></li><li><a href="tel:+919935064878">{TEL} {T2}</a></li>
<li><a href="{wa('Hello MS PVC Panels, I have an enquiry.', P1)}" target="_blank" rel="noopener">{WAI} WhatsApp us</a></li></ul>
<h3>Location</h3><p><a href="{DIRS}" target="_blank" rel="noopener">{ADDR1},<br>Hyderabad, Telangana.</a></p></div></div>
<div class="wrap copy"><span>&copy; 2026 MS PVC Panels (MS Traders). All rights reserved.</span><span><a href="privacy-policy.html">Privacy Policy</a> &nbsp;|&nbsp; <a href="terms-and-conditions.html">Terms &amp; Conditions</a></span></div></footer>
<a class="float" href="tel:+919848487800" aria-label="Call us now">{TEL}</a>
<dialog id="enq" aria-labelledby="enq-title"><div class="dh"><img id="enq-img" alt="" width="84" height="84"><div><h2 id="enq-title"></h2><div class="code" id="enq-meta"></div></div><button class="x" type="button" aria-label="Close">&times;</button></div>
<form id="enq-form"><h3>Interested in this Product?</h3><div id="enq-opts" class="two"></div>
<label>Your Name<input name="name" required autocomplete="name"></label>
<div class="two"><label>Mobile Number (optional)<input name="mobile" type="tel" inputmode="tel"></label><label>Quantity (optional)<input name="qty"></label></div>
<label>Message (optional)<textarea name="msg" rows="3"></textarea></label>
<label>Send to<select name="to"></select></label>
<button class="btn btn-wa" type="submit">{WAI} Send Enquiry on WhatsApp</button></form></dialog>
<script src="js/config.js" defer></script><script src="js/whatsapp.js" defer></script><script src="js/main.js" defer></script></body></html>'''
    w(fn, html)

def img(src, alt, cls='cimg', lazy=True, wh=400):
    return f'<img class="{cls}" src="images/{src}" alt="{alt}" width="{wh}" height="{wh}"{" loading=lazy" if lazy else ""} onerror="this.onerror=null;this.src=\'images/placeholder.svg\'">'

def pname(cat, i, name=None):
    if name: return name, f"{cat['code']}-{i:03d}"
    if cat.get('models'):
        m = cat['models'][i - 1]
        return (m[1] if len(m) > 1 else f"{cat['single']} {m[0]}"), m[0]
    return f"{cat['single']} {i:03d}", f"{cat['code']}-{i:03d}"

def card(cat, i, name=None, desc=None, dims=None):
    nm, cd = pname(cat, i, name)
    d = cat.get('dims', '') if dims is None else dims
    fn = f"{cat['slug']}/{slugn(cat, i)}.jpg" if cat['slug'] != 'hardware' else f"hardware/{nm.lower().replace(' ', '-')}.jpg"
    alt = f"{nm} - {cat['title']} at MS PVC Panels, Hyderabad"
    p = f'<p class="pd">{desc}</p>' if desc else ''
    sp = f'<ul class="specs">{specs(d)}</ul>' if d else ''
    pr = cat.get('prices', '')
    return f'''<article class="card" data-name="{nm}" data-code="{cd}" data-cat="{cat['title']}" data-dims="{d}" data-prices="{pr}">
{img(fn, alt)}<div class="cbody"><h3>{nm}</h3><div class="code">{cd}</div>{p}{sp}{price_html(pr)}
<button class="btn btn-wa enq-btn" type="button">{WAI} Enquire on WhatsApp</button></div></article>'''

def prod_ld(cat, items):
    pv = [int(x.split('=')[1]) for x in cat.get('prices', '').split('|') if x]
    return {"@context": "https://schema.org", "@type": "ItemList", "name": cat['title'] + ' at MS PVC Panels, Hyderabad', "itemListElement": [
        {"@type": "ListItem", "position": k + 1, "item": {"@type": "Product", "name": n, "sku": c, "category": cat['title'], "brand": {"@type": "Brand", "name": "MS PVC Panels"},
         "description": d, "image": f"{URL}/images/{f}"}|({"offers": {"@type": "AggregateOffer", "priceCurrency": "INR", "lowPrice": min(pv), "highPrice": max(pv)}} if pv else {})} for k, (n, c, d, f) in enumerate(items)]}

def tile_cat(c):
    cov = f"{c['slug']}/category-cover.jpg"
    return f'''<article class="card cat"><a href="{c['file']}" tabindex="-1" aria-hidden="true">{img(cov, c['title'] + ' category - MS PVC Panels Hyderabad', wh=400)}</a>
<div class="cbody"><h3>{c['title']}</h3><p>{c['desc']}</p><a class="btn btn-navy" href="{c['file']}">Explore Products</a></div></article>'''

# ---- category pages
for c in CATS:
    cards = ''.join(card(c, i) for i in range(1, c['n'] + 1))
    items = [(pname(c, i)[0], pname(c, i)[1], f"{c['title']} model {pname(c, i)[1]} available at MS PVC Panels, Hyderabad and across Telangana.", f"{c['slug']}/{slugn(c, i)}.jpg") for i in range(1, c['n'] + 1)]
    others = ' &middot; '.join(f'<a href="{o["file"]}">{o["title"]}</a>' for o in ALLC if o['file'] != c['file'])
    body = f'''<section class="pagehead"><div class="wrap"><h1>{c['title']} in Hyderabad</h1><p class="prose">{c['intro']}</p></div></section>
<section><div class="wrap"><h2>Choose a design</h2><p class="sub">Images are being updated. Prices are shown for each size. Tap Enquire on WhatsApp on any design to send us its name, code, size and price.</p>
<div class="grid pgrid">{cards}</div>
<p class="sub" style="margin-top:30px">Also see: {others}</p></div></section>'''
    page(c['file'], c['mt'], c['md'], body, [prod_ld(c, items)], [('Products', 'products.html'), (c['title'], c['file'])], 'deco' if c.get('deco') else '')

# ---- hardware
hc = ''.join(card(HWC | dict(single=n, code='HW'), i + 1, name=n, desc=d, dims='') for i, (n, d) in enumerate(HW))
hitems = [(n, f'HW-{i + 1:03d}', d, f"hardware/{n.lower().replace(' ', '-')}.jpg") for i, (n, d) in enumerate(HW)]
page(HWC['file'], 'PVC Clips, L Trims, U Trims & Gypsum Channels in Hyderabad | MS PVC Panels',
     'PVC accessories in Hyderabad: gypsum channels, gypsum screws, PVC clips, PVC L trims, PVC U trims and interior installation hardware at MS PVC Panels. Enquire on WhatsApp.',
     f'''<section class="pagehead"><div class="wrap"><h1>PVC Panel Hardware &amp; Accessories in Hyderabad</h1><p class="prose">Everything you need to install PVC panels in one place: gypsum channels, screws, PVC clips, L trims, U trims and other interior hardware. Message us with your requirement and we will help.</p></div></section>
<section><div class="wrap"><div class="grid pgrid">{hc}</div>
<p class="sub" style="margin-top:30px">Looking for panels? See <a href="pvc-panels.html">PVC Panels</a>, <a href="fluted-panels.html">Fluted Panels</a> or <a href="wpc-panels.html">WPC Panels</a>.</p></div></section>''',
     [prod_ld(HWC, hitems)], [('Products', 'products.html'), ('Hardware & Accessories', HWC['file'])])

# ---- home
WHY = [('🎨', 'Wide Variety of Designs', 'Dozens of panel designs across PVC, fluted, Bahubali fluted and WPC.'), ('📏', 'Multiple Sizes Available', 'Panels in 10 feet and 12 feet lengths (Bahubali in 10 feet), plus WPC panel sizes.'),
       ('✅', 'Quality Products', 'Durable panels chosen for a clean, long-lasting finish.'), ('🔧', 'Complete PVC Accessories', 'Clips, trims, gypsum channels and screws under one roof.'),
       ('🤝', 'Customer-Friendly Service', 'Talk to us directly on call or WhatsApp. No forms, no waiting.'), ('📍', 'Located in Hyderabad', 'Serving customers in Hyderabad and surrounding areas of Telangana.')]
why = ''.join(f'<div class="tile"><i aria-hidden="true">{a}</i><h3>{b}</h3><p>{d}</p></div>' for a, b, d in WHY)
cats = ''.join(tile_cat(c) for c in ALLC)
def contact_cards():
    return f'''<div class="grid">
<div class="tile"><h3>{T1}</h3><p class="acts"><a class="btn btn-navy" href="tel:+919848487800">{TEL} Call</a><a class="btn btn-wa" href="{wa('Hello MS PVC Panels, I have an enquiry.', P1)}" target="_blank" rel="noopener">{WAI} WhatsApp</a></p></div>
<div class="tile"><h3>{T2}</h3><p class="acts"><a class="btn btn-navy" href="tel:+919935064878">{TEL} Call</a><a class="btn btn-wa" href="{wa('Hello MS PVC Panels, I have an enquiry.', P2)}" target="_blank" rel="noopener">{WAI} WhatsApp</a></p></div>
<div class="tile"><h3>Our Shop</h3><p>MS PVC Panels (MS Traders)<br>{ADDR}</p><p class="acts"><a class="btn btn-navy" href="{DIRS}" target="_blank" rel="noopener">&#128205; Get Directions</a></p></div></div>'''
hero = f'''<section class="hero"><img src="images/banners/hero-banner.jpg" alt="Modern PVC wall panels in a stylish interior - MS PVC Panels Hyderabad" width="1600" height="700" onerror="this.onerror=null;this.src='images/placeholder.svg'">
<div class="wrap"><h1>Premium PVC Panels &amp; Interior Solutions in Hyderabad</h1>
<p>Explore a wide range of PVC Panels, WPC Panels, Fluted Panels, Bahubali Fluted Panels and Interior Hardware at MS PVC Panels.</p>
<div class="acts"><a class="btn btn-gold" href="products.html">Explore Products</a><a class="btn btn-wa" href="{GEN}" target="_blank" rel="noopener">{WAI} Enquire on WhatsApp</a></div></div></section>'''
FAQ = [('Where is MS PVC Panels located?', 'We are at ' + ADDR + '. Use the map on this page for directions.'),
       ('Do you supply outside Hyderabad?', 'Yes. We supply customers in Hyderabad and across Telangana. Call or WhatsApp us to confirm delivery to your town.'),
       ('What are the prices of PVC panels?', 'Prices are shown for each size on every product page. Message us on WhatsApp for the latest price for your quantity.'),
       ('How do I enquire about a panel?', 'Open a category, pick a model and tap Enquire on WhatsApp. The message carries the model number, size, price and photo link so we can reply quickly.')]
FAQLD = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}
faq = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)
chips = ''.join(f'<span>{a}</span>' for a in AREAS)
page('index.html', 'PVC Panels in Hyderabad & Telangana | PVC Panel Dealers & Suppliers | MS PVC Panels',
     'MS PVC Panels, Dammaiguda, Hyderabad: PVC wall and ceiling panels, fluted panels, Bahubali fluted panels, WPC panels, PVC clips, L and U trims. Supplying all over Telangana. Enquire on WhatsApp.',
     hero + f'''<div class="strip"><div class="wrap"><span>&#128205; {ADDR1}, Hyderabad</span><span>&#128666; Supplying across Telangana</span><a href="tel:+919848487800">{TEL} Call {T1}</a></div></div>
<section><div class="wrap"><h2>Our product categories</h2><p class="sub">Pick a category to see every model and enquire on WhatsApp.</p><div class="grid">{cats}</div></div></section>
<section class="alt"><div class="wrap"><h2>Why choose MS PVC Panels?</h2><p class="sub">What customers in Hyderabad and Telangana can expect from us.</p><div class="grid">{why}</div></div></section>
<section><div class="wrap prose"><h2>About MS PVC Panels</h2><p>MS PVC Panels is operated by MS Traders in Hyderabad, Telangana. We specialise in PVC panels, WPC panels, decorative wall panels, fluted panels and the interior hardware needed to install them. We serve homeowners, interior designers and contractors in Hyderabad and across Telangana.</p><p><a class="btn btn-navy" href="about-us.html">Read more about us</a></p></div></section>
<section class="alt"><div class="wrap"><h2>Visit our shop</h2><p class="sub">{ADDR}</p>{MAP}<p style="margin-top:16px"><a class="btn btn-navy" href="{DIRS}" target="_blank" rel="noopener">&#128205; Get Directions</a></p></div></section>
<section><div class="wrap"><h2>Supplying all over Telangana</h2><p class="sub">Based in Hyderabad, we supply PVC panels and hardware to customers in these areas and more. Call us to confirm delivery to your town.</p><div class="chips">{chips}</div></div></section>
<section class="alt"><div class="wrap prose"><h2>Frequently asked questions</h2><div class="faq">{faq}</div></div></section>
<section><div class="wrap"><h2>Contact us</h2><p class="sub">Call or message us. We usually reply on WhatsApp.</p>{contact_cards()}<p style="margin-top:20px"><a class="btn btn-gold" href="contact-us.html">Send an enquiry</a></p></div></section>''',
     [LB, FAQLD])

# ---- products, about, contact, legal, 404
page('products.html', 'PVC Panels, Fluted Panels, WPC Panels & Hardware in Hyderabad & Telangana | MS PVC Panels',
     'All products at MS PVC Panels, Hyderabad: PVC panels, fluted panels, Bahubali fluted panels, WPC panels and PVC hardware. Choose a category and enquire on WhatsApp.',
     f'<section class="pagehead"><div class="wrap"><h1>Our Products</h1><p class="prose">PVC panels and interior hardware for customers in Hyderabad and Telangana. Choose a category.</p></div></section><section><div class="wrap"><div class="grid">{cats}</div></div></section>',
     crumbs=[('Products', 'products.html')])
page('about-us.html', 'About MS PVC Panels | PVC Panel Suppliers in Hyderabad, Telangana',
     'MS PVC Panels, operated by MS Traders, supplies PVC panels, WPC panels, fluted panels and interior hardware to customers in Hyderabad and across Telangana.',
     f'''<section class="pagehead"><div class="wrap"><h1>About MS PVC Panels</h1></div></section>
<section><div class="wrap prose"><p>MS PVC Panels is a unit of MS Traders, based in Hyderabad, Telangana. We supply PVC panels, WPC panels, decorative wall panels, fluted panels and Bahubali fluted panels, along with the interior hardware that goes with them.</p>
<h2>What we offer</h2><p>Our range covers <a href="pvc-panels.html">PVC panels</a>, <a href="fluted-panels.html">fluted PVC panels</a>, <a href="bahubali-panels.html">Bahubali fluted panels</a> and <a href="wpc-panels.html">WPC panels</a>. For installation we stock <a href="hardware-accessories.html">gypsum channels, screws, PVC clips, L trims and U trims</a>.</p>
<h2>Who we serve</h2><p>We serve homeowners, interior designers, contractors and shop owners in Hyderabad and surrounding areas of Telangana.</p>
<h2>How to order</h2><p>Browse a category, pick a design and send an enquiry on WhatsApp. The message includes the product name, code and size, so we can reply quickly. You can also <a href="contact-us.html">call us</a>.</p>
<p><a class="btn btn-wa" href="{GEN}" target="_blank" rel="noopener">{WAI} Enquire on WhatsApp</a></p></div></section>''', crumbs=[('About Us', 'about-us.html')])
page('contact-us.html', 'Contact MS PVC Panels | PVC Panel Shop in Hyderabad, Telangana',
     'Contact MS PVC Panels at Dammaiguda, Hyderabad, Telangana. Call or WhatsApp +91 9848487800 or +91 9935064878 for PVC panels, WPC panels, fluted panels and accessories.',
     f'''<section class="pagehead"><div class="wrap"><h1>Contact MS PVC Panels</h1><p class="prose">Call us, message us on WhatsApp or send an enquiry below.</p></div></section>
<section><div class="wrap">{contact_cards()}
<div class="prose" style="margin-top:30px"><h2>Send an enquiry</h2>
<form id="contact-form" class="box"><label>Your Name<input name="name" required autocomplete="name"></label><label>Mobile Number (optional)<input name="mobile" type="tel"></label>
<label>Message<textarea name="msg" rows="4" required></textarea></label><label>Send to<select name="to"></select></label>
<button class="btn btn-wa" type="submit">{WAI} Send Enquiry on WhatsApp</button></form>
</div><h2 style="margin-top:34px">Find our shop</h2><p class="sub">{ADDR}</p>{MAP}</div></section>''', [LB], [('Contact Us', 'contact-us.html')])
def legal(fn, t, txt): page(fn, f'{t} | MS PVC Panels', f'{t} for the MS PVC Panels website.', f'<section class="pagehead"><div class="wrap"><h1>{t}</h1></div></section><section><div class="wrap prose">{txt}</div></section>', crumbs=[(t, fn)])
legal('privacy-policy.html', 'Privacy Policy', '<p>This website does not store your personal data. When you send a WhatsApp enquiry, the details you type (name, mobile number, quantity, message) are placed in a WhatsApp message that you choose to send to us. We use them only to reply to your enquiry.</p><p>Contact us on +91 9848487800 for any privacy question.</p>')
legal('terms-and-conditions.html', 'Terms & Conditions', '<p>Product images, names and designs shown on this website are for reference. Availability, sizes and prices are confirmed by MS PVC Panels when you enquire. Colours may vary slightly from photos. By using this site you agree to these terms.</p>')
page('404.html', 'Page not found | MS PVC Panels', 'Page not found. Go back to the MS PVC Panels home page.', '<section><div class="wrap prose"><h1>Page not found</h1><p>This page does not exist. Go to the <a href="index.html">home page</a> or see our <a href="products.html">products</a>.</p></div></section>')

# ---- seo files
urls = ['index.html'] + [f for _, f in NAV[1:]] + ['bahubali-panels.html', 'privacy-policy.html', 'terms-and-conditions.html']
urls = list(dict.fromkeys(urls))
w('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>{URL}/{"" if u == "index.html" else u}</loc><lastmod>{DATE}</lastmod></url>\n' for u in urls) + '</urlset>\n')
w('robots.txt', f'User-agent: *\nAllow: /\n\nSitemap: {URL}/sitemap.xml\n')

# ---- assets
w('images/placeholder.svg', '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400"><rect width="400" height="400" fill="#e9eef5"/>' + ''.join(f'<rect x="{x}" y="0" width="26" height="400" fill="#dbe3ee"/>' for x in range(20, 400, 52)) + '<text x="200" y="196" text-anchor="middle" font-family="Arial" font-size="22" fill="#0b2545">Product image</text><text x="200" y="226" text-anchor="middle" font-family="Arial" font-size="16" fill="#667">coming soon</text></svg>')
w('images/logo-placeholder.svg', '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect x="2" y="2" width="60" height="60" rx="10" fill="#f5f7fb" stroke="#9aa8bd" stroke-width="2" stroke-dasharray="5 4"/><text x="32" y="38" text-anchor="middle" font-family="Arial" font-weight="bold" font-size="14" fill="#667">LOGO</text></svg>')
w('images/favicon.svg', '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#0b2545"/><text x="32" y="42" text-anchor="middle" font-family="Arial" font-weight="bold" font-size="26" fill="#d99a2b">MS</text></svg>')
for c in CATS:
    names = [f"{slugn(c, i)}.jpg   (model {pname(c, i)[1]})" for i in range(1, c['n'] + 1)]
    w(f"images/{c['slug']}/README.txt", 'Drop your photos here using EXACTLY these file names (square photos, about 800x800 px, under 150 KB):\ncategory-cover.jpg  (picture shown on the category card)\n' + '\n'.join(names) + '\n')
w('images/hardware/README.txt', 'Square photos (about 800x800 px). File names:\ncategory-cover.jpg\n' + '\n'.join(f"{n.lower().replace(' ', '-')}.jpg" for n, _ in HW) + '\n')
w('images/banners/README.txt', 'hero-banner.jpg: wide home page banner, about 1600x700 px, under 250 KB. This is also the social sharing image.\n')

w('js/config.js', "/* Edit WhatsApp numbers here. Numbers use country code, no + or spaces. First number is the default. */\nwindow.MS={brand:'MS PVC Panels',numbers:[{label:'Primary: +91 9848487800',n:'919848487800'},{label:'Alternative: +91 9935064878',n:'919935064878'}]};\n")
w('js/whatsapp.js', r'''window.WA={
parse:function(s){return(s||'').split(';').filter(Boolean).map(function(p){var a=p.split('=');return{l:a[0].trim(),v:a[1].split('|').map(function(x){return x.trim()})}})},
message:function(o){var L=['Hello '+window.MS.brand+',',''];
if(o.product){L.push('I am interested in the following product:','','Product: '+o.product,'Product Code: '+o.code,'Category: '+o.cat);if(o.image)L.push('','Product Image (tap to view):',o.image,'')}else{L.push('I would like to make an enquiry.','')}
(o.dims||[]).forEach(function(d){L.push(d.l+': '+d.v)});
if(o.price)L.push('Price: Rs. '+o.price);
if(o.qty)L.push('Quantity: '+o.qty);
L.push('','Customer Name: '+o.name);if(o.mobile)L.push('Mobile Number: '+o.mobile);if(o.msg)L.push('Message: '+o.msg);
L.push('',o.product?'Please share more details and your best price.':'Please get in touch with me.','','Thank you.');return L.join('\n')},
url:function(n,t){return'https://wa.me/'+n+'?text='+encodeURIComponent(t)}};
''')
w('js/main.js', r'''(function(){var $=function(s,r){return(r||document).querySelector(s)},$$=function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))};
var b=$('.burger'),nav=$('.nav');b.onclick=function(){var o=nav.classList.toggle('open');b.setAttribute('aria-expanded',o)};
$$('select[name=to]').forEach(function(s){s.innerHTML=MS.numbers.map(function(n){return'<option value="'+n.n+'">'+n.label+'</option>'}).join('')});
$$('.card[data-dims]').forEach(function(c){var u=$('.specs',c);if(u)u.innerHTML=WA.parse(c.dataset.dims).map(function(d){return'<li><b>'+(d.l==='Size'?'Available Sizes':d.l)+':</b> '+d.v.join(' &amp; ')+'</li>'}).join('')});
var dlg=$('#enq'),f=$('#enq-form'),cur;
$$('.enq-btn').forEach(function(btn){btn.onclick=function(){var c=btn.closest('.card');var ci=$('img',c).src;cur={prices:c.dataset.prices||'',product:c.dataset.name,code:c.dataset.code,cat:c.dataset.cat,dims:WA.parse(c.dataset.dims),image:/^https?:/.test(ci)&&!/placeholder\.svg/.test(ci)?ci:''};
$('#enq-title').textContent=cur.product;$('#enq-meta').textContent=cur.code+' | '+cur.cat;var im=$('#enq-img');im.src=$('img',c).src;im.alt=cur.product;
$('#enq-opts').innerHTML=cur.dims.map(function(d,i){return d.v.length>1?'<label>'+d.l+'<select data-i="'+i+'">'+d.v.map(function(v){return'<option>'+v+'</option>'}).join('')+'</select></label>':''}).join('');
dlg.showModal()}});
$('.x',dlg).onclick=function(){dlg.close()};dlg.addEventListener('click',function(e){if(e.target===dlg)dlg.close()});
function go(form,extra){var d=new FormData(form),o=Object.assign({name:d.get('name'),mobile:d.get('mobile'),qty:d.get('qty'),msg:d.get('msg')},extra||{});
window.open(WA.url(d.get('to'),WA.message(o)),'_blank','noopener')}
f.onsubmit=function(e){e.preventDefault();var dims=cur.dims.map(function(d,i){var s=$('[data-i="'+i+'"]',f);return{l:d.l,v:s?s.value:d.v[0]}});var pm={};cur.prices.split('|').forEach(function(x){var a=x.split('=');if(a[1])pm[a[0]]=a[1]});var sz=dims.filter(function(d){return d.l==='Size'})[0];go(f,{product:cur.product,code:cur.code,cat:cur.cat,dims:dims,image:cur.image,price:pm.all||(sz&&pm[sz.v])||''});dlg.close()};
var cf=$('#contact-form');if(cf)cf.onsubmit=function(e){e.preventDefault();go(cf)};
})();
''')
w('css/styles.css', r''':root{--n:#0b2545;--n2:#13315c;--g:#d99a2b;--bg:#f5f7fb;--r:12px}
*{box-sizing:border-box}body{margin:0;font:16px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;color:#1d2733;background:#fff}
img{max-width:100%;display:block}a{color:var(--n2)}h1,h2,h3{line-height:1.25}
.wrap{max-width:1180px;margin:auto;padding:0 18px}.skip{position:absolute;left:-999px}.skip:focus{left:8px;top:8px;background:#fff;padding:8px;z-index:99}
:focus-visible{outline:3px solid var(--g);outline-offset:2px}
header{position:sticky;top:0;z-index:50;background:#fff;box-shadow:0 1px 8px #0b25451a}
.bar{display:flex;align-items:center;gap:16px;min-height:64px}
.logo{display:inline-flex;align-items:center;gap:10px;font-weight:800;font-size:1.3rem;color:var(--n);text-decoration:none;letter-spacing:-.3px}.logo i{font-style:normal;color:var(--g)}
.logo-img{width:44px;height:44px;object-fit:contain;flex:none;border-radius:8px}
.burger{margin-left:auto;background:none;border:1px solid #c9d2de;border-radius:8px;font-size:1.3rem;padding:4px 11px;cursor:pointer}
.nav{display:none;position:absolute;left:0;right:0;top:100%;background:#fff;flex-direction:column;padding:6px 18px 14px;box-shadow:0 10px 14px #0002}.nav.open{display:flex}
.nav a{padding:11px 0;text-decoration:none;color:var(--n);font-weight:600;font-size:.95rem;border-bottom:1px solid #eef1f6}.nav a.on,.nav a:hover{color:var(--g)}
.hdr-wa{display:none}
@media(min-width:1050px){.burger{display:none}.nav{display:flex;position:static;flex-direction:row;gap:15px;padding:0;box-shadow:none;margin-left:auto}.nav a{border:0;padding:6px 0;font-size:.9rem}.hdr-wa{display:inline-flex}}
.btn{display:inline-flex;gap:8px;align-items:center;justify-content:center;padding:11px 20px;border-radius:999px;font-weight:700;font-size:.95rem;font-family:inherit;text-decoration:none;border:0;cursor:pointer;transition:transform .2s,background .2s}
.btn:hover{transform:translateY(-2px)}.btn-wa{background:#1fa855;color:#fff}.btn-wa:hover{background:#188a45}.btn-gold{background:var(--g);color:#1a1200}.btn-navy{background:var(--n);color:#fff}
.hero{position:relative;background:linear-gradient(135deg,var(--n),var(--n2));color:#fff;overflow:hidden}
.hero img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.28}
.hero .wrap{position:relative;padding:72px 18px 80px}.hero h1{font-size:clamp(2rem,5.5vw,3.4rem);margin:0 0 16px;max-width:780px;letter-spacing:-.5px}
.hero p{max-width:620px;font-size:1.1rem;color:#e6ecf5}.acts{display:flex;flex-wrap:wrap;gap:12px;margin:22px 0 0}
section{padding:50px 0}.alt{background:var(--bg)}
h2{color:var(--n);font-size:clamp(1.45rem,3.5vw,2rem);margin:0 0 8px}.sub{color:#59667a;margin:0 0 26px}.prose{max-width:760px}
.grid{display:grid;gap:18px;grid-template-columns:repeat(auto-fill,minmax(260px,1fr))}
.pgrid{grid-template-columns:repeat(2,1fr);gap:12px}@media(min-width:700px){.pgrid{grid-template-columns:repeat(3,1fr);gap:18px}}@media(min-width:1000px){.pgrid{grid-template-columns:repeat(4,1fr)}}
.tile,.card{background:#fff;border:1px solid #e1e7ef;border-radius:var(--r);overflow:hidden;transition:transform .25s,box-shadow .25s}
.tile:hover,.card:hover{transform:translateY(-4px);box-shadow:0 14px 30px #0b25451f}
.tile{padding:22px}.tile i{font-style:normal;font-size:1.8rem}.tile h3{margin:8px 0 4px;color:var(--n)}.tile p{margin:0}
.tile .acts{margin-top:14px}
.cimg{aspect-ratio:1/1;width:100%;height:auto;object-fit:cover;background:#e9eef5}.cat .cimg{aspect-ratio:4/3}
.cbody{padding:12px 14px 16px}.cat .cbody{padding:16px}.card h3{margin:0;font-size:1.02rem;color:var(--n)}.cat p{margin:6px 0 14px;color:#59667a}
.code{font-size:.82rem;color:#a8700a;font-weight:700}.pd{margin:6px 0 0;font-size:.85rem;color:#59667a}
.price{list-style:none;margin:0 0 12px;padding:0;font-size:.9rem;color:#1d2733}.price b{color:#0b6b36;font-size:1rem}
.strip{background:var(--n);color:#fff;font-size:.92rem}.strip .wrap{display:flex;flex-wrap:wrap;gap:8px 26px;justify-content:center;padding-top:11px;padding-bottom:11px}.strip a{color:var(--g);font-weight:700;text-decoration:none;display:inline-flex;align-items:center;gap:6px}
.map{border-radius:var(--r);overflow:hidden;border:1px solid #e1e7ef;box-shadow:0 8px 24px #0b254514}.map iframe{display:block;width:100%;height:380px}
.chips{display:flex;flex-wrap:wrap;gap:10px}.chips span{background:#fff;border:1px solid #e1e7ef;border-radius:999px;padding:7px 16px;color:var(--n);font-weight:600;font-size:.92rem}
.faq details{background:#fff;border:1px solid #e1e7ef;border-radius:var(--r);margin-bottom:10px;padding:0 18px}.faq summary{cursor:pointer;padding:14px 0;font-weight:700;color:var(--n)}.faq details p{margin:0 0 14px;color:#3b4757}
.specs{list-style:none;margin:8px 0 12px;padding:0;font-size:.85rem;color:#4b5563}.card .enq-btn{width:100%;padding:9px 8px;font-size:.82rem}
.crumbs{font-size:.85rem;padding:14px 18px;max-width:1180px;margin:auto;color:#667}.crumbs a{text-decoration:none}
.pagehead{background:var(--bg);padding:8px 0 30px}.pagehead h1{color:var(--n);margin:6px 0 10px;font-size:clamp(1.7rem,4vw,2.4rem)}
.deco .pagehead{background:linear-gradient(135deg,var(--n),#3b2a08);color:#fff}.deco .pagehead h1{color:#f3c470}.deco .card{border-color:var(--g)}
footer{background:var(--n);color:#cdd7e6;padding:44px 0 20px;margin-top:20px}footer a{color:#fff;text-decoration:none}footer a:hover{color:var(--g)}
footer h3{color:#fff;margin:0 0 8px;font-size:1rem}.flogo{color:#fff}.fgrid{display:grid;gap:26px;grid-template-columns:repeat(auto-fit,minmax(210px,1fr))}
footer ul{list-style:none;padding:0;margin:0 0 14px}footer li{margin:6px 0}footer li a{display:inline-flex;gap:8px;align-items:center}
.copy{display:flex;flex-wrap:wrap;justify-content:space-between;gap:10px;margin-top:30px;padding-top:16px;border-top:1px solid #ffffff26;font-size:.88rem}
.float svg{width:26px;height:26px}.float{position:fixed;right:16px;bottom:16px;z-index:60;width:56px;height:56px;border-radius:50%;background:#1565c0;color:#fff;display:grid;place-items:center;box-shadow:0 6px 18px #0004}
dialog{border:0;border-radius:16px;padding:0;width:min(540px,94vw);max-height:92vh}dialog::backdrop{background:#000a}
.dh{display:flex;gap:14px;padding:16px 18px;background:var(--bg);align-items:center}.dh img{width:84px;height:84px;object-fit:cover;border-radius:10px;flex:none}.dh h2{font-size:1.15rem;margin:0}
.x{margin-left:auto;background:none;border:0;font-size:1.8rem;cursor:pointer;color:var(--n)}
form{padding:18px;display:grid;gap:12px}form h3{margin:0;color:var(--n)}.box{padding:0}label{font-size:.85rem;font-weight:600;display:grid;gap:4px}
input,select,textarea{font:inherit;padding:10px;border:1px solid #c0cad8;border-radius:8px;width:100%;background:#fff}.two{display:grid;gap:12px;grid-template-columns:1fr 1fr}.two:empty{display:none}
@media(prefers-reduced-motion:reduce){*{transition:none!important}}
''')
print('built')
