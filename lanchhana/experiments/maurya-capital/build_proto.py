import re,pathlib
src=pathlib.Path('../../register.html').read_text()
src=src.replace('<script src="data.js?v=9"></script>','<script src="../../data.js?v=9"></script>\n<script>for(const c of window.LR.cards){c.img="../../"+c.img;if(c.ev)c.ev.img="../../"+c.ev.img;}</script>')
css='''
.pbar{position:fixed;left:0;right:0;bottom:0;z-index:99999;background:#111;color:#fff;font:500 12px/1 monospace;padding:8px 12px;display:flex;gap:10px;align-items:center;justify-content:center;flex-wrap:wrap}
.pbar a{color:#fff;border:1px solid #888;border-radius:999px;padding:6px 10px;text-decoration:none}.pbar a.on{background:#fff;color:#111}
.stabs{display:flex;gap:6px;padding:10px 20px;border-bottom:1px solid var(--line);flex-wrap:wrap}
.stabs button{font:500 13px/1 var(--body);border:1px solid var(--line);background:transparent;color:var(--ink);border-radius:999px;padding:9px 14px;cursor:pointer}
.stabs button[aria-selected=true]{background:var(--ink);color:var(--paper);border-color:var(--ink)}
.scene{margin:0;display:grid;gap:0}
.scene img{width:100%;height:auto;display:block;aspect-ratio:3/2;object-fit:cover;background:var(--wash)}
.scene .cap{padding:18px 24px 24px;display:grid;gap:10px}
.scene h3{font:700 22px/1.2 var(--display);margin:0}
.lab{display:grid;grid-template-columns:auto 1fr;gap:4px 10px;font-size:13.5px;line-height:1.5;margin:0}
.lab dt{font:600 11px/1.5 var(--mono);letter-spacing:.06em;text-transform:uppercase;padding:1px 7px;border-radius:4px;height:fit-content;white-space:nowrap}
.lab dt.T{background:var(--verdigris);color:#fff}.lab dt.A{background:var(--copper);color:#fff}.lab dt.C{background:var(--line);color:var(--ink)}
.lab dd{margin:0;color:var(--muted)}
.hyp{font:500 12px/1.5 var(--mono);color:var(--muted);border-top:1px solid var(--line);padding-top:10px;margin:0}
.setting{border-top:1px solid var(--line);padding:20px 24px 24px;display:grid;gap:14px;background:var(--wash)}
.setting h4{margin:0}
.thumbs{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.thumbs button{border:1px solid var(--line);background:var(--panel);border-radius:8px;padding:0;cursor:pointer;text-align:left;overflow:hidden;color:var(--ink)}
.thumbs img{width:100%;aspect-ratio:3/2;object-fit:cover;display:block}
.thumbs b{display:block;font:600 13px/1.3 var(--body);padding:8px 10px}
.lb{position:fixed;inset:0;z-index:50;background:rgba(0,0,0,.88);overflow:auto;display:grid;place-items:center;padding:16px}
.lb .scene{max-width:1100px;background:var(--panel);border-radius:8px;overflow:hidden}
.lb .x{position:fixed;top:12px;right:16px;background:var(--panel);z-index:2}
.car{display:grid;gap:10px}
.track{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;gap:14px;scrollbar-width:thin}
.track .scene{flex:0 0 100%;scroll-snap-align:start;background:var(--panel);border:1px solid var(--line);border-radius:8px;overflow:hidden}
.dots{display:flex;gap:8px;justify-content:center;align-items:center}
.dots button{width:10px;height:10px;border-radius:50%;border:1px solid var(--ink);background:transparent;padding:0;cursor:pointer}
.dots button[aria-current=true]{background:var(--ink)}
@media(max-width:700px){.thumbs{grid-template-columns:1fr}.scene .cap{padding:14px 16px 18px}.stabs{padding:10px 12px}}

.gal{display:grid;gap:10px;min-width:0}
.gal-h{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.gal-h h4{margin:0 auto 0 0}
.gal .track{gap:12px;padding-bottom:4px}
.gal .track .scene{flex:0 0 88%;position:relative}
.gal .scene img{cursor:zoom-in}
.gal .scene h3{font-size:17px}
.gal .cap{padding:12px 14px 14px;gap:8px}
.gal .lab{font-size:12.5px}
.badge{position:absolute;top:8px;left:8px;font:600 10.5px/1 var(--mono);letter-spacing:.08em;text-transform:uppercase;background:rgba(14,21,19,.78);color:#fff;border-radius:4px;padding:5px 7px;pointer-events:none}
.gnav{display:flex;gap:6px;flex-wrap:wrap;align-items:center}
.gnav button{font:500 12.5px/1 var(--body);border:1px solid var(--line);background:transparent;color:var(--ink);border-radius:999px;padding:8px 12px;cursor:pointer}
.gnav button[aria-current=true]{background:var(--ink);color:var(--paper);border-color:var(--ink)}
.gnav .ct{font:500 11px/1 var(--mono);color:var(--muted);margin-left:auto}
.gal .hyp{font-size:11.5px}
.lb .scene{position:relative}
'''
js=r'''
const LAYOUT=new URLSearchParams(location.search).get("layout")||"a";
const SCENES=[
 {k:"city",label:"City",img:"img/city_v3.webp",title:"The city: Pāṭaliputra at the river confluence, c. 300 BCE",
  alt:"Hypothetical reconstruction of Pāṭaliputra: a long narrow riverside city behind a timber palisade and a lotus-filled ditch",
  T:"A long narrow city, about 80 stades by 15, at the meeting of two rivers, behind a timber palisade pierced for archers, with a ditch for defence and drainage (Megasthenes, in Strabo 15.1.35–36).",
  A:"Wide ditches with lotus and crocodiles, square towers, an arched gateway (Arthaśāstra 2.3, a prescription attributed to Kauṭilya; its date is debated).",
  C:"Roof forms, the palace hall, boats, vegetation, the light."},
 {k:"street",label:"Street",img:"img/street_v3.webp",title:"The street: a royal road in the morning market",
  alt:"Hypothetical reconstruction of a Pāṭaliputra royal road with market stalls, bullock carts and officials at a weighing scale",
  T:"City commissioners supervised the markets, in boards of five (Megasthenes, in Strabo 15.1.50–51).",
  A:"Royal roads four daṇḍas (about 24 ft) wide; sellers of scents, garlands and grain on the east side; a well for every ten houses (Arthaśāstra 2.4).",
  C:"House fronts, dress, carts, the individual figures."},
 {k:"temple",label:"Temple",img:"img/shiva_temple_ne.webp",title:"The temple: a grand Śiva shrine, entrance facing north-east",
  alt:"Hypothetical reconstruction of a grand brick and timber Śiva temple at Pāṭaliputra with worshippers at the steps",
  T:"Temples (hiera) were under the commissioners' care (Megasthenes, in Strabo 15.1.51). No eyewitness describes one.",
  A:"At the centre of the city, the apartments of the gods, Śiva among them (Arthaśāstra 2.4).",
  C:"Everything visible: the brick plinth, timber hall, tiered tiled roof, the figure in the sanctum, its size, and its north-east facing."}
];
const HYP="Hypothetical reconstruction, painted with an AI image model from the texts above. Nothing here is an archaeological finding. Figures follow early Indian relief and sculpture idiom; ornament is illustrative.";
const sceneFig=(s,lazy)=>`<figure class="scene"><img src="${s.img}" alt="${esc(s.alt)}" width="1536" height="1024" ${lazy?'loading="lazy"':''}><figcaption class="cap"><h3>${esc(s.title)}</h3><dl class="lab"><dt class="T">Attested</dt><dd>${esc(s.T)}</dd><dt class="A">Prescribed</dt><dd>${esc(s.A)}</dd><dt class="C">Conjecture</dt><dd>${esc(s.C)}</dd></dl><p class="hyp">${esc(HYP)}</p></figcaption></figure>`;
const entryHtml0=entryHtml;
const HYP2="Hypothetical reconstruction, painted with an AI image model from the texts above; not an archaeological finding. Figures follow early Indian relief idiom; ornament is illustrative.";
const slide=(s,n,lazy)=>`<figure class="scene" ${n!=null?`data-slide="${n}"`:""}><img src="${s.img}" alt="${esc(s.alt)}" width="1536" height="1024" ${lazy?'loading="lazy"':''} data-zoom="${s.k}"><span class="badge">Reconstruction</span><figcaption class="cap"><h3>${esc(s.title)}</h3><dl class="lab"><dt class="T">Attested</dt><dd>${esc(s.T)}</dd><dt class="A">Prescribed</dt><dd>${esc(s.A)}</dd><dt class="C">Conjecture</dt><dd>${esc(s.C)}</dd></dl><p class="hyp">${esc(HYP2)}</p></figcaption></figure>`;
entryHtml=function(c){
  const h=entryHtml0(c); if(c.id!=="maurya") return h;
  const g=`<section class="gal" aria-label="Pāṭaliputra under Candragupta, c. 321–297 BCE, reconstructions"><div class="gal-h"><h4>Setting · Pāṭaliputra, c. 321–297 BCE</h4></div>
   <div class="gnav" id="gnav">${SCENES.map((s,n)=>`<button type="button" data-dot="${n}" ${n?'':'aria-current="true"'}>${esc(s.label)}</button>`).join("")}<span class="ct" id="gct" aria-live="polite">1 / ${SCENES.length}</span></div>
   <div class="track" id="track" tabindex="0" aria-label="Scene gallery">${SCENES.map((s,n)=>slide(s,n,n>0)).join("")}</div></section>`;
  return h.replace('<p class="t">',g+'<p class="t">');
};
function gscroll(n){ const t=dlg.querySelector("#track"); const sl=t.children[n]; if(sl) t.scrollTo({left:sl.offsetLeft-t.offsetLeft,behavior:"smooth"}); }
dlg.addEventListener("click",e=>{
  const z=e.target.closest("[data-zoom]"); if(z){ const s=SCENES.find(x=>x.k===z.dataset.zoom); const d=document.createElement("div"); d.className="lb"; d.innerHTML=`<button class="ib x" type="button">Close</button>`+slide(s,null,false); d.onclick=ev=>{ if(ev.target===d||ev.target.classList.contains("x")) d.remove(); }; dlg.appendChild(d); d.querySelector(".x").focus(); return; }
  const dt=e.target.closest("[data-dot]"); if(dt) gscroll(+dt.dataset.dot);
});
dlg.addEventListener("scroll",e=>{ if(e.target.id!=="track") return; const t=e.target; let n=0,best=1e9; [...t.children].forEach((c,k)=>{ const d=Math.abs(c.offsetLeft-t.offsetLeft-t.scrollLeft); if(d<best){best=d;n=k;} }); dlg.querySelectorAll("[data-dot]").forEach((b,k)=>b.toggleAttribute("aria-current",k===n)); const ct=dlg.querySelector("#gct"); if(ct) ct.textContent=`${n+1} / ${SCENES.length}`; },true);
dlg.addEventListener("keydown",e=>{ if(e.key==="Escape"){ const l=dlg.querySelector(".lb"); if(l){ e.preventDefault(); l.remove(); } } if(e.target.id==="track"&&(e.key==="ArrowRight"||e.key==="ArrowLeft")){ e.stopPropagation(); } });
if(location.hash==="#maurya"){ if(dlg.open) dlg.close(); openEntry("maurya"); }
'''
# insert css and js
src=src.replace('</style>',css+'</style>',1)
# define entryHtml as reassignable: it's a function declaration, reassignment works in sloppy script.
idx=src.rindex('</script>')
src=src[:idx]+js+src[idx:]
pathlib.Path('proto.html').write_text(src)
