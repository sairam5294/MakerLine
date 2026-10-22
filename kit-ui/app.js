// MakerLine cockpit: the only script. Served as a file so the Content-Security-Policy can
// forbid inline scripts (script-src 'self'). The page works without it; this adds Copy buttons
// and moves keyboard focus to form errors or results so screen readers hear them.
(function () {
  "use strict";
  document.documentElement.classList.add("js"); // reveals the .js-only Copy buttons

  var live = function (message) {
    var region = document.getElementById("live");
    if (!region) return;
    region.textContent = ""; // clear first so the same message is announced again on a second copy
    window.setTimeout(function () { region.textContent = message; }, 50);
  };

  var fallbackCopy = function (field) {
    // Older browsers / blocked clipboard API: select the text and use the legacy copy command.
    field.focus();
    field.select();
    try { return document.execCommand("copy"); } catch (e) { return false; }
  };

  document.addEventListener("click", function (event) {
    var button = event.target.closest("button[data-copy]");
    if (!button) return;
    var field = document.getElementById(button.getAttribute("data-copy"));
    if (!field) return;
    var done = function (ok) {
      if (!ok) {
        field.focus();
        field.select();
        live("Couldn't copy automatically. The text is selected: press Command+C or Ctrl+C.");
        return;
      }
      live("Copied");
      button.textContent = "Copied ✓";
      button.setAttribute("data-state", "copied");
      window.setTimeout(function () {
        button.textContent = "Copy";
        button.removeAttribute("data-state");
      }, 2000);
    };
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(field.value).then(function () { done(true); }, function () { done(fallbackCopy(field)); });
    } else {
      done(fallbackCopy(field));
    }
  });

  document.addEventListener("DOMContentLoaded", function () {
    // After submitting the form, send focus to what changed: the errors, or the new prompt.
    // Focus is the single announcement: the error summary deliberately has no role="alert",
    // otherwise screen readers would read it twice (once as an alert, once on focus).
    var target = document.getElementById("error-summary") || document.getElementById("result");
    if (target) target.focus();
  });
})();

// ml-ui:start — identical to plugin/skills/product-opportunity-review/assets/ui.js (tests check)
/* MakerLine UI helpers, shared by the offline review report, the portfolio page and the kit UI (kit-ui/app.js
   carries an identical copy between ml-ui:start and ml-ui:end; tests check they match).
   - Tables: long cells are clipped to two lines; hover shows the full text (a tooltip that stays while hovered and
     closes with Esc), and a "View" button on every row opens a drawer with the whole row. Tables marked
     data-sortable get sortable columns. Without this script every cell shows in full.
   - Accordions (details.ml-acc): "Expand all / Collapse all" buttons (data-acc="open|close" data-acc-target="#id"),
     and a link to a step (#step-…) opens it.
   No dependencies; uses the CSSOM only (no inline style markup), so it runs under a strict Content-Security-Policy. */
(function () {
  if (window.mlUI) return;
  window.mlUI = true;
  var doc = document;
  var each = function (list, fn) { Array.prototype.forEach.call(list, fn); };
  var text = function (el) { return (el.textContent || "").replace(/\s+/g, " ").trim(); };
  // The row's name: the first line of its first cell (a project cell also holds its folder path on a second line).
  var rowName = function (row) {
    var c = row.cells[0], first = "";
    for (var n = (c.querySelector(".ml-clip") || c).firstChild; n; n = n.nextSibling) {
      if (n.nodeName === "BR") break;
      first += n.textContent;
    }
    return first.replace(/\s+/g, " ").trim() || text(c);
  };
  doc.documentElement.classList.add("js");

  /* ---------- Tooltip (WCAG 1.4.13: dismissible, hoverable, persistent) ---------- */
  var tip = doc.createElement("div");
  tip.className = "ml-tip"; tip.id = "ml-tip"; tip.setAttribute("role", "tooltip"); tip.hidden = true;
  var tipCell = null, hideTimer = 0;
  function showTip(cell) {
    clearTimeout(hideTimer);
    var clip = cell.querySelector(".ml-clip");
    if (!clip || !cell.classList.contains("is-clipped")) return;
    tip.textContent = text(clip); tip.hidden = false; tipCell = cell;
    var r = cell.getBoundingClientRect(), w = Math.min(380, innerWidth - 24);
    tip.style.maxWidth = w + "px";
    tip.style.left = Math.min(Math.max(12, r.left), innerWidth - w - 12) + "px";
    tip.style.top = (r.bottom + 6) + "px";
    var h = tip.getBoundingClientRect().height;
    if (r.bottom + 6 + h > innerHeight - 8) tip.style.top = Math.max(8, r.top - h - 6) + "px";
  }
  function hideTip(now) {
    clearTimeout(hideTimer);
    hideTimer = setTimeout(function () { tip.hidden = true; tipCell = null; }, now ? 0 : 160);
  }
  doc.addEventListener("mouseover", function (e) {
    if (e.target.closest && e.target.closest(".ml-tip")) { clearTimeout(hideTimer); return; }
    var cell = e.target.closest && e.target.closest("td.is-clipped, th.is-clipped");
    if (cell) { if (cell !== tipCell) showTip(cell); else clearTimeout(hideTimer); }
    else if (!tip.hidden) hideTip();
  });
  doc.addEventListener("keydown", function (e) { if (e.key === "Escape" && !tip.hidden) hideTip(true); });
  addEventListener("scroll", function () { if (!tip.hidden) hideTip(true); }, true);

  /* ---------- Drawer with the whole row ---------- */
  var drawer = null, opener = null;
  function makeDrawer() {
    drawer = doc.createElement("dialog");
    drawer.className = "ml-drawer";
    drawer.setAttribute("aria-labelledby", "ml-drawer-h");
    var head = doc.createElement("div"); head.className = "ml-drawer-head";
    var h = doc.createElement("h2"); h.id = "ml-drawer-h";
    var x = doc.createElement("button"); x.type = "button"; x.className = "ml-drawer-x"; x.setAttribute("aria-label", "Close details"); x.textContent = "×";
    x.addEventListener("click", function () { drawer.close(); });
    head.append(h, x);
    var body = doc.createElement("dl"); body.className = "ml-drawer-body";
    drawer.append(head, body);
    drawer.addEventListener("click", function (e) { if (e.target === drawer) drawer.close(); });
    drawer.addEventListener("close", function () { if (opener) opener.focus(); });
    doc.body.append(drawer);
  }
  function openDrawer(row, heads, from) {
    if (!drawer) makeDrawer();
    opener = from;
    var cells = Array.prototype.filter.call(row.cells, function (c) { return !c.classList.contains("ml-col-open"); });
    drawer.querySelector("h2").textContent = rowName(row) || "Details";
    var body = drawer.querySelector("dl"); body.textContent = "";
    cells.forEach(function (c, i) {
      var dt = doc.createElement("dt"); dt.textContent = heads[i] || "";
      var dd = doc.createElement("dd");
      var src = c.querySelector(".ml-clip") || c;
      each(src.childNodes, function (n) { dd.append(n.cloneNode(true)); });
      if (!text(dd)) dd.textContent = "—";
      body.append(dt, dd);
    });
    if (drawer.showModal) drawer.showModal(); else drawer.setAttribute("open", "");
    drawer.querySelector(".ml-drawer-x").focus();
  }

  /* ---------- Tables ---------- */
  function measure(scope) {
    each((scope || doc).querySelectorAll("table.ml-enhanced .ml-clip"), function (c) {
      c.parentNode.classList.toggle("is-clipped", c.scrollHeight > c.clientHeight + 1);
    });
  }
  function sortable(t, heads) {
    each(t.tHead.rows[0].cells, function (th, i) {
      if (th.classList.contains("ml-col-open")) return;
      var b = doc.createElement("button"); b.type = "button"; b.className = "ml-sort";
      while (th.firstChild) b.append(th.firstChild);
      th.append(b);
      b.addEventListener("click", function () {
        var dir = th.getAttribute("aria-sort") === "ascending" ? "descending" : "ascending";
        each(t.tHead.rows[0].cells, function (o) { o.removeAttribute("aria-sort"); });
        th.setAttribute("aria-sort", dir);
        var rows = Array.prototype.slice.call(t.tBodies[0].rows);
        rows.sort(function (a, z) {
          var r = text(a.cells[i]).localeCompare(text(z.cells[i]), undefined, { numeric: true, sensitivity: "base" });
          return dir === "ascending" ? r : -r;
        });
        rows.forEach(function (r) { t.tBodies[0].append(r); });
      });
    });
  }
  function enhance(t) {
    if (t.classList.contains("ml-enhanced") || !t.tHead || !t.tBodies[0]) return;
    var heads = Array.prototype.map.call(t.tHead.rows[0].cells, text);
    var th = doc.createElement("th"); th.scope = "col"; th.className = "ml-col-open";
    var sr = doc.createElement("span"); sr.className = "sr-only"; sr.textContent = "Details"; th.append(sr);
    t.tHead.rows[0].append(th);
    each(t.tBodies[0].rows, function (row) {
      if (row.cells.length === 1 && row.cells[0].colSpan > 1) { row.cells[0].colSpan += 1; return; }
      each(row.cells, function (c) {
        var w = doc.createElement("div"); w.className = "ml-clip";
        while (c.firstChild) w.append(c.firstChild);
        c.append(w);
      });
      var td = doc.createElement("td"); td.className = "ml-col-open";
      var b = doc.createElement("button"); b.type = "button"; b.className = "ml-open"; b.textContent = "View";
      b.setAttribute("aria-label", "View all details: " + rowName(row));
      b.addEventListener("click", function () { openDrawer(row, heads, b); });
      td.append(b); row.append(td);
      row.addEventListener("click", function (e) {
        if (e.target.closest("a, button, input, textarea, select")) return;
        if (e.target.closest(".is-clipped")) openDrawer(row, heads, b);
      });
    });
    t.classList.add("ml-enhanced");
    if (t.hasAttribute("data-sortable")) sortable(t, heads);
  }

  /* ---------- Accordions ---------- */
  function openTo(hash) {
    if (!hash || hash.length < 2) return;
    var el = doc.getElementById(decodeURIComponent(hash.slice(1)));
    if (!el) return;
    var d = el.tagName === "DETAILS" ? el : el.querySelector("details") || el.closest("details");
    for (var p = d; p; p = p.parentElement && p.parentElement.closest("details")) p.open = true;
  }
  doc.addEventListener("click", function (e) {
    var b = e.target.closest && e.target.closest("button[data-acc]");
    if (!b) return;
    var scope = doc.querySelector(b.getAttribute("data-acc-target")) || doc;
    var open = b.getAttribute("data-acc") === "open";
    each(scope.querySelectorAll("details.ml-acc"), function (d) { d.open = open; });
    measure(scope);
  });
  doc.addEventListener("toggle", function (e) { if (e.target.open) measure(e.target); }, true);
  addEventListener("hashchange", function () { openTo(location.hash); });

  function start() {
    doc.body.append(tip);
    each(doc.querySelectorAll(".review table, table[data-ml]"), enhance);
    measure();
    openTo(location.hash);
    var t = 0;
    addEventListener("resize", function () { clearTimeout(t); t = setTimeout(function () { measure(); }, 150); });
  }
  if (doc.readyState === "loading") doc.addEventListener("DOMContentLoaded", start); else start();
})();
// ml-ui:end
