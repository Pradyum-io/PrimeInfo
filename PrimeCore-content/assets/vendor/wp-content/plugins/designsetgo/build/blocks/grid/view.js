!(function () {
  "use strict";
  class t {
    constructor(t) {
      (this.element = t),
        (this.inner = t.querySelector(".dsgo-grid__inner")),
        this.inner &&
          ((this.tabletBreakpoint = 1024),
          (this.mobileBreakpoint = 767),
          (this.matchRows = t.classList.contains("dsgo-grid--match-rows")),
          this.init());
    }
    init() {
      let t;
      this.handleResize(),
        (this.handleResize = this.handleResize.bind(this)),
        window.addEventListener("resize", () => {
          clearTimeout(t), (t = setTimeout(() => this.handleResize(), 150));
        });
    }
    getResponsiveColumns() {
      const t = window.innerWidth;
      if (t <= this.mobileBreakpoint) {
        for (let t = 1; t <= 12; t++)
          if (this.element.classList.contains(`dsgo-grid-cols-mobile-${t}`))
            return { breakpoint: "mobile", columns: t };
        return { breakpoint: "mobile", columns: 1 };
      }
      if (t <= this.tabletBreakpoint) {
        for (let t = 1; t <= 12; t++)
          if (this.element.classList.contains(`dsgo-grid-cols-tablet-${t}`))
            return { breakpoint: "tablet", columns: t };
        return { breakpoint: "tablet", columns: 2 };
      }
      return { breakpoint: "desktop", columns: null };
    }
    handleResize() {
      const t = this.getResponsiveColumns(),
        e = null === t.columns ? this.getDesktopColumns() : t.columns,
        n = this.matchRows ? this.getRenderedColumns(e) : null;
      "desktop" === t.breakpoint
        ? this.removeConstraints()
        : this.applyConstraints(t.columns),
        this.applyRowMatching(n);
    }
    getDesktopColumns() {
      for (let t = 12; t >= 1; t--)
        if (this.element.classList.contains(`dsgo-grid-cols-${t}`)) return t;
      return 1;
    }
    getRenderedColumns(t) {
      const e = window.getComputedStyle(this.inner).gridTemplateColumns;
      return (e && "none" !== e && e.split(/\s+/).filter(Boolean).length) || t;
    }
    countCardRows(t) {
      const e =
        t.querySelector(
          ":scope > .dsgo-stack__inner, :scope > .dsgo-flex__inner"
        ) || (t.classList.contains("wp-block-group") ? t : null);
      return e ? e.children.length : 0;
    }
    applyRowMatching(t) {
      if (!this.matchRows) return;
      const e = "dsgo-grid__inner--rows-matched";
      if (!t || t <= 1)
        return (
          this.inner.classList.remove(e),
          void this.inner.style.removeProperty("--dsgo-row-count")
        );
      const n = Array.from(this.inner.children).reduce(
        (t, e) => Math.max(t, this.countCardRows(e)),
        0
      );
      if (n < 1)
        return (
          this.inner.classList.remove(e),
          void this.inner.style.removeProperty("--dsgo-row-count")
        );
      this.inner.style.setProperty("--dsgo-row-count", String(n)),
        this.inner.classList.add(e);
    }
    applyConstraints(t) {
      Array.from(this.inner.children).forEach((e) => {
        const n = e.style.gridColumn;
        if (!n) return;
        const s = n.match(/span\s+(\d+)|^(\d+)$/);
        s && parseInt(s[1] || s[2]) > t && (e.style.gridColumn = `span ${t}`);
      });
    }
    removeConstraints() {}
  }
  function e() {
    document.querySelectorAll(".dsgo-grid").forEach((e) => {
      e.hasAttribute("data-dsgo-initialized") ||
        (e.setAttribute("data-dsgo-initialized", "true"), new t(e));
    });
  }
  "loading" === document.readyState
    ? document.addEventListener("DOMContentLoaded", e)
    : e(),
    document.addEventListener("dsgo-content-loaded", e),
    (window.DSGGrid = t);
})();
