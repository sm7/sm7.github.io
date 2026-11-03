/* GoatCounter: cookie-free, privacy-friendly page counts. See "About" for what it records. */
(function () {
  var s = document.createElement("script");
  s.async = true;
  s.src = "//gc.zgo.at/count.js";
  s.setAttribute("data-goatcounter", "https://lanchhana.goatcounter.com/count");
  document.head.appendChild(s);

  var el = document.getElementById("visit-count");
  if (!el || !window.fetch) return;
  fetch("https://lanchhana.goatcounter.com/counter/TOTAL.json")
    .then(function (r) { return r.ok ? r.json() : Promise.reject(); })
    .then(function (d) {
      if (d && d.count && d.count !== "0") { el.textContent = d.count + " page views"; el.hidden = false; }
    })
    .catch(function () { /* counter not enabled or blocked: stay hidden */ });
})();
