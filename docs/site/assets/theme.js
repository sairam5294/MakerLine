// Runs in <head>, before the page paints, so a saved light/dark choice never flashes the wrong theme.
// No choice saved = follow the device setting (prefers-color-scheme). The choice lives only in this
// browser (localStorage), is never sent anywhere, and storage can be blocked, so every access is guarded.
(function () {
  var root = document.documentElement;
  root.classList.add("js");
  try {
    var saved = localStorage.getItem("makerline-theme");
    if (saved === "light" || saved === "dark") root.setAttribute("data-theme", saved);
  } catch (e) { /* storage blocked: follow the device setting */ }
})();
