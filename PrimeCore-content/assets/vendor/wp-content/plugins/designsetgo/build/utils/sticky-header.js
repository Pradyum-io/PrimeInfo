(() => {
  "use strict";
  !(function () {
    const o = window.dsgStickyHeaderSettings || {
      enable: !0,
      customSelector: "",
      zIndex: 100,
      shadowOnScroll: !0,
      shadowSize: "medium",
      shrinkOnScroll: !0,
      shrinkAmount: 50,
      mobileEnabled: !0,
      mobileBreakpoint: 768,
      transitionSpeed: 300,
      scrollThreshold: 50,
      hideOnScrollDown: !1,
      backgroundOnScroll: !1,
      backgroundScrollColor: "",
      backgroundScrollOpacity: 100,
      textScrollColor: "",
    };
    if (!o.enable) return;
    const t =
        "body:not(.block-editor-page) .wp-block-template-part:not(footer):first-of-type, body:not(.block-editor-page) header.wp-block-template-part, body:not(.block-editor-page) .wp-block-template-part:not(footer):has(.wp-block-navigation), body:not(.block-editor-page) .wp-block-template-part:not(footer):has(.is-position-sticky)",
      e = o.customSelector || t;
    let s = window.scrollY,
      n = !1;
    const l = new Set();
    function i(o) {
      if (!o.classList.contains("dsgo-sticky-skip-top-bar")) return;
      if (document.body.classList.contains("dsgo-page-overlay-header")) return;
      let t = o;
      if (
        (1 === o.children.length &&
          o.children[0].children.length >= 2 &&
          (t = o.children[0]),
        t.children.length < 2)
      )
        return;
      const e = document.getElementById("wpadminbar"),
        s = e ? e.getBoundingClientRect().height : 0,
        n = t.children[0].getBoundingClientRect().height;
      o.style.top = s - n + "px";
    }
    function d(o) {
      o.classList.contains("dsgo-sticky-shrink-logo") &&
        o
          .querySelectorAll(".wp-block-image img, .wp-block-site-logo img")
          .forEach((o) => {
            const t = () => {
              const t = o.offsetWidth,
                e = o.offsetHeight;
              t > 0 &&
                e > 0 &&
                (o.style.setProperty(
                  "--dsgo-sticky-logo-original-width",
                  `${t}px`
                ),
                o.style.setProperty(
                  "--dsgo-sticky-logo-original-height",
                  `${e}px`
                ));
            };
            o.complete && o.naturalWidth > 0
              ? t()
              : o.dataset.dsgoLogoLoadBound ||
                ((o.dataset.dsgoLogoLoadBound = "true"),
                o.addEventListener("load", t, { once: !0 }));
          });
    }
    function r(t) {
      const e = window.scrollY;
      (!o.mobileEnabled && window.innerWidth < o.mobileBreakpoint) ||
        (e > o.scrollThreshold
          ? t.classList.add("dsgo-scrolled")
          : t.classList.remove("dsgo-scrolled"),
        o.hideOnScrollDown &&
          e > o.scrollThreshold &&
          (e > s
            ? (t.classList.add("dsgo-scroll-down"),
              t.classList.remove("dsgo-scroll-up"))
            : (t.classList.add("dsgo-scroll-up"),
              t.classList.remove("dsgo-scroll-down"))));
    }
    function c(o) {
      l.forEach((t) => {
        t.isConnected ? o(t) : l.delete(t);
      });
    }
    function a() {
      n ||
        (window.requestAnimationFrame(() => {
          c(r), (s = window.scrollY), (n = !1);
        }),
        (n = !0));
    }
    let g = !1;
    function h(t) {
      t.dataset.dsgoInitialized ||
        ((t.dataset.dsgoInitialized = "true"),
        (function (t) {
          t.style.setProperty("--dsgo-sticky-header-z-index", o.zIndex),
            t.style.setProperty(
              "--dsgo-sticky-header-transition-speed",
              `${o.transitionSpeed}ms`
            );
          const e = t.classList.contains("dsgo-sticky-shrink-logo"),
            s =
              t.dataset.dsgoShrinkAmount ??
              t.dataset.dsgShrinkAmount ??
              (e || o.shrinkOnScroll ? o.shrinkAmount ?? 50 : null);
          if (s) {
            const o = parseInt(s, 10) / 100,
              e = Math.max(0.1, 1 - o);
            t.style.setProperty("--dsgo-sticky-logo-scale", e);
          }
          if (
            o.backgroundOnScroll ||
            t.classList.contains("dsgo-sticky-bg-on-scroll")
          ) {
            if (o.backgroundScrollColor) {
              const e = o.backgroundScrollOpacity / 100;
              let s = o.backgroundScrollColor;
              if (s.startsWith("#")) {
                const o = parseInt(s.slice(1, 3), 16),
                  t = parseInt(s.slice(3, 5), 16),
                  n = parseInt(s.slice(5, 7), 16);
                s = `rgba(${o}, ${t}, ${n}, ${e})`;
              }
              t.style.setProperty("--dsgo-sticky-scroll-bg-color", s);
            } else t.style.removeProperty("--dsgo-sticky-scroll-bg-color");
            o.textScrollColor
              ? t.style.setProperty(
                  "--dsgo-sticky-scroll-text-color",
                  o.textScrollColor
                )
              : t.style.removeProperty("--dsgo-sticky-scroll-text-color");
          }
        })(t),
        (function (t) {
          t.classList.contains("dsgo-sticky-header-enabled") ||
            (o.shadowOnScroll &&
              t.classList.add(`dsgo-sticky-shadow-${o.shadowSize}`),
            o.shrinkOnScroll && t.classList.add("dsgo-sticky-shrink-logo"),
            o.hideOnScrollDown &&
              t.classList.add("dsgo-sticky-hide-on-scroll-down"),
            o.backgroundOnScroll && t.classList.add("dsgo-sticky-bg-on-scroll"),
            !1 !== o.skipTopBar && t.classList.add("dsgo-sticky-skip-top-bar"),
            o.mobileEnabled || t.classList.add("dsgo-sticky-mobile-disabled"));
        })(t),
        t.classList.contains("dsgo-sticky-shrink") &&
          !t.classList.contains("dsgo-sticky-shrink-logo") &&
          t.classList.add("dsgo-sticky-shrink-logo"),
        d(t),
        i(t),
        l.add(t),
        (function () {
          if (g) return;
          let o;
          (g = !0),
            window.addEventListener("scroll", a, { passive: !0 }),
            window.addEventListener("resize", () => {
              clearTimeout(o),
                (o = setTimeout(() => {
                  p(),
                    c((o) => {
                      o.classList.contains("dsgo-scrolled") || d(o);
                    });
                }, 150));
            });
        })());
    }
    function p() {
      (s = window.scrollY),
        c((o) => {
          (function (o) {
            if (!document.body.classList.contains("dsgo-page-overlay-header"))
              return;
            if (
              o !==
              document.querySelector(
                ".wp-site-blocks > header.wp-block-template-part, .wp-site-blocks > .wp-block-template-part:not(footer):first-of-type"
              )
            )
              return;
            const t = document.body.classList.contains(
              "dsgo-page-overlay-skip-top-bar"
            );
            (() => {
              let e = o.getBoundingClientRect().height;
              if (t) {
                let t = o;
                if (
                  (1 === o.children.length &&
                    o.children[0].children.length >= 2 &&
                    (t = o.children[0]),
                  t.children.length >= 2)
                ) {
                  const o = t.children[0].getBoundingClientRect().height;
                  e = Math.max(0, e - o);
                }
              }
              document.documentElement.style.setProperty(
                "--dsgo-overlay-header-height",
                `${e}px`
              );
            })(),
              (function (o) {
                const t = o.nextElementSibling?.firstElementChild;
                t &&
                  ("string" != typeof t.dataset.dsgoOverlayBasePaddingTop &&
                    (t.dataset.dsgoOverlayBasePaddingTop =
                      t.style.paddingTop ||
                      window.getComputedStyle(t).paddingTop ||
                      "0px"),
                  (t.style.paddingTop = `calc(${t.dataset.dsgoOverlayBasePaddingTop} + var(--dsgo-overlay-hero-clearance, var(--dsgo-overlay-header-height, 0px)))`));
              })(o);
          })(o),
            i(o),
            r(o);
        });
    }
    function y() {
      (function (o) {
        try {
          return document.querySelectorAll(o);
        } catch (e) {
          if (o !== t)
            try {
              return document.querySelectorAll(t);
            } catch (o) {}
          return document.querySelectorAll(":not(*)");
        }
      })(e).forEach(h),
        p();
    }
    "loading" === document.readyState
      ? document.addEventListener("DOMContentLoaded", y)
      : y(),
      window.addEventListener(
        "load",
        () => {
          p(),
            c((o) => {
              o.classList.contains("dsgo-scrolled") || d(o);
            });
        },
        { once: !0 }
      ),
      document.addEventListener("dsgo-content-loaded", y);
  })();
})();
