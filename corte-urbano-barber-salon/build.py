P=[('index','Home'),('services','Services'),('gallery','Gallery'),('about','About'),('contact','Visit')]
ADDR='317 B Chatham Dr, Newport News, VA 23602';TEL='757-898-3437'
def page(slug,title,desc,body):
    nav=''.join(f'<li><a href="{"/" if s=="index" else "/"+s}"{" aria-current=page" if s==slug else ""}>{n}</a></li>' for s,n in P)
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | Corte Urbano Barber &amp; Salon, Newport News</title><meta name="description" content="{desc}">
<link rel="icon" href="/assets/logo.jpg"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700;800&family=Barlow:wght@400;600&display=swap" rel="stylesheet"><link rel="stylesheet" href="/assets/style.css"></head><body>
<header><div class="wrap nav"><a class="brand" href="/"><img src="/assets/logo.jpg" alt="">Corte Urbano</a><nav aria-label="Main"><button class="menu" aria-expanded="false">Menu</button><ul>{nav}</ul></nav></div><div class="pole"></div></header>
<main>{body}</main>
<footer><div class="wrap"><div><h3>Corte Urbano Barber &amp; Salon</h3><p>{ADDR}<br>Next to Tobacco &amp; Vape, unit 317 B</p></div>
<div><h3>Hours</h3><p>Mon–Fri 10 AM–6 PM<br>Sat 9 AM–6 PM<br>Sun closed</p></div>
<div><h3>Call</h3><p><a href="tel:+1{TEL.replace("-","")}">{TEL}</a><br>LGBTQ+ friendly</p></div></div></footer>
<script src="/assets/site.js"></script></body></html>'''
cta='<a class="btn" href="tel:+17578983437">Call to book</a>'
hours=[(1,'Monday','10 AM–6 PM'),(2,'Tuesday','10 AM–6 PM'),(3,'Wednesday','10 AM–6 PM'),(4,'Thursday','10 AM–6 PM'),(5,'Friday','10 AM–6 PM'),(6,'Saturday','9 AM–6 PM'),(0,'Sunday','Closed')]
ht=''.join(f'<tr data-d="{d}"><td>{n}</td><td>{h}</td></tr>' for d,n,h in hours)
svc=[('Fades','Low, mid and high fades blended clean, the cut regulars have been coming back for over seven years.'),('High fades','Sharp, tight and high on the sides, finished to match your top.'),('Line ups','Crisp edges along the hairline and neckline.'),('Design','Custom razor designs cut into the sides: bolts, florals, lines and more.'),('Mustache','Shaped and trimmed to suit your face.'),('Eyebrows','Cleaned up and defined.'),('Hot towel shave','A hot towel and a close, comfortable shave.')]
sg=''.join(f'<div><h3>{a}</h3><p>{b}</p></div>' for a,b in svc)
out={}
out['index']=page('index','Barber Shop in Newport News, VA','Fades, line ups and custom designs at Corte Urbano Barber & Salon, 317 B Chatham Dr, Newport News. Rated 4.6 from 181 reviews.',f'''
<div class="wrap hero"><div class="intro"><h1>Fresh cuts.<span>Clean lines.</span></h1><p>Corte Urbano is a neighborhood barber shop and salon in Newport News. Fades, line ups, razor designs and hot towel shaves, for the whole family.</p><div class="btns">{cta}<a class="btn alt" href="/services">See services</a></div><div class="rate"><b>4.6</b> rated by 181 Google reviewers</div></div><img src="/assets/cut-flower.jpg" alt="Floral razor design on a short natural cut"></div>
<div class="pole"></div>
<section><div class="wrap"><h2>What we do</h2><div class="grid">{sg[:sg.index("<div><h3>Mustache")]}</div><p style="margin-top:24px"><a class="btn alt" href="/services">All services</a></p></div></section>
<section class="band"><div class="wrap split"><img src="/assets/barber-chair.jpg" alt="A barber and a young client in the chair at Corte Urbano" loading="lazy"><div><h2>Patient with every client</h2><div class="quote"><p>Our barber was patient, professional and extremely talented with my 4 year old who was moving the whole time.</p><small>Local Guide review, paraphrased</small></div><div class="quote"><p>Prices are very reasonable for the quality, and low fades are the specialty.</p><small>Customer of 7+ years, paraphrased</small></div><a class="btn alt" href="/gallery">See the work</a></div></div></section>''')
out['services']=page('services','Services','Fades, high fades, line ups, designs, mustache, eyebrows and hot towel shaves in Newport News.',f'''
<div class="wrap ph"><h1>Services</h1><p style="margin-top:20px">Walk in or call ahead. Ask the shop for current pricing.</p></div><div class="pole"></div>
<section><div class="wrap"><div class="grid">{sg}</div></div></section>
<section class="band"><div class="wrap split"><div><h2>Designs cut to order</h2><p>Bring a reference photo or describe the idea. Bolts, petals and sweeping lines are cut into a clean fade with a razor.</p><p style="margin:20px 0">{cta}</p></div><img src="/assets/cut-bolt.jpg" alt="Lightning bolt design cut into the side of a fade" loading="lazy"></div></section>''')
gi=[('cut-flower','Floral design on a natural cut'),('cut-boy-fade','Skin fade with razor lines'),('cut-bolt','Bolt design with parallel lines'),('barber-chair','In the chair at Corte Urbano')]
out['gallery']=page('gallery','Gallery','Photos of fades, razor designs and the shop at Corte Urbano in Newport News.',f'''
<div class="wrap ph"><h1>Gallery</h1></div><div class="pole"></div>
<section><div class="wrap gal">{"".join(f'<img src="/assets/{n}.jpg" alt="{a}" loading="lazy">' for n,a in gi)}<img src="/assets/storefront.jpg" alt="Corte Urbano storefront on Chatham Drive" loading="lazy"></div></section>''')
out['about']=page('about','About','About Corte Urbano Barber & Salon, a Newport News neighborhood barber shop.','''
<div class="wrap ph"><h1>About us</h1></div><div class="pole"></div>
<section><div class="wrap split"><div><h2>Good music, good cuts</h2><p>Corte Urbano Barber &amp; Salon has been cutting hair on Chatham Drive for years. Customers describe a relaxed shop with good music, friendly staff and a clean space.</p><p style="margin-top:16px">Our barbers are known for low fades, sharp line ups and custom designs. We cut for kids, teens and adults, and we welcome everyone. The shop is LGBTQ+ friendly.</p></div><img src="/assets/storefront.jpg" alt="Corte Urbano storefront" loading="lazy"></div></section>
<section class="band"><div class="wrap"><h2>Rated 4.6 from 181 reviews</h2><div class="quote"><p>Great shop and always good customer assistance. Recommended to anyone.</p><small>Google review, paraphrased</small></div><div class="quote"><p>A great atmosphere and good music for a cut or shape up.</p><small>Google review, paraphrased</small></div></div></section>''')
out['contact']=page('contact','Visit & Contact','Hours, address and phone for Corte Urbano Barber & Salon, 317 B Chatham Dr, Newport News, VA.',f'''
<div class="wrap ph"><h1>Visit us</h1></div><div class="pole"></div>
<section><div class="wrap split"><div><h2>Hours</h2><table>{ht}</table><p style="margin-top:28px"><b style="color:var(--ink)">{ADDR}</b><br>Unit 317 B, beside Tobacco &amp; Vape</p><p style="margin:20px 0"><a class="btn" href="tel:+17578983437">Call {TEL}</a> <a class="btn alt" href="https://www.google.com/maps/search/?api=1&query=Corte+Urbano+Barber+Salon+317+B+Chatham+Dr+Newport+News+VA">Directions</a></p></div><img src="/assets/pano.jpg" alt="Shopping center parking lot in front of Corte Urbano" loading="lazy"></div></section>''')
for s,h in out.items(): open(f'{s}.html','w').write(h)
