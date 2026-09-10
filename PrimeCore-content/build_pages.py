#!/usr/bin/env python3
"""Generate the rebuilt Primecoreinfo static pages."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def chrome(root: str, page: str):
    def href(p):
        return root + p

    def active(name):
        return " is-active" if page == name else ""

    header = f'''<header class="site-header">
  <a class="brand" href="{href("")}" aria-label="Primecoreinfo home"><span class="brand-mark"></span><span>PRIMECOREINFO</span></a>
  <nav class="nav" aria-label="Primary">
    <a class="{active("about").strip()}" href="{href("about/")}">About</a>
    <a class="{active("services").strip()}" href="{href("services/")}">Services</a>
    <a class="{active("insights").strip()}" href="{href("insights/")}">Insights</a>
    <a class="{active("contact").strip()}" href="{href("contact/")}">Contact</a>
    <a class="btn-talk" data-magnetic href="{href("contact/")}">Let's talk</a>
  </nav>
  <button class="menu-btn" type="button" aria-controls="mobile-nav" aria-expanded="false"><span></span><span></span><span></span><b class="sr-only">Open menu</b></button>
</header>
<nav class="mobile-nav" id="mobile-nav" hidden>
  <a href="{href("about/")}">About</a>
  <a href="{href("services/")}">Services</a>
  <a href="{href("insights/")}">Insights</a>
  <a href="{href("contact/")}">Contact</a>
  <a href="{href("contact/")}">Let's talk</a>
</nav>'''

    cta = f'''<section class="wrap" style="padding-bottom:96px">
  <div class="cta-band reveal">
    <p class="kicker">Next conversation</p>
    <h2>Let's build what's next.</h2>
    <p>Share your environment, constraints, and goals. We'll help you move from complexity to a clearer operating model.</p>
    <a class="btn" data-magnetic href="{href("contact/")}">Let's talk <span aria-hidden="true">→</span></a>
  </div>
</section>'''

    footer = f'''<footer class="site-footer">
  <div class="footer-grid">
    <div class="footer-brand">
      <a class="brand" href="{href("")}"><span class="brand-mark"></span><span>PRIMECOREINFO</span></a>
      <p>A practical technology partner for cloud transformation, infrastructure modernization, and dependable IT operations.</p>
    </div>
    <div>
      <h4>Navigate</h4>
      <a href="{href("about/")}">About</a>
      <a href="{href("services/")}">Services</a>
      <a href="{href("insights/")}">Insights</a>
      <a href="{href("contact/")}">Contact</a>
    </div>
    <div>
      <h4>Services</h4>
      <a href="{href("cloud-transformation/")}">Cloud Transformation</a>
      <a href="{href("infrastructure-modernization/")}">Infrastructure Modernization</a>
      <a href="{href("managed-it-services/")}">Managed IT Services</a>
    </div>
    <div>
      <h4>Contact</h4>
      <a href="mailto:hello@primecoreinfo.com">hello@primecoreinfo.com</a>
      <a href="{href("privacy-policy/")}">Privacy</a>
      <a href="{href("insights/")}">Insights</a>
    </div>
  </div>
  <div class="footer-bottom">
    <span>© 2026 Primecoreinfo. Cloud &amp; IT transformation.</span>
    <span class="sig" aria-hidden="true"></span>
  </div>
</footer>'''
    return header, cta, footer


HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{title}</title>
<meta name="description" content="{desc}"/>
<link rel="stylesheet" href="{css}"/>
</head>
<body data-root="{root}" data-page="{page}">
<div class="atmosphere" aria-hidden="true"></div>
<div class="cursor-light" aria-hidden="true"></div>
'''

TAIL = '''
<script src="{js}"></script>
</body>
</html>
'''

ARCH = '''<div class="arch" aria-label="Cloud infrastructure visualization">
<svg viewBox="0 0 640 560" role="img">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#35D6E8"/><stop offset="1" stop-color="#159FE8"/>
    </linearGradient>
  </defs>
  <g fill="none" stroke="rgba(155,239,229,0.22)" stroke-width="1.2">
    <line x1="320" y1="270" x2="320" y2="92"/>
    <line x1="320" y1="270" x2="128" y2="168"/>
    <line x1="320" y1="270" x2="512" y2="168"/>
    <line x1="320" y1="270" x2="150" y2="400"/>
    <line x1="320" y1="270" x2="490" y2="400"/>
    <line x1="320" y1="270" x2="320" y2="488"/>
  </g>
  <circle class="particle" r="3"><animateMotion dur="7s" repeatCount="indefinite" path="M320,270 L320,92"/></circle>
  <circle class="particle" r="3"><animateMotion dur="9s" repeatCount="indefinite" path="M320,270 L512,168"/></circle>
  <circle class="particle" r="2.5"><animateMotion dur="8s" repeatCount="indefinite" path="M320,270 L150,400"/></circle>
  <g class="arch-core">
    <rect x="250" y="228" width="140" height="84" rx="18" fill="rgba(10,32,53,0.86)" stroke="url(#g)"/>
    <text x="320" y="268" text-anchor="middle" class="arch-label">CLOUD CORE</text>
    <text x="320" y="290" text-anchor="middle" class="arch-label" style="fill:#9BEFE5;font-size:10px;font-weight:600">CONNECTED SYSTEMS</text>
  </g>
  <g class="arch-float">
    <rect class="arch-node" x="262" y="54" width="116" height="54" rx="14"/>
    <text x="320" y="86" text-anchor="middle" class="arch-label">Cloud</text>
  </g>
  <g class="arch-float">
    <rect class="arch-node" x="52" y="140" width="140" height="54" rx="14"/>
    <text x="122" y="172" text-anchor="middle" class="arch-label">Infrastructure</text>
  </g>
  <g class="arch-float">
    <rect class="arch-node" x="448" y="140" width="140" height="54" rx="14"/>
    <text x="518" y="172" text-anchor="middle" class="arch-label">Security</text>
  </g>
  <g class="arch-float">
    <rect class="arch-node" x="64" y="374" width="140" height="54" rx="14"/>
    <text x="134" y="406" text-anchor="middle" class="arch-label">Data</text>
  </g>
  <g class="arch-float">
    <rect class="arch-node" x="436" y="374" width="140" height="54" rx="14"/>
    <text x="506" y="406" text-anchor="middle" class="arch-label">Applications</text>
  </g>
  <g class="arch-float">
    <rect class="arch-node" x="250" y="462" width="140" height="54" rx="14"/>
    <text x="320" y="494" text-anchor="middle" class="arch-label">Operations</text>
  </g>
</svg>
</div>'''


def footer_block(root, with_cta=True):
    _, cta, foot = chrome(root, "")
    return (cta + "\n" if with_cta else "") + foot


def doc(title, desc, root, page, body, cta=True):
    css = root + "assets/css/prime.css"
    js = root + "assets/js/prime.js"
    header, _, _ = chrome(root, page)
    html = HEAD.format(title=title, desc=desc, css=css, root=root, page=page)
    html += header + "\n<main>\n" + body + "\n</main>\n"
    html += footer_block(root, cta)
    html += TAIL.format(js=js)
    return html


def write(rel, html):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    print("wrote", rel)


home_body = f'''
<section class="hero">
  <div class="hero-copy">
    <p class="kicker reveal">Cloud &amp; IT Transformation</p>
    <h1 class="reveal">Driving Cloud<br>Transformation<br>With <em class="accent">Clarity</em></h1>
    <p class="lede reveal">Primecoreinfo helps organizations modernize infrastructure, accelerate cloud adoption, and strengthen day-to-day IT operations — with strategy and execution held together.</p>
    <div class="hero-actions reveal">
      <a class="btn" data-magnetic href="contact/">Let's talk</a>
      <a class="btn-ghost" href="services/">Explore services</a>
    </div>
  </div>
  {ARCH}
  <div class="scroll-hint"><i></i> Scroll</div>
</section>

<section class="trust">
  <div class="wrap trust-row">
    <div class="trust-item">Cloud Transformation<span>Planning, architecture, migration, optimization</span></div>
    <div class="trust-item">Infrastructure Modernization<span>A stronger foundation for growth</span></div>
    <div class="trust-item">Managed IT<span>Proactive support and continuity</span></div>
    <div class="trust-item">Enterprise Reliability<span>Security-conscious, operations-ready delivery</span></div>
  </div>
</section>

<section>
  <div class="wrap statement">
    <div class="reveal">
      <p class="kicker">Positioning</p>
      <h2>Technology transformation shouldn't create more complexity.</h2>
    </div>
    <div class="reveal">
      <p class="lede">We bring advisory insight and hands-on delivery together so cloud, infrastructure, and operations decisions stay aligned to business priorities — from early planning through ongoing support.</p>
      <div class="line-flow"><b>Legacy</b><i></i><b>Modernization</b><i></i><b>Cloud</b><i></i><b>Optimization</b></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">What we transform</p>
      <h2>Services built for modern growth</h2>
      <p>From transformation planning to day-to-day support, each engagement is designed to reduce complexity, improve reliability, and keep momentum.</p>
    </div>
    <div class="service-stack stagger">
      <a class="service-panel reveal" href="cloud-transformation/">
        <span class="sp-num">01</span>
        <div class="sp-copy"><h3>Cloud Transformation</h3><p>Plan and execute cloud initiatives that improve scalability, streamline operations, and keep control of cost, security, and governance.</p></div>
        <span class="sp-go" aria-hidden="true">→</span>
      </a>
      <a class="service-panel reveal" href="infrastructure-modernization/">
        <span class="sp-num">02</span>
        <div class="sp-copy"><h3>Infrastructure Modernization</h3><p>Refresh legacy environments with modern architecture, stronger performance, and a foundation built for hybrid and cloud-first operations.</p></div>
        <span class="sp-go" aria-hidden="true">→</span>
      </a>
      <a class="service-panel reveal" href="managed-it-services/">
        <span class="sp-num">03</span>
        <div class="sp-copy"><h3>Managed IT Services</h3><p>Maintain continuity with proactive monitoring, responsive support, and ongoing optimization for the systems your teams rely on.</p></div>
        <span class="sp-go" aria-hidden="true">→</span>
      </a>
    </div>
  </div>
</section>

<section>
  <div class="wrap split">
    <div class="media reveal">
      <img class="clip-in" src="assets/images/about-process.jpg" alt="Primecoreinfo infrastructure environment at dusk"/>
      <div class="media-overlay"></div>
      <div class="glass-chip" style="left:20px;bottom:20px">FROM<small>Legacy infrastructure</small></div>
      <div class="glass-chip" style="right:20px;top:20px">TO<small>Scalable cloud architecture</small></div>
    </div>
    <div class="reveal">
      <p class="kicker">Transformation</p>
      <h2>Making complex environments operable again</h2>
      <p class="lede" style="margin-top:16px">Aging systems slow delivery and raise operational risk. We assess the current estate, sequence change around business impact, and modernize in measured stages so critical systems stay under control.</p>
      <div class="stages"><span>Assess</span><span>Modernize</span><span>Migrate</span><span>Optimize</span><span>Operate</span></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">How we work</p>
      <h2>Strategy backed by execution</h2>
      <p>A clear delivery model improves visibility, governance, and performance across the environment.</p>
    </div>
    <div class="process">
      <div class="process-line" aria-hidden="true"></div>
      <article class="step is-on"><span class="step-dot"></span><span class="step-index">01</span><h3>Discover</h3><p>Evaluate the current environment, priorities, risks, and opportunities.</p></article>
      <article class="step"><span class="step-dot"></span><span class="step-index">02</span><h3>Strategize</h3><p>Build a roadmap for architecture, sequencing, governance, and readiness.</p></article>
      <article class="step"><span class="step-dot"></span><span class="step-index">03</span><h3>Architect</h3><p>Define target platforms, landing zones, and operating standards.</p></article>
      <article class="step"><span class="step-dot"></span><span class="step-index">04</span><h3>Transform</h3><p>Execute in disciplined phases with alignment and minimal disruption.</p></article>
      <article class="step"><span class="step-dot"></span><span class="step-index">05</span><h3>Operate</h3><p>Refine performance, strengthen resilience, and support improvement.</p></article>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">Why Primecoreinfo</p>
      <h2>Technology transformation without unnecessary complexity.</h2>
    </div>
    <div class="why-grid stagger">
      <article class="why-item reveal"><h3>Strategy before technology</h3><p>Architecture and sequencing follow business risk, not a catalogue of tools. Clarity first, then execution.</p></article>
      <article class="why-item reveal"><h3>Execution with accountability</h3><p>Advisory insight is paired with hands-on delivery so plans become operating environments, not slide decks.</p></article>
      <article class="why-item reveal"><h3>Designed for scale</h3><p>Every engagement is structured around scalable architecture, operational continuity, and long-term partnership.</p></article>
      <article class="why-item reveal"><h3>Built for reliability</h3><p>Security, monitoring, and support are part of delivery — not an afterthought once systems are live.</p></article>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">Outcomes</p>
      <h2>From fragmented operations to a clearer foundation</h2>
    </div>
    <div class="outcomes reveal">
      <div class="outcome">
        <h3>Before</h3>
        <ul><li>Legacy infrastructure</li><li>Complex operations</li><li>Fragmented systems</li><li>Limited visibility</li></ul>
      </div>
      <div class="outcome-mid">→</div>
      <div class="outcome after">
        <h3>After</h3>
        <ul><li>Modern infrastructure</li><li>Connected systems</li><li>Reliable operations</li><li>Scalable foundation</li></ul>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap quote reveal">
    <p class="kicker">Client perspective</p>
    <div class="stars" aria-label="Five stars">★★★★★</div>
    <blockquote>“Primecoreinfo brings structure to complex transformation work. Their team balances strategic planning with dependable execution, helping organizations modernize with less disruption and stronger long-term outcomes.”</blockquote>
    <cite>Technology Leadership<span>Enterprise Transformation Program</span></cite>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">Technology leadership</p>
      <h2>People who hold strategy and operations together</h2>
      <p>Cloud strategy, infrastructure expertise, service operations, and client leadership — structured to reduce complexity and move with accountability.</p>
    </div>
    <div class="team-feature reveal">
      <div class="team-photo"><img src="assets/images/avery-chen.jpg" alt="Avery Chen"/></div>
      <div>
        <p class="team-meta">10+ years experience</p>
        <h2>Avery Chen</h2>
        <p class="team-role">Cloud Transformation Lead</p>
        <p class="lede">Helps organizations move from legacy infrastructure to scalable cloud environments — with landing zones, migration waves, and operational readiness designed as one program.</p>
      </div>
    </div>
    <div class="team-grid stagger">
      <article class="team-card reveal"><img src="assets/images/jordan-patel.jpg" alt="Jordan Patel"/><div><p class="team-meta">Infrastructure</p><h3>Jordan Patel</h3><p>Infrastructure Modernization Director. Architecture, reliability, and stronger technical foundations.</p></div></article>
      <article class="team-card reveal"><img src="assets/images/taylor-brooks.jpg" alt="Taylor Brooks"/><div><p class="team-meta">Managed operations</p><h3>Taylor Brooks</h3><p>Managed Services Manager. Continuity, proactive monitoring, and long-term operational stability.</p></div></article>
      <article class="team-card reveal"><img src="assets/images/morgan-ellis.jpg" alt="Morgan Ellis"/><div><p class="team-meta">Client operations</p><h3>Morgan Ellis</h3><p>Client Success Partner. Connects technology work to business goals and lasting outcomes.</p></div></article>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">Insights</p>
      <h2>Clear thinking for technology change</h2>
    </div>
    <a class="insight-feature reveal" href="insights/cloud-readiness/">
      <img src="assets/vendor/wp-content/uploads/2026/08/2286378241.jpg" alt="Technology operations environment"/>
      <div class="insight-copy">
        <p class="cat">Cloud</p>
        <h3>Cloud readiness: what to clarify before the first migration wave</h3>
        <p style="margin:14px 0 20px">Dependencies, risk, cost, and operating model — the decisions that determine whether cloud work creates clarity or more complexity.</p>
        <span class="text-link">Read article <span class="arrow">→</span></span>
      </div>
    </a>
    <div class="insight-grid">
      <a class="insight-card reveal" href="insights/modern-foundations/"><div class="thumb"><img src="assets/vendor/wp-content/uploads/2026/08/1455786903-1-2048x1147.jpg" alt=""/></div><div><p class="cat">Infrastructure</p><h3>Modern foundations</h3><p>How to sequence infrastructure improvements around business risk.</p></div></a>
      <a class="insight-card reveal" href="insights/operational-resilience/"><div class="thumb"><img src="assets/vendor/wp-content/uploads/2026/08/1928146086-768x512.jpg" alt=""/></div><div><p class="cat">IT Operations</p><h3>Operational resilience</h3><p>Why visibility and ownership matter as environments grow.</p></div></a>
      <a class="insight-card reveal" href="insights/"><div class="thumb"><img src="assets/images/tech-cloud.jpg" alt=""/></div><div><p class="cat">Transformation</p><h3>All insights</h3><p>Practical perspectives for cloud, infrastructure, and operations decisions.</p></div></a>
    </div>
  </div>
</section>
'''

about_body = '''
<section class="page-hero">
  <p class="kicker reveal">About</p>
  <h1 class="reveal">Driving Cloud Transformation With <em class="accent">Clarity</em></h1>
  <p class="lede reveal">Primecoreinfo helps organizations modernize infrastructure, accelerate cloud adoption, and build resilient IT operations with a practical, outcomes-focused approach.</p>
</section>
<section>
  <div class="wrap split">
    <div class="reveal">
      <p class="kicker">Our story</p>
      <h2>Built for modern IT change</h2>
      <p class="lede" style="margin-top:16px">Primecoreinfo was created to help businesses move beyond legacy constraints and adopt cloud strategies that support growth, security, and operational efficiency. We focus on practical transformation plans that align technology decisions with business priorities.</p>
      <p class="lede">From early planning through implementation and ongoing support, our work is grounded in clear communication, technical depth, and a commitment to measurable progress for every client environment.</p>
      <p style="margin-top:24px"><a class="btn" href="../services/">Explore services</a></p>
    </div>
    <div class="media reveal"><img class="clip-in" src="../assets/images/about-story.jpg" alt="Technology team collaborating"/><div class="media-overlay"></div></div>
  </div>
</section>
<section>
  <div class="wrap split reverse">
    <div class="media reveal"><img class="clip-in" src="../assets/images/about-process.jpg" alt="Modern infrastructure"/><div class="media-overlay"></div></div>
    <div class="reveal">
      <p class="kicker">How we work</p>
      <h2>Strategy backed by execution</h2>
      <p class="lede" style="margin-top:16px">We combine advisory insight with hands-on delivery across cloud transformation, infrastructure modernization, and managed IT services. The team is structured to reduce complexity, improve reliability, and help internal stakeholders move with confidence.</p>
      <p class="lede">Every engagement is designed around scalable architecture, operational continuity, and long-term partnership so clients can modernize without losing control of critical systems.</p>
    </div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">What we believe</p>
      <h2>Clarity is an operating advantage</h2>
    </div>
    <div class="why-grid">
      <article class="why-item reveal"><h3>Business-first strategy</h3><p>Technology choices follow operational reality — risk, continuity, cost visibility, and the work your teams need to do next.</p></article>
      <article class="why-item reveal"><h3>Measured progress</h3><p>Phased delivery, explicit ownership, and communication that keeps transformation understandable for every stakeholder.</p></article>
      <article class="why-item reveal"><h3>Technical depth</h3><p>Architecture, migration, modernization, and operations are treated as one system, not disconnected workstreams.</p></article>
      <article class="why-item reveal"><h3>Long-term partnership</h3><p>Implementation is the midpoint. Optimization, support, and reliability keep the environment useful after go-live.</p></article>
    </div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">Technology leadership</p>
      <h2>The people behind the work</h2>
      <p>Cloud strategy, infrastructure expertise, service operations, and client leadership — together.</p>
    </div>
    <div class="team-feature reveal">
      <div class="team-photo"><img src="../assets/images/avery-chen.jpg" alt="Avery Chen"/></div>
      <div>
        <p class="team-meta">10+ years experience · Cloud</p>
        <h2>Avery Chen</h2>
        <p class="team-role">Cloud Transformation Lead</p>
        <p class="lede">10+ years in cloud transformation, helping organizations move from legacy infrastructure to scalable cloud environments — with architecture, migration, and operational readiness designed as one program.</p>
      </div>
    </div>
    <div class="team-grid">
      <article class="team-card reveal"><img src="../assets/images/jordan-patel.jpg" alt="Jordan Patel"/><div><p class="team-meta">Infrastructure</p><h3>Jordan Patel</h3><p class="team-role">Infrastructure Modernization Director</p><p>Specializes in infrastructure modernization, architecture, reliability, and building stronger technical foundations.</p></div></article>
      <article class="team-card reveal"><img src="../assets/images/taylor-brooks.jpg" alt="Taylor Brooks"/><div><p class="team-meta">Managed operations</p><h3>Taylor Brooks</h3><p class="team-role">Managed Services Manager</p><p>Focused on managed IT operations, service continuity, proactive monitoring, and long-term operational stability.</p></div></article>
      <article class="team-card reveal"><img src="../assets/images/morgan-ellis.jpg" alt="Morgan Ellis"/><div><p class="team-meta">Client operations</p><h3>Morgan Ellis</h3><p class="team-role">Client Success Partner</p><p>Bridges technology and business goals, ensuring projects deliver measurable outcomes and lasting client value.</p></div></article>
    </div>
  </div>
</section>
'''

services_body = '''
<section class="page-hero">
  <p class="kicker reveal">What we do</p>
  <h1 class="reveal">IT Services Built for Modern Growth</h1>
  <p class="lede reveal">Primecoreinfo helps organizations modernize infrastructure, accelerate cloud adoption, and maintain dependable IT operations with a strategic, security-conscious approach.</p>
</section>
<section>
  <div class="wrap svc-layout">
    <nav class="svc-nav" aria-label="Service categories">
      <a class="is-active" href="#cloud">01 Cloud</a>
      <a href="#infra">02 Infrastructure</a>
      <a href="#managed">03 Managed IT</a>
      <a href="#process">How we work</a>
    </nav>
    <div>
      <article class="svc-block" id="cloud">
        <p class="num">01</p>
        <h2>Cloud Transformation</h2>
        <p class="lede" style="margin-top:14px">Plan and execute cloud initiatives that improve scalability, streamline operations, and align technology investments with business goals — without losing operational control.</p>
        <div class="caps"><span>Architecture</span><span>Migration</span><span>Optimization</span><span>Security</span><span>Governance</span></div>
        <p>We map workloads, define the right target architecture, and guide migration in measured stages: assess dependencies and readiness, deliver secure landing zones, then improve governance, performance, and spend.</p>
        <details class="details"><summary>What this typically includes</summary><p>Workload assessment, target architecture, landing zones, migration waves, cost visibility, security controls, and operational readiness for steady-state operations.</p></details>
        <p style="margin-top:22px"><a class="btn" href="../cloud-transformation/">Explore cloud transformation</a></p>
      </article>
      <article class="svc-block" id="infra">
        <p class="num">02</p>
        <h2>Infrastructure Modernization</h2>
        <p class="lede" style="margin-top:14px">Refresh legacy environments with modern architecture, stronger performance, and a foundation built for security, automation, and growth.</p>
        <div class="caps"><span>Assessment</span><span>Platform refresh</span><span>Hybrid readiness</span><span>Resilience</span></div>
        <p>Aging infrastructure can slow delivery and increase operational risk. We assess compute, storage, networking, and platform readiness, then sequence upgrades so teams can move faster with confidence.</p>
        <details class="details"><summary>What this typically includes</summary><p>Server and storage upgrades, network improvements, virtualization, automation, security enhancements, monitoring, backup and recovery, and preparation for hybrid or cloud-connected operations.</p></details>
        <p style="margin-top:22px"><a class="btn" href="../infrastructure-modernization/">Explore modernization</a></p>
      </article>
      <article class="svc-block" id="managed">
        <p class="num">03</p>
        <h2>Managed IT Services</h2>
        <p class="lede" style="margin-top:14px">Maintain business continuity with proactive monitoring, responsive support, and ongoing optimization for critical systems and users.</p>
        <div class="caps"><span>Monitoring</span><span>Support</span><span>Maintenance</span><span>Improvement</span></div>
        <p>We bring structure to routine operations and fast response to unexpected issues — tracking health before small problems become disruptions, and turning operational data into a roadmap for reliability.</p>
        <details class="details"><summary>What this typically includes</summary><p>Proactive monitoring, responsive support for users and technical teams, operational management, performance and reliability improvements, and ongoing service continuity.</p></details>
        <p style="margin-top:22px"><a class="btn" href="../managed-it-services/">Explore managed IT</a></p>
      </article>
      <article class="svc-block" id="process">
        <p class="kicker">Delivery</p>
        <h2>A clear process</h2>
        <div class="process" style="margin-top:36px">
          <div class="process-line"></div>
          <article class="step is-on"><span class="step-dot"></span><span class="step-index">01</span><h3>Discover</h3><p>Evaluate environment, priorities, risks, and opportunities.</p></article>
          <article class="step"><span class="step-dot"></span><span class="step-index">02</span><h3>Strategy</h3><p>Roadmap for architecture, sequencing, governance, and readiness.</p></article>
          <article class="step"><span class="step-dot"></span><span class="step-index">03</span><h3>Execute</h3><p>Disciplined delivery, alignment, and minimal disruption.</p></article>
          <article class="step"><span class="step-dot"></span><span class="step-index">04</span><h3>Optimize</h3><p>Refine performance, strengthen resilience, support improvement.</p></article>
          <article class="step"><span class="step-dot"></span><span class="step-index">05</span><h3>Support</h3><p>Ongoing operations, monitoring, and partnership after go-live.</p></article>
        </div>
      </article>
    </div>
  </div>
</section>
'''

contact_body = '''
<section class="page-hero">
  <p class="kicker reveal">Start a conversation</p>
  <h1 class="reveal">Let's build what's next.</h1>
  <p class="lede reveal">The conversation starts with understanding your environment and goals — cloud strategy, infrastructure priorities, or ongoing IT support.</p>
</section>
<section>
  <div class="wrap contact-grid">
    <aside class="contact-card reveal">
      <p class="kicker">Direct</p>
      <h2 style="font-size:2rem">Tell us what you're building.</h2>
      <p style="margin-top:14px">Share the constraint, the system, or the outcome you need. We'll help shape the next step.</p>
      <dl>
        <div class="contact-meta"><dt>Email</dt><dd><a href="mailto:hello@primecoreinfo.com">hello@primecoreinfo.com</a></dd></div>
        <div class="contact-meta"><dt>Office hours</dt><dd>Monday – Friday<br>9:00 AM – 6:00 PM EST</dd></div>
        <div class="contact-meta"><dt>Response</dt><dd>We aim to respond to all inquiries within 1 business day.</dd></div>
      </dl>
    </aside>
    <div class="form-card reveal">
      <form id="contact-form" novalidate>
        <div class="form-grid">
          <div class="field"><input id="name" name="name" type="text" required placeholder=" "/><label for="name">Name</label><p class="help">Please add your name.</p></div>
          <div class="field"><input id="company" name="company" type="text" placeholder=" "/><label for="company">Company</label></div>
          <div class="field"><input id="email" name="email" type="email" required placeholder=" "/><label for="email">Work email</label><p class="help">A valid email is required.</p></div>
          <div class="field"><input id="phone" name="phone" type="tel" placeholder=" "/><label for="phone">Phone</label></div>
          <div class="field full">
            <select id="service" name="service" required>
              <option value="" selected disabled></option>
              <option>Cloud Transformation</option>
              <option>Infrastructure Modernization</option>
              <option>Managed IT Services</option>
              <option>Technology strategy</option>
              <option>Something else</option>
            </select>
            <label for="service">Service / area of interest</label>
            <p class="help">Choose an area of interest.</p>
          </div>
          <div class="field full"><textarea id="message" name="message" required placeholder=" "></textarea><label for="message">Project / message</label><p class="help">Tell us what needs to move forward.</p></div>
        </div>
        <p style="margin:18px 0 20px;font-size:0.92rem">This form opens your email client to send the inquiry to hello@primecoreinfo.com. Information is used only to respond.</p>
        <button class="btn" type="submit" data-magnetic>Start the conversation →</button>
      </form>
      <div class="form-success">
        <p class="kicker">Received</p>
        <h3>Thank you. We'll take it from here.</h3>
        <p style="margin-top:12px">If your email client opened, send the message to complete the inquiry. Otherwise write us directly at hello@primecoreinfo.com.</p>
      </div>
    </div>
  </div>
</section>
'''

insights_body = '''
<section class="page-hero">
  <p class="kicker reveal">Insights</p>
  <h1 class="reveal">Clear thinking for technology change.</h1>
  <p class="lede reveal">Practical perspectives for making cloud, infrastructure, and operations decisions with confidence.</p>
</section>
<section>
  <div class="wrap">
    <div class="filters" role="tablist">
      <button class="filter is-on" type="button" data-filter="all">All</button>
      <button class="filter" type="button" data-filter="cloud">Cloud</button>
      <button class="filter" type="button" data-filter="infra">Infrastructure</button>
      <button class="filter" type="button" data-filter="ops">IT Operations</button>
      <button class="filter" type="button" data-filter="transform">Transformation</button>
    </div>
    <a class="insight-feature reveal" data-cat="cloud" href="cloud-readiness/">
      <img src="../assets/vendor/wp-content/uploads/2026/08/2286378241.jpg" alt="Cloud operations"/>
      <div class="insight-copy">
        <p class="cat">Cloud</p>
        <h3>Cloud readiness: what to clarify before the first migration wave</h3>
        <p style="margin:14px 0 20px">The questions that keep cloud programs from creating more complexity than they remove.</p>
        <span class="text-link">Read article <span class="arrow">→</span></span>
      </div>
    </a>
    <div class="insight-grid" style="margin-top:16px">
      <a class="insight-card reveal" data-cat="infra" href="modern-foundations/"><div class="thumb"><img src="../assets/vendor/wp-content/uploads/2026/08/1455786903-1-2048x1147.jpg" alt=""/></div><div><p class="cat">Infrastructure</p><h3>Modern foundations</h3><p>How to sequence infrastructure improvements around business risk.</p></div></a>
      <a class="insight-card reveal" data-cat="ops" href="operational-resilience/"><div class="thumb"><img src="../assets/vendor/wp-content/uploads/2026/08/1928146086-768x512.jpg" alt=""/></div><div><p class="cat">IT Operations</p><h3>Operational resilience</h3><p>Why visibility and ownership matter as environments grow.</p></div></a>
      <a class="insight-card reveal" data-cat="transform" href="../cloud-transformation/"><div class="thumb"><img src="../assets/images/tech-cloud.jpg" alt=""/></div><div><p class="cat">Transformation</p><h3>From assessment to steady state</h3><p>How Primecoreinfo structures cloud work from readiness through operations.</p></div></a>
    </div>
  </div>
</section>
'''

privacy_body = '''
<section class="page-hero">
  <p class="kicker">Your information</p>
  <h1>Privacy policy</h1>
  <p class="lede">We respect the information you share when you explore Primecoreinfo or contact our team.</p>
</section>
<section>
  <div class="wrap prose">
    <h2>How we use information</h2>
    <p>Information submitted through this static site is used only to respond to your inquiry. We do not sell personal information or use it for unrelated marketing.</p>
    <h2>Questions</h2>
    <p>For privacy questions, contact us directly.</p>
    <p><a class="btn" href="mailto:hello@primecoreinfo.com?subject=Privacy%20question">Email privacy questions</a></p>
  </div>
</section>
'''

notfound_body = '''
<section class="page-hero" style="min-height:58vh;display:flex;flex-direction:column;justify-content:center">
  <p class="kicker">Unavailable</p>
  <h1>That page is outside this environment.</h1>
  <p class="lede">The route you requested does not exist. Return to the homepage to continue.</p>
  <p style="margin-top:28px"><a class="btn" href="./">Return home</a></p>
</section>
'''

cloud_body = '''
<section class="page-hero">
  <p class="kicker reveal">Services / Cloud</p>
  <h1 class="reveal">Move to the cloud with a plan you can trust.</h1>
  <p class="lede reveal">Build a cloud environment that improves agility, resilience, and cost visibility without losing operational control.</p>
</section>
<section>
  <div class="wrap">
    <div class="section-head reveal">
      <h2>From assessment to steady-state operations</h2>
      <p>We map workloads, define the right target architecture, and guide migration in measured stages.</p>
    </div>
    <div class="why-grid stagger">
      <article class="why-item reveal"><h3>01 Assess</h3><p>Understand dependencies, risk, cost, and readiness before the first wave moves.</p></article>
      <article class="why-item reveal"><h3>02 Transform</h3><p>Deliver secure landing zones and migration waves with governance in place.</p></article>
      <article class="why-item reveal"><h3>03 Optimize</h3><p>Improve performance, spend, security, and operating standards after cutover.</p></article>
      <article class="why-item reveal"><h3>04 Operate</h3><p>Keep the environment visible, supportable, and aligned to the business.</p></article>
    </div>
    <p class="reveal" style="margin-top:40px;display:flex;gap:12px;flex-wrap:wrap">
      <a class="btn" href="../contact/">Discuss your cloud journey</a>
      <a class="btn-ghost" href="../services/">All services</a>
    </p>
  </div>
</section>
'''

infra_body = '''
<section class="page-hero">
  <p class="kicker reveal">Services</p>
  <h1 class="reveal">Infrastructure Modernization</h1>
  <p class="lede reveal">Modernize core infrastructure to improve performance, resilience, and readiness for cloud-first operations. Primecoreinfo helps organizations simplify legacy environments, strengthen security, and build scalable foundations for growth.</p>
</section>
<section>
  <div class="wrap split">
    <div class="media reveal"><img class="clip-in" src="../assets/vendor/wp-content/uploads/2026/08/2286378241.jpg" alt="Infrastructure and operations"/><div class="media-overlay"></div></div>
    <div class="reveal">
      <p class="kicker">Overview</p>
      <h2>Build a stronger foundation</h2>
      <p class="lede" style="margin-top:14px">Aging infrastructure can slow delivery, increase operational risk, and make it harder to support modern workloads. We assess your current environment and create a practical modernization roadmap aligned to business priorities.</p>
      <p>From compute and storage to networking and platform readiness, the approach focuses on stability, efficiency, and long-term flexibility.</p>
    </div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="section-head reveal"><p class="kicker">Path</p><h2>A structured path with less disruption</h2></div>
    <div class="process">
      <div class="process-line"></div>
      <article class="step is-on"><span class="step-dot"></span><span class="step-index">01</span><h3>Assess</h3><p>Review infrastructure, dependencies, risks, and operational pain points.</p></article>
      <article class="step"><span class="step-dot"></span><span class="step-index">02</span><h3>Design</h3><p>Define target architecture, sequencing, and investment priorities.</p></article>
      <article class="step"><span class="step-dot"></span><span class="step-index">03</span><h3>Execute</h3><p>Implement upgrades in manageable stages.</p></article>
      <article class="step"><span class="step-dot"></span><span class="step-index">04</span><h3>Govern</h3><p>Establish monitoring, automation, security controls, and standards.</p></article>
      <article class="step"><span class="step-dot"></span><span class="step-index">05</span><h3>Support</h3><p>Continue optimization and operations after rollout.</p></article>
    </div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="section-head reveal"><p class="kicker">Capabilities</p><h2>Where we deliver value</h2></div>
    <div class="why-grid">
      <article class="why-item reveal"><h3>Platform refresh</h3><p>Upgrade core systems, reduce technical debt, and improve reliability across compute, storage, and network layers.</p></article>
      <article class="why-item reveal"><h3>Hybrid readiness</h3><p>Prepare infrastructure for hybrid and cloud-connected operations with better integration, scalability, and control.</p></article>
      <article class="why-item reveal"><h3>Operational resilience</h3><p>Strengthen monitoring, backup, recovery, and security practices to support uptime and continuity.</p></article>
    </div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="section-head reveal"><p class="kicker">Planning</p><h2>Answers for the planning stage</h2></div>
    <div class="faq">
      <details><summary>What does infrastructure modernization include?</summary><p>It can include server and storage upgrades, network improvements, virtualization, automation, security enhancements, and preparation for hybrid or cloud environments.</p></details>
      <details><summary>Can modernization happen without major downtime?</summary><p>Yes. A phased approach helps reduce disruption by sequencing changes carefully, validating dependencies, and planning cutovers around business needs.</p></details>
      <details><summary>How do you prioritize what to modernize first?</summary><p>We prioritize based on business impact, operational risk, performance constraints, security exposure, and the value of enabling future cloud initiatives.</p></details>
      <details><summary>Will this support future cloud transformation?</summary><p>Yes. Modern infrastructure creates the stability, visibility, and interoperability needed to support migration, scaling, and cloud-native adoption.</p></details>
      <details><summary>How long does a modernization project take?</summary><p>Timelines vary by environment size and complexity, but most engagements begin with an assessment and roadmap that define phased delivery milestones.</p></details>
      <details><summary>Do you help after implementation?</summary><p>Yes. We can support ongoing optimization, governance, monitoring, and managed services after rollout.</p></details>
    </div>
  </div>
</section>
'''

managed_body = '''
<section class="page-hero">
  <p class="kicker reveal">Services / Operations</p>
  <h1 class="reveal">Keep your systems steady while your team focuses on the work.</h1>
  <p class="lede reveal">Proactive monitoring, responsive support, and clear operational ownership for the systems your business relies on.</p>
</section>
<section>
  <div class="wrap">
    <div class="section-head reveal">
      <h2>Support that stays ahead of the day</h2>
      <p>We bring structure to routine operations and fast response to unexpected issues.</p>
    </div>
    <div class="why-grid stagger">
      <article class="why-item reveal"><h3>01 Monitor</h3><p>Track health and availability before small issues become disruptions.</p></article>
      <article class="why-item reveal"><h3>02 Support</h3><p>Give users and technical teams a responsive partner.</p></article>
      <article class="why-item reveal"><h3>03 Improve</h3><p>Turn operational data into a roadmap for reliability.</p></article>
    </div>
    <p class="reveal" style="margin-top:40px;display:flex;gap:12px;flex-wrap:wrap">
      <a class="btn" href="../contact/">Build your support plan</a>
      <a class="btn-ghost" href="../services/">All services</a>
    </p>
  </div>
</section>
'''

article_cloud = '''
<article class="page-hero article">
  <p class="cat">Cloud</p>
  <h1>Cloud readiness: what to clarify before the first migration wave</h1>
  <p class="lede">Cloud programs create value when the operating model is clear before workloads move. The first wave should follow a plan — not a sense of urgency.</p>
</article>
<section>
  <div class="wrap article">
    <p>Cloud transformation is often described as a destination. In practice it is a sequence of decisions: which workloads move, in what order, into which architecture, under which controls, and with which team accountable once they are live.</p>
    <h2>Start with dependencies</h2>
    <p>Most disruption in early migration waves comes from incomplete maps — identity, data, integrations, and operational tooling that were assumed to be simple. Assessment is not a delay. It is how you protect the business while you change the platform.</p>
    <h2>Name the operating model</h2>
    <p>Landing zones, governance, cost visibility, and security controls need owners. If those owners are undefined, cloud adoption tends to recreate the same complexity in a new environment.</p>
    <h2>Migrate in measured stages</h2>
    <p>Primecoreinfo structures cloud work around assessment, target architecture, migration waves, and optimization. The aim is agility and resilience without losing operational control.</p>
    <p><a class="btn" href="../../contact/">Discuss your cloud journey</a></p>
  </div>
</section>
'''

article_found = '''
<article class="page-hero article">
  <p class="cat">Infrastructure</p>
  <h1>Modern foundations: sequencing change around business risk</h1>
  <p class="lede">Infrastructure modernization is not a single upgrade. It is a prioritized path through technical debt, performance, and readiness for what the business needs next.</p>
</article>
<section>
  <div class="wrap article">
    <p>Aging infrastructure slows delivery and raises operational risk. The useful question is not “what is newest” but “what is blocking reliability, security, or the next cloud initiative.”</p>
    <h2>Prioritize by impact</h2>
    <p>Compute, storage, networking, and platform readiness should be sequenced around business impact, security exposure, and the value of enabling later transformation — not around a catalogue of tools.</p>
    <h2>Reduce disruption on purpose</h2>
    <p>Phased delivery, validated dependencies, and planned cutovers keep critical systems under control. Modernization can proceed without treating downtime as inevitable.</p>
    <h2>Leave the environment operable</h2>
    <p>Monitoring, backup, recovery, and standards are part of the work. A refreshed platform that nobody can see or support is not a stronger foundation.</p>
    <p><a class="btn" href="../../contact/">Talk about modernization</a></p>
  </div>
</section>
'''

article_ops = '''
<article class="page-hero article">
  <p class="cat">IT Operations</p>
  <h1>Operational resilience: visibility and ownership as environments grow</h1>
  <p class="lede">As systems expand, resilience depends less on heroics and more on who is watching, who is accountable, and how quickly small issues are caught.</p>
</article>
<section>
  <div class="wrap article">
    <p>Support that only reacts after users feel the problem is already late. Primecoreinfo’s managed services work is built around monitoring, responsive support, and improvement — so operations stay ahead of the day.</p>
    <h2>See the system before it fails</h2>
    <p>Health, availability, and performance need a clear signal. Visibility is how teams protect continuity without waiting for disruption to announce itself.</p>
    <h2>Give the work an owner</h2>
    <p>Users and technical teams need a partner with defined response, not a queue with no narrative. Ownership is what turns monitoring into action.</p>
    <h2>Use operations as a roadmap</h2>
    <p>Operational data should feed the next reliability decision — not sit unused. Improvement is part of support, not a separate project that never starts.</p>
    <p><a class="btn" href="../../contact/">Build your support plan</a></p>
  </div>
</section>
'''

home_redirect = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta http-equiv="refresh" content="0; url=../"/>
<link rel="canonical" href="../"/>
<title>Primecoreinfo</title>
<script>location.replace("../");</script>
</head>
<body>
<p><a href="../">Continue to Primecoreinfo</a></p>
</body>
</html>
'''

pages = [
    ("index.html", doc(
        "Primecoreinfo | Driving Cloud Transformation With Clarity",
        "Primecoreinfo helps organizations modernize infrastructure, accelerate cloud adoption, and maintain dependable IT operations.",
        "./", "home", home_body, True)),
    ("about/index.html", doc("About | Primecoreinfo", "Driving Cloud Transformation With Clarity — the Primecoreinfo story, approach, and technology leadership.", "../", "about", about_body)),
    ("services/index.html", doc("Services | Primecoreinfo", "IT services built for modern growth: cloud transformation, infrastructure modernization, and managed IT.", "../", "services", services_body)),
    ("contact/index.html", doc("Contact | Primecoreinfo", "Start a conversation about cloud strategy, infrastructure priorities, or ongoing IT support.", "../", "contact", contact_body, False)),
    ("insights/index.html", doc("Insights | Primecoreinfo", "Practical perspectives for cloud, infrastructure, and operations decisions.", "../", "insights", insights_body)),
    ("privacy-policy/index.html", doc("Privacy Policy | Primecoreinfo", "How Primecoreinfo uses information shared through this website.", "../", "home", privacy_body)),
    ("cloud-transformation/index.html", doc("Cloud Transformation | Primecoreinfo", "Move to the cloud with a plan you can trust.", "../", "services", cloud_body)),
    ("infrastructure-modernization/index.html", doc("Infrastructure Modernization | Primecoreinfo", "Modernize core infrastructure for performance, resilience, and cloud-first operations.", "../", "services", infra_body)),
    ("managed-it-services/index.html", doc("Managed IT Services | Primecoreinfo", "Proactive monitoring, responsive support, and operational ownership.", "../", "services", managed_body)),
    ("insights/cloud-readiness/index.html", doc("Cloud readiness | Primecoreinfo Insights", "What to clarify before the first migration wave.", "../../", "insights", article_cloud)),
    ("insights/modern-foundations/index.html", doc("Modern foundations | Primecoreinfo Insights", "How to sequence infrastructure improvements around business risk.", "../../", "insights", article_found)),
    ("insights/operational-resilience/index.html", doc("Operational resilience | Primecoreinfo Insights", "Why visibility and ownership matter as environments grow.", "../../", "insights", article_ops)),
    ("404.html", doc("Page Not Found | Primecoreinfo", "The requested route does not exist.", "./", "home", notfound_body, False)),
    ("home/index.html", home_redirect),
]

for rel, html in pages:
    write(rel, html)
print("done")
