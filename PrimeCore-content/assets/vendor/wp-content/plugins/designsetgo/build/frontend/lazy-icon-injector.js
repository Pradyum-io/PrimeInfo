(() => {
  function e(e = document) {
    if (void 0 === window.dsgoIcons) return;
    const t = e.querySelectorAll(".dsgo-lazy-icon[data-icon-name]");
    0 !== t.length &&
      t.forEach((e) => {
        if ("true" === e.dataset.iconInjected) return;
        const t = e.dataset.iconName,
          o = "string" == typeof t ? t.trim().toLowerCase() : "",
          n =
            void 0 !== window.dsgoIconDefaults && window.dsgoIconDefaults.style
              ? window.dsgoIconDefaults.style
              : "filled",
          d = e.dataset.iconStyle ? null : e.closest("[data-dsgo-icon-style]"),
          a = e.dataset.iconStyle || d?.dataset.dsgoIconStyle || n,
          i =
            e.dataset.iconStrokeWidth ||
            d?.dataset.dsgoIconStrokeWidth ||
            "1.5",
          s =
            o &&
            !window.dsgoIcons[o] &&
            void 0 !== window.dsgoIconAliases &&
            window.dsgoIconAliases[o]
              ? window.dsgoIconAliases[o]
              : o;
        if (s && window.dsgoIcons[s])
          try {
            const t = window.dsgoIcons[s],
              o = new DOMParser().parseFromString(t, "image/svg+xml"),
              n = o.documentElement;
            if (o.querySelector("parsererror"))
              throw new Error("Invalid SVG markup");
            if (
              (["role", "aria-label", "aria-hidden"].forEach((t) => {
                const o = e.getAttribute(t);
                o && n.setAttribute(t, o);
              }),
              "outlined" === a)
            ) {
              const t = document.createElement("span");
              (t.className = "dsgo-icon-outlined"),
                (t.style.display = "contents"),
                t.style.setProperty("--icon-stroke-width", i),
                t.appendChild(n),
                e.appendChild(t);
            } else e.appendChild(n);
            e.dataset.iconInjected = "true";
          } catch (e) {
            console.error(`Failed to inject icon "${s}":`, e);
          }
      });
  }
  if (
    ((window.dsgoInjectIcons = e),
    "loading" === document.readyState
      ? document.addEventListener("DOMContentLoaded", () => e())
      : e(),
    document.addEventListener("dsgo-content-loaded", (t) => {
      const o = t.detail?.container || document;
      "bfcache" === t.detail?.source &&
        document
          .querySelectorAll('.dsgo-lazy-icon[data-icon-injected="true"]')
          .forEach((e) => {
            e.querySelector("svg") || e.removeAttribute("data-icon-injected");
          }),
        e(o);
    }),
    "undefined" != typeof MutationObserver)
  ) {
    let t = null;
    const o = new MutationObserver((o) => {
      for (const n of o)
        for (const o of n.addedNodes)
          if (
            o.nodeType === Node.ELEMENT_NODE &&
            ((o.matches?.(".dsgo-lazy-icon[data-icon-name]") &&
              "true" !== o.dataset.iconInjected) ||
              o.querySelector?.(
                '.dsgo-lazy-icon[data-icon-name]:not([data-icon-injected="true"])'
              ))
          )
            return (
              t && cancelAnimationFrame(t),
              void (t = requestAnimationFrame(() => {
                e(), (t = null);
              }))
            );
    });
    document.body
      ? o.observe(document.body, { childList: !0, subtree: !0 })
      : document.addEventListener("DOMContentLoaded", () => {
          o.observe(document.body, { childList: !0, subtree: !0 });
        });
  }
})();
