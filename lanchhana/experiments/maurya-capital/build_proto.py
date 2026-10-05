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
entryHtml=function(c){
  const h=entryHtml0(c); if(c.id!=="maurya") return h;
  const i=h.indexOf('<div class="dlg">'), pre=h.slice(0,i), rest=h.slice(i);
  if(LAYOUT==="a"){
    return pre+`<div class="stabs" role="tablist"><button role="tab" aria-selected="true" data-st="emblem">Emblem</button>${SCENES.map(s=>`<button role="tab" aria-selected="false" data-st="${s.k}">${s.label}</button>`).join("")}</div>
    <div data-pane="emblem">${rest}</div>`+SCENES.map(s=>`<div data-pane="${s.k}" hidden>${sceneFig(s,true)}</div>`).join("");
  }
  if(LAYOUT==="b"){
    return pre+rest+`<section class="setting"><h4>Setting · Pāṭaliputra under Candragupta, c. 321–297 BCE</h4><div class="thumbs">${SCENES.map(s=>`<button type="button" data-lb="${s.k}"><img src="${s.img}" alt="${esc(s.alt)}" loading="lazy"><b>${esc(s.label)}</b></button>`).join("")}</div></section>`;
  }
  return pre+rest+`<section class="setting"><h4>Setting · Pāṭaliputra under Candragupta, c. 321–297 BCE</h4><div class="car"><div class="track" id="track">${SCENES.map(s=>sceneFig(s,true)).join("")}</div><div class="dots" id="dots">${SCENES.map((s,n)=>`<button type="button" aria-label="${esc(s.label)}" data-dot="${n}" ${n?'':'aria-current="true"'}></button>`).join("")}</div></div></section>`;
};
dlg.addEventListener("click",e=>{
  const st=e.target.closest("[data-st]"); if(st){ dlg.querySelectorAll("[data-st]").forEach(b=>b.setAttribute("aria-selected",b===st)); dlg.querySelectorAll("[data-pane]").forEach(p=>p.hidden=p.dataset.pane!==st.dataset.st); dlg.scrollTop=0; return; }
  const lb=e.target.closest("[data-lb]"); if(lb){ const s=SCENES.find(x=>x.k===lb.dataset.lb); const d=document.createElement("div"); d.className="lb"; d.innerHTML=`<button class="ib x" type="button">Close</button>`+sceneFig(s); d.onclick=ev=>{ if(ev.target===d||ev.target.classList.contains("x")) d.remove(); }; dlg.appendChild(d); d.querySelector(".x").focus(); return; }
  const dt=e.target.closest("[data-dot]"); if(dt){ const t=dlg.querySelector("#track"); t.scrollTo({left:t.clientWidth*+dt.dataset.dot+ +dt.dataset.dot*14,behavior:"smooth"}); }
});
dlg.addEventListener("scroll",e=>{ if(e.target.id!=="track") return; const t=e.target, n=Math.round(t.scrollLeft/(t.clientWidth+14)); dlg.querySelectorAll("[data-dot]").forEach((b,k)=>b.toggleAttribute("aria-current",k===n)); },true);
dlg.addEventListener("keydown",e=>{ if(e.key==="Escape"){ const l=dlg.querySelector(".lb"); if(l){ e.preventDefault(); l.remove(); } } });
const pb=document.createElement("div"); pb.className="pbar"; pb.innerHTML="Modal layout prototype (open Maurya): "+["a","b","c"].map(x=>`<a class="${x===LAYOUT?"on":""}" href="?layout=${x}#maurya">${x.toUpperCase()}</a>`).join("")+"<span>A tabs · B thumbnails+viewer · C swipe gallery</span>"; document.body.appendChild(pb);
if(location.hash==="#maurya"){ if(dlg.open) dlg.close(); openEntry("maurya"); }
'''
# insert css and js
src=src.replace('</style>',css+'</style>',1)
# define entryHtml as reassignable: it's a function declaration, reassignment works in sloppy script.
idx=src.rindex('</script>')
src=src[:idx]+js+src[idx:]
pathlib.Path('proto.html').write_text(src)
