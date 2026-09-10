(() => { const button = document.querySelector('.reference-menu'); const menu = document.querySelector('#reference-mobile-menu'); if (!button || !menu) return; button.addEventListener('click', () => { const open = button.getAttribute('aria-expanded') === 'true'; button.setAttribute('aria-expanded', String(!open)); menu.hidden = open; document.body.classList.toggle('mobile-open', !open); }); menu.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => { menu.hidden = true; button.setAttribute('aria-expanded', 'false'); document.body.classList.remove('mobile-open'); })); })();

(() => {
  // Parallax Effect for Dynamic Cloud System
  const hero = document.querySelector('.reference-hero');
  const system = document.querySelector('.dynamic-system');
  const dsCenter = document.querySelector('.ds-center');

  if (!hero || !system || !dsCenter) return;

  let mouseX = 0;
  let mouseY = 0;
  let currentX = 0;
  let currentY = 0;

  hero.addEventListener('mousemove', (e) => {
    const rect = hero.getBoundingClientRect();
    const centerX = rect.width / 2;
    const centerY = rect.height / 2;
    
    // Normalize to -1 to 1
    mouseX = (e.clientX - rect.left - centerX) / centerX;
    mouseY = (e.clientY - rect.top - centerY) / centerY;
  });

  hero.addEventListener('mouseleave', () => {
    mouseX = 0;
    mouseY = 0;
  });

  function animateParallax() {
    // Smooth easing
    currentX += (mouseX - currentX) * 0.05;
    currentY += (mouseY - currentY) * 0.05;

    // Apply subtle parallax to the entire system
    system.style.transform = `translate(${currentX * -15}px, ${currentY * -15}px)`;
    
    // Counter-move the center slightly to create depth
    dsCenter.style.marginLeft = `${currentX * 25}px`;
    dsCenter.style.marginTop = `${currentY * 25}px`;

    requestAnimationFrame(animateParallax);
  }

  // Only run on desktop
  if (window.matchMedia("(min-width: 900px)").matches) {
    animateParallax();
  }
})();
