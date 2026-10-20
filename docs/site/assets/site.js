// MakerLine docs site: small progressive enhancements. Every page reads and works without this file.
// 1. Theme switch  2. Mobile menu  3. Copy buttons on code  4. Contents panel open on wide screens
// 5. Gentle reveal of home-page diagrams as they scroll into view (skipped for reduced motion).
(function () {
  "use strict";
  var root = document.documentElement;
  var darkQuery = window.matchMedia("(prefers-color-scheme: dark)");
  var calm = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var tools = document.querySelector("header.site .tools");
  // Interface words follow the page language (the home page is also in Hindi and Spanish).
  var WORDS = {
    en: { dark: "Switch to dark theme", light: "Switch to light theme", menu: "Menu", copy: "Copy", copied: "Copied",
          copyCode: "Copy code", copiedSay: "Code copied to clipboard", copyFail: "Couldn't copy. Select the text and copy it instead." },
    hi: { dark: "डार्क थीम पर जाएँ", light: "लाइट थीम पर जाएँ", menu: "मेन्यू", copy: "कॉपी", copied: "कॉपी हो गया",
          copyCode: "कोड कॉपी करें", copiedSay: "कोड क्लिपबोर्ड पर कॉपी हो गया", copyFail: "कॉपी नहीं हो सका। टेक्स्ट चुनकर कॉपी करें।" },
    es: { dark: "Cambiar al tema oscuro", light: "Cambiar al tema claro", menu: "Menú", copy: "Copiar", copied: "Copiado",
          copyCode: "Copiar código", copiedSay: "Código copiado", copyFail: "No se pudo copiar. Selecciona el texto y cópialo." }
  };
  var W = WORDS[(root.lang || "en").slice(0, 2)] || WORDS.en;

  function icon(path) {
    return '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="' + path + '"/></svg>';
  }
  var SUN = "M12 4V2m0 20v-2m8-8h2M2 12h2m13.66-5.66 1.41-1.41M4.93 19.07l1.41-1.41m0-11.32L4.93 4.93m14.14 14.14-1.41-1.41M16 12a4 4 0 1 1-8 0 4 4 0 0 1 8 0Z";
  var MOON = "M20.5 14.5A8.5 8.5 0 0 1 9.5 3.5a8.5 8.5 0 1 0 11 11Z";

  // 1. Theme switch — a real button with a label that says what it will do.
  function currentTheme() {
    return root.getAttribute("data-theme") || (darkQuery.matches ? "dark" : "light");
  }
  if (tools) {
    var themeBtn = document.createElement("button");
    themeBtn.type = "button";
    themeBtn.className = "icon-btn theme-btn";
    var paint = function () {
      var next = currentTheme() === "dark" ? "light" : "dark";
      themeBtn.setAttribute("aria-label", next === "dark" ? W.dark : W.light);
      themeBtn.innerHTML = icon(next === "dark" ? MOON : SUN);
    };
    themeBtn.addEventListener("click", function () {
      var next = currentTheme() === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      try { localStorage.setItem("makerline-theme", next); } catch (e) { /* not saved; still switches */ }
      paint();
    });
    darkQuery.addEventListener("change", paint);
    paint();
    tools.insertBefore(themeBtn, tools.firstChild);

    // 2. Mobile menu — on narrow screens the nav folds behind a disclosure button.
    var list = document.getElementById("site-nav");
    if (list) {
      var menuBtn = document.createElement("button");
      menuBtn.type = "button";
      menuBtn.className = "menu-btn";
      menuBtn.setAttribute("aria-expanded", "false");
      menuBtn.setAttribute("aria-controls", "site-nav");
      menuBtn.innerHTML = icon("M4 7h16M4 12h16M4 17h16") + "<span>" + W.menu + "</span>";
      var setOpen = function (open) {
        menuBtn.setAttribute("aria-expanded", String(open));
        document.querySelector("header.site").classList.toggle("nav-open", open);
      };
      menuBtn.addEventListener("click", function () {
        setOpen(menuBtn.getAttribute("aria-expanded") !== "true");
      });
      document.addEventListener("keydown", function (e) {
        if (e.key === "Escape" && menuBtn.getAttribute("aria-expanded") === "true") {
          setOpen(false);
          menuBtn.focus();
        }
      });
      list.addEventListener("click", function (e) { if (e.target.closest("a")) setOpen(false); });
      tools.appendChild(menuBtn);
    }
  }

  // 3. Copy buttons on code blocks, with a spoken confirmation.
  var status = document.createElement("p");
  status.className = "sr-only";
  status.setAttribute("role", "status");
  document.body.appendChild(status);
  if (navigator.clipboard) {
    document.querySelectorAll("main pre").forEach(function (pre) {
      var wrap = document.createElement("div");
      wrap.className = "codeblock";
      pre.parentNode.insertBefore(wrap, pre);
      wrap.appendChild(pre);
      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "copy-btn";
      btn.textContent = W.copy;
      btn.setAttribute("aria-label", W.copyCode);
      btn.addEventListener("click", function () {
        navigator.clipboard.writeText(pre.innerText.trim()).then(function () {
          btn.textContent = W.copied;
          status.textContent = W.copiedSay;
          setTimeout(function () { btn.textContent = W.copy; status.textContent = ""; }, 2000);
        }, function () { status.textContent = W.copyFail; });
      });
      wrap.appendChild(btn);
    });
  }

  // 4. Contents panel starts open where there's room for it beside the text.
  var toc = document.querySelector(".toc details");
  if (toc && window.matchMedia("(min-width: 68rem)").matches) toc.open = true;

  // 5. Reveal: diagrams draw in once, when they first come into view.
  var reveal = document.querySelectorAll("[data-reveal]");
  if (calm || !("IntersectionObserver" in window)) {
    reveal.forEach(function (el) { el.classList.add("in"); });
  } else {
    root.classList.add("reveal-ready");
    var seen = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { entry.target.classList.add("in"); seen.unobserve(entry.target); }
      });
    }, { rootMargin: "0px 0px -10% 0px" });
    reveal.forEach(function (el) { seen.observe(el); });
  }

  // 6. The demo can be replayed (it plays once by itself, in about four seconds).
  var demo = document.querySelector(".demo");
  var replay = demo && demo.querySelector(".replay");
  if (replay && !calm) {
    replay.hidden = false;
    replay.addEventListener("click", function () {
      demo.classList.remove("in");
      void demo.offsetWidth; // restart the CSS animations
      demo.classList.add("in");
    });
  }
})();
