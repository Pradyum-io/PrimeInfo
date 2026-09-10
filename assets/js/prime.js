(() => {
  const root = document.body.dataset.root || "./";
  const page = document.body.dataset.page || "";

  const header = document.querySelector(".site-header");
  const menuBtn = document.querySelector(".menu-btn");
  const mobile = document.querySelector(".mobile-nav");

  const onScroll = () => {
    if (header) header.classList.toggle("is-scrolled", window.scrollY > 12);
  };
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  if (menuBtn && mobile) {
    const toggle = () => {
      const open = menuBtn.getAttribute("aria-expanded") === "true";
      menuBtn.setAttribute("aria-expanded", String(!open));
      mobile.classList.toggle("is-open", !open);
      mobile.hidden = open;
      document.body.classList.toggle("nav-open", !open);
    };
    menuBtn.addEventListener("click", toggle);
    mobile.querySelectorAll("a").forEach((a) => a.addEventListener("click", () => {
      if (menuBtn.getAttribute("aria-expanded") === "true") toggle();
    }));
  }

  document.querySelectorAll("[data-magnetic]").forEach((el) => {
    if (!window.matchMedia("(pointer:fine)").matches) return;
    el.addEventListener("mousemove", (e) => {
      const r = el.getBoundingClientRect();
      const x = (e.clientX - r.left - r.width / 2) / 8;
      const y = (e.clientY - r.top - r.height / 2) / 8;
      el.style.transform = `translate(${x}px, ${y}px)`;
    });
    el.addEventListener("mouseleave", () => { el.style.transform = ""; });
  });

  const light = document.querySelector(".cursor-light");
  if (light && window.matchMedia("(pointer:fine) and (min-width: 1024px)").matches) {
    window.addEventListener("pointermove", (e) => {
      light.style.left = `${e.clientX}px`;
      light.style.top = `${e.clientY}px`;
    }, { passive: true });
  }

  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (!reduce && "IntersectionObserver" in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-in");
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
    document.querySelectorAll(".reveal").forEach((el) => io.observe(el));
  } else {
    document.querySelectorAll(".reveal").forEach((el) => el.classList.add("is-in"));
  }

  const process = document.querySelector(".process");
  const processLine = document.querySelector(".process-line");
  if (process && processLine && !reduce) {
    const steps = [...process.querySelectorAll(".step")];
    const update = () => {
      const rect = process.getBoundingClientRect();
      const start = window.innerHeight * 0.72;
      const end = window.innerHeight * 0.28;
      const t = Math.min(1, Math.max(0, (start - rect.top) / (rect.height + start - end)));
      processLine.style.width = `${t * 88}%`;
      const active = Math.min(steps.length - 1, Math.floor(t * steps.length));
      steps.forEach((s, i) => s.classList.toggle("is-on", i <= active));
    };
    update();
    window.addEventListener("scroll", update, { passive: true });
  }

  const svcNav = document.querySelector(".svc-nav");
  if (svcNav) {
    const links = [...svcNav.querySelectorAll("a")];
    const blocks = links.map((a) => document.querySelector(a.getAttribute("href"))).filter(Boolean);
    const spy = () => {
      let current = blocks[0];
      blocks.forEach((b) => {
        if (b.getBoundingClientRect().top < 160) current = b;
      });
      links.forEach((a) => a.classList.toggle("is-active", a.getAttribute("href") === `#${current.id}`));
    };
    window.addEventListener("scroll", spy, { passive: true });
    spy();
  }

  const filters = document.querySelectorAll("[data-filter]");
  if (filters.length) {
    filters.forEach((btn) => btn.addEventListener("click", () => {
      filters.forEach((b) => b.classList.remove("is-on"));
      btn.classList.add("is-on");
      const key = btn.dataset.filter;
      document.querySelectorAll("[data-cat]").forEach((card) => {
        card.style.display = key === "all" || card.dataset.cat === key ? "" : "none";
      });
    }));
  }

  const form = document.querySelector("#contact-form");
  if (form) {
    const card = form.closest(".form-card");
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      let ok = true;
      form.querySelectorAll("[required]").forEach((field) => {
        const wrap = field.closest(".field");
        const valid = field.checkValidity() && String(field.value).trim() !== "";
        wrap.classList.toggle("error", !valid);
        if (!valid) ok = false;
      });
      if (!ok) return;
      card.classList.add("is-loading");
      const data = Object.fromEntries(new FormData(form).entries());
      const body = [
        `Name: ${data.name}`,
        `Company: ${data.company || "—"}`,
        `Email: ${data.email}`,
        `Phone: ${data.phone || "—"}`,
        `Service: ${data.service}`,
        "",
        data.message
      ].join("\n");
      const mailto = `mailto:hello@primecoreinfo.com?subject=${encodeURIComponent("Project inquiry from " + data.name)}&body=${encodeURIComponent(body)}`;
      window.setTimeout(() => {
        card.classList.remove("is-loading");
        card.classList.add("is-done");
        window.location.href = mailto;
      }, 700);
    });
  }

  document.querySelectorAll(".faq summary").forEach((s) => {
    s.addEventListener("click", () => {});
  });

  void root;
  void page;
})();
