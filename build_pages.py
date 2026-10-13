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
  <a class="brand" href="{href('home/')}" aria-label="Primecore Info Systems home"><img class="brand-mark-img" src="{href('assets/images/brand-logo.png')}" alt="Primecore Info Systems Logo"/><span>PRIMECORE INFO SYSTEMS</span></a>
  <nav class="nav" aria-label="Primary">
    <a class="{active("about").strip()}" href="{href("about/")}">About Us</a>
    <a class="{active("services").strip()}" href="{href("services/")}">Services</a>
    <a class="{active("solutions").strip()}" href="{href("#solutions")}">Solutions</a>
    <a class="{active("technologies").strip()}" href="{href("#technologies")}">Technologies</a>
    <a class="{active("privacy").strip()}" href="{href("privacy-policy/")}">Privacy Policy</a>
    <a class="{active("contact").strip()}" href="{href("contact/")}">Contact</a>
    <a class="btn-talk" data-magnetic href="{href("contact/")}">Get Started</a>
  </nav>
  <button class="menu-btn" type="button" aria-controls="mobile-nav" aria-expanded="false"><span></span><span></span><span></span><b class="sr-only">Open menu</b></button>
</header>
<nav class="mobile-nav" id="mobile-nav" hidden>
  <a href="{href("about/")}">About Us</a>
  <a href="{href("services/")}">Services</a>
  <a href="{href("#solutions")}">Solutions</a>
  <a href="{href("#technologies")}">Technologies</a>
  <a href="{href("privacy-policy/")}">Privacy Policy</a>
  <a href="{href("contact/")}">Contact</a>
  <a href="{href("contact/")}">Get Started</a>
</nav>'''

    cta = f'''<section class="wrap" style="padding-bottom:96px">
  <div class="cta-band reveal">
    <p class="kicker">Get Started</p>
    <h2>Build. Migrate. Automate. Optimize.</h2>
    <p>Primecore Info Systems helps businesses design, migrate, automate and optimize their IT infrastructure across AWS, Microsoft Azure and hybrid cloud environments.</p>
    <a class="btn" data-magnetic href="{href("contact/")}">Get Started <span aria-hidden="true">→</span></a>
  </div>
</section>'''

    footer = f'''<footer class="site-footer">
  <div class="footer-grid">
    <div class="footer-brand">
      <a class="brand" href="{href('home/')}"><img class="brand-mark-img" src="{href('assets/images/brand-logo.png')}" alt="Primecore Info Systems Logo"/><span>PRIMECORE INFO SYSTEMS</span></a>
      <p>Primecore Info Systems Pvt. Ltd. is an IT services and technology solutions company helping organizations modernize their infrastructure, adopt cloud technologies and build reliable digital platforms.</p>
    </div>
    <div>
      <h4>Navigation</h4>
      <a href="{href("about/")}">About Us</a>
      <a href="{href("services/")}">Services</a>
      <a href="{href("projects/")}">Case Studies &amp; Projects</a>
      <a href="{href("#solutions")}">Solutions</a>
      <a href="{href("#technologies")}">Technologies</a>
      <a href="{href("contact/")}">Contact</a>
    </div>
    <div>
      <h4>Services</h4>
      <a href="{href("services/#cloud-infrastructure")}">Cloud Infrastructure</a>
      <a href="{href("services/#devops-sre")}">DevOps &amp; SRE</a>
      <a href="{href("services/#cloud-migration")}">Cloud Migration</a>
      <a href="{href("services/#managed-infrastructure")}">Managed Infrastructure</a>
      <a href="{href("services/#security-governance")}">Security &amp; Governance</a>
      <a href="{href("services/#cloud-finops")}">Cloud Cost Optimization</a>
    </div>
    <div>
      <h4>Contact</h4>
      <a href="mailto:connect@primecoreinfo.com">connect@primecoreinfo.com</a>
      <a href="{href("privacy-policy/")}">Privacy Policy</a>
      <a href="{href("data-protection/")}">Data Protection</a>
      <a href="{href("terms-of-service/")}">Terms of Service</a>
      <a href="{href("data-deletion/")}">Data Deletion</a>
    </div>
  </div>
  <div class="footer-bottom">
    <span>© 2026 Primecore Info Systems Pvt. Ltd. All rights reserved.</span>
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
<link rel="icon" type="image/png" href="{root}assets/images/favicon.png"/>
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
    <text x="320" y="268" text-anchor="middle" class="arch-label">PRIMECORE</text>
    <text x="320" y="290" text-anchor="middle" class="arch-label" style="fill:#9BEFE5;font-size:10px;font-weight:600">AWS &amp; AZURE</text>
  </g>
  <g class="arch-float">
    <rect class="arch-node" x="262" y="54" width="116" height="54" rx="14"/>
    <text x="320" y="86" text-anchor="middle" class="arch-label">Cloud</text>
  </g>
  <g class="arch-float">
    <rect class="arch-node" x="52" y="140" width="140" height="54" rx="14"/>
    <text x="122" y="172" text-anchor="middle" class="arch-label">DevOps</text>
  </g>
  <g class="arch-float">
    <rect class="arch-node" x="448" y="140" width="140" height="54" rx="14"/>
    <text x="518" y="172" text-anchor="middle" class="arch-label">Security</text>
  </g>
  <g class="arch-float">
    <rect class="arch-node" x="64" y="374" width="140" height="54" rx="14"/>
    <text x="134" y="406" text-anchor="middle" class="arch-label">Migration</text>
  </g>
  <g class="arch-float">
    <rect class="arch-node" x="436" y="374" width="140" height="54" rx="14"/>
    <text x="506" y="406" text-anchor="middle" class="arch-label">FinOps</text>
  </g>
  <g class="arch-float">
    <rect class="arch-node" x="250" y="462" width="140" height="54" rx="14"/>
    <text x="320" y="494" text-anchor="middle" class="arch-label">Managed IT</text>
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
    <p class="kicker reveal">Primecore Info Systems</p>
    <h1 class="reveal">Build. Migrate.<br>Automate.<br><em class="accent">Optimize.</em></h1>
    <p class="lede reveal" style="font-weight:600;color:var(--white);margin-bottom:12px">Modern IT Infrastructure &amp; Cloud Solutions for a Smarter, More Secure Business</p>
    <p class="lede reveal">Primecore Info Systems helps businesses design, migrate, automate and optimize their IT infrastructure across AWS, Microsoft Azure and hybrid cloud environments.</p>
    <div class="hero-actions reveal" style="margin-top:28px">
      <a class="btn" data-magnetic href="../contact/">Get Started</a>
      <a class="btn-ghost" href="../services/">Explore Our Services</a>
    </div>
  </div>
  {ARCH}
  <div class="scroll-hint"><i></i> Scroll</div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="hero-highlights reveal">
      <div class="highlight-card">
        <h4>Cloud &amp; Infrastructure</h4>
        <p>Scalable and reliable cloud infrastructure built around your business needs.</p>
      </div>
      <div class="highlight-card">
        <h4>DevOps &amp; Automation</h4>
        <p>Accelerate software delivery with modern CI/CD, Infrastructure as Code and automation.</p>
      </div>
      <div class="highlight-card">
        <h4>Migration &amp; Modernization</h4>
        <p>Seamlessly migrate applications, databases and infrastructure to modern cloud platforms.</p>
      </div>
      <div class="highlight-card">
        <h4>Security &amp; Governance</h4>
        <p>Build secure, compliant and well-governed cloud environments.</p>
      </div>
      <div class="highlight-card">
        <h4>Cost Optimization</h4>
        <p>Identify waste, optimize cloud resources and improve infrastructure efficiency.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">About Us</p>
      <h2>Technology That Works for Your Business</h2>
    </div>
    <div class="statement">
      <div class="reveal">
        <p class="lede" style="font-size:1.15rem;color:var(--white)">Primecore Info Systems Pvt. Ltd. is an IT services and technology solutions company helping organizations modernize their infrastructure, adopt cloud technologies and build reliable digital platforms.</p>
        <p style="margin-top:16px">Our expertise spans AWS, Microsoft Azure, Kubernetes, DevOps, Infrastructure Automation, Cloud Migration, Security, Governance and FinOps.</p>
      </div>
      <div class="reveal">
        <p>We work with businesses of different sizes to simplify complex infrastructure challenges and deliver solutions that are scalable, secure, reliable and cost-efficient.</p>
        <div class="line-flow">
          <b>Assess</b><i></i>
          <b>Plan</b><i></i>
          <b>Implement</b><i></i>
          <b>Optimize</b><i></i>
          <b>Support</b>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="services">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">Our Services</p>
      <h2>Comprehensive IT &amp; Cloud Capabilities</h2>
      <p>From cloud architecture to ongoing FinOps and managed infrastructure, we cover every aspect of modern IT operations.</p>
    </div>
    <div class="service-stack stagger">
      <a class="service-panel reveal" href="../services/#cloud-infrastructure">
        <span class="sp-num">01</span>
        <div class="sp-copy">
          <h3>Cloud Infrastructure</h3>
          <p>AWS Cloud Solutions, Microsoft Azure Solutions, Cloud Architecture, Hybrid &amp; Multi-Cloud, Landing Zones, Networking &amp; Infrastructure, High Availability, Disaster Recovery.</p>
        </div>
        <span class="sp-go" aria-hidden="true">→</span>
      </a>
      <a class="service-panel reveal" href="../services/#devops-sre">
        <span class="sp-num">02</span>
        <div class="sp-copy">
          <h3>DevOps &amp; SRE</h3>
          <p>DevOps Consulting, Site Reliability Engineering, CI/CD Implementation, Infrastructure as Code, Terraform / OpenTofu, Kubernetes, Containerization, Monitoring &amp; Observability, Automation.</p>
        </div>
        <span class="sp-go" aria-hidden="true">→</span>
      </a>
      <a class="service-panel reveal" href="../services/#cloud-migration">
        <span class="sp-num">03</span>
        <div class="sp-copy">
          <h3>Cloud Migration</h3>
          <p>Application Migration, Database Migration, Infrastructure Migration, Cloud Modernization, AWS &amp; Azure Migration, Hybrid Cloud Migration, Migration Planning &amp; Assessment.</p>
        </div>
        <span class="sp-go" aria-hidden="true">→</span>
      </a>
      <a class="service-panel reveal" href="../services/#managed-infrastructure">
        <span class="sp-num">04</span>
        <div class="sp-copy">
          <h3>Managed Infrastructure Services</h3>
          <p>Cloud Infrastructure Management, Monitoring &amp; Support, Incident Management, Infrastructure Maintenance, Backup &amp; Disaster Recovery, Performance Optimization.</p>
        </div>
        <span class="sp-go" aria-hidden="true">→</span>
      </a>
      <a class="service-panel reveal" href="../services/#security-governance">
        <span class="sp-num">05</span>
        <div class="sp-copy">
          <h3>Security &amp; Governance</h3>
          <p>Cloud Security, Identity &amp; Access Management, Security Best Practices, Infrastructure Security, Governance Frameworks, Policy &amp; Compliance, Secure Cloud Architecture.</p>
        </div>
        <span class="sp-go" aria-hidden="true">→</span>
      </a>
      <a class="service-panel reveal" href="../services/#cloud-finops">
        <span class="sp-num">06</span>
        <div class="sp-copy">
          <h3>Cloud Cost Optimization / FinOps</h3>
          <p>Cloud Cost Assessment, Resource Optimization, Kubernetes Cost Optimization, Cost Visibility, Cloud Waste Reduction, FinOps Strategy, Cost Allocation &amp; Reporting.</p>
        </div>
        <span class="sp-go" aria-hidden="true">→</span>
      </a>
      <a class="service-panel reveal" href="../services/#app-tech-services">
        <span class="sp-num">07</span>
        <div class="sp-copy">
          <h3>Application &amp; Technology Services</h3>
          <p>Application Deployment, Java Application Infrastructure, Automation, Infrastructure Support, Technology Consulting.</p>
        </div>
        <span class="sp-go" aria-hidden="true">→</span>
      </a>
    </div>
  </div>
</section>

<section id="solutions">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">Solutions</p>
      <h2>Targeted Solutions for Critical Challenges</h2>
    </div>
    <div class="solutions-grid stagger">
      <div class="solution-card reveal">
        <h3>Cloud Migration &amp; Modernization</h3>
        <p>“Move from traditional infrastructure to modern cloud environments with minimal disruption.”</p>
      </div>
      <div class="solution-card reveal">
        <h3>High Availability &amp; Disaster Recovery</h3>
        <p>“Design resilient infrastructure to keep critical applications available and recoverable.”</p>
      </div>
      <div class="solution-card reveal">
        <h3>Kubernetes &amp; Container Platforms</h3>
        <p>“Build, operate and optimize scalable Kubernetes environments across AWS and Azure.”</p>
      </div>
      <div class="solution-card reveal">
        <h3>DevOps Transformation</h3>
        <p>“Automate development and deployment processes to improve speed, reliability and consistency.”</p>
      </div>
      <div class="solution-card reveal">
        <h3>Cloud Cost Optimization</h3>
        <p>“Gain visibility into cloud spending and optimize infrastructure without compromising performance.”</p>
      </div>
      <div class="solution-card reveal">
        <h3>Secure Cloud Infrastructure</h3>
        <p>“Implement security, identity, governance and best practices from the foundation up.”</p>
      </div>
    </div>
  </div>
</section>

<section id="technologies">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">Technologies</p>
      <h2>Modern Tooling &amp; Platform Ecosystem</h2>
    </div>
    <div class="tech-grid stagger">
      <div class="tech-category reveal">
        <h3>Cloud</h3>
        <div class="tech-tags">
          <span class="tech-tag">AWS</span>
          <span class="tech-tag">Microsoft Azure</span>
        </div>
      </div>
      <div class="tech-category reveal">
        <h3>Containers</h3>
        <div class="tech-tags">
          <span class="tech-tag">Kubernetes</span>
          <span class="tech-tag">Amazon EKS</span>
          <span class="tech-tag">Azure AKS</span>
          <span class="tech-tag">Docker</span>
        </div>
      </div>
      <div class="tech-category reveal">
        <h3>Infrastructure as Code</h3>
        <div class="tech-tags">
          <span class="tech-tag">Terraform</span>
          <span class="tech-tag">OpenTofu</span>
        </div>
      </div>
      <div class="tech-category reveal">
        <h3>CI/CD</h3>
        <div class="tech-tags">
          <span class="tech-tag">GitHub Actions</span>
          <span class="tech-tag">Jenkins</span>
        </div>
      </div>
      <div class="tech-category reveal">
        <h3>Observability</h3>
        <div class="tech-tags">
          <span class="tech-tag">Datadog</span>
          <span class="tech-tag">Prometheus</span>
          <span class="tech-tag">Grafana</span>
        </div>
      </div>
      <div class="tech-category reveal">
        <h3>Automation</h3>
        <div class="tech-tags">
          <span class="tech-tag">Ansible</span>
          <span class="tech-tag">Chef</span>
          <span class="tech-tag">Rundeck</span>
        </div>
      </div>
      <div class="tech-category reveal">
        <h3>Scripting</h3>
        <div class="tech-tags">
          <span class="tech-tag">Python</span>
          <span class="tech-tag">Shell</span>
          <span class="tech-tag">PowerShell</span>
          <span class="tech-tag">Ruby</span>
        </div>
      </div>
      <div class="tech-category reveal">
        <h3>Databases &amp; Platforms</h3>
        <div class="tech-tags">
          <span class="tech-tag">MongoDB</span>
          <span class="tech-tag">PostgreSQL</span>
          <span class="tech-tag">InfluxDB</span>
          <span class="tech-tag">Aiven</span>
          <span class="tech-tag">MongoDB Atlas</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="why-primecore">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">Why Primecore</p>
      <h2>Built Around Technical Precision and Partnership</h2>
    </div>
    <div class="why-grid stagger">
      <article class="why-item reveal">
        <h3>Deep Technical Expertise</h3>
        <p>“Strong expertise across cloud, DevOps, infrastructure and automation.”</p>
      </article>
      <article class="why-item reveal">
        <h3>Cloud Agnostic Approach</h3>
        <p>“Solutions designed around your requirements rather than a single technology.”</p>
      </article>
      <article class="why-item reveal">
        <h3>Security First</h3>
        <p>“Security and governance are considered throughout the infrastructure lifecycle.”</p>
      </article>
      <article class="why-item reveal">
        <h3>Automation Driven</h3>
        <p>“Reduce manual effort through Infrastructure as Code and intelligent automation.”</p>
      </article>
      <article class="why-item reveal">
        <h3>Cost Conscious</h3>
        <p>“Build infrastructure with performance, scalability and cost efficiency in mind.”</p>
      </article>
      <article class="why-item reveal">
        <h3>Long-Term Partnership</h3>
        <p>“We don't just implement solutions. We help maintain, improve and evolve them.”</p>
      </article>
    </div>
  </div>
</section>

<section id="clients">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">Our Clients</p>
      <h2>Trusted by Industry Leaders</h2>
      <p>We work with enterprise technology organizations to engineer, optimize, and manage resilient cloud infrastructure.</p>
    </div>
    <div class="clients-grid stagger">
      <div class="client-card reveal">
        <div class="client-card-header">
          <span class="client-badge-pill">Enterprise Client</span>
          <span class="client-domain-tag">AWS Cloud Infrastructure</span>
        </div>
        <div class="client-brand-display">
          <h3 class="client-name-title">StarNext Innovations Pvt. Ltd.</h3>
          <p class="client-scope-subtitle">AWS Infrastructure, FinOps, Disaster Recovery &amp; Monitoring</p>
        </div>
        <p class="client-description">StarNext Innovations Pvt. Ltd. is an enterprise technology client leveraging AWS cloud infrastructure to support business-critical applications, reliable operations, and scalable IT services.</p>
        <div class="client-card-footer">
          <a class="client-case-link" href="../projects/starnext-innovations-aws-infrastructure/">Read Case Study <span aria-hidden="true">&rarr;</span></a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="demo-slideshow-section" id="demo">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">See Our Solutions in Action</p>
      <h2>Explore our software solutions through quick product demonstrations.</h2>
    </div>
    <div class="demo-showcase-container">
      <div class="demo-tab-nav" role="tablist" aria-label="Demo videos">
        <button class="demo-tab is-active" type="button" role="tab" aria-selected="true" aria-controls="home-demo-slide-0" data-demo="0">
          <span class="demo-tab-num">01</span> Kitchen Order System
        </button>
        <button class="demo-tab" type="button" role="tab" aria-selected="false" aria-controls="home-demo-slide-1" data-demo="1">
          <span class="demo-tab-num">02</span> Restaurant OS
        </button>
        <button class="demo-tab" type="button" role="tab" aria-selected="false" aria-controls="home-demo-slide-2" data-demo="2">
          <span class="demo-tab-num">03</span> Clinic OS
        </button>
      </div>
      <div class="demo-viewport">
        <div class="demo-slide" id="home-demo-slide-0" role="tabpanel">
          <div class="demo-frame">
            <div class="demo-frame-header">
              <div class="demo-frame-dots">
                <span class="demo-dot red"></span>
                <span class="demo-dot yellow"></span>
                <span class="demo-dot green"></span>
              </div>
              <span class="demo-badge">LIVE DEMO</span>
            </div>
            <div class="demo-video-wrapper">
              <video class="demo-player" id="home-demo-video-0" poster="../assets/videos/poster-01.jpg" controls preload="none">
                <source src="../assets/videos/01.mp4" type="video/mp4"/>
              </video>
            </div>
          </div>
          <div class="demo-details">
            <div class="demo-meta">
              <span class="demo-pill">Product Demo</span>
              <span class="demo-domain">Restaurant Tech</span>
            </div>
            <h3 class="demo-title">Kitchen Order System</h3>
            <p class="demo-desc">Explore kitchen order management and ticket tracking.</p>
          </div>
        </div>
        <div class="demo-slide" id="home-demo-slide-1" role="tabpanel" hidden>
          <div class="demo-frame">
            <div class="demo-frame-header">
              <div class="demo-frame-dots">
                <span class="demo-dot red"></span>
                <span class="demo-dot yellow"></span>
                <span class="demo-dot green"></span>
              </div>
              <span class="demo-badge">LIVE DEMO</span>
            </div>
            <div class="demo-video-wrapper">
              <video class="demo-player" id="home-demo-video-1" poster="../assets/videos/poster-02.jpg" controls preload="none">
                <source src="../assets/videos/02.mp4" type="video/mp4"/>
              </video>
            </div>
          </div>
          <div class="demo-details">
            <div class="demo-meta">
              <span class="demo-pill">Product Demo</span>
              <span class="demo-domain">Restaurant Tech</span>
            </div>
            <h3 class="demo-title">Restaurant OS</h3>
            <p class="demo-desc">End-to-end restaurant operations and management platform.</p>
          </div>
        </div>
        <div class="demo-slide" id="home-demo-slide-2" role="tabpanel" hidden>
          <div class="demo-frame">
            <div class="demo-frame-header">
              <div class="demo-frame-dots">
                <span class="demo-dot red"></span>
                <span class="demo-dot yellow"></span>
                <span class="demo-dot green"></span>
              </div>
              <span class="demo-badge">LIVE DEMO</span>
            </div>
            <div class="demo-video-wrapper">
              <video class="demo-player" id="home-demo-video-2" poster="../assets/videos/poster-03.jpg" controls preload="none">
                <source src="../assets/videos/03.mp4" type="video/mp4"/>
              </video>
            </div>
          </div>
          <div class="demo-details">
            <div class="demo-meta">
              <span class="demo-pill">Product Demo</span>
              <span class="demo-domain">Healthcare Tech</span>
            </div>
            <h3 class="demo-title">Clinic OS</h3>
            <p class="demo-desc">Clinic management and patient operations platform.</p>
          </div>
        </div>
      </div>
      <div class="demo-controls-bar">
        <button class="demo-nav-btn" id="home-demo-prev" aria-label="Previous demo" type="button">&#8592;</button>
        <div class="demo-indicators" role="group" aria-label="Demo slide indicators">
          <button class="demo-dot-btn is-active" type="button" aria-label="Demo 1" data-demo="0"></button>
          <button class="demo-dot-btn" type="button" aria-label="Demo 2" data-demo="1"></button>
          <button class="demo-dot-btn" type="button" aria-label="Demo 3" data-demo="2"></button>
        </div>
        <button class="demo-nav-btn" id="home-demo-next" aria-label="Next demo" type="button">&#8594;</button>
      </div>
    </div>
  </div>
</section>
<script>
  (function() {{
    var section = document.getElementById('demo');
    if (!section) return;
    var tabs = section.querySelectorAll('.demo-tab');
    var slides = section.querySelectorAll('.demo-slide');
    var dots = section.querySelectorAll('.demo-dot-btn');
    var videos = section.querySelectorAll('.demo-player');
    var current = 0;
    function switchTo(n) {{
      videos[current].pause();
      slides[current].hidden = true;
      tabs[current].classList.remove('is-active');
      tabs[current].setAttribute('aria-selected', 'false');
      dots[current].classList.remove('is-active');
      current = (n + slides.length) % slides.length;
      slides[current].hidden = false;
      tabs[current].classList.add('is-active');
      tabs[current].setAttribute('aria-selected', 'true');
      dots[current].classList.add('is-active');
    }}
    tabs.forEach(function(tab, i) {{ tab.addEventListener('click', function() {{ switchTo(i); }}); }});
    dots.forEach(function(dot, i) {{ dot.addEventListener('click', function() {{ switchTo(i); }}); }});
    document.getElementById('home-demo-prev').addEventListener('click', function() {{ switchTo(current - 1); }});
    document.getElementById('home-demo-next').addEventListener('click', function() {{ switchTo(current + 1); }});
  }})();
</script>

<section id="industries">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">Industries</p>
      <h2>Sectors We Serve</h2>
    </div>
    <div class="industries-grid stagger">
      <div class="industry-card reveal"><span class="industry-icon"></span>Financial Services &amp; Banking</div>
      <div class="industry-card reveal"><span class="industry-icon"></span>Education</div>
      <div class="industry-card reveal"><span class="industry-icon"></span>Healthcare &amp; Wellness</div>
      <div class="industry-card reveal"><span class="industry-icon"></span>Retail &amp; E-commerce</div>
      <div class="industry-card reveal"><span class="industry-icon"></span>Technology Companies</div>
      <div class="industry-card reveal"><span class="industry-icon"></span>Startups &amp; SMEs</div>
      <div class="industry-card reveal"><span class="industry-icon"></span>Professional Services</div>
      <div class="industry-card reveal"><span class="industry-icon"></span>Local Businesses</div>
    </div>
  </div>
</section>

<section id="our-process">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">Our Process</p>
      <h2>A Structured Path to Success</h2>
    </div>
    <div class="process">
      <div class="process-line" aria-hidden="true"></div>
      <article class="step is-on">
        <span class="step-dot"></span><span class="step-index">01</span>
        <h3>Discover</h3>
        <p>“Understand your business, infrastructure and challenges.”</p>
      </article>
      <article class="step">
        <span class="step-dot"></span><span class="step-index">02</span>
        <h3>Assess</h3>
        <p>“Analyze your existing environment, technology and costs.”</p>
      </article>
      <article class="step">
        <span class="step-dot"></span><span class="step-index">03</span>
        <h3>Design</h3>
        <p>“Create a secure, scalable and cost-effective solution.”</p>
      </article>
      <article class="step">
        <span class="step-dot"></span><span class="step-index">04</span>
        <h3>Implement</h3>
        <p>“Migrate, automate and deploy with minimal disruption.”</p>
      </article>
      <article class="step">
        <span class="step-dot"></span><span class="step-index">05</span>
        <h3>Optimize</h3>
        <p>“Continuously improve performance, security, reliability and cost.”</p>
      </article>
    </div>
  </div>
</section>
'''

about_body = '''
<section class="page-hero">
  <p class="kicker reveal">About Us</p>
  <h1 class="reveal">Technology That Works for Your Business</h1>
  <p class="lede reveal" style="font-size:1.25rem;color:var(--white);margin-top:16px">Primecore Info Systems Pvt. Ltd. is an IT services and technology solutions company helping organizations modernize their infrastructure, adopt cloud technologies and build reliable digital platforms.</p>
</section>
<section>
  <div class="wrap split">
    <div class="reveal">
      <p class="kicker">Our Expertise</p>
      <h2>Deep Domain Expertise Across AWS, Azure &amp; Modern DevOps</h2>
      <p class="lede" style="margin-top:16px">Our expertise spans AWS, Microsoft Azure, Kubernetes, DevOps, Infrastructure Automation, Cloud Migration, Security, Governance and FinOps.</p>
      <p class="lede" style="margin-top:12px">We work with businesses of different sizes to simplify complex infrastructure challenges and deliver solutions that are scalable, secure, reliable and cost-efficient.</p>
      <p style="margin-top:24px"><a class="btn" href="../services/">Explore Our Services</a></p>
    </div>
    <div class="media reveal"><img class="clip-in" src="../assets/images/about-story.jpg" alt="Technology team collaborating"/><div class="media-overlay"></div></div>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">Our Approach</p>
      <h2>Assess → Plan → Implement → Optimize → Support</h2>
      <p>A structured, end-to-end approach to infrastructure and cloud management.</p>
    </div>
    <div class="process" style="margin-top:36px">
      <div class="process-line" aria-hidden="true"></div>
      <article class="step is-on"><span class="step-dot"></span><span class="step-index">01</span><h3>Assess</h3><p>Understand your business, infrastructure, existing environment, technology and costs.</p></article>
      <article class="step"><span class="step-dot"></span><span class="step-index">02</span><h3>Plan</h3><p>Build a secure, scalable and cost-effective solution roadmap aligned with your business goals.</p></article>
      <article class="step"><span class="step-dot"></span><span class="step-index">03</span><h3>Implement</h3><p>Migrate, automate and deploy with minimal disruption to ongoing operations.</p></article>
      <article class="step"><span class="step-dot"></span><span class="step-index">04</span><h3>Optimize</h3><p>Continuously improve performance, security, reliability and cloud spending.</p></article>
      <article class="step"><span class="step-dot"></span><span class="step-index">05</span><h3>Support</h3><p>Long-term operational management, proactive monitoring, and evolving technical support.</p></article>
    </div>
  </div>
</section>
<section id="clients">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">Our Clients</p>
      <h2>Client Partnerships &amp; Engagements</h2>
      <p>We partner with enterprise organizations to deliver dependable cloud solutions, FinOps optimization, and resilient IT operations.</p>
    </div>
    <div class="clients-grid stagger">
      <div class="client-card reveal">
        <div class="client-card-header">
          <span class="client-badge-pill">Enterprise Client</span>
          <span class="client-domain-tag">AWS Cloud Infrastructure</span>
        </div>
        <div class="client-brand-display">
          <h3 class="client-name-title">StarNext Innovations Pvt. Ltd.</h3>
          <p class="client-scope-subtitle">AWS Infrastructure, FinOps, Disaster Recovery &amp; Monitoring</p>
        </div>
        <p class="client-description">StarNext Innovations Pvt. Ltd. is an enterprise technology client leveraging AWS cloud infrastructure to support business-critical applications, reliable operations, and scalable IT services.</p>
        <div class="client-card-footer">
          <a class="client-case-link" href="../projects/starnext-innovations-aws-infrastructure/">Read Case Study <span aria-hidden="true">&rarr;</span></a>
        </div>
      </div>
    </div>
  </div>
</section>
'''

services_body = '''
<section class="page-hero">
  <p class="kicker reveal">Services</p>
  <h1 class="reveal">Our Services</h1>
  <p class="lede reveal" style="margin-top:14px">Primecore Info Systems delivers end-to-end cloud, DevOps, migration, security, FinOps, and managed infrastructure services.</p>
</section>

<section>
  <div class="wrap svc-layout">
    <nav class="svc-nav" aria-label="Service categories">
      <a class="is-active" href="#cloud-infrastructure">01 Cloud Infrastructure</a>
      <a href="#devops-sre">02 DevOps &amp; SRE</a>
      <a href="#cloud-migration">03 Cloud Migration</a>
      <a href="#managed-infrastructure">04 Managed Infrastructure</a>
      <a href="#security-governance">05 Security &amp; Governance</a>
      <a href="#cloud-finops">06 Cloud Cost Optimization</a>
      <a href="#app-tech-services">07 App &amp; Tech Services</a>
    </nav>
    <div>
      <article class="svc-block" id="cloud-infrastructure">
        <p class="num">01</p>
        <h2>Cloud Infrastructure</h2>
        <p class="lede" style="margin-top:14px">Scalable and reliable cloud infrastructure built around your business needs.</p>
        <div class="svc-list-grid">
          <div class="svc-list-item">AWS Cloud Solutions</div>
          <div class="svc-list-item">Microsoft Azure Solutions</div>
          <div class="svc-list-item">Cloud Architecture</div>
          <div class="svc-list-item">Hybrid &amp; Multi-Cloud</div>
          <div class="svc-list-item">Landing Zones</div>
          <div class="svc-list-item">Networking &amp; Infrastructure</div>
          <div class="svc-list-item">High Availability</div>
          <div class="svc-list-item">Disaster Recovery</div>
        </div>
      </article>

      <article class="svc-block" id="devops-sre">
        <p class="num">02</p>
        <h2>DevOps &amp; SRE</h2>
        <p class="lede" style="margin-top:14px">Accelerate software delivery with modern CI/CD, Infrastructure as Code and automation.</p>
        <div class="svc-list-grid">
          <div class="svc-list-item">DevOps Consulting</div>
          <div class="svc-list-item">Site Reliability Engineering</div>
          <div class="svc-list-item">CI/CD Implementation</div>
          <div class="svc-list-item">Infrastructure as Code</div>
          <div class="svc-list-item">Terraform / OpenTofu</div>
          <div class="svc-list-item">Kubernetes</div>
          <div class="svc-list-item">Containerization</div>
          <div class="svc-list-item">Monitoring &amp; Observability</div>
          <div class="svc-list-item">Automation</div>
        </div>
      </article>

      <article class="svc-block" id="cloud-migration">
        <p class="num">03</p>
        <h2>Cloud Migration</h2>
        <p class="lede" style="margin-top:14px">Seamlessly migrate applications, databases and infrastructure to modern cloud platforms.</p>
        <div class="svc-list-grid">
          <div class="svc-list-item">Application Migration</div>
          <div class="svc-list-item">Database Migration</div>
          <div class="svc-list-item">Infrastructure Migration</div>
          <div class="svc-list-item">Cloud Modernization</div>
          <div class="svc-list-item">AWS &amp; Azure Migration</div>
          <div class="svc-list-item">Hybrid Cloud Migration</div>
          <div class="svc-list-item">Migration Planning &amp; Assessment</div>
        </div>
      </article>

      <article class="svc-block" id="managed-infrastructure">
        <p class="num">04</p>
        <h2>Managed Infrastructure Services</h2>
        <p class="lede" style="margin-top:14px">Proactive monitoring, maintenance, and continuous optimization for peak uptime.</p>
        <div class="svc-list-grid">
          <div class="svc-list-item">Cloud Infrastructure Management</div>
          <div class="svc-list-item">Monitoring &amp; Support</div>
          <div class="svc-list-item">Incident Management</div>
          <div class="svc-list-item">Infrastructure Maintenance</div>
          <div class="svc-list-item">Backup &amp; Disaster Recovery</div>
          <div class="svc-list-item">Performance Optimization</div>
        </div>
      </article>

      <article class="svc-block" id="security-governance">
        <p class="num">05</p>
        <h2>Security &amp; Governance</h2>
        <p class="lede" style="margin-top:14px">Build secure, compliant and well-governed cloud environments.</p>
        <div class="svc-list-grid">
          <div class="svc-list-item">Cloud Security</div>
          <div class="svc-list-item">Identity &amp; Access Management</div>
          <div class="svc-list-item">Security Best Practices</div>
          <div class="svc-list-item">Infrastructure Security</div>
          <div class="svc-list-item">Governance Frameworks</div>
          <div class="svc-list-item">Policy &amp; Compliance</div>
          <div class="svc-list-item">Secure Cloud Architecture</div>
        </div>
      </article>

      <article class="svc-block" id="cloud-finops">
        <p class="num">06</p>
        <h2>Cloud Cost Optimization / FinOps</h2>
        <p class="lede" style="margin-top:14px">Identify waste, optimize cloud resources and improve infrastructure efficiency.</p>
        <div class="svc-list-grid">
          <div class="svc-list-item">Cloud Cost Assessment</div>
          <div class="svc-list-item">Resource Optimization</div>
          <div class="svc-list-item">Kubernetes Cost Optimization</div>
          <div class="svc-list-item">Cost Visibility</div>
          <div class="svc-list-item">Cloud Waste Reduction</div>
          <div class="svc-list-item">FinOps Strategy</div>
          <div class="svc-list-item">Cost Allocation &amp; Reporting</div>
        </div>
      </article>

      <article class="svc-block" id="app-tech-services">
        <p class="num">07</p>
        <h2>Application &amp; Technology Services</h2>
        <p class="lede" style="margin-top:14px">End-to-end technology consulting and application infrastructure support.</p>
        <div class="svc-list-grid">
          <div class="svc-list-item">Application Deployment</div>
          <div class="svc-list-item">Java Application Infrastructure</div>
          <div class="svc-list-item">Automation</div>
          <div class="svc-list-item">Infrastructure Support</div>
          <div class="svc-list-item">Technology Consulting</div>
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
        <div class="contact-meta"><dt>Email</dt><dd><a href="mailto:connect@primecoreinfo.com">connect@primecoreinfo.com</a></dd></div>
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
        <p style="margin:18px 0 16px;font-size:0.92rem">Information submitted is used only to respond to your inquiry.</p>
        <div class="form-error-banner" hidden style="color:#e08a8a;font-size:0.92rem;margin:0 0 16px;padding:10px 14px;border-radius:8px;background:rgba(224,138,138,0.1);border:1px solid rgba(224,138,138,0.3)"></div>
        <button class="btn" type="submit" data-magnetic>Start the conversation →</button>
      </form>
      <div class="form-success">
        <p class="kicker">Received</p>
        <h3>Thank you. We'll take it from here.</h3>
        <p style="margin-top:12px">If your email client opened, send the message to complete the inquiry. Otherwise write us directly at connect@primecoreinfo.com.</p>
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
  <p class="kicker">Transparency &amp; Legal Notices</p>
  <h1>Privacy Policy</h1>
  <p class="lede">How Primecore Info Systems collects, handles, and protects information submitted through this website.</p>
</section>

<section>
  <div class="wrap prose">
    <div class="legal-badge">Current Policy &bull; Last Updated: October 2026</div>

    <details class="legal-nav-box" open>
      <summary>Table of Contents</summary>
      <ul>
        <li><a href="#introduction">1. Introduction &amp; Scope</a></li>
        <li><a href="#information-collected">2. Information We Collect</a></li>
        <li><a href="#processing-purposes">3. Purposes of Processing</a></li>
        <li><a href="#submissions-storage">4. Contact Inquiries &amp; Storage</a></li>
        <li><a href="#cookies-tracking">5. Cookies &amp; Tracking Tools</a></li>
        <li><a href="#service-providers">6. Third-Party Service Providers</a></li>
        <li><a href="#security-retention">7. Data Security &amp; Retention</a></li>
        <li><a href="#privacy-rights">8. Your Privacy Rights</a></li>
        <li><a href="#deletion-correction">9. Correction &amp; Deletion Requests</a></li>
        <li><a href="#international">10. International Visitors</a></li>
        <li><a href="#updates-contact">11. Updates &amp; Contact Information</a></li>
      </ul>
    </details>

    <h2 id="introduction">1. Introduction &amp; Scope</h2>
    <p>Primecore Info Systems Pvt. Ltd. (&ldquo;Primecore Info Systems,&rdquo; &ldquo;we,&rdquo; &ldquo;our,&rdquo; or &ldquo;us&rdquo;) provides IT consulting, cloud infrastructure, and managed technology services. This Privacy Policy outlines our transparent data practices concerning our public website (PrimeCoreInfo.com) and the inquiries submitted by business visitors.</p>
    <p>This policy applies specifically to personal data and technical details transmitted when visiting our website or reaching out through our contact forms. For dedicated data governance practices, please review our companion <a href="../data-protection/">Data Protection Statement</a>.</p>

    <h2 id="information-collected">2. Information We Collect Through the Website</h2>
    <p>We believe in data minimization. We only collect information that you knowingly provide or that is technically necessary to serve our web pages reliably:</p>
    <ul>
      <li><strong>Contact Form Inputs:</strong> When you submit a project inquiry or request consultation via our contact form, we collect your <em>Full Name</em>, <em>Work Email Address</em>, <em>Company / Organization Name</em> (optional), <em>Phone Number</em> (optional), <em>Service of Interest</em>, and your written <em>Message / Project Description</em>.</li>
      <li><strong>Direct Inquiries:</strong> If you contact us via direct email links, we collect your email address, subject line, and message body.</li>
      <li><strong>Technical Request Headers:</strong> Our web server automatically receives standard network transmission data, including your client IP address and user-agent string, strictly used for transient request handling and rate limiting to prevent automated spam and abuse.</li>
    </ul>

    <h2 id="processing-purposes">3. Purposes for Collecting and Processing Information</h2>
    <p>We process the information you submit strictly for legitimate business purposes:</p>
    <ul>
      <li>To review, evaluate, and respond to your direct service inquiries and technical requests.</li>
      <li>To scope enterprise IT, cloud transformation, and infrastructure engineering consultations.</li>
      <li>To protect the security and availability of our website by detecting spam submissions, brute-force attempts, and service abuse.</li>
      <li>To maintain legitimate business records of inbound communications.</li>
    </ul>
    <p><strong>We do not sell, rent, lease, or monetize your personal information</strong> to data brokers, advertising networks, or unrelated third parties.</p>

    <h2 id="submissions-storage">4. Contact-Form Submission, Storage, and Email Notifications</h2>
    <p>When you submit an inquiry through our website, the data undergoes the following workflow:</p>
    <ol>
      <li><strong>Anti-Abuse Verification:</strong> The submission passes an automated honeypot inspection, request-rate checks, and validation on our application server.</li>
      <li><strong>Database Record:</strong> The inquiry is stored in our internal application database (SQLite) containing the submitted fields and an automated submission timestamp.</li>
      <li><strong>Internal Notification Dispatch:</strong> The backend generates an automated administrative email notification dispatched via encrypted SMTP to our designated company inbox (<code>connect@primecoreinfo.com</code>) so our engineering and operations team can promptly reply.</li>
      <li><strong>Static Fallback:</strong> If our backend API is temporarily unreachable or operated in a static environment, the form offers a fallback mailto draft mechanism that enables you to send your inquiry directly via your local mail client.</li>
    </ol>

    <h2 id="cookies-tracking">5. Cookies, Browser Storage, and Third-Party Tracking</h2>
    <div class="legal-card">
      <h4>Current Tracking Status</h4>
      <p><strong>Meta Pixel, Meta Conversions API (CAPI), and third-party tracking scripts are NOT currently installed or active on this website.</strong> We do not track visitors across third-party websites or deploy behavioral advertising cookies.</p>
    </div>
    <p>Our website utilizes standard, privacy-friendly front-end architecture. We do not use third-party behavioral profiling cookies or persistent tracking cookies. The only client-side browser mechanisms utilized are standard ephemeral browser document properties and responsive media-query state evaluators required for site navigation and visual layout.</p>
    <p>If we integrate third-party analytics or business tools (such as Meta Business Tools or analytics platforms) in the future to evaluate marketing campaigns, we will update this policy accordingly and deploy appropriate user consent mechanisms prior to firing non-essential tracking technologies.</p>

    <h2 id="service-providers">6. Third-Party Service Providers and Disclosures</h2>
    <p>We do not share your inquiry details with external marketers. Information is disclosed only to trusted infrastructure providers that support our direct operations under strict confidentiality:</p>
    <ul>
      <li><strong>Hosting and Cloud Infrastructure:</strong> Web hosting and server infrastructure environments that power our site availability.</li>
      <li><strong>Email Delivery Infrastructure:</strong> Standard SMTP mail servers utilized solely to transmit notifications of your inquiry to our team.</li>
      <li><strong>Legal and Regulatory Compliance:</strong> We may disclose information if required to comply with a valid legal obligation, court order, or official governmental request.</li>
    </ul>

    <h2 id="security-retention">7. Data Security and Retention</h2>
    <p>We implement appropriate technical and administrative safeguards to protect submitted inquiry data against unauthorized access, loss, or disclosure. These measures include server-side input sanitization, rate-limiting spam mitigations, access-controlled server storage, and transport layer security (TLS) for network communications.</p>
    <p><strong>Retention Period:</strong> Inbound inquiries are retained only for as long as necessary to fulfill the operational business purpose—specifically, answering your inquiry, assessing project feasibility, and maintaining regular business correspondence records—or as required by applicable legal and accounting retention obligations.</p>

    <h2 id="privacy-rights">8. User Privacy Rights</h2>
    <p>Depending on your jurisdiction (such as the European Economic Area, the United Kingdom, or applicable US state laws), you may have the following statutory privacy rights regarding your personal information:</p>
    <ul>
      <li><strong>Right to Access / Know:</strong> The right to request confirmation of whether we hold personal information about you and receive a copy of that data.</li>
      <li><strong>Right to Rectification:</strong> The right to request correction of inaccurate, incomplete, or outdated personal information.</li>
      <li><strong>Right to Erasure / Deletion:</strong> The right to request the deletion of your personal contact records, subject to legitimate record-keeping requirements.</li>
      <li><strong>Right to Restriction or Objection:</strong> The right to object to or restrict processing of your data under specific conditions.</li>
      <li><strong>Non-Discrimination:</strong> We will never discriminate against you, alter service terms, or deny inquiries because you exercised your privacy rights.</li>
    </ul>

    <h2 id="deletion-correction">9. Data Deletion and Correction Request Procedures</h2>
    <p>Because our website provides public informational content without user account logins, requests for data inspection, correction, or deletion are processed directly by our team:</p>
    <div class="legal-card">
      <h4>How to Submit a Data Request</h4>
      <p>Send an email to: <a href="mailto:connect@primecoreinfo.com?subject=Privacy%20Data%20Request">connect@primecoreinfo.com</a></p>
      <p>Please include your full name, the email address used when submitting your website inquiry, and the specific action you are requesting (e.g., &ldquo;Delete my inquiry record&rdquo; or &ldquo;Update my contact phone number&rdquo;). We will verify your identity using the associated email address and respond within thirty (30) days without charging a fee.</p>
    </div>

    <h2 id="international">10. International Visitors &amp; Cross-Border Transfers</h2>
    <p>Primecore Info Systems operates globally. Information submitted through our website may be received and processed in the regions where our servers or administrative email systems operate. By submitting your inquiry, you acknowledge that your information will be processed in accordance with this Privacy Policy and applicable data protection legislation.</p>

    <h2 id="updates-contact">11. Policy Updates and Contact Information</h2>
    <p>We may update this Privacy Policy periodically to reflect enhancements in our digital infrastructure, legal requirements, or business operations. Any updates will be published on this page with an updated &ldquo;Last Updated&rdquo; date.</p>
    <p>For questions, feedback, or privacy concerns regarding this policy, please contact:</p>
    <div class="legal-card">
      <h4>Primecore Info Systems Pvt. Ltd.</h4>
      <p>Inquiry &amp; Privacy Contact: <a href="mailto:connect@primecoreinfo.com">connect@primecoreinfo.com</a></p>
      <p>Website: <a href="https://primecoreinfo.com" target="_blank" rel="noopener noreferrer">primecoreinfo.com</a></p>
    </div>
  </div>
</section>
'''

terms_body = '''
<section class="page-hero">
  <p class="kicker">Legal &amp; Usage</p>
  <h1>Terms of Service</h1>
  <p class="lede">Conditions governing the use of Primecore Info Systems' website and services.</p>
</section>

<section>
  <div class="wrap prose">
    <div class="legal-badge">Current Version &bull; Last Updated: October 2026</div>
    <details class="legal-nav-box" open>
      <summary>Table of Contents</summary>
      <ul>
        <li><a href="#introduction">1. Introduction</a></li>
        <li><a href="#use-of-site">2. Use of the Site</a></li>
        <li><a href="#intellectual-property">3. Intellectual Property</a></li>
        <li><a href="#disclaimer">4. Disclaimer &amp; Limitation of Liability</a></li>
        <li><a href="#governing-law">5. Governing Law</a></li>
        <li><a href="#contact-info">6. Contact Information</a></li>
      </ul>
    </details>

    <h2 id="introduction">1. Introduction</h2>
    <p>Welcome to the website of Primecore Info Systems Pvt. Ltd. (&ldquo;Primecore Info Systems,&rdquo; &ldquo;we,&rdquo; &ldquo;our,&rdquo; or &ldquo;us&rdquo;). By accessing or using our website at PrimeCoreInfo.com (the &ldquo;Site&rdquo;), you agree to be bound by these Terms of Service (&ldquo;Terms&rdquo;). If you do not agree with any part of these Terms, you should not use this Site.</p>
    <p>These Terms apply to all visitors, users, and others who access or use the Site. We may update these Terms from time to time. Continued use of the Site after changes constitutes acceptance of the revised Terms.</p>

    <h2 id="use-of-site">2. Use of the Site</h2>
    <p>You may use this Site for lawful purposes only. You agree not to:</p>
    <ul>
      <li>Use the Site in any way that violates applicable local, national, or international laws or regulations.</li>
      <li>Attempt to gain unauthorized access to any portion of the Site, its servers, or any systems connected to the Site.</li>
      <li>Use automated tools, bots, or scripts to scrape, collect, or extract data from the Site without our prior written consent.</li>
      <li>Transmit any material that is defamatory, obscene, fraudulent, or otherwise objectionable.</li>
      <li>Interfere with or disrupt the integrity or performance of the Site or its underlying infrastructure.</li>
    </ul>
    <p>We reserve the right to restrict or terminate access to the Site for any user who violates these Terms.</p>

    <h2 id="intellectual-property">3. Intellectual Property</h2>
    <p>All content on this Site&mdash;including but not limited to text, graphics, logos, images, icons, software, and the overall design and layout&mdash;is the property of Primecore Info Systems Pvt. Ltd. or its content suppliers and is protected by applicable intellectual property laws.</p>
    <p>You may not reproduce, distribute, modify, create derivative works of, publicly display, or otherwise use any content from this Site without our prior written permission, except for personal, non-commercial viewing purposes.</p>
    <p>The Primecore Info Systems name, logo, and all related names, logos, product and service names, designs, and slogans are trademarks of Primecore Info Systems Pvt. Ltd. You must not use such marks without our prior written permission.</p>

    <h2 id="disclaimer">4. Disclaimer &amp; Limitation of Liability</h2>
    <p>The information provided on this Site is for general informational purposes only. While we strive to keep the content accurate and up to date, we make no warranties or representations of any kind, express or implied, about the completeness, accuracy, reliability, suitability, or availability of the Site or the information, products, services, or related content contained on the Site.</p>
    <p>To the fullest extent permitted by applicable law:</p>
    <ul>
      <li>Primecore Info Systems shall not be liable for any indirect, incidental, special, consequential, or punitive damages arising out of or in connection with your use of this Site.</li>
      <li>Our total liability for any claims related to the Site shall not exceed the amount you paid to us (if any) for accessing the Site.</li>
      <li>We are not responsible for any loss or damage resulting from reliance on information published on this Site.</li>
    </ul>
    <p>This Site may contain links to external websites. We have no control over the content or availability of those sites and accept no responsibility for them.</p>

    <h2 id="governing-law">5. Governing Law</h2>
    <p>These Terms shall be governed by and construed in accordance with the laws of India. Any disputes arising under or in connection with these Terms shall be subject to the jurisdiction of the competent courts in India.</p>
    <p><em>Note: The specific court jurisdiction for dispute resolution will be updated once the registered office details are confirmed by the company.</em></p>

    <h2 id="contact-info">6. Contact Information</h2>
    <p>If you have any questions about these Terms, please contact us:</p>
    <div class="legal-card">
      <h4>Primecore Info Systems Pvt. Ltd.</h4>
      <p>Email: <a href="mailto:connect@primecoreinfo.com">connect@primecoreinfo.com</a></p>
      <p>Website: <a href="https://primecoreinfo.com" target="_blank" rel="noopener noreferrer">primecoreinfo.com</a></p>
    </div>
  </div>
</section>
'''

data_deletion_body = '''
<section class="page-hero">
  <p class="kicker">User Rights</p>
  <h1>Data Deletion Request</h1>
  <p class="lede">How to request removal of personal data from Primecore Info Systems' records.</p>
</section>

<section>
  <div class="wrap prose">
    <div class="legal-badge">Policy Effective: October 2026</div>
    <details class="legal-nav-box" open>
      <summary>Table of Contents</summary>
      <ul>
        <li><a href="#request-process">1. Request Process</a></li>
        <li><a href="#verification">2. Verification of Identity</a></li>
        <li><a href="#timeline">3. Timeline &amp; Confirmation</a></li>
        <li><a href="#scope">4. Scope of Deletion</a></li>
        <li><a href="#contact">5. Contact &amp; Support</a></li>
      </ul>
    </details>

    <h2 id="request-process">1. How to Request Data Deletion</h2>
    <p>If you have previously submitted personal information through our website&mdash;for example, via the contact form or a direct email inquiry&mdash;you may request that we delete that information from our records.</p>
    <p>To submit a data deletion request, send an email to:</p>
    <div class="legal-card">
      <h4>Data Deletion Request</h4>
      <p>Email: <a href="mailto:connect@primecoreinfo.com?subject=Data%20Deletion%20Request">connect@primecoreinfo.com</a></p>
      <p>Subject line: <strong>Data Deletion Request</strong></p>
    </div>
    <p>In your email, please include:</p>
    <ul>
      <li>Your <strong>full name</strong> as it was provided in your original inquiry.</li>
      <li>The <strong>email address</strong> used when contacting us or submitting the form.</li>
      <li>A brief description of the data you would like deleted (e.g., &ldquo;Delete my contact form submission from [approximate date]&rdquo;).</li>
    </ul>

    <h2 id="verification">2. Verification of Identity</h2>
    <p>To protect your privacy, we will verify your identity before processing any deletion request. Verification is performed by confirming that the deletion request originates from the same email address associated with the original submission.</p>
    <p>If the request is sent from a different email address, we may ask for additional information to confirm your identity before proceeding.</p>

    <h2 id="timeline">3. Timeline &amp; Confirmation</h2>
    <p>We aim to process all verified data deletion requests within <strong>30 days</strong> of receiving the request. Once your data has been deleted, we will send a confirmation email to the address from which the request was made.</p>
    <p>Please note:</p>
    <ul>
      <li>Deletion is permanent and cannot be reversed.</li>
      <li>If your data has already been deleted as part of our standard retention practices, we will inform you accordingly.</li>
      <li>We do not charge any fee for processing deletion requests.</li>
    </ul>

    <h2 id="scope">4. Scope of Deletion</h2>
    <p>Data deletion covers personal information stored in our internal systems as a result of your website inquiry, including:</p>
    <ul>
      <li>Contact form submission records (name, email, company, phone, message).</li>
      <li>Associated internal notification emails generated by the submission.</li>
    </ul>
    <p>Deletion does not affect:</p>
    <ul>
      <li>Publicly available information that was not submitted through our website.</li>
      <li>Anonymized or aggregated data that cannot be linked back to you.</li>
      <li>Data we are required to retain for legal or regulatory compliance.</li>
    </ul>

    <h2 id="contact">5. Contact &amp; Support</h2>
    <p>If you have questions about the deletion process, your privacy rights, or our data practices, please contact us:</p>
    <div class="legal-card">
      <h4>Primecore Info Systems Pvt. Ltd.</h4>
      <p>Email: <a href="mailto:connect@primecoreinfo.com">connect@primecoreinfo.com</a></p>
      <p>Website: <a href="https://primecoreinfo.com" target="_blank" rel="noopener noreferrer">primecoreinfo.com</a></p>
    </div>
    <p>For our complete data practices, please review our <a href="../privacy-policy/">Privacy Policy</a> and <a href="../data-protection/">Data Protection Statement</a>.</p>
  </div>
</section>
'''

data_protection_body = '''
<section class="page-hero">
  <p class="kicker">Security &amp; Governance</p>
  <h1>Data Protection Statement</h1>
  <p class="lede">Our operational principles for securing website information, safeguarding visitor data, and maintaining privacy integrity.</p>
</section>

<section>
  <div class="wrap prose">
    <div class="legal-badge">Governance Overview &bull; Active Practice</div>

    <div class="legal-card">
      <h4>Our Commitment</h4>
      <p>At Primecore Info Systems Pvt. Ltd., data protection and infrastructure resilience are foundational to our work as enterprise IT architects. This statement explains how we operationalize data security, respect visitor privacy, and manage technical controls across PrimeCoreInfo.com.</p>
      <p style="margin-top:10px">Looking for our complete legal disclosures? Read our full <a href="../privacy-policy/">Privacy Policy</a>.</p>
    </div>

    <h2>1. Data Governance Principles</h2>
    <p>Our handling of digital information is governed by four core tenets:</p>
    <ul>
      <li><strong>Data Minimization:</strong> We only collect data that is strictly necessary to conduct direct business correspondence and safeguard website availability.</li>
      <li><strong>Purpose Limitation:</strong> Information submitted for engineering inquiries is never repurposed for unsolicited commercial broadcasts, data reselling, or unauthorized tracking.</li>
      <li><strong>Confidentiality &amp; Access Control:</strong> Inbound communications are restricted exclusively to authorized team members who require access to evaluate technical projects.</li>
      <li><strong>Transparency:</strong> We provide clear, unambiguous documentation of our data flows, tracking status, and contact procedures.</li>
    </ul>

    <h2>2. Categories of Website Data Handled</h2>
    <table class="legal-table">
      <thead>
        <tr>
          <th>Category</th>
          <th>Specific Elements</th>
          <th>Storage Mechanism</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Inquiry Data</strong></td>
          <td>Name, work email, company name, phone, chosen service, and project message.</td>
          <td>Application database (SQLite) &amp; encrypted operational email notification.</td>
        </tr>
        <tr>
          <td><strong>Transient Network Logs</strong></td>
          <td>Client IP address, user-agent string, and request timestamps.</td>
          <td>Temporary memory-based rate limiting buffers for spam prevention.</td>
        </tr>
        <tr>
          <td><strong>Client UI Preferences</strong></td>
          <td>Responsive navigation state and motion reduction preferences.</td>
          <td>Local device CSS/browser execution; zero remote transmission.</td>
        </tr>
      </tbody>
    </table>

    <h2>3. Security Practices &amp; Safeguards</h2>
    <p>We deploy defense-in-depth measures designed to protect information submitted via our digital interfaces:</p>
    <ul>
      <li><strong>Transport Layer Security:</strong> All data in transit between your browser and our server is secured using modern TLS encryption protocols.</li>
      <li><strong>Server-Side Input Validation:</strong> All form inputs are validated and sanitized server-side to prevent cross-site scripting (XSS), SQL injection, and payload overflow attempts.</li>
      <li><strong>Anti-Abuse Protections:</strong> Our application server incorporates automated honeypot trap fields, burst rate-limiting per IP address, and duplicate submission suppressors to block malicious bots without collecting extraneous visitor identifiers.</li>
      <li><strong>Infrastructure Isolation:</strong> Databases storing inquiry submissions are isolated within the backend runtime environment without public internet exposure.</li>
    </ul>
    <p><em>Please note: While we implement industry-standard safeguards, no digital transmission or internet infrastructure is 100% impenetrable. We do not make unreasonable or absolute security guarantees.</em></p>

    <h2>4. Advertising Tracking &amp; Meta Business Tools Status</h2>
    <div class="legal-card">
      <h4>Tracking &amp; Third-Party Pixels</h4>
      <p><strong>Verified Status:</strong> Meta Pixel, Meta Conversions API (CAPI), and third-party advertising cookies are currently <strong>not implemented</strong> on PrimeCoreInfo.com.</p>
    </div>
    <p>We maintain an advertising-tracker-free website baseline. If Meta Business Tools, conversion tracking APIs, or advertising pixels are evaluated or integrated in the future for campaign measurement:</p>
    <ul>
      <li>Tracking scripts will not be loaded unconditionally where applicable law requires user consent.</li>
      <li>Clear opt-in / opt-out controls will be deployed prior to the transmission of client browser identifiers.</li>
      <li>Any server-side conversions API integration will enforce data hashing (SHA-256) of personal identifiers in accordance with technical privacy guidelines.</li>
    </ul>

    <h2>5. Third-Party Sharing Principles</h2>
    <p>Primecore Info Systems operates under a strict no-sale policy:</p>
    <ul>
      <li>We do not sell, license, or barter customer or visitor contact information.</li>
      <li>We do not share your project details with external advertising brokers or behavioral advertising exchanges.</li>
      <li>Data is only processed by essential operational service partners (such as SMTP mail gateways) acting under our direct instructions.</li>
    </ul>

    <h2>6. Data Retention &amp; Deletion Process</h2>
    <p>We retain submitted project inquiries for as long as needed to fulfill consultative discussions, maintain professional business history, and satisfy legitimate record-keeping standards.</p>
    <p>If you have previously submitted an inquiry through our website and wish to have your contact details purged from our records, you can submit a deletion request:</p>
    <ul>
      <li>Email your request to: <a href="mailto:connect@primecoreinfo.com?subject=Data%20Deletion%20Request">connect@primecoreinfo.com</a></li>
      <li>Specify the email address associated with your original submission.</li>
      <li>Our team will locate the record in our database and notify you once the record has been permanently removed.</li>
    </ul>

    <h2>7. Questions &amp; Data Protection Inquiries</h2>
    <p>For inquiries regarding our data handling practices or to discuss secure infrastructure integration with our engineering architects, contact our team directly:</p>
    <div class="legal-card">
      <h4>Contact Information</h4>
      <p><strong>Email:</strong> <a href="mailto:connect@primecoreinfo.com">connect@primecoreinfo.com</a></p>
      <p><strong>Company:</strong> Primecore Info Systems Pvt. Ltd.</p>
      <p><strong>Reference:</strong> <a href="../privacy-policy/">View Complete Privacy Policy &rarr;</a></p>
    </div>
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

project_cloud_migration_body = '''
<!-- 01 — HERO -->
<section class="hero project-hero">
  <div class="hero-copy">
    <p class="kicker reveal">Project Showcase / Cloud Solution</p>
    <h1 class="reveal">Enterprise Cloud<br><em class="accent">Migration Platform</em></h1>
    <p class="lede reveal" style="font-weight:600;color:var(--white);margin-bottom:12px">Automated Workload Discovery, Risk-Free Landing Zones &amp; Zero-Downtime Migration Orchestration</p>
    <p class="lede reveal">Accelerate your transition to AWS, Microsoft Azure, and hybrid cloud environments with automated dependency mapping, security guardrails, and real-time operational telemetry.</p>
    <div class="hero-actions reveal" style="margin-top:28px">
      <a class="btn" data-magnetic href="../../contact/?ref=demo">Book Free Demo</a>
      <a class="btn-ghost project-whatsapp-btn" href="https://wa.me/918208531278?text=Hello%20PrimeCoreInfo%20team,%20I%20am%20interested%20in%20the%20Enterprise%20Cloud%20Migration%20Platform" target="_blank" rel="noopener">Chat on WhatsApp</a>
    </div>
  </div>
  <div class="project-hero-visual reveal">
    <div class="project-visual-frame">
      <div class="pv-header">
        <span class="pv-dot red"></span>
        <span class="pv-dot yellow"></span>
        <span class="pv-dot green"></span>
        <span class="pv-title">cloud-migration-dashboard.v1.0</span>
      </div>
      <div class="pv-body">
        <div class="pv-metric-row">
          <div class="pv-stat">
            <span class="pv-label">Migration Status</span>
            <span class="pv-val highlight">Active Wave 03</span>
          </div>
          <div class="pv-stat">
            <span class="pv-label">Workloads Discovered</span>
            <span class="pv-val">142 / 142</span>
          </div>
          <div class="pv-stat">
            <span class="pv-label">Downtime Risk</span>
            <span class="pv-val mint">0% (Zero-Downtime)</span>
          </div>
        </div>
        <div class="pv-diagram">
          <div class="pv-node src">Legacy Datacenter</div>
          <div class="pv-flow"><span class="flow-line"></span><span class="flow-particle"></span></div>
          <div class="pv-node core">PrimeCore Engine</div>
          <div class="pv-flow"><span class="flow-line"></span><span class="flow-particle"></span></div>
          <div class="pv-node dest">AWS / Azure Cloud</div>
        </div>
        <div class="pv-footer-note">
          <span class="pv-badge">Live System Architecture</span>
          <small class="pv-config-text">[ Project Visual Container ]</small>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- 02 — PROBLEM -->
<section class="project-problem">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">02 — The Problem</p>
      <h2>Enterprise Cloud Migration Risk &amp; Complexity</h2>
      <p>Legacy systems often delay digital transformation due to unmapped dependencies, fear of downtime, and operational uncertainty.</p>
    </div>
    <div class="why-grid stagger">
      <article class="why-item reveal">
        <h3>Hidden System Dependencies</h3>
        <p>Complex enterprise applications often rely on undocumented database linkages, legacy APIs, and hardcoded IPs that risk broken workflows during migration.</p>
      </article>
      <article class="why-item reveal">
        <h3>Fear of Unplanned Downtime</h3>
        <p>Mission-critical applications cannot afford operational cutover outages. Traditional lift-and-shift methods risk hours of revenue-impacting downtime.</p>
      </article>
      <article class="why-item reveal">
        <h3>Uncontrolled Cloud Spend</h3>
        <p>Without upfront workload rightsizing and FinOps governance, cloud environments frequently over-provision resources, resulting in unexpected budget overruns.</p>
      </article>
      <article class="why-item reveal">
        <h3>Security &amp; Compliance Gaps</h3>
        <p>Migrating sensitive workloads requires strict adherence to regulatory standards (CIS, HIPAA, ISO). Missing guardrails during cutover exposes critical vulnerabilities.</p>
      </article>
    </div>
  </div>
</section>

<!-- 03 — FEATURES -->
<section class="project-features">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">03 — Core Features</p>
      <h2>Built for Seamless Transformation</h2>
      <p>A comprehensive platform engineered to automate, secure, and streamline every stage of your cloud journey.</p>
    </div>
    <div class="solutions-grid">
      <article class="solution-card reveal">
        <div class="project-feat-icon">
          <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <rect x="2" y="3" width="20" height="5" rx="2"></rect>
            <rect x="2" y="16" width="9" height="5" rx="2"></rect>
            <rect x="13" y="16" width="9" height="5" rx="2"></rect>
            <path d="M12 8v4"></path>
            <path d="M6.5 12h11"></path>
            <path d="M6.5 12v4"></path>
            <path d="M17.5 12v4"></path>
          </svg>
        </div>
        <h3>Automated Dependency Discovery</h3>
        <p>Agentless scanning automatically maps all server, database, and API interconnectivity to eliminate migration blind spots.</p>
      </article>
      <article class="solution-card reveal">
        <div class="project-feat-icon">
          <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <path d="M18 10a4 4 0 0 0-7.75-1.2A3.5 3.5 0 0 0 4 12a3.5 3.5 0 0 0 3.5 3.5h2"></path>
            <path d="M12 13.5v7.5s4.5-1.5 4.5-4.5v-3z"></path>
          </svg>
        </div>
        <h3>IaC Landing Zone Generator</h3>
        <p>Deploys pre-configured, security-hardened AWS and Azure landing zones using Terraform and CloudFormation templates.</p>
      </article>
      <article class="solution-card reveal">
        <div class="project-feat-icon">
          <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <ellipse cx="12" cy="6" rx="8" ry="3"></ellipse>
            <path d="M4 6v6c0 1.66 3.58 3 8 3 1.1 0 2.15-.08 3.12-.24"></path>
            <path d="M4 12v6c0 1.66 3.58 3 8 3 1.5 0 2.92-.15 4.18-.43"></path>
            <path d="M20 6v5"></path>
            <path d="M16 16.5a4 4 0 0 1 3.5-3.5M19.5 13l2 2m-2-2l-2 2"></path>
            <path d="M22 19.5a4 4 0 0 1-3.5 3.5M18.5 23l-2-2m2 2l2-2"></path>
          </svg>
        </div>
        <h3>Zero-Downtime Data Sync</h3>
        <p>Continuous block-level and database replication allows live validation before switching traffic over seamlessly.</p>
      </article>
      <article class="solution-card reveal">
        <div class="project-feat-icon">
          <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <line x1="18" y1="20" x2="18" y2="10"></line>
            <line x1="12" y1="20" x2="12" y2="4"></line>
            <line x1="6" y1="20" x2="6" y2="14"></line>
            <path d="M3 20h18"></path>
            <path d="M4 11l4-4 4 2 7-7"></path>
            <polyline points="15 2 19 2 19 6"></polyline>
          </svg>
        </div>
        <h3>Real-Time FinOps Modeling</h3>
        <p>Simulate target cloud costs prior to cutover and optimize resource instances for maximum cost efficiency.</p>
      </article>
      <article class="solution-card reveal">
        <div class="project-feat-icon">
          <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
            <rect x="9" y="11" width="6" height="5" rx="1"></rect>
            <path d="M10 11V9a2 2 0 0 1 4 0v2"></path>
          </svg>
        </div>
        <h3>Automated Governance &amp; IAM</h3>
        <p>Enforces zero-trust access, encrypted transport, and compliance logging automatically across target cloud environments.</p>
      </article>
      <article class="solution-card reveal">
        <div class="project-feat-icon">
          <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
            <line x1="8" y1="21" x2="16" y2="21"></line>
            <line x1="12" y1="17" x2="12" y2="21"></line>
            <path d="M6 10h2l2-3 3 6 2-3h3"></path>
          </svg>
        </div>
        <h3>Post-Cutover Telemetry</h3>
        <p>Unified performance dashboard monitors latency, uptime, and system health in real-time post-migration.</p>
      </article>
    </div>
  </div>
</section>

<!-- 04 — SCREENSHOTS -->
<section class="project-screenshots">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">04 — System Screenshots</p>
      <h2>Platform Interface Showcase</h2>
      <p>Explore the intuitive interface, real-time migration dashboards, and orchestration tools.</p>
    </div>

    <div class="project-screenshot-grid stagger">
      <!-- Card 01 — Migration Control Center Dashboard -->
      <div class="project-ss-card reveal">
        <div class="project-ss-frame">
          <div class="ss-frame-header">
            <div class="ss-frame-dots"><span></span><span></span><span></span></div>
            <span class="ss-frame-title">control-center // wave-03</span>
            <span class="ss-ph-badge">INTERFACE PREVIEW</span>
          </div>
          <div class="ss-frame-canvas">
            <div class="dash-preview-grid">
              <div class="dash-mini-card">
                <span class="dash-mini-label">Migration Wave 03</span>
                <span class="dash-mini-val mint">78% Complete</span>
                <div class="dash-progress-bar"><div class="dash-progress-fill" style="width: 78%"></div></div>
              </div>
              <div class="dash-mini-card">
                <span class="dash-mini-label">Discovered Workloads</span>
                <span class="dash-mini-val cyan">142 / 142 Active</span>
                <div class="dash-status-dots">
                  <span class="dot-active"></span><span class="dot-active"></span><span class="dot-active"></span><span class="dot-active"></span><span class="dot-syncing"></span>
                </div>
              </div>
            </div>
            <div class="dash-preview-chart">
              <svg viewBox="0 0 320 80" width="100%" height="80" fill="none" aria-hidden="true">
                <defs>
                  <linearGradient id="chartGrad1" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="0%" stop-color="#35d6e8" stop-opacity="0.35"/>
                    <stop offset="100%" stop-color="#35d6e8" stop-opacity="0.0"/>
                  </linearGradient>
                </defs>
                <path d="M0,60 Q40,40 80,50 T160,25 T240,35 T320,15 L320,80 L0,80 Z" fill="url(#chartGrad1)"/>
                <path d="M0,60 Q40,40 80,50 T160,25 T240,35 T320,15" stroke="#35d6e8" stroke-width="2"/>
                <circle cx="160" cy="25" r="4" fill="#62e6d1" stroke="#061525" stroke-width="2"/>
                <circle cx="320" cy="15" r="4" fill="#35d6e8" stroke="#061525" stroke-width="2"/>
              </svg>
            </div>
          </div>
        </div>
        <div class="project-ss-info">
          <h4>Migration Control Center Dashboard</h4>
          <p>Real-time orchestration interface for monitoring active migration waves, server status, and cutover throughput.</p>
        </div>
        <div class="project-ss-caption">
          <strong>Interface Preview</strong> — Live tracking of workload wave execution and automated risk telemetry.
        </div>
      </div>

      <!-- Card 02 — Application Dependency Topology Graph -->
      <div class="project-ss-card reveal">
        <div class="project-ss-frame">
          <div class="ss-frame-header">
            <div class="ss-frame-dots"><span></span><span></span><span></span></div>
            <span class="ss-frame-title">topology // app-mesh</span>
            <span class="ss-ph-badge">INTERFACE PREVIEW</span>
          </div>
          <div class="ss-frame-canvas canvas-topology">
            <svg viewBox="0 0 320 150" width="100%" height="150" fill="none" aria-hidden="true">
              <path d="M50,75 L130,35" stroke="rgba(53, 214, 232, 0.4)" stroke-width="1.5" stroke-dasharray="4,3"/>
              <path d="M50,75 L130,115" stroke="rgba(53, 214, 232, 0.4)" stroke-width="1.5" stroke-dasharray="4,3"/>
              <path d="M130,35 L230,45" stroke="#35d6e8" stroke-width="1.5"/>
              <path d="M130,35 L230,105" stroke="rgba(98, 230, 209, 0.5)" stroke-width="1.5"/>
              <path d="M130,115 L230,105" stroke="#62e6d1" stroke-width="1.5"/>

              <g transform="translate(50,75)">
                <circle r="17" fill="rgba(10,32,53,0.95)" stroke="#35d6e8" stroke-width="2"/>
                <text y="3.5" text-anchor="middle" fill="#f7fafc" font-size="8.5" font-weight="700" font-family="sans-serif">GATEWAY</text>
              </g>

              <g transform="translate(130,35)">
                <circle r="15" fill="rgba(10,32,53,0.95)" stroke="#62e6d1" stroke-width="2"/>
                <text y="3.5" text-anchor="middle" fill="#f7fafc" font-size="8.5" font-weight="700" font-family="sans-serif">APP-API</text>
              </g>

              <g transform="translate(130,115)">
                <circle r="15" fill="rgba(10,32,53,0.95)" stroke="#159fe8" stroke-width="2"/>
                <text y="3.5" text-anchor="middle" fill="#f7fafc" font-size="8.5" font-weight="700" font-family="sans-serif">AUTH-SVC</text>
              </g>

              <g transform="translate(230,45)">
                <rect x="-22" y="-11" width="44" height="22" rx="5" fill="rgba(10,32,53,0.95)" stroke="#35d6e8" stroke-width="2"/>
                <text y="3" text-anchor="middle" fill="#9BEFE5" font-size="8" font-weight="700" font-family="sans-serif">POSTGRES</text>
              </g>

              <g transform="translate(230,105)">
                <rect x="-22" y="-11" width="44" height="22" rx="5" fill="rgba(10,32,53,0.95)" stroke="#62e6d1" stroke-width="2"/>
                <text y="3" text-anchor="middle" fill="#9BEFE5" font-size="8" font-weight="700" font-family="sans-serif">REDIS</text>
              </g>
            </svg>
          </div>
        </div>
        <div class="project-ss-info">
          <h4>Application Dependency Topology Graph</h4>
          <p>Interactive discovery map displaying interconnected microservices, legacy database links, and API routes.</p>
        </div>
        <div class="project-ss-caption">
          <strong>Interface Preview</strong> — Auto-generated network graph mapping system dependencies prior to cutover.
        </div>
      </div>

      <!-- Card 03 — FinOps Cloud Cost Optimization Portal -->
      <div class="project-ss-card reveal">
        <div class="project-ss-frame">
          <div class="ss-frame-header">
            <div class="ss-frame-dots"><span></span><span></span><span></span></div>
            <span class="ss-frame-title">finops // cost-optimizer</span>
            <span class="ss-ph-badge">INTERFACE PREVIEW</span>
          </div>
          <div class="ss-frame-canvas">
            <div class="dash-preview-grid">
              <div class="dash-mini-card">
                <span class="dash-mini-label">Monthly Cloud Spend</span>
                <span class="dash-mini-val mint">-32% Optimized</span>
                <span class="dash-mini-sub">Target spend model</span>
              </div>
              <div class="dash-mini-card">
                <span class="dash-mini-label">Instance Efficiency</span>
                <span class="dash-mini-val cyan">94% Rightsized</span>
                <div class="dash-progress-bar"><div class="dash-progress-fill mint-bg" style="width: 94%"></div></div>
              </div>
            </div>
            <div class="finops-bars-preview">
              <div class="finops-bar-item"><span class="bar-tag">AWS Compute</span><div class="bar-track"><div class="bar-fill cyan-bg" style="width: 75%"></div></div></div>
              <div class="finops-bar-item"><span class="bar-tag">Azure DB</span><div class="bar-track"><div class="bar-fill mint-bg" style="width: 55%"></div></div></div>
              <div class="finops-bar-item"><span class="bar-tag">Storage S3</span><div class="bar-track"><div class="bar-fill blue-bg" style="width: 40%"></div></div></div>
            </div>
          </div>
        </div>
        <div class="project-ss-info">
          <h4>FinOps Cloud Cost Optimization Portal</h4>
          <p>Pre-migration cost simulation dashboard analyzing target cloud expenditure and instance rightsizing.</p>
        </div>
        <div class="project-ss-caption">
          <strong>Interface Preview</strong> — Resource utilization modeling and projected cloud cost management.
        </div>
      </div>
    </div>
  </div>
</section>

<!-- 05 — BENEFITS -->
<section class="project-benefits">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">05 — Business Benefits</p>
      <h2>Quantifiable Business Value</h2>
      <p>Engineered to deliver tangible operational efficiency, cost reduction, and security assurance.</p>
    </div>
    <div class="outcomes">
      <div class="outcome reveal">
        <h3>Operational Challenges Avoided</h3>
        <ul>
          <li>Manual inventory tracking and lost dependency records</li>
          <li>High-risk cutovers with extended maintenance windows</li>
          <li>Unanticipated cloud billing spikes post-migration</li>
          <li>Inconsistent security policy enforcement across cloud regions</li>
        </ul>
      </div>
      <div class="outcome-mid reveal">VS</div>
      <div class="outcome after reveal">
        <h3>Platform Business Outcomes</h3>
        <ul>
          <li>Automated 100% dependency visibility prior to migration</li>
          <li>Predictable, zero-downtime cutover execution</li>
          <li>Optimized cloud resource allocation for maximum cost savings</li>
          <li>Continuous compliance and automated zero-trust security</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- 06 — PRICING -->
<section class="project-pricing">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">06 — Pricing &amp; Packages</p>
      <h2>Flexible Enterprise Investment Plans</h2>
      <p>Transparent pricing tiers tailored to your organization's workload volume and infrastructure requirements.</p>
    </div>
    <div class="project-pricing-grid stagger">
      <div class="project-price-card reveal">
        <div class="price-header">
          <h3>Assessment &amp; Discovery</h3>
          <p class="price-desc">Ideal for initial cloud readiness audit &amp; workload mapping.</p>
        </div>
        <div class="price-amount">
          <span class="price-num">Contact us for pricing</span>
          <span class="price-period">Per Environment Audit</span>
          <p class="price-desc">Need help choosing the right plan? Connect with our team at <a href="mailto:connect@primecoreinfo.com">connect@primecoreinfo.com</a>.</p>
        </div>
        <ul class="price-features">
          <li>Automated dependency mapping</li>
          <li>Cloud readiness risk report</li>
          <li>FinOps target cost estimation</li>
          <li>Migration wave roadmap design</li>
        </ul>
        <a class="btn-ghost" href="../../contact/?plan=assessment">Request Assessment</a>
      </div>

      <div class="project-price-card featured reveal">
        <div class="price-badge">Recommended</div>
        <div class="price-header">
          <h3>Full Migration Orchestration</h3>
          <p class="price-desc">Complete end-to-end migration execution with zero-downtime SLA.</p>
        </div>
        <div class="price-amount">
          <span class="price-num">[ Custom Pricing Placeholder ]</span>
          <span class="price-period">Based on Workload Volume</span>
        </div>
        <ul class="price-features">
          <li>Everything in Assessment tier</li>
          <li>IaC Landing zone deployment</li>
          <li>Zero-downtime data replication</li>
          <li>24/7 Cutover support &amp; rollback protection</li>
          <li>Post-cutover performance tuning</li>
        </ul>
        <a class="btn" href="../../contact/?plan=enterprise">Schedule Consultation</a>
      </div>

      <div class="project-price-card reveal">
        <div class="price-header">
          <h3>Continuous Managed Cloud</h3>
          <p class="price-desc">Post-migration 24/7 monitoring, FinOps &amp; governance.</p>
        </div>
        <div class="price-amount">
          <span class="price-num">[ Retainer Placeholder ]</span>
          <span class="price-period">Monthly Managed Service</span>
        </div>
        <ul class="price-features">
          <li>Continuous monitoring &amp; incident response</li>
          <li>Ongoing cloud cost optimization</li>
          <li>Automated compliance audits</li>
          <li>Dedicated cloud architect support</li>
        </ul>
        <a class="btn-ghost" href="../../contact/?plan=managed">Discuss Managed Services</a>
      </div>
    </div>
    <p class="pricing-note reveal" style="text-align:center;margin-top:24px;font-size:0.88rem;color:var(--text-3)">
      <em>[ Pricing Configuration Placeholder — Final pricing models and figures are customized based on verified project scope ]</em>
    </p>
  </div>
</section>

<!-- 07 — DEMO VIDEO -->
<section class="demo-slideshow-section" id="demo">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">See Our Solutions in Action</p>
      <h2>Explore our software solutions through quick product demonstrations.</h2>
    </div>
    <div class="demo-showcase-container">
      <!-- Tab Nav -->
      <div class="demo-tab-nav" role="tablist" aria-label="Demo videos">
        <button class="demo-tab is-active" type="button" role="tab" aria-selected="true" aria-controls="demo-slide-0" data-demo="0">
          <span class="demo-tab-num">01</span> Kitchen Order System
        </button>
        <button class="demo-tab" type="button" role="tab" aria-selected="false" aria-controls="demo-slide-1" data-demo="1">
          <span class="demo-tab-num">02</span> Restaurant OS
        </button>
        <button class="demo-tab" type="button" role="tab" aria-selected="false" aria-controls="demo-slide-2" data-demo="2">
          <span class="demo-tab-num">03</span> Clinic OS
        </button>
      </div>
      <!-- Viewport -->
      <div class="demo-viewport">
        <!-- Slide 0 -->
        <div class="demo-slide" id="demo-slide-0" role="tabpanel">
          <div class="demo-frame">
            <div class="demo-frame-header">
              <div class="demo-frame-dots">
                <span class="demo-dot red"></span>
                <span class="demo-dot yellow"></span>
                <span class="demo-dot green"></span>
              </div>
              <span class="demo-badge">LIVE DEMO</span>
            </div>
            <div class="demo-video-wrapper">
              <video class="demo-player" id="demo-video-0" poster="../../assets/videos/poster-01.jpg" controls preload="none">
                <source src="../../assets/videos/01.mp4" type="video/mp4"/>
              </video>
            </div>
          </div>
          <div class="demo-details">
            <div class="demo-meta">
              <span class="demo-pill">Product Demo</span>
              <span class="demo-domain">Restaurant Tech</span>
            </div>
            <h3 class="demo-title">Kitchen Order System</h3>
            <p class="demo-desc">Explore kitchen order management and ticket tracking.</p>
          </div>
        </div>
        <!-- Slide 1 -->
        <div class="demo-slide" id="demo-slide-1" role="tabpanel" hidden>
          <div class="demo-frame">
            <div class="demo-frame-header">
              <div class="demo-frame-dots">
                <span class="demo-dot red"></span>
                <span class="demo-dot yellow"></span>
                <span class="demo-dot green"></span>
              </div>
              <span class="demo-badge">LIVE DEMO</span>
            </div>
            <div class="demo-video-wrapper">
              <video class="demo-player" id="demo-video-1" poster="../../assets/videos/poster-02.jpg" controls preload="none">
                <source src="../../assets/videos/02.mp4" type="video/mp4"/>
              </video>
            </div>
          </div>
          <div class="demo-details">
            <div class="demo-meta">
              <span class="demo-pill">Product Demo</span>
              <span class="demo-domain">Restaurant Tech</span>
            </div>
            <h3 class="demo-title">Restaurant OS</h3>
            <p class="demo-desc">End-to-end restaurant operations and management platform.</p>
          </div>
        </div>
        <!-- Slide 2 -->
        <div class="demo-slide" id="demo-slide-2" role="tabpanel" hidden>
          <div class="demo-frame">
            <div class="demo-frame-header">
              <div class="demo-frame-dots">
                <span class="demo-dot red"></span>
                <span class="demo-dot yellow"></span>
                <span class="demo-dot green"></span>
              </div>
              <span class="demo-badge">LIVE DEMO</span>
            </div>
            <div class="demo-video-wrapper">
              <video class="demo-player" id="demo-video-2" poster="../../assets/videos/poster-03.jpg" controls preload="none">
                <source src="../../assets/videos/03.mp4" type="video/mp4"/>
              </video>
            </div>
          </div>
          <div class="demo-details">
            <div class="demo-meta">
              <span class="demo-pill">Product Demo</span>
              <span class="demo-domain">Healthcare Tech</span>
            </div>
            <h3 class="demo-title">Clinic OS</h3>
            <p class="demo-desc">Clinic management and patient operations platform.</p>
          </div>
        </div>
      </div>
      <!-- Controls -->
      <div class="demo-controls-bar">
        <button class="demo-nav-btn" id="demo-prev" aria-label="Previous demo" type="button">&#8592;</button>
        <div class="demo-indicators" role="group" aria-label="Demo slide indicators">
          <button class="demo-dot-btn is-active" type="button" aria-label="Demo 1" data-demo="0"></button>
          <button class="demo-dot-btn" type="button" aria-label="Demo 2" data-demo="1"></button>
          <button class="demo-dot-btn" type="button" aria-label="Demo 3" data-demo="2"></button>
        </div>
        <button class="demo-nav-btn" id="demo-next" aria-label="Next demo" type="button">&#8594;</button>
      </div>
    </div>
  </div>
</section>
<script>
  (function() {
    const tabs = document.querySelectorAll('.demo-tab');
    const slides = document.querySelectorAll('.demo-slide');
    const dots = document.querySelectorAll('.demo-dot-btn');
    const videos = document.querySelectorAll('.demo-player');
    let current = 0;
    function switchTo(n) {
      videos[current].pause();
      slides[current].hidden = true;
      tabs[current].classList.remove('is-active');
      tabs[current].setAttribute('aria-selected', 'false');
      dots[current].classList.remove('is-active');
      current = (n + slides.length) % slides.length;
      slides[current].hidden = false;
      tabs[current].classList.add('is-active');
      tabs[current].setAttribute('aria-selected', 'true');
      dots[current].classList.add('is-active');
    }
    tabs.forEach((tab, i) => tab.addEventListener('click', () => switchTo(i)));
    dots.forEach((dot, i) => dot.addEventListener('click', () => switchTo(i)));
    document.getElementById('demo-prev').addEventListener('click', () => switchTo(current - 1));
    document.getElementById('demo-next').addEventListener('click', () => switchTo(current + 1));
  })();
</script>

<!-- 08 — CUSTOMER STORY -->
<section class="project-story">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">08 — Customer Story</p>
      <h2>Real-World Implementation Journey</h2>
      <p>A structured look at how complex workload challenges are transformed into operational success.</p>
    </div>
    <div class="project-story-flow stagger">
      <div class="story-step reveal">
        <div class="story-dot">1</div>
        <div class="story-content">
          <span class="cat">Customer Profile</span>
          <h3>[ Customer Profile Placeholder ]</h3>
          <p>Enterprise Healthcare / Financial Services Organization with multi-region hybrid datacenters.</p>
        </div>
      </div>

      <div class="story-step reveal">
        <div class="story-dot">2</div>
        <div class="story-content">
          <span class="cat">The Challenge</span>
          <h3>[ Migration Challenge Placeholder ]</h3>
          <p>150+ legacy VMs with inter-dependent SQL databases requiring zero downtime cutover under strict HIPAA compliance rules.</p>
        </div>
      </div>

      <div class="story-step reveal">
        <div class="story-dot">3</div>
        <div class="story-content">
          <span class="cat">The Implementation</span>
          <h3>[ Implementation Solution Placeholder ]</h3>
          <p>Deployed automated discovery agents, built automated IaC landing zones in AWS, and executed continuous data replication over 4 wave stages.</p>
        </div>
      </div>

      <div class="story-step reveal">
        <div class="story-dot">4</div>
        <div class="story-content">
          <span class="cat">The Business Outcome</span>
          <h3>[ Business Outcome Placeholder ]</h3>
          <p>100% of workloads migrated on schedule with zero customer-facing downtime and complete compliance verification.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- OUR CLIENTS -->
<section class="project-clients">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">Our Clients</p>
      <h2>Ongoing Client Engagements</h2>
      <p>Primecore Info Systems partners with forward-looking technology enterprises across cloud infrastructure, FinOps, and continuous operations.</p>
    </div>
    <div class="clients-grid stagger">
      <div class="client-card reveal">
        <div class="client-card-header">
          <span class="client-badge-pill">Enterprise Client</span>
          <span class="client-domain-tag">AWS Cloud Infrastructure</span>
        </div>
        <div class="client-brand-display">
          <h3 class="client-name-title">StarNext Innovations Pvt. Ltd.</h3>
          <p class="client-scope-subtitle">AWS Infrastructure, FinOps, Disaster Recovery &amp; Monitoring</p>
        </div>
        <p class="client-description">StarNext Innovations Pvt. Ltd. is an enterprise technology client leveraging AWS cloud infrastructure to support business-critical applications, reliable operations, and scalable IT services.</p>
        <div class="client-card-footer">
          <a class="client-case-link" href="../../projects/starnext-innovations-aws-infrastructure/">Read Case Study <span aria-hidden="true">&rarr;</span></a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- 09 — FAQ -->
<section class="project-faq">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">09 — Frequently Asked Questions</p>
      <h2>Project Details &amp; Technical FAQs</h2>
      <p>Clear answers to common questions about deployment, integration, and security.</p>
    </div>
    <div class="faq">
      <details>
        <summary>What cloud platforms are supported by this migration platform?</summary>
        <p>The platform natively supports migration to AWS (Amazon Web Services), Microsoft Azure, Google Cloud Platform (GCP), and hybrid VMware/on-premises landing zones.</p>
      </details>
      <details>
        <summary>How does the platform ensure zero-downtime cutover?</summary>
        <p>It utilizes continuous, block-level and database sync engines that keep target cloud instances completely up-to-date while legacy systems remain live until final DNS cutover.</p>
      </details>
      <details>
        <summary>Are application discovery agents required on every server?</summary>
        <p>Both agentless (via hypervisor / API credentials) and lightweight agent-based discovery options are available to fit your security and network architecture requirements.</p>
      </details>
      <details>
        <summary>Can pricing be customized for smaller or larger workloads?</summary>
        <p>Yes. Pricing is flexible and scalable based on the number of workloads, databases, and continuous management requirements.</p>
      </details>
      <details>
        <summary>How do I book a live demonstration or consultation?</summary>
        <p>You can click the "Book Free Demo" button on this page or reach out directly via our contact form or WhatsApp connection.</p>
      </details>
    </div>
  </div>
</section>

<!-- 10 & 11 — BOOK FREE DEMO & WHATSAPP US -->
<section class="project-cta-section wrap" style="padding-bottom:96px">
  <div class="cta-band reveal">
    <p class="kicker">10 &amp; 11 — Get Started &amp; Direct Contact</p>
    <h2>Ready to Accelerate Your Cloud Migration?</h2>
    <p>Book a personalized demonstration with our cloud infrastructure team or connect with us directly via WhatsApp to discuss your project requirements.</p>
    <div style="display:flex;gap:16px;flex-wrap:wrap;align-items:center;position:relative;z-index:1">
      <a class="btn" data-magnetic href="../../contact/?ref=project-cta">Book Free Demo <span aria-hidden="true">→</span></a>
      <a class="btn-ghost project-whatsapp-btn" href="https://wa.me/918208531278?text=Hello%20PrimeCoreInfo%20team,%20I%20would%20like%20to%20book%20a%20demo%20for%20the%20Cloud%20Migration%20Platform" target="_blank" rel="noopener">Chat on WhatsApp</a>
    </div>
  </div>
</section>
'''

# Projects & Case Studies Listing Page
projects_listing_body = '''
<section class="page-hero">
  <p class="kicker reveal">Projects &amp; Case Studies</p>
  <h1 class="reveal">Enterprise Engagements &amp; Solutions</h1>
  <p class="lede reveal" style="margin-top:14px">Real-world cloud infrastructure management, FinOps optimization, disaster recovery, and automated migration solutions delivered by Primecore Info Systems.</p>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">Case Studies</p>
      <h2>Featured Client Work &amp; Platforms</h2>
      <p>Explore how we help technology enterprises modernize, optimize, and operate dependable cloud platforms.</p>
    </div>

    <div class="projects-grid stagger">
      <!-- Card 01 — StarNext Innovations -->
      <article class="project-card reveal">
        <div class="client-card-header">
          <span class="client-badge-pill">Enterprise Client</span>
          <span class="client-domain-tag">AWS Cloud</span>
        </div>
        <div>
          <h2>StarNext Innovations Pvt. Ltd.</h2>
          <p class="client-scope-subtitle">AWS Infrastructure, FinOps, Disaster Recovery &amp; Monitoring</p>
        </div>
        <p>StarNext Innovations Pvt. Ltd. is an enterprise technology client leveraging AWS cloud infrastructure to support business-critical applications, reliable operations, and scalable IT services.</p>
        <div class="project-tags">
          <span class="project-tag">AWS Data Centre</span>
          <span class="project-tag">Cloud FinOps</span>
          <span class="project-tag">Disaster Recovery (DR)</span>
          <span class="project-tag">Monitoring &amp; Observability</span>
        </div>
        <div style="margin-top:auto;padding-top:12px">
          <a class="btn" href="starnext-innovations-aws-infrastructure/">Read Case Study <span aria-hidden="true">&rarr;</span></a>
        </div>
      </article>

      <!-- Card 02 — Cloud Migration Platform -->
      <article class="project-card reveal">
        <div class="client-card-header">
          <span class="client-badge-pill">Solution Showcase</span>
          <span class="client-domain-tag">AWS &amp; Azure</span>
        </div>
        <div>
          <h2>Enterprise Cloud Migration Platform</h2>
          <p class="client-scope-subtitle">Discovery, Landing Zones &amp; Zero-Downtime Migration</p>
        </div>
        <p>Automated workload discovery, risk-free landing zones, and zero-downtime cloud migration orchestration for mission-critical enterprise environments.</p>
        <div class="project-tags">
          <span class="project-tag">Workload Discovery</span>
          <span class="project-tag">IaC Landing Zones</span>
          <span class="project-tag">Zero-Downtime Replication</span>
          <span class="project-tag">FinOps Modeling</span>
        </div>
        <div style="margin-top:auto;padding-top:12px">
          <a class="btn-ghost" href="cloud-migration-platform/">Explore Platform <span aria-hidden="true">&rarr;</span></a>
        </div>
      </article>
    </div>
  </div>
</section>
'''

# StarNext Innovations Case Study Page
starnext_case_study_body = '''
<!-- 01 — HERO -->
<section class="hero project-hero">
  <div class="hero-copy">
    <div class="back-nav-bar reveal" style="margin-bottom:16px">
      <a class="client-case-link" href="../../projects/" style="font-size:0.88rem;letter-spacing:0.04em;text-transform:uppercase">&larr; Back to Projects &amp; Case Studies</a>
    </div>
    <p class="kicker reveal">Client Case Study / AWS Cloud Infrastructure</p>
    <h1 class="reveal">StarNext Innovations<br><em class="accent">Pvt. Ltd.</em></h1>
    <p class="lede reveal" style="font-weight:600;color:var(--white);margin-bottom:12px">AWS Infrastructure, FinOps, Disaster Recovery &amp; Monitoring</p>
    <p class="lede reveal">StarNext Innovations Pvt. Ltd. is an enterprise technology client leveraging AWS cloud infrastructure to support business-critical applications, reliable operations, and scalable IT services.</p>
    <div class="hero-actions reveal" style="margin-top:28px">
      <a class="btn" data-magnetic href="../../contact/?ref=starnext-case-study">Discuss Your Infrastructure</a>
      <a class="btn-ghost" href="../../projects/">Explore All Case Studies</a>
    </div>
  </div>
  <div class="project-hero-visual reveal">
    <div class="project-visual-frame">
      <div class="pv-header">
        <span class="pv-dot red"></span>
        <span class="pv-dot yellow"></span>
        <span class="pv-dot green"></span>
        <span class="pv-title">starnext.aws-infrastructure.telemetry</span>
      </div>
      <div class="pv-body">
        <div class="pv-metric-row">
          <div class="pv-stat">
            <span class="pv-label">Infrastructure Scope</span>
            <span class="pv-val highlight">AWS Cloud</span>
          </div>
          <div class="pv-stat">
            <span class="pv-label">FinOps &amp; DR</span>
            <span class="pv-val cyan">Active Governance</span>
          </div>
          <div class="pv-stat">
            <span class="pv-label">Observability</span>
            <span class="pv-val mint">Continuous Monitoring</span>
          </div>
        </div>
        <div class="pv-diagram">
          <div class="pv-node src">AWS Data Centre</div>
          <div class="pv-flow"><span class="flow-line"></span><span class="flow-particle"></span></div>
          <div class="pv-node core">FinOps &amp; DR</div>
          <div class="pv-flow"><span class="flow-line"></span><span class="flow-particle"></span></div>
          <div class="pv-node dest">Monitoring &amp; Obs</div>
        </div>
        <div class="pv-footer-note">
          <span class="pv-badge">Client Engagement</span>
          <small class="pv-config-text">StarNext Innovations Pvt. Ltd.</small>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- 02 — OVERVIEW -->
<section class="project-overview">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">01 — Client Overview</p>
      <h2>Enterprise Technology Client</h2>
      <p>StarNext Innovations Pvt. Ltd. is an enterprise technology client leveraging AWS cloud infrastructure to support business-critical applications, reliable operations, and scalable IT services.</p>
    </div>
    <div class="hero-highlights reveal" style="margin-top:28px">
      <div class="highlight-card">
        <h4>Enterprise Technology</h4>
        <p>Supporting business-critical applications with dependable, high-availability architecture.</p>
      </div>
      <div class="highlight-card">
        <h4>AWS Cloud Infrastructure</h4>
        <p>Scalable cloud environments tailored for operational reliability and performance.</p>
      </div>
      <div class="highlight-card">
        <h4>Scalable IT Services</h4>
        <p>Continuous operational support engineered for business agility and sustained resilience.</p>
      </div>
    </div>
  </div>
</section>

<!-- 03 — THE CHALLENGES -->
<section class="project-problem">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">02 — The Challenges</p>
      <h2>AWS Infrastructure Reliability, Cost Optimization &amp; Disaster Recovery</h2>
      <p>Managing AWS data centre infrastructure required continuous monitoring, cost optimization, effective disaster recovery planning, and improved operational visibility. The objective was to optimize cloud spending while maintaining infrastructure reliability, security, and business continuity.</p>
    </div>
    <div class="why-grid stagger">
      <article class="why-item reveal">
        <h3>Infrastructure Reliability</h3>
        <p>Managing AWS data centre infrastructure to maintain high system reliability, security, and consistent application delivery.</p>
      </article>
      <article class="why-item reveal">
        <h3>Cost Optimization</h3>
        <p>Analyzing and optimizing cloud resource utilization to curb unwarranted spend while preserving performance.</p>
      </article>
      <article class="why-item reveal">
        <h3>Disaster Recovery Planning</h3>
        <p>Establishing effective disaster recovery readiness, connectivity protocols, and recovery initiatives to safeguard business continuity.</p>
      </article>
      <article class="why-item reveal">
        <h3>Operational Visibility</h3>
        <p>Overcoming operational blind spots through continuous monitoring and real-time detection of infrastructure issues.</p>
      </article>
    </div>
  </div>
</section>

<!-- 04 — IMPLEMENTATION SOLUTION -->
<section class="project-story">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">03 — Implementation Solution</p>
      <h2>AWS Infrastructure Management &amp; Cloud Optimization</h2>
      <p>Primecore Infosystems supported StarNext Innovations through four key initiatives:</p>
    </div>
    <div class="project-story-flow stagger">
      <div class="story-step reveal">
        <div class="story-dot">1</div>
        <div class="story-content">
          <span class="cat">Key Initiative 01</span>
          <h3>AWS Data Centre Infrastructure</h3>
          <p>Infrastructure management, configuration, deployment, and operational support for AWS environments.</p>
        </div>
      </div>

      <div class="story-step reveal">
        <div class="story-dot">2</div>
        <div class="story-content">
          <span class="cat">Key Initiative 02</span>
          <h3>Cloud Cost Optimization</h3>
          <p>Analysis and optimization of cloud resource utilization to improve cost efficiency.</p>
        </div>
      </div>

      <div class="story-step reveal">
        <div class="story-dot">3</div>
        <div class="story-content">
          <span class="cat">Key Initiative 03</span>
          <h3>Disaster Recovery (DR)</h3>
          <p>DR planning, infrastructure readiness, connectivity, and recovery initiatives to strengthen business continuity.</p>
        </div>
      </div>

      <div class="story-step reveal">
        <div class="story-dot">4</div>
        <div class="story-content">
          <span class="cat">Key Initiative 04</span>
          <h3>Monitoring &amp; Observability</h3>
          <p>Infrastructure monitoring, performance visibility, and operational issue detection to support reliable services.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- 05 — BUSINESS OUTCOME -->
<section class="project-benefits">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="kicker">04 — Business Outcome</p>
      <h2>Improved Cloud Efficiency, Visibility &amp; Resilience</h2>
      <p>The engagement focused on improving AWS infrastructure reliability, optimizing cloud expenditure, strengthening disaster recovery preparedness, and enhancing monitoring capabilities.</p>
    </div>
    <div class="outcomes">
      <div class="outcome reveal">
        <h3>Engagement Initiatives</h3>
        <ul>
          <li>AWS Data Centre infrastructure management and deployment support</li>
          <li>Cloud resource utilization analysis and cost efficiency optimization</li>
          <li>Disaster recovery readiness, connectivity, and recovery planning</li>
          <li>Infrastructure monitoring and operational issue detection</li>
        </ul>
      </div>
      <div class="outcome-mid reveal">&rarr;</div>
      <div class="outcome after reveal">
        <h3>Delivered Outcomes</h3>
        <p style="margin-bottom:16px;color:var(--text-1)">Through these initiatives, Primecore Infosystems supports StarNext Innovations in building a more cost-efficient, observable, and resilient cloud infrastructure environment.</p>
        <ul>
          <li>Improved AWS infrastructure reliability and operational stability</li>
          <li>Optimized cloud expenditure and reduced resource waste</li>
          <li>Strengthened disaster recovery preparedness and continuity</li>
          <li>Enhanced visibility across operational services and performance</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- 06 — CTA BAND -->
<section class="wrap" style="padding-bottom:96px">
  <div class="cta-band reveal">
    <p class="kicker">Get Started</p>
    <h2>Build. Migrate. Automate. Optimize.</h2>
    <p>Primecore Info Systems helps businesses design, migrate, automate and optimize their IT infrastructure across AWS, Microsoft Azure and hybrid cloud environments.</p>
    <div style="display:flex;gap:16px;flex-wrap:wrap;align-items:center;position:relative;z-index:1;margin-top:20px">
      <a class="btn" data-magnetic href="../../contact/?ref=starnext-case-study">Get Started <span aria-hidden="true">&rarr;</span></a>
      <a class="btn-ghost" href="../../projects/">← View All Projects &amp; Case Studies</a>
    </div>
  </div>
</section>
'''

# Root Landing Page: Cloud Migration Platform with root relative paths ("./")
root_project_body = (
    project_cloud_migration_body
    .replace('href="../../contact/', 'href="contact/')
    .replace('href="../../projects/', 'href="projects/')
    .replace('href="../../home/', 'href="home/')
)

pages = [
    ("index.html", doc(
        "Enterprise Cloud Migration Platform | Primecore Info Systems",
        "Automated workload discovery, risk-free landing zones, and zero-downtime cloud migration orchestration.",
        "./", "projects", root_project_body, False)),
    ("home/index.html", doc(
        "Primecore Info Systems | Modern IT Infrastructure & Cloud Solutions",
        "Primecore Info Systems helps businesses design, migrate, automate and optimize their IT infrastructure across AWS, Microsoft Azure and hybrid cloud environments.",
        "../", "home", home_body, True)),
    ("about/index.html", doc("About Us | Primecore Info Systems", "Primecore Info Systems Pvt. Ltd. is an IT services and technology solutions company helping organizations modernize infrastructure and adopt cloud.", "../", "about", about_body)),
    ("services/index.html", doc("Services | Primecore Info Systems", "Cloud Infrastructure, DevOps & SRE, Cloud Migration, Managed Infrastructure, Security & Governance, FinOps, and Technology Services.", "../", "services", services_body)),
    ("contact/index.html", doc("Contact | Primecore Info Systems", "Get started with Primecore Info Systems for cloud, infrastructure, and DevOps solutions.", "../", "contact", contact_body, False)),
    ("insights/index.html", doc("Insights | Primecore Info Systems", "Practical perspectives for cloud, infrastructure, and operations decisions.", "../", "insights", insights_body)),
    ("privacy-policy/index.html", doc("Privacy Policy | Primecore Info Systems", "How Primecore Info Systems uses information shared through this website.", "../", "privacy", privacy_body)),
    ("data-protection/index.html", doc("Data Protection Statement | Primecore Info Systems", "Data governance, information security principles, and privacy protections at Primecore Info Systems.", "../", "home", data_protection_body)),
    ("terms-of-service/index.html", doc("Terms of Service | Primecore Info Systems", "Conditions governing use of the Primecore Info Systems website and services.", "../", "terms", terms_body)),
    ("data-deletion/index.html", doc("Data Deletion Request | Primecore Info Systems", "How users can request removal of their personal data.", "../", "deletion", data_deletion_body)),
    ("cloud-transformation/index.html", doc("Cloud Transformation | Primecore Info Systems", "Move to the cloud with a plan you can trust.", "../", "services", cloud_body)),
    ("infrastructure-modernization/index.html", doc("Infrastructure Modernization | Primecore Info Systems", "Modernize core infrastructure for performance, resilience, and cloud-first operations.", "../", "services", infra_body)),
    ("managed-it-services/index.html", doc("Managed IT Services | Primecore Info Systems", "Proactive monitoring, responsive support, and operational ownership.", "../", "services", managed_body)),
    ("projects/index.html", doc(
        "Projects & Case Studies | Primecore Info Systems",
        "Explore Primecore Info Systems enterprise client case studies and cloud solution platforms.",
        "../", "projects", projects_listing_body)),
    ("projects/cloud-migration-platform/index.html", doc(
        "Enterprise Cloud Migration Platform | Primecore Info Systems",
        "Automated workload discovery, risk-free landing zones, and zero-downtime cloud migration orchestration.",
        "../../", "projects", project_cloud_migration_body, False)),
    ("projects/starnext-innovations-aws-infrastructure/index.html", doc(
        "StarNext Innovations Pvt. Ltd. — AWS Infrastructure, FinOps, Disaster Recovery & Monitoring | Primecore Info Systems",
        "StarNext Innovations Pvt. Ltd. is an enterprise technology client leveraging AWS cloud infrastructure to support business-critical applications, reliable operations, and scalable IT services.",
        "../../", "projects", starnext_case_study_body, False)),
    ("insights/cloud-readiness/index.html", doc("Cloud readiness | Primecore Info Systems Insights", "What to clarify before the first migration wave.", "../../", "insights", article_cloud)),
    ("insights/modern-foundations/index.html", doc("Modern foundations | Primecore Info Systems Insights", "How to sequence infrastructure improvements around business risk.", "../../", "insights", article_found)),
    ("insights/operational-resilience/index.html", doc("Operational resilience | Primecore Info Systems Insights", "Why visibility and ownership matter as environments grow.", "../../", "insights", article_ops)),
    ("404.html", doc("Page Not Found | Primecore Info Systems", "The requested route does not exist.", "./", "home", notfound_body, False)),
]

if __name__ == "__main__":
    for rel, html in pages:
        write(rel, html)
    print("done")
