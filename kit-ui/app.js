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
