#!/usr/bin/env python3
"""Builds the Together WorX static site. Run from the repo root: python3 _src/build.py"""
import os, json

SITE = "https://togetherworx.org"
DESC = "Together WorX creates unexpected possibilities through creativity and collaboration."

def head(title, desc, path, og="/assets/og.jpg"):
    full = title if title == "Together WorX" else f"{title} | Together WorX"
    ld = json.dumps({"@context": "https://schema.org", "@type": "NGO", "name": "Together WorX",
                     "legalName": "Together WorX Inc.", "url": SITE, "email": "hello@togetherworx.org",
                     "nonprofitStatus": "Nonprofit501c3", "slogan": "No one paints the whole picture."})
    return f'''<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{full}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}{path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Together WorX">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:title" content="{full}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}{og}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/together-worx-logo-dark.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter+Tight:wght@300;400;500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
<script type="application/ld+json">{ld}</script>
<script>document.documentElement.classList.remove('no-js')</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''

NAV = [("Our Work", "/work/"), ("About", "/about/"), ("Collaborate", "/collaborate/"), ("Contact", "/contact/")]

def header(current="", dark=False):
    links = "\n".join(f'      <a href="{u}"{" aria-current=\"page\"" if current == n else ""}>{n}</a>' for n, u in NAV)
    return f'''<header class="site-head{' on-dark' if dark else ''}">
    <a class="brand" href="/" aria-label="Together WorX home">Together Wor<span>X</span></a>
    <button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Main">
{links}
      <a class="support" href="/collaborate/#support">Support</a>
    </nav>
  </header>'''

STAY = '''<section class="stay" aria-labelledby="stay-h">
  <img class="bg" src="/assets/img/urban-zen-room.jpg" alt="" loading="lazy">
  <div class="fade" aria-hidden="true"></div>
  <div class="inner g12">
    <div class="copy">
      <h2 id="stay-h">Stay Connected.</h2>
      <p>Be the first to hear about new projects and collaborations.</p>
    </div>
    <form name="updates" method="POST" data-netlify="true" netlify-honeypot="bot-field" class="js-form" data-ok="Thank you. You're on the list.">
      <input type="hidden" name="form-name" value="updates">
      <p hidden><label>Leave this empty <input name="bot-field"></label></p>
      <label>Email address<input type="email" name="email" autocomplete="email" required></label>
      <button class="btn btn-light" type="submit">Subscribe</button>
      <p class="note" role="status"></p>
    </form>
  </div>
</section>'''

FOOT = '''<footer class="site-foot">
  <div class="foot-top">
    <div>
      <a class="foot-brand" href="/" aria-label="Together WorX home">Together Wor<span>X</span></a>
      <p class="foot-tag">No one paints the whole picture.</p>
    </div>
    <div class="foot-right">
      <nav class="foot-nav" aria-label="Footer">
        <a href="/work/">Our Work</a><a href="/about/">About</a><a href="/collaborate/">Collaborate</a><a href="/contact/">Contact</a><a href="/collaborate/#support">Support</a>
      </nav>
      <a class="foot-mail" href="mailto:hello@togetherworx.org">hello@togetherworx.org</a>
    </div>
  </div>
  <div class="legal"><span>© 2026 Together WorX · Together WorX Inc. is a registered 501(c)(3) nonprofit</span><a href="/privacy/">Privacy</a></div>
</footer>
<script src="/assets/site.js" defer></script>
</body>
</html>
'''

def page(path, title, desc, body, current="", stay=True, og="/assets/og.jpg"):
    html = head(title, desc, path, og) + body.replace("{{HEADER}}", header(current)) + (STAY if stay else "") + FOOT
    out = path.strip("/")
    d = os.path.join(".", out) if out else "."
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w") as f:
        f.write(html)
    return path

# ---------- shared project blocks ----------
P1 = '''<div class="g12 proj-a rv">
      <a class="main" href="/work/urban-zen/"><img src="/assets/img/urban-zen.jpg" alt="Guests in candlelight at Urban Zen for the first Together WorX event" width="1800" height="1350"></a>
      <figure class="over"><img src="/assets/img/group-bw.jpg" alt="Gary Zukav and Linda Francis with Infinity Song, Rebekah and guests at Urban Zen" loading="lazy" width="1200" height="900"></figure>
      <a class="text proj-text card-link" href="/work/urban-zen/">
        <p class="meta">Urban Zen | New York</p>
        <h3 class="h3">A Conversation with Gary Zukav and Linda Francis</h3>
        <p class="desc">Gary Zukav and Linda Francis in conversation at Donna Karan's Urban Zen, with a live performance by Infinity Song.</p>
      </a>
    </div>'''
P23 = '''<div class="g12 proj-b">
      <a class="left card-link rv" href="/work/art-of-coming-together/">
        <img src="/assets/img/gallery.jpg" alt="Guests gathered in the brick gallery for The Art of Coming Together" loading="lazy" width="1800" height="1350">
        <div class="proj-text">
          <p class="meta">New York | Hurricane Dorian Relief</p>
          <h3 class="h3">The Art of Coming Together</h3>
          <p class="with">With Gary Zukav and Linda Francis</p>
          <p class="desc">An evening of conversation, live music, and a collective artwork created by guests, raising funds for hurricane relief in the Bahamas.</p>
        </div>
      </a>
      <a class="right card-link rv" href="/work/science-of-spirituality/">
        <img src="/assets/img/science-talk.jpg" alt="Guests listening at The Science of Spirituality" loading="lazy" width="1350" height="1800">
        <img class="over2" src="/assets/img/fire-ceremony-2.jpg" alt="Guests gathered around a fire ceremony in a courtyard at The Science of Spirituality" loading="lazy" width="1000" height="1333">
        <div class="proj-text">
          <p class="meta">New York</p>
          <h3 class="h3">The Science of Spirituality</h3>
          <p class="with">With Dr. Anna Yusim and Dr. Srini Pillay</p>
          <p class="desc">An immersive experience exploring the connection between science and spirituality, combining thought-provoking conversations with interactive workshops.</p>
        </div>
      </a>
    </div>'''
P4 = '''<div class="g12 proj-c rv">
      <a class="flyer card-link" href="/work/soul-sunday/">
        <img src="/assets/img/flyer-soul-sunday.jpg" alt="Original flyer for Soul Sunday with Gary Zukav and Linda Francis at Tantris, West Hollywood" loading="lazy" width="1500" height="1500">
        <p class="cap">Original flyer</p>
      </a>
      <a class="proj-text card-link" href="/work/soul-sunday/">
        <p class="meta">Tantris | West Hollywood, California</p>
        <h3 class="h3">Soul Sunday</h3>
        <p class="with">Authentic Power &amp; Spiritual Partnership</p>
        <p class="desc">An afternoon with Gary Zukav and Linda Francis featuring movement, a community brunch, and a conversation on authentic power and spiritual partnership.</p>
      </a>
    </div>'''

# ---------- home ----------
home = '''<main id="main">
<section class="hero">
  <img class="poster" src="/assets/img/hero-poster.jpg" alt="" aria-hidden="true">
  <video id="film" muted loop playsinline preload="metadata" poster="/assets/img/hero-poster.jpg" aria-label="Hands painting bright streaks of color on a canvas"><source src="/assets/video/painting-loop.mp4" type="video/mp4"></video>
  <div class="on-dark">{{HEADER}}</div>
  <div class="hero-foot">
    <h1>No one paints<br><em>the whole picture.</em></h1>
    <div class="hero-links"><a class="explore" href="#work">Explore Our Work <span aria-hidden="true">↓</span></a><button class="pause" id="pause" type="button">Pause</button></div>
  </div>
</section>

<section class="idea g12">
  <h2 class="rv">What becomes possible<br><span>together.</span></h2>
  <p class="rv">Together WorX brings people together to turn ideas into reality through creativity and collaboration.</p>
</section>

<section class="work" id="work" aria-labelledby="work-h">
  <div class="g12 rule work-head"><h2 id="work-h">Our Work</h2><a class="tlink" href="/work/">All projects →</a></div>
  ''' + P1 + '''
  ''' + P23 + '''
</section>

<section class="founder" aria-labelledby="founder-h">
  <div class="g12 rule">
    <figure class="rv"><img src="/assets/img/bethesda-wide.jpg" alt="The Boyd family singing at Bethesda Fountain in Central Park" loading="lazy" width="2000" height="1500"><figcaption class="cap">Bethesda Fountain, Central Park</figcaption></figure>
    <div class="story rv">
      <p class="label">How it started</p>
      <h2 id="founder-h">It began with a song in the park.</h2>
      <p class="body">I was jogging through Central Park one Sunday when I heard voices so beautiful they seemed almost angelic. I followed the music to Bethesda Fountain, where a family was singing together. Their harmonies were extraordinary. I stood listening, completely captivated.</p>
      <p class="body">At the time, I was preparing the first Together WorX event. Gary Zukav and Linda Francis had agreed to speak, and Donna Karan's Urban Zen would be our setting. As I listened to the family, I began to imagine their voices filling that beautiful space. I knew I wanted them there.</p>
      <p style="margin-top:28px"><a class="tlink" href="/about/">Read the full story →</a></p>
      <p class="sig">Rebekah Hoyle</p>
      <p>Founder, Together WorX</p>
    </div>
  </div>
</section>

<section class="collab" aria-labelledby="collab-h">
  <div class="g12 rule">
    <div class="intro"><h2 id="collab-h">Collaborate.</h2><p>We welcome new ideas and opportunities to work together.</p></div>
    <div class="path p1"><h3 class="h3">Collaborate</h3><p>Have an idea or an interest in working together? We'd love to hear from you.</p><a class="tlink" href="/contact/?interest=collaborate">Get in touch →</a></div>
    <div class="path p2"><h3 class="h3">Support</h3><p>Help bring future Together WorX projects to life.</p><a class="tlink" href="https://donate.stripe.com/aFacN64Sw7XKcl4etDcEw01">Donate →</a></div>
  </div>
</section>
</main>
'''
pages = []
html = head("Together WorX", DESC, "/") + home.replace("{{HEADER}}", header()) + STAY + FOOT
open("index.html", "w").write(html); pages.append("/")

# ---------- our work ----------
ARCH = '''<section class="archive" aria-labelledby="arch-h">
  <div class="rule"><h2 id="arch-h">From the Archive</h2></div>
  <div class="arch-grid">
    <article class="rv">
      <figure class="arch-fig"><img class="tall" src="/assets/img/flyer-rising-tour.jpg" alt="Original flyer for The Rising Musical Family Tour featuring Infinity's Song, Victory and Syncopated Ladies, naming Together WorX as Bahamas relief partner" loading="lazy" width="1218" height="1624"></figure>
      <p class="cap">Original flyer</p>
      <h3 class="h3">The Rising Musical Family Tour</h3>
      <p class="meta">Harlem, New York | Planned Event</p>
      <p class="adesc">Featuring Infinity's Song, Victory, and Syncopated Ladies, with Together WorX supporting Bahamas relief alongside Roc Nation.</p>
      <p class="canceled">Canceled due to COVID.</p>
    </article>
    <article class="rv">
      <figure class="arch-fig"><img class="wide" src="/assets/img/artwork-robotics.jpg" alt="Original event artwork for Robotics, AI and Consciousness, with Hanson Robotics, AngelVest, Arcadia and Together WorX" loading="lazy" width="1752" height="897"></figure>
      <p class="cap">Original event artwork</p>
      <h3 class="h3">Robotics, AI and Consciousness</h3>
      <p class="meta">Arcadia Earth, New York | Planned Event, 2020</p>
      <p class="adesc">A planned conversation exploring robotics, artificial intelligence, and consciousness, featuring Sophia the Robot and a guided breathwork meditation.</p>
      <p class="canceled">Canceled due to COVID.</p>
    </article>
  </div>
</section>'''
work = '''<main id="main">
{{HEADER}}
<section class="work" style="padding-top:110px">
  <h1 class="page-title">Our Work</h1>
  ''' + P1 + P23 + P4 + '''
</section>
''' + ARCH + '''
</main>
'''
pages.append(page("/work/", "Our Work", "Projects and collaborations from Together WorX, from Urban Zen in New York to Tantris in Los Angeles.", work, "Our Work"))

def facts(rows):
    return '<dl class="facts">' + "".join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in rows) + '</dl>'

def nxt(label, href):
    return f'''<section class="next"><div class="in"><div><p class="label">Next</p><a class="big" href="{href}">{label} →</a></div><a class="btn btn-light" href="/collaborate/">Be part of the next one</a></div></section>'''

def top(label, title, sub):
    return f'''<section class="pj-top"><a class="back" href="/work/">← All projects</a><p class="label">{label}</p><h1>{title}</h1>{f'<p class="sub">{sub}</p>' if sub else ''}</section>'''

# urban zen
uz = '''<main id="main">
{{HEADER}}
''' + top("Urban Zen | New York", "A Conversation with Gary Zukav and Linda Francis", "") + '''
<img class="pj-hero" src="/assets/img/urban-zen.jpg" alt="The first Together WorX event at Urban Zen, a candlelit room with tall windows" width="1800" height="1350">
<section class="pj-body g12">
  <p class="lede">The first Together WorX event.</p>
  <div class="facts-wrap" style="grid-column:8/span 5">''' + facts([("Where", "Urban Zen, New York"), ("With", "Gary Zukav, Linda Francis and Infinity Song"), ("Space", "Given by Donna Karan's Urban Zen")]) + '''</div>
</section>
<section class="pj-section g12">
  <h2>The evening</h2>
  <p class="txt">Gary Zukav and Linda Francis spoke in a room given for the night by Donna Karan's Urban Zen. The Boyd family, found singing at Bethesda Fountain a few weeks earlier, performed live. Today they are known as Infinity Song.</p>
</section>
<section class="pj-gallery">
  <div class="g12">
    <figure class="gal-a rv"><video src="/assets/video/boyds-first-evening.mp4" poster="/assets/img/boyds-first-evening-poster.jpg" muted loop playsinline autoplay preload="none" aria-label="The Boyd family performing at the first Together WorX event"></video><figcaption class="cap">The Boyds performing that night</figcaption></figure>
    <figure class="gal-b rv"><img src="/assets/img/first-night.jpg" alt="Rebekah with Gary Zukav, Linda Francis and the Boyds after the evening" loading="lazy" width="640" height="1136" style="object-position:center 30%"><figcaption class="cap">Rebekah, Gary Zukav, Linda Francis and the Boyds</figcaption></figure>
    <figure class="gal-c rv"><img src="/assets/img/bethesda-wide.jpg" alt="The Boyd family singing at Bethesda Fountain in Central Park" loading="lazy" width="2000" height="1500"><figcaption class="cap">Singing at Bethesda Fountain, Central Park</figcaption></figure>
  </div>
</section>
''' + nxt("The Art of Coming Together", "/work/art-of-coming-together/") + '''
</main>
'''
pages.append(page("/work/urban-zen/", "A Conversation with Gary Zukav and Linda Francis", "The first Together WorX event: Gary Zukav and Linda Francis in conversation at Donna Karan's Urban Zen, with a live performance by Infinity Song.", uz, "Our Work", stay=False, og="/assets/img/urban-zen.jpg"))

# art of coming together
ac = '''<main id="main">
{{HEADER}}
''' + top("New York | Hurricane Dorian Relief", "The Art of Coming Together", "With Gary Zukav and Linda Francis") + '''
<img class="pj-hero" src="/assets/img/gallery.jpg" alt="Guests gathered in the brick gallery, facing Gary Zukav and Linda Francis" width="1800" height="1350">
<section class="pj-body g12">
  <p class="lede">An evening of conversation, live music, and a collective artwork created by guests, raising funds for hurricane relief in the Bahamas.</p>
  <div style="grid-column:8/span 5">''' + facts([("Where", "New York"), ("With", "Gary Zukav and Linda Francis"), ("For", "Hurricane Dorian relief in the Bahamas")]) + '''</div>
</section>
<section class="pj-section g12">
  <h2>Bahamas relief</h2>
  <p class="txt">Relief work continued after the evening, including a fire truck, a sponsored Thanksgiving, a plane full of supplies and early work toward a sustainable rebuild.</p>
</section>
<section class="pj-gallery">
  <div class="g12">
    <figure class="gal-l rv"><img src="/assets/img/gallery-2.jpg" alt="Guests seated in the brick gallery during the conversation" loading="lazy" width="1350" height="1800"></figure>
    <figure class="gal-r rv" style="margin-top:200px"><img src="/assets/img/bahamas-relief.jpg" alt="Volunteers in Together WorX shirts" loading="lazy" width="1600" height="886" style="aspect-ratio:16/9"><figcaption class="cap" style="margin-top:12px">Bahamas relief.</figcaption></figure>
  </div>
</section>
''' + nxt("The Science of Spirituality", "/work/science-of-spirituality/") + '''
</main>
'''
pages.append(page("/work/art-of-coming-together/", "The Art of Coming Together", "An evening with Gary Zukav and Linda Francis raising funds for hurricane relief in the Bahamas.", ac, "Our Work", stay=False, og="/assets/img/gallery.jpg"))

# science
sc = '''<main id="main">
{{HEADER}}
''' + top("New York", "The Science of Spirituality", "With Dr. Anna Yusim and Dr. Srini Pillay") + '''
<img class="pj-hero" src="/assets/img/science-room.jpg" alt="Guests seated in a white gallery room listening at The Science of Spirituality" width="1800" height="1350" style="object-position:center 40%">
<section class="pj-body g12">
  <p class="lede">An immersive experience exploring the connection between science and spirituality, combining thought-provoking conversations with interactive workshops.</p>
  <div style="grid-column:8/span 5">''' + facts([("Where", "New York"), ("With", "Dr. Anna Yusim and Dr. Srini Pillay")]) + '''</div>
</section>
<section class="pj-gallery">
  <div class="g12">
    <figure class="gal-l rv"><img src="/assets/img/science-talk.jpg" alt="Guests listening as The Science of Spirituality begins" loading="lazy" width="1350" height="1800"></figure>
    <figure class="gal-r rv"><img src="/assets/img/fire-ceremony.jpg" alt="Guests gathered around a fire ceremony in a courtyard" loading="lazy" width="1350" height="1800"><img class="over3" src="/assets/img/fire-ceremony-2.jpg" alt="The fire ceremony from another angle" loading="lazy" width="1000" height="1333"><figcaption class="cap">The fire ceremony</figcaption></figure>
  </div>
</section>
<section class="pj-archive"><div class="inner g12"><figure><img src="/assets/img/artwork-science.jpg" alt="Original promotional artwork: Together WorX presents The Science of Spirituality with Dr. Anna Yusim and Dr. Srini Pillay" loading="lazy" width="1340" height="746"><figcaption class="cap">Original promotional artwork</figcaption></figure></div></section>
''' + nxt("Soul Sunday", "/work/soul-sunday/") + '''
</main>
'''
pages.append(page("/work/science-of-spirituality/", "The Science of Spirituality", "Dr. Anna Yusim and Dr. Srini Pillay on the connection between science and spirituality.", sc, "Our Work", stay=False, og="/assets/img/science-room.jpg"))

# soul sunday
ss = '''<main id="main">
{{HEADER}}
''' + top("Tantris | West Hollywood, California", "Soul Sunday", "Authentic Power &amp; Spiritual Partnership") + '''
<section class="split g12">
  <figure class="rv"><img src="/assets/img/flyer-soul-sunday.jpg" alt="Original flyer for Soul Sunday with Gary Zukav and Linda Francis at Tantris, West Hollywood" width="1500" height="1500"><figcaption class="cap">Original flyer</figcaption></figure>
  <div class="side">
    <p class="lede">An afternoon with Gary Zukav and Linda Francis featuring movement, a community brunch, and a conversation on authentic power and spiritual partnership.</p>
    ''' + facts([("Where", "Tantris, 9200 Sunset Boulevard, West Hollywood"), ("When", "December 3"), ("With", "Gary Zukav and Linda Francis")]) + '''
    <h2>The afternoon</h2>
    <ul class="list"><li>Tantris Flow class with Ivorie Jenkins</li><li>Community brunch</li><li>Lecture with Gary Zukav and Linda Francis</li></ul>
  </div>
</section>
''' + nxt("A Conversation with Gary Zukav and Linda Francis", "/work/urban-zen/") + '''
</main>
'''
pages.append(page("/work/soul-sunday/", "Soul Sunday", "Soul Sunday: Authentic Power & Spiritual Partnership with Gary Zukav and Linda Francis at Tantris, West Hollywood.", ss, "Our Work", stay=False, og="/assets/img/flyer-soul-sunday.jpg"))

# about
story = [
 "I was jogging through Central Park one Sunday when I heard voices so beautiful they seemed almost angelic. I followed the music to Bethesda Fountain, where a family was singing together. Their harmonies were extraordinary. I stood listening, completely captivated.",
 "At the time, I was preparing the first Together WorX event. Gary Zukav and Linda Francis had agreed to speak, and Donna Karan's Urban Zen would be our setting. As I listened to the family, I began to imagine their voices filling that beautiful space. I knew I wanted them there.",
 "The following Sunday, I returned to the fountain, hoping to find them. To my delight, they were there. I introduced myself, told them about the event, and was given a number to call.",
 "TURN:The answer was no.",
 "Still, their music stayed with me. The next Sunday, I found myself back at the fountain. I was becoming something of a nudnik, I admit, but I couldn't resist asking once more. I told them how deeply their music had moved me and how much it would mean to have them join us.",
 "TURN:This time, they agreed.",
 "A few weeks later, I stood at Urban Zen listening to those same extraordinary voices, now filling a room of people who had come together for our very first event.",
 "The family I met that Sunday was the Boyd family, now known as Infinity Song.",
]
sp = "\n      ".join(f'<p class="turn">{s[5:]}</p>' if s.startswith("TURN:") else f"<p>{s}</p>" for s in story)
about = '''<main id="main">
{{HEADER}}
<section class="about-top"><p class="label" style="margin-bottom:22px;font-weight:600">About</p><h1>It began with a song in the park.</h1></section>
<figure class="about-hero"><img src="/assets/img/bethesda-wide.jpg" alt="The Boyd family singing under the arcade at Bethesda Fountain in Central Park" width="2000" height="1500"></figure>
<section class="story-body g12">
  <div class="text">
      ''' + sp + '''
      <p class="sig" style="margin-top:40px">Rebekah Hoyle</p>
      <p style="font-size:14px;color:#6b6b6b">Founder, Together WorX</p>
  </div>
  <aside class="rv"><img src="/assets/img/first-night.jpg" alt="Rebekah with Gary Zukav, Linda Francis and the Boyds at the first event" loading="lazy" width="640" height="1136"><p class="cap">The first Together WorX event, Urban Zen</p></aside>
</section>
<section class="org"><div class="inner g12"><p>Together WorX Inc. is a registered 501(c)(3) nonprofit organization based in New York.</p></div></section>
</main>
'''
pages.append(page("/about/", "About", "How Together WorX began: a song at Bethesda Fountain and the first event at Urban Zen.", about, "About", og="/assets/img/bethesda-wide.jpg"))

# collaborate
col = '''<main id="main">
{{HEADER}}
<section class="simple">
  <h1>Collaborate.</h1>
  <p class="lead">We welcome new ideas and opportunities to work together.</p>
  <div class="g12 paths">
    <div class="p"><h2>Collaborate</h2><p>Have an idea or an interest in working together? We'd love to hear from you.</p><a class="btn btn-dark" href="/contact/?interest=collaborate">Get in touch</a></div>
    <div class="p" id="support"><h2>Support</h2><p>Help bring future Together WorX projects to life.</p><a class="btn btn-dark" href="https://donate.stripe.com/aFacN64Sw7XKcl4etDcEw01">Donate</a><p style="margin:18px 0 0;font-size:15px"><a class="tlink" href="/contact/?interest=support">Questions about giving? Get in touch →</a></p><p class="tax">Together WorX Inc. is a registered 501(c)(3) nonprofit. Gifts are tax-deductible to the extent allowed by law.</p></div>
  </div>
</section>
</main>
'''
pages.append(page("/collaborate/", "Collaborate", "Work with Together WorX or support future projects.", col, "Collaborate"))

# contact
con = '''<main id="main">
{{HEADER}}
<section class="simple">
  <h1>Contact.</h1>
  <p class="lead">Tell us who you are and what brought you here.</p>
  <div class="g12 contact-grid">
    <div class="info"><a class="mail" href="mailto:hello@togetherworx.org">hello@togetherworx.org</a></div>
    <form name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field" class="js-form" data-ok="Thank you. Your message is on its way.">
      <input type="hidden" name="form-name" value="contact">
      <p hidden><label>Leave this empty <input name="bot-field"></label></p>
      <label class="field">Your name<input name="name" autocomplete="name" required></label>
      <label class="field">Email<input name="email" type="email" autocomplete="email" required></label>
      <label class="field">I'm interested in
        <select name="interest" id="interest">
          <option value="Collaboration">Collaboration</option>
          <option value="Support">Supporting the work</option>
          <option value="Something else">Something else</option>
        </select>
      </label>
      <label class="field">Message<textarea name="message" required></textarea></label>
      <button class="btn btn-dark" type="submit">Send</button>
      <p class="note" role="status"></p>
    </form>
  </div>
</section>
</main>
'''
pages.append(page("/contact/", "Contact", "Get in touch with Together WorX.", con, "Contact", stay=False))

# privacy
pv = '''<main id="main">
{{HEADER}}
<section class="simple">
  <h1>Privacy.</h1>
  <div class="prose">
    <p>When you write to us or sign up for updates, we receive the details you choose to share, such as your name and email address.</p>
    <p>We use them only to reply to you or to send the updates you asked for. We don't sell or share them.</p>
    <p>To be removed from our list or to ask about your information, write to <a href="mailto:hello@togetherworx.org">hello@togetherworx.org</a>.</p>
  </div>
</section>
</main>
'''
pages.append(page("/privacy/", "Privacy", "How Together WorX handles the information you share.", pv, stay=False))

# thank-you fallback for no-JS form posts
open("sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{SITE}{p}</loc></url>\n" for p in pages) + "</urlset>\n")
open("robots.txt", "w").write(f"User-agent: *\nDisallow: /_src/\nSitemap: {SITE}/sitemap.xml\n")
print("built", len(pages), "pages")
