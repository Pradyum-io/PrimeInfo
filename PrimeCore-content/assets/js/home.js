(() => {
  const root = document.documentElement;
  const canvas = document.querySelector('#core-canvas');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const mobile = window.matchMedia('(max-width: 700px)').matches;
  const pointer = { x: 0, y: 0, tx: 0, ty: 0 };

  if (canvas) {
    const context = canvas.getContext('2d');
    const particles = Array.from({ length: mobile ? 38 : 78 }, (_, index) => ({
      angle: Math.random() * Math.PI * 2,
      radius: 0.18 + Math.random() * 0.42,
      speed: 0.00015 + Math.random() * 0.00035,
      size: 0.7 + Math.random() * 1.8,
      phase: index * 0.7
    }));
    let frame;
    let start = performance.now();

    const resize = () => {
      const ratio = Math.min(window.devicePixelRatio || 1, 2);
      canvas.width = canvas.clientWidth * ratio;
      canvas.height = canvas.clientHeight * ratio;
      context.setTransform(ratio, 0, 0, ratio, 0, 0);
    };
    const draw = (now) => {
      const width = canvas.clientWidth;
      const height = canvas.clientHeight;
      const time = reducedMotion ? 0 : now - start;
      context.clearRect(0, 0, width, height);
      const centerX = width * 0.72 + pointer.x * 22;
      const centerY = height * 0.49 + pointer.y * 18;
      const radius = Math.min(width, height) * (mobile ? 0.22 : 0.28);
      const glow = context.createRadialGradient(centerX, centerY, radius * 0.05, centerX, centerY, radius * 1.9);
      glow.addColorStop(0, 'rgba(95, 230, 214, .26)');
      glow.addColorStop(.38, 'rgba(37, 160, 175, .12)');
      glow.addColorStop(1, 'rgba(8, 17, 35, 0)');
      context.fillStyle = glow;
      context.fillRect(0, 0, width, height);
      context.save();
      context.translate(centerX, centerY);
      context.rotate(time * 0.00008 + pointer.x * 0.06);
      for (let ring = 0; ring < 5; ring += 1) {
        context.beginPath();
        context.ellipse(0, 0, radius * (0.76 + ring * .11), radius * (0.28 + ring * .055), ring * .44, 0, Math.PI * 2);
        context.strokeStyle = `rgba(113, 229, 218, ${.16 - ring * .02})`;
        context.lineWidth = ring === 0 ? 1.4 : 0.7;
        context.stroke();
      }
      context.restore();
      particles.forEach((particle) => {
        const angle = particle.angle + time * particle.speed;
        const x = centerX + Math.cos(angle) * radius * (1 + particle.radius) + pointer.x * (particle.phase % 13);
        const y = centerY + Math.sin(angle) * radius * (0.42 + particle.radius * .45) + pointer.y * (particle.phase % 9);
        context.beginPath();
        context.arc(x, y, particle.size, 0, Math.PI * 2);
        context.fillStyle = `rgba(160, 247, 232, ${.25 + particle.radius * .8})`;
        context.fill();
      });
      if (!reducedMotion) frame = requestAnimationFrame(draw);
    };
    const drawOnce = () => draw(performance.now());
    window.addEventListener('resize', resize);
    resize();
    drawOnce();
    if (!reducedMotion) frame = requestAnimationFrame(draw);
    window.addEventListener('beforeunload', () => cancelAnimationFrame(frame));
  }

  window.addEventListener('pointermove', (event) => {
    pointer.tx = (event.clientX / window.innerWidth - .5) * 2;
    pointer.ty = (event.clientY / window.innerHeight - .5) * 2;
    pointer.x += (pointer.tx - pointer.x) * .08;
    pointer.y += (pointer.ty - pointer.y) * .08;
    root.style.setProperty('--pointer-x', `${pointer.x * 18}px`);
    root.style.setProperty('--pointer-y', `${pointer.y * 18}px`);
  }, { passive: true });

  const header = document.querySelector('[data-header]');
  const scenes = document.querySelectorAll('.scene');
  const observer = new IntersectionObserver((entries) => entries.forEach((entry) => entry.isIntersecting && entry.target.classList.add('is-visible')), { threshold: .18 });
  scenes.forEach((scene) => observer.observe(scene));
  window.addEventListener('scroll', () => header?.classList.toggle('is-scrolled', window.scrollY > 36), { passive: true });

  const menuButton = document.querySelector('.menu-button');
  const mobileMenu = document.querySelector('#mobile-menu');
  menuButton?.addEventListener('click', () => {
    const open = menuButton.getAttribute('aria-expanded') === 'true';
    menuButton.setAttribute('aria-expanded', String(!open));
    mobileMenu.hidden = open;
    document.body.classList.toggle('menu-open', !open);
  });
  mobileMenu?.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => {
    mobileMenu.hidden = true;
    menuButton?.setAttribute('aria-expanded', 'false');
    document.body.classList.remove('menu-open');
  }));

  document.querySelectorAll('.magnetic-button').forEach((button) => button.addEventListener('pointermove', (event) => {
    if (reducedMotion) return;
    const box = button.getBoundingClientRect();
    button.style.transform = `translate(${(event.clientX - box.left - box.width / 2) * .12}px, ${(event.clientY - box.top - box.height / 2) * .12}px)`;
  }));
  document.querySelectorAll('.magnetic-button').forEach((button) => button.addEventListener('pointerleave', () => { button.style.transform = ''; }));
  document.querySelectorAll('[data-service]').forEach((node) => node.addEventListener('mouseenter', () => document.body.dataset.focus = node.dataset.service));
  document.querySelectorAll('[data-service]').forEach((node) => node.addEventListener('mouseleave', () => delete document.body.dataset.focus));
})();
