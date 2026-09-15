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
  <a class="brand" href="{href("")}" aria-label="Primecore Info Systems home"><img class="brand-mark-img" src="{href("assets/images/brand-logo.png")}" alt="Primecore Info Systems Logo"/><span>PRIMECORE INFO SYSTEMS</span></a>
  <nav class="nav" aria-label="Primary">
    <a class="{active("about").strip()}" href="{href("about/")}">About Us</a>
    <a class="{active("services").strip()}" href="{href("services/")}">Services</a>
    <a class="{active("solutions").strip()}" href="{href("#solutions")}">Solutions</a>
    <a class="{active("technologies").strip()}" href="{href("#technologies")}">Technologies</a>
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
      <a class="brand" href="{href("")}"><img class="brand-mark-img" src="{href("assets/images/brand-logo.png")}" alt="Primecore Info Systems Logo"/><span>PRIMECORE INFO SYSTEMS</span></a>
      <p>Primecore Info Systems Pvt. Ltd. is an IT services and technology solutions company helping organizations modernize their infrastructure, adopt cloud technologies and build reliable digital platforms.</p>
    </div>
    <div>
      <h4>Navigation</h4>
      <a href="{href("about/")}">About Us</a>
      <a href="{href("services/")}">Services</a>
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
      <a href="mailto:hello@primecoreinfo.com">hello@primecoreinfo.com</a>
      <a href="{href("privacy-policy/")}">Privacy Policy</a>
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
      <a class="btn" data-magnetic href="contact/">Get Started</a>
      <a class="btn-ghost" href="services/">Explore Our Services</a>
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
      <a class="service-panel reveal" href="services/#cloud-infrastructure">
        <span class="sp-num">01</span>
        <div class="sp-copy">
          <h3>Cloud Infrastructure</h3>
          <p>AWS Cloud Solutions, Microsoft Azure Solutions, Cloud Architecture, Hybrid &amp; Multi-Cloud, Landing Zones, Networking &amp; Infrastructure, High Availability, Disaster Recovery.</p>
        </div>
        <span class="sp-go" aria-hidden="true">→</span>
      </a>
      <a class="service-panel reveal" href="services/#devops-sre">
        <span class="sp-num">02</span>
        <div class="sp-copy">
          <h3>DevOps &amp; SRE</h3>
          <p>DevOps Consulting, Site Reliability Engineering, CI/CD Implementation, Infrastructure as Code, Terraform / OpenTofu, Kubernetes, Containerization, Monitoring &amp; Observability, Automation.</p>
        </div>
        <span class="sp-go" aria-hidden="true">→</span>
      </a>
      <a class="service-panel reveal" href="services/#cloud-migration">
        <span class="sp-num">03</span>
        <div class="sp-copy">
          <h3>Cloud Migration</h3>
          <p>Application Migration, Database Migration, Infrastructure Migration, Cloud Modernization, AWS &amp; Azure Migration, Hybrid Cloud Migration, Migration Planning &amp; Assessment.</p>
        </div>
        <span class="sp-go" aria-hidden="true">→</span>
      </a>
      <a class="service-panel reveal" href="services/#managed-infrastructure">
        <span class="sp-num">04</span>
        <div class="sp-copy">
          <h3>Managed Infrastructure Services</h3>
          <p>Cloud Infrastructure Management, Monitoring &amp; Support, Incident Management, Infrastructure Maintenance, Backup &amp; Disaster Recovery, Performance Optimization.</p>
        </div>
        <span class="sp-go" aria-hidden="true">→</span>
      </a>
      <a class="service-panel reveal" href="services/#security-governance">
        <span class="sp-num">05</span>
        <div class="sp-copy">
          <h3>Security &amp; Governance</h3>
          <p>Cloud Security, Identity &amp; Access Management, Security Best Practices, Infrastructure Security, Governance Frameworks, Policy &amp; Compliance, Secure Cloud Architecture.</p>
        </div>
        <span class="sp-go" aria-hidden="true">→</span>
      </a>
      <a class="service-panel reveal" href="services/#cloud-finops">
        <span class="sp-num">06</span>
        <div class="sp-copy">
          <h3>Cloud Cost Optimization / FinOps</h3>
          <p>Cloud Cost Assessment, Resource Optimization, Kubernetes Cost Optimization, Cost Visibility, Cloud Waste Reduction, FinOps Strategy, Cost Allocation &amp; Reporting.</p>
        </div>
        <span class="sp-go" aria-hidden="true">→</span>
      </a>
      <a class="service-panel reveal" href="services/#app-tech-services">
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
        "Primecore Info Systems | Modern IT Infrastructure & Cloud Solutions",
        "Primecore Info Systems helps businesses design, migrate, automate and optimize their IT infrastructure across AWS, Microsoft Azure and hybrid cloud environments.",
        "./", "home", home_body, True)),
    ("about/index.html", doc("About Us | Primecore Info Systems", "Primecore Info Systems Pvt. Ltd. is an IT services and technology solutions company helping organizations modernize infrastructure and adopt cloud.", "../", "about", about_body)),
    ("services/index.html", doc("Services | Primecore Info Systems", "Cloud Infrastructure, DevOps & SRE, Cloud Migration, Managed Infrastructure, Security & Governance, FinOps, and Technology Services.", "../", "services", services_body)),
    ("contact/index.html", doc("Contact | Primecore Info Systems", "Get started with Primecore Info Systems for cloud, infrastructure, and DevOps solutions.", "../", "contact", contact_body, False)),
    ("insights/index.html", doc("Insights | Primecore Info Systems", "Practical perspectives for cloud, infrastructure, and operations decisions.", "../", "insights", insights_body)),
    ("privacy-policy/index.html", doc("Privacy Policy | Primecore Info Systems", "How Primecore Info Systems uses information shared through this website.", "../", "home", privacy_body)),
    ("cloud-transformation/index.html", doc("Cloud Transformation | Primecore Info Systems", "Move to the cloud with a plan you can trust.", "../", "services", cloud_body)),
    ("infrastructure-modernization/index.html", doc("Infrastructure Modernization | Primecore Info Systems", "Modernize core infrastructure for performance, resilience, and cloud-first operations.", "../", "services", infra_body)),
    ("managed-it-services/index.html", doc("Managed IT Services | Primecore Info Systems", "Proactive monitoring, responsive support, and operational ownership.", "../", "services", managed_body)),
    ("insights/cloud-readiness/index.html", doc("Cloud readiness | Primecore Info Systems Insights", "What to clarify before the first migration wave.", "../../", "insights", article_cloud)),
    ("insights/modern-foundations/index.html", doc("Modern foundations | Primecore Info Systems Insights", "How to sequence infrastructure improvements around business risk.", "../../", "insights", article_found)),
    ("insights/operational-resilience/index.html", doc("Operational resilience | Primecore Info Systems Insights", "Why visibility and ownership matter as environments grow.", "../../", "insights", article_ops)),
    ("404.html", doc("Page Not Found | Primecore Info Systems", "The requested route does not exist.", "./", "home", notfound_body, False)),
    ("home/index.html", home_redirect),
]

for rel, html in pages:
    write(rel, html)
print("done")
