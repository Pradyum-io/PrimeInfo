(() => {
  var e = {
      96756() {
        !(function () {
          "use strict";
          function e(e) {
            if (!e || "string" != typeof e) return !1;
            try {
              const t = new URL(e, window.location.href);
              return "http:" === t.protocol || "https:" === t.protocol;
            } catch (e) {
              return !1;
            }
          }
          function t() {
            document
              .querySelectorAll(".dsgo-has-video-background")
              .forEach((t) => {
                const n = t.getAttribute("data-video-url"),
                  o = "true" === t.getAttribute("data-video-muted"),
                  a = "true" === t.getAttribute("data-video-loop"),
                  i = "true" === t.getAttribute("data-video-autoplay"),
                  s = "true" === t.getAttribute("data-video-mobile-hide");
                if (!n || !e(n)) return;
                if (window.innerWidth <= 767 && s) return;
                if (t.querySelector(".dsgo-video-background")) return;
                const r = document.createElement("div");
                (r.className = "dsgo-video-background"),
                  (r.style.position = "absolute"),
                  (r.style.top = "0"),
                  (r.style.left = "0"),
                  (r.style.width = "100%"),
                  (r.style.height = "100%"),
                  (r.style.zIndex = "0"),
                  (r.style.overflow = "hidden"),
                  (r.style.pointerEvents = "none");
                const d = document.createElement("video");
                d.src = n;
                const l = t.getAttribute("data-video-poster");
                l && e(l) && (d.poster = l),
                  (d.muted = o),
                  (d.loop = a),
                  (d.autoplay = i),
                  (d.playsInline = !0),
                  (d.style.width = "100%"),
                  (d.style.height = "100%"),
                  (d.style.objectFit = "cover"),
                  r.appendChild(d);
                const c = t.getAttribute("data-video-overlay-color");
                if (
                  c &&
                  (function (e) {
                    if (!e || "string" != typeof e) return !1;
                    const t = e.trim();
                    return (
                      !(0 === t.length || t.length > 64) &&
                      !/[<>"'`\\\u0000-\u001f]/.test(t) &&
                      !/url\s*\(|expression\s*\(|javascript:/i.test(t) &&
                      /^(#[0-9a-fA-F]{3}|#[0-9a-fA-F]{4}|#[0-9a-fA-F]{6}|#[0-9a-fA-F]{8}|rgba?\([\d\s,.%/]+\)|hsla?\([\d\s,.%/]+\)|var\(--[a-zA-Z0-9_-]+(,\s*[^)]+)?\)|[a-zA-Z]+)$/.test(
                        t
                      )
                    );
                  })(c)
                ) {
                  const e = document.createElement("div");
                  (e.className = "dsgo-video-overlay"),
                    (e.style.position = "absolute"),
                    (e.style.top = "0"),
                    (e.style.left = "0"),
                    (e.style.width = "100%"),
                    (e.style.height = "100%"),
                    (e.style.backgroundColor = c),
                    (e.style.opacity = "0.7"),
                    (e.style.zIndex = "1"),
                    (e.style.pointerEvents = "none"),
                    r.appendChild(e);
                }
                if (
                  ("static" === window.getComputedStyle(t).position &&
                    (t.style.position = "relative"),
                  t.insertBefore(r, t.firstChild),
                  Array.from(t.children).forEach((e) => {
                    e !== r &&
                      "static" === window.getComputedStyle(e).position &&
                      ((e.style.position = "relative"), (e.style.zIndex = "2"));
                  }),
                  i)
                ) {
                  const e = d.play();
                  void 0 !== e && e.catch(() => {});
                }
              });
          }
          let n;
          "loading" === document.readyState
            ? document.addEventListener("DOMContentLoaded", t)
            : t(),
            document.addEventListener("dsgo-content-loaded", t),
            window.addEventListener("resize", () => {
              clearTimeout(n),
                (n = setTimeout(() => {
                  document
                    .querySelectorAll(".dsgo-video-background")
                    .forEach((e) => {
                      e.remove();
                    }),
                    t();
                }, 250));
            });
        })();
      },
      57855() {
        function e() {
          if (window.matchMedia("(prefers-reduced-motion: reduce)").matches)
            return;
          const e = document.querySelectorAll(
            '[data-dsgo-animation-enabled="true"]'
          );
          e.length &&
            e.forEach((e) => {
              if ("true" === e.dataset.dsgoScrollLinked) return;
              if (e.dataset.dsgoAnimationInitialized) return;
              e.dataset.dsgoAnimationInitialized = "true";
              const o = e.dataset.dsgoAnimationTrigger || "scroll",
                a = e.dataset.dsgoAnimationDuration || "600",
                i = e.dataset.dsgoAnimationDelay || "0",
                s = e.dataset.dsgoAnimationEasing || "ease-out";
              switch (
                ((e.style.animationDuration = `${a}ms`),
                (e.style.animationDelay = `${i}ms`),
                (e.style.animationTimingFunction = s),
                e.style.setProperty("--dsgo-animation-duration", `${a}ms`),
                e.style.setProperty("--dsgo-animation-delay", `${i}ms`),
                e.style.setProperty("--dsgo-animation-easing", s),
                e.dataset.dsgoStaggerStep &&
                  e.style.setProperty(
                    "--dsgo-stagger-step",
                    `${e.dataset.dsgoStaggerStep}ms`
                  ),
                o)
              ) {
                case "load":
                  !(function (e) {
                    requestAnimationFrame(() => {
                      e.classList.add("dsgo-entrance-active");
                    });
                  })(e);
                  break;
                case "scroll":
                default:
                  !(function (e) {
                    const o = parseInt(e.dataset.dsgoAnimationOffset),
                      a = Number.isFinite(o) ? o : 100,
                      i = "false" !== e.dataset.dsgoAnimationOnce,
                      s =
                        e.dataset.dsgoExitAnimation &&
                        "" !== e.dataset.dsgoExitAnimation,
                      r = parseInt(e.dataset.dsgoAnimationDuration) || 600;
                    n.set(e, {
                      once: i,
                      hasExitAnimation: s,
                      duration: r,
                      shouldRepeat: s || !i,
                      hasAnimated: !1,
                      isAnimating: !1,
                      wasIntersecting: !1,
                      previousRatio: 0,
                      animationTimeout: null,
                    });
                    (function (e) {
                      if (t.has(e)) return t.get(e);
                      const o = new IntersectionObserver(
                        (e) => {
                          e.forEach((e) => {
                            const t = e.target,
                              a = n.get(t);
                            if (!a) return;
                            const i = e.intersectionRatio,
                              s = e.isIntersecting && !a.wasIntersecting,
                              r =
                                a.wasIntersecting &&
                                i < a.previousRatio &&
                                i < 0.8;
                            s
                              ? ((a.hasAnimated && !a.shouldRepeat) ||
                                  (a.animationTimeout &&
                                    (clearTimeout(a.animationTimeout),
                                    (a.animationTimeout = null)),
                                  (a.isAnimating = !1),
                                  t.classList.remove("dsgo-exit-active"),
                                  t.classList.add("dsgo-entrance-active"),
                                  (a.hasAnimated = !0),
                                  (a.isAnimating = !0),
                                  (a.animationTimeout = setTimeout(() => {
                                    (a.isAnimating = !1),
                                      (a.animationTimeout = null);
                                  }, a.duration))),
                                a.once &&
                                  !a.hasExitAnimation &&
                                  (o.unobserve(t), n.delete(t)))
                              : r &&
                                a.hasExitAnimation &&
                                a.shouldRepeat &&
                                a.hasAnimated
                              ? a.isAnimating ||
                                (a.animationTimeout &&
                                  (clearTimeout(a.animationTimeout),
                                  (a.animationTimeout = null)),
                                (a.isAnimating = !0),
                                t.classList.remove("dsgo-entrance-active"),
                                t.classList.add("dsgo-exit-active"),
                                (a.animationTimeout = setTimeout(() => {
                                  t.classList.remove("dsgo-exit-active"),
                                    (a.isAnimating = !1),
                                    (a.animationTimeout = null);
                                }, a.duration)))
                              : e.isIntersecting ||
                                !a.wasIntersecting ||
                                a.hasExitAnimation ||
                                t.classList.remove("dsgo-entrance-active"),
                              (a.wasIntersecting = e.isIntersecting),
                              (a.previousRatio = i);
                          });
                        },
                        { rootMargin: `-${e}px`, threshold: [0, 0.5, 0.8] }
                      );
                      return t.set(e, o), o;
                    })(a).observe(e);
                  })(e);
                  break;
                case "hover":
                  !(function (e) {
                    const t = parseInt(e.dataset.dsgoAnimationDuration) || 600,
                      n =
                        e.dataset.dsgoExitAnimation &&
                        "" !== e.dataset.dsgoExitAnimation;
                    let o = !1;
                    e.addEventListener("mouseenter", () => {
                      o ||
                        ((o = !0),
                        e.classList.remove("dsgo-exit-active"),
                        e.classList.add("dsgo-entrance-active"),
                        setTimeout(() => {
                          o = !1;
                        }, t));
                    }),
                      e.addEventListener("mouseleave", () => {
                        n && !o
                          ? ((o = !0),
                            e.classList.remove("dsgo-entrance-active"),
                            e.classList.add("dsgo-exit-active"),
                            setTimeout(() => {
                              e.classList.remove("dsgo-exit-active"), (o = !1);
                            }, t))
                          : e.classList.remove("dsgo-entrance-active");
                      });
                  })(e);
                  break;
                case "click":
                  !(function (e) {
                    const t = parseInt(e.dataset.dsgoAnimationDuration) || 600;
                    let n = !1;
                    e.addEventListener("click", (o) => {
                      o.target.closest?.("a, button") ||
                        n ||
                        ((n = !0),
                        e.classList.remove("dsgo-exit-active"),
                        e.classList.add("dsgo-entrance-active"),
                        setTimeout(() => {
                          e.classList.remove("dsgo-entrance-active"), (n = !1);
                        }, t + 100));
                    }),
                      e.hasAttribute("tabindex") ||
                        (e.setAttribute("tabindex", "0"),
                        e.setAttribute("role", "button")),
                      e.addEventListener("keydown", (t) => {
                        ("Enter" !== t.key && " " !== t.key) ||
                          (t.preventDefault(), e.click());
                      });
                  })(e);
              }
            });
        }
        document.addEventListener("DOMContentLoaded", e),
          document.addEventListener("dsgo-content-loaded", e);
        const t = new Map(),
          n = new WeakMap();
      },
      18684() {
        function e() {
          document.querySelectorAll(".dsgo-clickable").forEach((e) => {
            if (e.dataset.dsgoInitialized) return;
            e.dataset.dsgoInitialized = "true";
            const t = e.getAttribute("data-link-url");
            if (!t) return;
            if (
              !(n = t) ||
              "string" != typeof n ||
              ((n = n.trim()),
              /^(javascript|data|vbscript|file|about):/i.test(n) ||
                !/^(https?:\/\/|mailto:|tel:|\/|\.\/|\.\.\/|#)/i.test(n))
            )
              return void (
                window.console &&
                console.warn &&
                console.warn("DesignSetGo: Blocked potentially unsafe URL:", t)
              );
            var n;
            const o = e.getAttribute("data-link-target");
            (e.style.cursor = "pointer"),
              e.addEventListener("click", function (e) {
                const n = e.target;
                if (
                  "A" !== n.tagName &&
                  "BUTTON" !== n.tagName &&
                  "INPUT" !== n.tagName &&
                  "TEXTAREA" !== n.tagName &&
                  "SELECT" !== n.tagName &&
                  !n.closest("a") &&
                  !n.closest("button")
                ) {
                  let e;
                  try {
                    e = new URL(t, window.location.href);
                  } catch {
                    return;
                  }
                  if (
                    !["https:", "http:", "mailto:", "tel:"].includes(e.protocol)
                  )
                    return;
                  "_blank" === o
                    ? window.open(e.href, "_blank", "noopener,noreferrer")
                    : window.location.assign(e.href);
                }
              });
          });
        }
        document.addEventListener("DOMContentLoaded", e),
          document.addEventListener("dsgo-content-loaded", e);
      },
      97935() {
        const e = new Map(),
          t = new WeakSet();
        let n = null;
        const o = new WeakMap();
        function a(e, t, n) {
          const {
            color: o,
            initialSize: a,
            blur: i,
            speed: s,
            triggerOffset: r,
            completionPoint: d,
          } = t;
          let l = (function (e, t, n) {
            const o = e.getBoundingClientRect(),
              a = o.height,
              i = o.top,
              s = window.innerHeight,
              r = n - i;
            if (r <= 0) return 0;
            const d = a + s;
            let l = (r - (d * t) / 100) / d;
            return (l = Math.max(0, Math.min(1, l))), l;
          })(e, r, n);
          const c = Math.max(0.01, d / 100);
          l = Math.min(1, (l / c) * s);
          const u = e.getBoundingClientRect(),
            g = Math.max(u.width, u.height),
            m = window.innerHeight / 2 - u.top,
            p = a + l * (1.5 * g - a),
            f = i * (1 - l);
          e.style.setProperty("--dsgo-expanding-bg-progress", l),
            e.style.setProperty("--dsgo-expanding-bg-size", `${p}px`),
            e.style.setProperty("--dsgo-expanding-bg-blur", `${f}px`),
            e.style.setProperty("--dsgo-expanding-bg-color", o),
            e.style.setProperty("--dsgo-expanding-bg-top", `${m}px`);
        }
        function i() {
          const i = document.querySelectorAll(
            '[data-dsgo-expanding-bg-enabled="true"]'
          );
          0 !== i.length &&
            (n ||
              (n = new IntersectionObserver(
                (t) => {
                  t.forEach((t) => {
                    t.isIntersecting
                      ? (function (t) {
                          if (
                            e.has(t) ||
                            window.matchMedia(
                              "(prefers-reduced-motion: reduce)"
                            ).matches
                          )
                            return;
                          const n = t.dataset.dsgoExpandingBgColor || "#e8e8e8",
                            i = {
                              color:
                                ((s = n),
                                s &&
                                "string" == typeof s &&
                                [
                                  /^#[0-9A-Fa-f]{3,8}$/,
                                  /^rgb\([^)]+\)$/,
                                  /^rgba\([^)]+\)$/,
                                  /^hsl\([^)]+\)$/,
                                  /^hsla\([^)]+\)$/,
                                  /^[a-z]+$/i,
                                ].some((e) => e.test(s.trim()))
                                  ? n
                                  : "#e8e8e8"),
                              initialSize:
                                parseInt(
                                  t.dataset.dsgoExpandingBgInitialSize,
                                  10
                                ) || 50,
                              blur:
                                parseInt(t.dataset.dsgoExpandingBgBlur, 10) ||
                                30,
                              speed:
                                parseFloat(t.dataset.dsgoExpandingBgSpeed) || 1,
                              triggerOffset:
                                parseInt(
                                  t.dataset.dsgoExpandingBgTriggerOffset,
                                  10
                                ) || 0,
                              completionPoint:
                                parseInt(
                                  t.dataset.dsgoExpandingBgCompletionPoint,
                                  10
                                ) || 80,
                            };
                          var s;
                          o.has(t) || o.set(t, t.getBoundingClientRect().top);
                          const r = o.get(t);
                          let d = null;
                          const l = () => {
                            d ||
                              (d = requestAnimationFrame(() => {
                                a(t, i, r), (d = null);
                              }));
                          };
                          a(t, i, r),
                            window.addEventListener("scroll", l, {
                              passive: !0,
                            }),
                            e.set(t, l);
                        })(t.target)
                      : (function (t) {
                          const n = e.get(t);
                          n &&
                            (window.removeEventListener("scroll", n),
                            e.delete(t));
                        })(t.target);
                  });
                },
                { rootMargin: "100px 0px", threshold: 0 }
              )),
            i.forEach((e) => {
              t.has(e) || (n.observe(e), t.add(e));
            }));
        }
        function s() {
          i(),
            "undefined" != typeof window &&
              "MutationObserver" in window &&
              document.body &&
              new MutationObserver((e) => {
                let t = !1;
                e.forEach((e) => {
                  e.addedNodes.forEach((e) => {
                    1 === e.nodeType &&
                      (e.hasAttribute("data-dsgo-expanding-bg-enabled") ||
                        e.querySelector("[data-dsgo-expanding-bg-enabled]")) &&
                      (t = !0);
                  });
                }),
                  t && i();
              }).observe(document.body, { childList: !0, subtree: !0 });
        }
        "loading" === document.readyState
          ? document.addEventListener("DOMContentLoaded", s)
          : s(),
          document.addEventListener("dsgo-content-loaded", i);
      },
      89133() {
        const e = "dsgo-show-focus-outlines",
          t = () => {
            document.body && document.body.classList.remove(e);
          },
          n = (n) => {
            "Tab" === n.key &&
              document.body &&
              (document.body.classList.add(e),
              window.addEventListener("pointerdown", t, { once: !0 }));
          },
          o = () => {
            "undefined" != typeof document &&
              (document.body
                ? document.body.classList.remove(e)
                : document.addEventListener(
                    "DOMContentLoaded",
                    () => document.body?.classList.remove(e),
                    { once: !0 }
                  ),
              window.addEventListener("keydown", n));
          };
        "undefined" != typeof document &&
          ("loading" === document.readyState
            ? document.addEventListener("DOMContentLoaded", o, { once: !0 })
            : o());
      },
    },
    t = {};
  function n(o) {
    var a = t[o];
    if (void 0 !== a) return a.exports;
    var i = (t[o] = { exports: {} });
    return e[o](i, i.exports, n), i.exports;
  }
  (() => {
    "use strict";
    n(89133), n(57855);
    const e = "dsgo-svg-draw-ready",
      t = "dsgo-svg-draw-active";
    let o = null;
    function a(t) {
      t.classList.contains(e) ||
        (t
          .querySelectorAll("path, line, polyline, circle, ellipse, rect")
          .forEach((e) => {
            if ("function" != typeof e.getTotalLength) return;
            let t;
            try {
              t = e.getTotalLength();
            } catch (e) {
              return;
            }
            if (!t || !Number.isFinite(t)) return;
            const n = Math.ceil(t);
            (e.style.strokeDasharray = String(n)),
              (e.style.strokeDashoffset = String(n));
          }),
        t.classList.add(e));
    }
    function i(e = document) {
      if (window.matchMedia?.("(prefers-reduced-motion: reduce)")?.matches)
        return;
      const n = e.querySelectorAll('[data-dsgo-svg-draw="true"]');
      n.length &&
        (n.forEach(a),
        "IntersectionObserver" in window
          ? (o ||
              (o = new IntersectionObserver(
                (e) => {
                  e.forEach((e) => {
                    e.isIntersecting &&
                      (e.target.classList.add(t), o.unobserve(e.target));
                  });
                },
                { rootMargin: "0px 0px -10% 0px" }
              )),
            n.forEach((e) => {
              e.classList.contains(t) || o.observe(e);
            }))
          : n.forEach((e) => e.classList.add(t)));
    }
    "undefined" != typeof document &&
      ("loading" === document.readyState
        ? document.addEventListener("DOMContentLoaded", () => i())
        : i(),
      document.addEventListener("dsgo-content-loaded", () => i())),
      n(18684),
      n(96756);
    const s = "dsgo-text-reveal-unit",
      r = new WeakMap();
    function d(e) {
      if ("true" === e.dataset.dsgoTextRevealInitialized) return;
      const t = e.dataset.dsgoTextRevealColor || "#2563eb",
        n = e.dataset.dsgoTextRevealSplitMode || "word",
        o = e.dataset.dsgoTextRevealTransition || 150,
        a = e.dataset.dsgoTextRevealEffect || "color";
      e.classList.add(`dsgo-text-reveal--${a}`),
        e.style.setProperty("--dsgo-text-reveal-color", t),
        e.style.setProperty("--dsgo-text-reveal-transition", `${o}ms`),
        (function (e, t) {
          if (e.querySelector(`.${s}`)) return;
          const n = e.textContent;
          if (!n || !n.trim()) return;
          e.setAttribute("aria-label", n);
          const o = document.createTreeWalker(
              e,
              NodeFilter.SHOW_TEXT,
              null,
              !1
            ),
            a = [];
          let i;
          for (; (i = o.nextNode()); ) i.textContent.trim() && a.push(i);
          let r = 0;
          const d = (e) => {
            const t = document.createElement("span");
            return (
              (t.className = s),
              t.setAttribute("aria-hidden", "true"),
              t.style.setProperty("--dsgo-unit-index", String(r)),
              (t.textContent = e),
              r++,
              t
            );
          };
          a.forEach((e) => {
            const n = e.parentNode,
              o = document.createDocumentFragment();
            "character" === t
              ? e.textContent.split("").forEach((e) => {
                  " " === e
                    ? o.appendChild(document.createTextNode(" "))
                    : o.appendChild(d(e));
                })
              : e.textContent.split(/(\s+)/).forEach((e) => {
                  /^\s+$/.test(e)
                    ? o.appendChild(document.createTextNode(e))
                    : e && o.appendChild(d(e));
                }),
              n.replaceChild(o, e);
          });
        })(e, n);
      const i = e.querySelectorAll(`.${s}`),
        d = i.length;
      if (0 === d) return;
      if (
        ((e.dataset.dsgoTextRevealInitialized = "true"),
        window.matchMedia("(prefers-reduced-motion: reduce)").matches)
      )
        return void i.forEach((e) => e.classList.add("is-revealed"));
      let l = !1;
      const c = () => {
          l ||
            (requestAnimationFrame(() => {
              (function (e, t, n) {
                const o = e.getBoundingClientRect(),
                  a = window.innerHeight,
                  i = 0.8 * a,
                  s = o.top + o.height / 2,
                  r =
                    s -
                    (function () {
                      const e = document.documentElement,
                        t = Math.max(
                          0,
                          Math.max(
                            e.scrollHeight,
                            document.body ? document.body.scrollHeight : 0
                          ) - window.innerHeight
                        );
                      return Math.max(
                        0,
                        t - (window.scrollY || e.scrollTop || 0)
                      );
                    })(),
                  d = i - Math.max(a / 2, r);
                let l = d > 0 ? (i - s) / d : 1;
                l = Math.max(0, Math.min(1, l));
                const c = Math.floor(l * n);
                t.forEach((e, t) => {
                  t < c
                    ? e.classList.add("is-revealed")
                    : e.classList.remove("is-revealed");
                });
              })(e, i, d),
                (l = !1);
            }),
            (l = !0));
        },
        u = new IntersectionObserver(
          (e) => {
            e.forEach((e) => {
              e.isIntersecting
                ? (window.addEventListener("scroll", c, { passive: !0 }), c())
                : window.removeEventListener("scroll", c);
            });
          },
          { threshold: [0, 0.1], rootMargin: "50px 0px 50px 0px" }
        );
      r.set(e, u), u.observe(e);
    }
    function l() {
      document
        .querySelectorAll(
          '[data-dsgo-text-reveal-enabled="true"]:not([data-dsgo-text-reveal-initialized="true"])'
        )
        .forEach(d);
    }
    document.addEventListener("DOMContentLoaded", function () {
      if (window.dsgoTextRevealInitialized) return;
      window.dsgoTextRevealInitialized = !0;
      const e = document.querySelectorAll(
        '[data-dsgo-text-reveal-enabled="true"]'
      );
      e.length && e.forEach(d);
    }),
      document.addEventListener("dsgo-content-loaded", l),
      (window.dsgoTextReveal = {
        reinit: l,
        init: d,
        destroy: function (e) {
          const t = r.get(e);
          t && (t.disconnect(), r.delete(e));
        },
      }),
      n(97935);
    let c = null,
      u = null,
      g = null;
    function m() {
      if (window.dsgoParallaxInitialized) return;
      if (
        ((window.dsgoParallaxInitialized = !0),
        window.matchMedia("(prefers-reduced-motion: reduce)").matches)
      )
        return;
      const e = document.querySelectorAll(
        '[data-dsgo-parallax-enabled="true"]'
      );
      if (0 === e.length) return;
      let t = window.innerHeight,
        n = !1;
      const o = new Set();
      function a() {
        const e = window.scrollY;
        o.forEach((n) => {
          if (
            !(function (e) {
              const t = (function () {
                  const e = window.innerWidth;
                  return e >= 1024 ? "desktop" : e >= 768 ? "tablet" : "mobile";
                })(),
                n = "false" !== e.dataset.dsgoParallaxDesktop,
                o = "false" !== e.dataset.dsgoParallaxTablet,
                a = "true" === e.dataset.dsgoParallaxMobile;
              switch (t) {
                case "desktop":
                  return n;
                case "tablet":
                  return o;
                case "mobile":
                  return a;
                default:
                  return !0;
              }
            })(n)
          )
            return void (n.style.transform = "");
          const o = (function (e) {
              return {
                direction: e.dataset.dsgoParallaxDirection || "up",
                speed: parseInt(e.dataset.dsgoParallaxSpeed, 10) || 5,
                viewportStart:
                  parseInt(e.dataset.dsgoParallaxViewportStart, 10) || 0,
                viewportEnd:
                  parseInt(e.dataset.dsgoParallaxViewportEnd, 10) || 100,
                relativeTo: e.dataset.dsgoParallaxRelativeTo || "viewport",
                rotateEnabled: "true" === e.dataset.dsgoParallaxRotateEnabled,
                rotateDirection: e.dataset.dsgoParallaxRotateDirection || "cw",
                rotateSpeed: Number.isFinite(
                  parseInt(e.dataset.dsgoParallaxRotateSpeed, 10)
                )
                  ? parseInt(e.dataset.dsgoParallaxRotateSpeed, 10)
                  : 3,
              };
            })(n),
            a = (function (e, t, n, o) {
              const a = (function (e) {
                  let t = 0,
                    n = e;
                  for (; n; ) (t += n.offsetTop), (n = n.offsetParent);
                  return t;
                })(e),
                i = e.offsetHeight;
              let s, r;
              "viewport" === t.relativeTo
                ? ((s = a - o), (r = a + i))
                : ((s = 0), (r = document.body.scrollHeight - o));
              const d = r - s,
                l = s + (d * Math.min(t.viewportStart, t.viewportEnd)) / 100,
                c =
                  s + (d * Math.max(t.viewportStart, t.viewportEnd)) / 100 - l,
                u =
                  0 === c
                    ? 0
                    : ((g = (n - l) / c), Math.min(Math.max(g, 0), 1));
              var g;
              const m = 20 * t.speed,
                p = u - 0.5;
              let f = 0,
                v = 0;
              switch (t.direction) {
                case "up":
                default:
                  v = -p * m;
                  break;
                case "down":
                  v = p * m;
                  break;
                case "left":
                  f = -p * m;
                  break;
                case "right":
                  f = p * m;
              }
              let h = 0;
              return (
                t.rotateEnabled &&
                  ((h = p * (36 * t.rotateSpeed)),
                  "ccw" === t.rotateDirection && (h = -h)),
                { x: f, y: v, rotation: h }
              );
            })(n, o, e, t);
          let i = `translate3d(${a.x}px, ${a.y}px, 0)`;
          0 !== a.rotation && (i += ` rotate(${a.rotation}deg)`),
            (n.style.transform = i);
        }),
          (n = !1);
      }
      function i() {
        n || (requestAnimationFrame(a), (n = !0));
      }
      let s;
      (g = new IntersectionObserver(
        (e) => {
          e.forEach((e) => {
            e.isIntersecting
              ? o.add(e.target)
              : (o.delete(e.target), (e.target.style.transform = ""));
          });
        },
        { rootMargin: "50% 0px 50% 0px", threshold: 0 }
      )),
        e.forEach((e) => {
          (e.style.willChange = "transform"), g.observe(e);
        }),
        (c = i),
        (u = () => {
          clearTimeout(s),
            (s = setTimeout(() => {
              (t = window.innerHeight), i();
            }, 150));
        }),
        window.addEventListener("scroll", c, { passive: !0 }),
        window.addEventListener("resize", u, { passive: !0 }),
        i();
    }
    "loading" === document.readyState
      ? document.addEventListener("DOMContentLoaded", m)
      : m(),
      document.addEventListener("dsgo-content-loaded", () => {
        c && (window.removeEventListener("scroll", c), (c = null)),
          u && (window.removeEventListener("resize", u), (u = null)),
          g && (g.disconnect(), (g = null)),
          delete window.dsgoParallaxInitialized,
          m();
      }),
      window.addEventListener("pageshow", (e) => {
        e.persisted &&
          document.dispatchEvent(
            new CustomEvent("dsgo-content-loaded", {
              detail: { source: "bfcache" },
            })
          );
      });
  })();
})();
