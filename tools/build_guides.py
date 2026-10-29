import json, os, html, sys
OUT = sys.argv[1] if len(sys.argv)>1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://pureintonation.com"

PAGES = [
dict(slug="tonal-energy-alternative",
 nav="Tonal Energy alternative",
 title="Free Tonal Energy & iStrobosoft Alternative – Pure Intonation Tuner",
 desc="A free alternative to Tonal Energy Tuner and iStrobosoft: a strobe tuner and just-intonation chord drone in one, focused only on tuning. Runs in any browser.",
 h1="A free alternative to Tonal Energy and iStrobosoft",
 lede="Pure Intonation Tuner puts a <strong>strobe tuner</strong> and a <strong>just-intonation chord drone</strong> in one screen. Think of a strobe tuner like iStrobosoft combined with the drone and pure-tuning ideas of Tonal Energy Tuner, focused on one job: playing in tune. It's free and runs in your browser.",
 body="""
<h2>Why musicians switch</h2>
<ul>
<li><strong>Free, no download.</strong> Open pureintonation.com on iPhone, Android, iPad, Mac or PC. Add it to your home screen and it works offline.</li>
<li><strong>Strobe precision.</strong> Four strobe bands stand still when you're in tune and drift right or left when you're sharp or flat. Easy, Normal and Expert modes set how strict it is.</li>
<li><strong>Chords, not just single notes.</strong> Play any chord on the keyboard or tone wheel. It names the chord (from triads up to C13♯11♭9), finds the root and tunes every other note to its pure ratio above that root.</li>
<li><strong>The tuner follows the chord.</strong> In Pure mode, the strobe freezes on the <em>just</em> pitch for your note in that chord, not the equal-tempered one. A major third reads in tune at −14¢, the way it should sound in a chord.</li>
<li><strong>One switch: Equal or Pure.</strong> Flip between equal temperament and pure (just) intonation to hear exactly how far each note moves.</li>
<li><strong>Plays like an instrument.</strong> Connect a MIDI keyboard and every chord you play is tuned pure in real time, with velocity and sustain pedal.</li>
</ul>
<h2>How it compares</h2>
<div class="tablewrap"><table>
<thead><tr><th>What you need</th><th>Pure Intonation Tuner</th></tr></thead>
<tbody>
<tr><td>Price</td><td>Free</td></tr>
<tr><td>Devices</td><td>Any modern browser; installs to your home screen</td></tr>
<tr><td>Tuner display</td><td>4-band strobe, three sensitivity levels</td></tr>
<tr><td>Drone</td><td>Full chords, 17 sounds, real concert-hall reverbs</td></tr>
<tr><td>Tuning</td><td>Equal or pure, switchable; automatic root detection</td></tr>
<tr><td>Harmonic 7th</td><td>7/4 (−31¢) or 9/5 (+18¢)</td></tr>
<tr><td>MIDI keyboard</td><td>Yes, tuned pure in real time</td></tr>
<tr><td>Notation</td><td>Grand staff with the chord symbol and each note's function</td></tr>
</tbody></table></div>
<p>Tonal Energy and iStrobosoft are excellent apps with many more features, such as metronomes, recording and analysis. If what you want is to <em>tune</em>, and especially to tune chords, Pure Intonation Tuner keeps everything you need on one screen and costs nothing.</p>
""",
 faq=[("Is Pure Intonation Tuner really free?","Yes. It runs free in any modern browser, with no account, no ads and no download. A Support button lets you leave a tip if you find it useful."),
      ("Does it work like a strobe tuner?","Yes. Its four-band strobe display stands still when you are in tune, so you can see deviations of a cent or two. In Pure mode the strobe targets the just pitch for your note in the current chord."),
      ("Is it affiliated with Tonal Energy or iStrobosoft?","No. Pure Intonation Tuner is an independent project by Michael Van Bebber. Tonal Energy and iStrobosoft are products of their respective owners.")]),

dict(slug="just-intonation-drone",
 nav="Just intonation drone",
 title="Just Intonation Chord Drone – Free Online | Pure Intonation Tuner",
 desc="Free just intonation drone that plays full chords tuned pure. Detects the root, tunes every note to its pure ratio, and switches between equal and just in one tap.",
 h1="A just intonation drone that plays whole chords",
 lede="Most drones give you one note. Pure Intonation Tuner plays the <strong>whole chord</strong>, tuned pure: pick the notes and it finds the root, names the chord and tunes every other note to its just ratio above that root.",
 body="""
<h2>How it works</h2>
<ol>
<li>Tap notes on the keyboard or the tone wheel. The drone starts on its own.</li>
<li>The root lights up purple. Each other note is retuned to its pure interval: the major third 14 cents low, the fifth 2 cents high, the harmonic seventh 31 cents low.</li>
<li>Flip <strong>EQUAL / PURE</strong> to hear how the chord changes from beating to ringing.</li>
<li>Double-tap any key to move the whole chord so its root lands on that note.</li>
</ol>
<h2>Sounds and rooms</h2>
<p>Choose from 17 sounds, including synth pads, organ, strings, brass and choir, and place them in real recorded spaces, from a studio to a large concert hall to a cathedral. Sustained pure chords in a live room are the fastest way to train your ear to hear a chord lock.</p>
<h2>Practice ideas</h2>
<ul>
<li>Hold a major triad and play its third against the drone until the beats disappear.</li>
<li>Build a dominant seventh with the 7/4 harmonic seventh and hear how smooth it becomes.</li>
<li>Sing or play each chord tone in turn and watch the strobe tuner confirm the pure pitch.</li>
</ul>
""",
 faq=[("What is a just intonation drone?","A drone that sustains pitches tuned to simple whole-number ratios, such as 3:2 for the fifth and 5:4 for the major third, so the chord rings without beats."),
      ("Can the drone play more than one note?","Yes. It plays any chord you choose and tunes every note relative to the detected root.")]),

dict(slug="strobe-tuner",
 nav="Free strobe tuner",
 title="Free Online Strobe Tuner with Just Intonation – Pure Intonation Tuner",
 desc="A free strobe tuner in your browser. Four strobe bands stand still when you're in tune, and in Pure mode they target the just pitch for your note in the chord.",
 h1="A free strobe tuner that knows the chord you're in",
 lede="Strobe tuners are the most precise way to see your pitch. Pure Intonation Tuner gives you a four-band strobe in any browser, free, and it does something other tuners don't: in Pure mode it tunes you to the <strong>just</strong> pitch for your note in the current chord.",
 body="""
<h2>Reading the strobe</h2>
<ul>
<li><strong>Still bands:</strong> in tune.</li>
<li><strong>Drifting right:</strong> sharp. <strong>Drifting left:</strong> flat. The faster they move, the further off you are.</li>
<li>The note name and cents offset sit below the strobe, and the bands turn green when you're within range.</li>
</ul>
<h2>Easy, Normal and Expert</h2>
<p>Choose how strict the tuner is. Easy is forgiving and steady for students and beginners. Expert shows every cent for professional work.</p>
<h2>Tune to the chord, not just the note</h2>
<p>Set a chord in the drone, start the microphone and play. If you're playing the third of a C major chord, the strobe stands still at E −14¢, the pure major third, instead of the tempered E that sounds sharp in a sustained chord. Switch to Equal any time for standard equal-temperament tuning, and adjust A4 from 400 to 480 Hz.</p>
""",
 faq=[("Do I need to install anything?","No. It runs in your browser and only asks for microphone access. On iPhone and iPad, tap Start microphone when you're ready to tune."),
      ("Is a strobe tuner more accurate than a needle tuner?","Strobe displays show small deviations very clearly, because even a one-cent difference makes the bands move. That makes them ideal for fine intonation work.")]),

dict(slug="midi-just-intonation",
 nav="Play MIDI in just intonation",
 title="Play a MIDI Keyboard in Just Intonation, Live – Pure Intonation Tuner",
 desc="Connect a MIDI keyboard and play in pure (just) or equal intonation in real time. Every chord is detected and retuned as you play, with velocity and sustain.",
 h1="Play your MIDI keyboard in just intonation, live",
 lede="Plug in a MIDI keyboard and Pure Intonation Tuner becomes a <strong>live instrument</strong>. Every chord you play is identified and retuned to pure intonation as you play it, or left in equal temperament with one tap. Very few instruments of any kind can do this, and this one is free.",
 body="""
<h2>What happens when you play</h2>
<ul>
<li>Each new chord is named instantly and its root found.</li>
<li>Every note is tuned to its pure ratio above that root, and held notes glide to their new pitch when the harmony moves. Choose Hold instead to keep them fixed.</li>
<li>Velocity and the sustain pedal work the way you expect.</li>
<li>The grand staff and keyboard show what you're playing, with each note's function and cents offset.</li>
</ul>
<h2>Set up in under a minute</h2>
<ol>
<li>Plug your keyboard in by USB.</li>
<li>Open pureintonation.com in Chrome, Edge or Firefox and click the MIDI button.</li>
<li>Pick your keyboard under <em>MIDI in</em> and play.</li>
</ol>
<p>On iPhone or iPad, use the free Web MIDI Browser app. Latency is kept as low as the browser allows; use wired headphones or speakers, not Bluetooth.</p>
<h2>For performance and teaching</h2>
<p>Use it on stage for pure-tuned pads and choir sounds, in rehearsal to show an ensemble what a locked chord sounds like, or at home to explore how harmony changes when every chord is pure.</p>
""",
 faq=[("Which browsers support MIDI keyboards?","Chrome, Edge and Firefox on Mac, Windows, Linux and Android. Safari and iPhone browsers do not support web MIDI; on iPhone or iPad, use the Web MIDI Browser app."),
      ("Can I switch between equal and just intonation while playing?","Yes. The Equal / Pure switch changes the tuning instantly, so you can compare the same chord both ways.")]),

dict(slug="just-intonation-chart",
 nav="Just intonation cents chart",
 title="Just Intonation Cents Chart – How Far to Adjust Each Interval",
 desc="How many cents to raise or lower each interval for pure (just) intonation: major third −13.7¢, minor third +15.6¢, fifth +2.0¢, harmonic seventh −31.2¢, and more.",
 h1="Just intonation cents chart",
 lede="How far each pure interval sits from equal temperament, measured from the chord root. Use these numbers to adjust your pitch in a sustained chord, or let Pure Intonation Tuner do it for you.",
 body="""
<div class="tablewrap"><table>
<thead><tr><th>Interval</th><th>Ratio</th><th>Cents vs. equal</th></tr></thead>
<tbody>
<tr><td>Unison</td><td>1/1</td><td>0</td></tr>
<tr><td>Minor 2nd</td><td>16/15</td><td>+11.7</td></tr>
<tr><td>Major 2nd</td><td>9/8</td><td>+3.9</td></tr>
<tr><td>Minor 3rd</td><td>6/5</td><td>+15.6</td></tr>
<tr><td>Major 3rd</td><td>5/4</td><td>−13.7</td></tr>
<tr><td>Perfect 4th</td><td>4/3</td><td>−2.0</td></tr>
<tr><td>Tritone</td><td>45/32</td><td>−9.8</td></tr>
<tr><td>Perfect 5th</td><td>3/2</td><td>+2.0</td></tr>
<tr><td>Minor 6th</td><td>8/5</td><td>+13.7</td></tr>
<tr><td>Major 6th</td><td>5/3</td><td>−15.6</td></tr>
<tr><td>Harmonic 7th</td><td>7/4</td><td>−31.2</td></tr>
<tr><td>Minor 7th</td><td>9/5</td><td>+17.6</td></tr>
<tr><td>Major 7th</td><td>15/8</td><td>−11.7</td></tr>
<tr><td>Octave</td><td>2/1</td><td>0</td></tr>
</tbody></table></div>
<h2>Rules of thumb</h2>
<ul>
<li><strong>Major thirds low, minor thirds high.</strong> Lower the third of a major chord about 14 cents; raise the third of a minor chord about 16.</li>
<li><strong>Fifths barely move.</strong> A pure fifth is only 2 cents wider than equal.</li>
<li><strong>The seventh of a dominant chord</strong> can sit very low (7/4, −31¢) for the smoothest sound, or a little high (9/5, +18¢) for a brighter one.</li>
</ul>
<p>Every number is relative to the <em>root of the chord</em>, not the key. That's why the same written note moves differently from chord to chord, and why Pure Intonation Tuner detects the root for you.</p>
""",
 faq=[("How many cents flat is a just major third?","A just major third (5:4) is 13.7 cents lower than an equal-tempered major third."),
      ("How many cents sharp is a just minor third?","A just minor third (6:5) is 15.6 cents higher than an equal-tempered minor third.")]),

dict(slug="band-intonation",
 nav="For band, orchestra and choir",
 title="Teach Ensemble Intonation with a Just Intonation Drone – Pure Intonation Tuner",
 desc="A free tool for band, orchestra, jazz and choir directors: play any chord tuned pure through the speakers and show each section exactly how to adjust.",
 h1="Teach your ensemble to tune chords",
 lede="Equal temperament gets players close, but sustained chords only lock when the thirds and sevenths are adjusted. Pure Intonation Tuner lets you <strong>play the chord your ensemble is holding, tuned pure</strong>, and shows every section how far to move.",
 body="""
<h2>In rehearsal</h2>
<ol>
<li>Enter the chord from the score on the keyboard, or play it on a MIDI keyboard.</li>
<li>Play it through the room speakers in Pure mode. Each note shows its function (1, 3, 5, ♭7) and its cents offset, such as 3rd −14¢.</li>
<li>Flip to Equal and back so players hear the difference between a beating chord and a ringing one.</li>
<li>Have each section match the drone, then take it away and hold the chord on their own.</li>
</ol>
<h2>At home</h2>
<p>Students can open the same page on their phone, set the chord, and use the strobe tuner to practice placing their note exactly where it belongs in that chord. No accounts, no app store, nothing to buy.</p>
<h2>Works for</h2>
<p>Concert and jazz bands, orchestras, brass and saxophone sections, string quartets and choirs: any group that sustains chords. Built by Michael Van Bebber, a trumpeter, pianist, singer and educator who directs high-school jazz ensembles in Seattle.</p>
""",
 faq=[("Can students use it on their phones?","Yes. It runs in any modern phone browser and can be added to the home screen to work offline."),
      ("Why do ensembles adjust thirds and sevenths?","In a sustained chord, equal-tempered thirds and sevenths beat against the root. Adjusting them toward pure ratios makes the chord lock and ring.")]),
]

CSS = """:root{--bg:#13121b;--panel:#1c1b27;--raise:#262434;--line:#322f44;--fg:#eceaf4;--muted:#9b97b0;--root:#a96dff;--note:#e8b44a;
--display:"Bricolage Grotesque","Avenir Next",system-ui,sans-serif;--mono:"IBM Plex Mono",ui-monospace,Menlo,monospace;color-scheme:dark}
*{box-sizing:border-box}
html,body{margin:0;background:var(--bg);color:var(--fg)}
body{font-family:var(--display);line-height:1.6;-webkit-text-size-adjust:100%}
a{color:var(--root)}
.wrap{max-width:760px;margin:0 auto;padding:20px 16px 48px}
.top{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:28px}
.brand{display:flex;align-items:center;gap:10px;color:var(--fg);text-decoration:none;font-weight:700;font-size:1.15rem}
.brand img{width:32px;height:32px;border-radius:8px}
.brand span{color:var(--root)}
.cta{display:inline-block;background:var(--root);color:#fff;text-decoration:none;font-weight:700;padding:10px 18px;border-radius:10px}
.cta.small{padding:7px 14px;font-size:.9rem}
h1{font-size:clamp(1.7rem,4.5vw,2.4rem);line-height:1.15;margin:0 0 14px;text-wrap:balance}
h2{font-size:1.3rem;margin:32px 0 8px}
p,li{color:var(--muted)}
strong{color:var(--fg);font-weight:600}
.lede{font-size:1.1rem}
.lede strong{color:var(--fg)}
ul,ol{padding-left:1.2em}
li{margin:6px 0}
.hero{margin:22px 0 8px}
.shot{display:block;width:100%;height:auto;border-radius:14px;border:1px solid var(--line);margin:22px 0}
.tablewrap{overflow-x:auto}
table{border-collapse:collapse;width:100%;font-size:.95rem;margin:8px 0}
th,td{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}
th{color:var(--fg)} td{color:var(--muted)} td:first-child{color:var(--fg)}
.faq details{border-bottom:1px solid var(--line);padding:10px 0}
.faq summary{cursor:pointer;font-weight:600}
.faq p{margin:8px 0 0}
.band{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:20px;margin:36px 0;text-align:center}
.band p{margin:0 0 14px;color:var(--fg)}
.more{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px;padding:0;list-style:none}
.more a{display:block;background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:12px 14px;text-decoration:none;color:var(--fg)}
.more a:hover{border-color:var(--root)}
footer{border-top:1px solid var(--line);margin-top:40px;padding-top:16px;font-size:.85rem;color:var(--muted)}
footer p{margin:0 0 6px}
"""

def page(p):
    url=f"{SITE}/{p['slug']}/"
    faq_html="".join(f"<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>" for q,a in p['faq'])
    ld=[{"@context":"https://schema.org","@type":"WebPage","name":p['title'],"url":url,"description":p['desc'],
         "isPartOf":{"@type":"WebSite","name":"Pure Intonation Tuner","url":SITE+"/"},
         "about":{"@type":"WebApplication","name":"Pure Intonation Tuner","url":SITE+"/","applicationCategory":"MusicApplication","operatingSystem":"Any (web browser)","offers":{"@type":"Offer","price":"0","priceCurrency":"USD"}},
         "author":{"@type":"Person","name":"Michael Van Bebber"}},
        {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in p['faq']]},
        {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Pure Intonation Tuner","item":SITE+"/"},{"@type":"ListItem","position":2,"name":p['nav'],"item":url}]}]
    more="".join(f'<li><a href="/{q["slug"]}/">{html.escape(q["nav"])}</a></li>' for q in PAGES if q is not p)
    t=html.escape(p['title']); d=html.escape(p['desc'])
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="author" content="Michael Van Bebber">
<meta name="theme-color" content="#13121b">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Pure Intonation Tuner">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700&display=swap">
<link rel="stylesheet" href="/guides.css?v=75">
<script type="application/ld+json">{json.dumps(ld,ensure_ascii=False)}</script>
</head>
<body>
<div class="wrap">
<header class="top"><a class="brand" href="/"><img src="/icon-192.png" alt="" width="32" height="32">Pure Intonation <span>Tuner</span></a><a class="cta small" href="/">Open the tuner</a></header>
<main>
<h1>{p['h1']}</h1>
<p class="lede">{p['lede']}</p>
<p class="hero"><a class="cta" href="/">Open Pure Intonation Tuner – free</a></p>
<img class="shot" src="/app-screenshot.jpg?v=75" alt="Pure Intonation Tuner: a C7 chord tuned pure (E −14¢, G +2¢, B♭ −31¢) and the strobe tuner standing still, green, on a pure major third" width="1590" height="1152" loading="lazy">
{p['body']}
<section class="faq"><h2>Questions</h2>{faq_html}</section>
<div class="band"><p>Free in your browser. No account, no download.</p><a class="cta" href="/">Open the tuner</a></div>
<h2>More guides</h2>
<ul class="more">{more}</ul>
</main>
<footer>
<p>Pure Intonation Tuner is built by <strong>Michael Van Bebber</strong>, trumpeter, pianist, singer and educator in Seattle. Also by Michael: <a href="https://vibratotrainer.com">Vibrato Trainer</a> and <a href="https://slowdownbuddy.com">Slow Down Buddy</a>.</p>
<p>Tonal Energy, iStrobosoft and other product names are trademarks of their respective owners. Pure Intonation Tuner is independent and not affiliated with them.</p>
<p>© 2026 Michael Van Bebber</p>
</footer>
</div>
</body>
</html>
"""

open(os.path.join(OUT,"guides.css"),"w").write(CSS)
for p in PAGES:
    d=os.path.join(OUT,p['slug']);os.makedirs(d,exist_ok=True)
    open(os.path.join(d,"index.html"),"w").write(page(p))
# guides list for main page + sitemap
print("built",len(PAGES))
