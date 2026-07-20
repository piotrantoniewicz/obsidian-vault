#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Galaxy Dashboard — generator statycznego, samowystarczalnego dashboardu vaultu.

Skanuje vault Obsidiana i generuje jeden plik HTML (offline, bez CDN) z:
  - liczbą notatek w każdym folderze,
  - top 10 labels, top 10 authors, top 10 wikilinks,
  - interaktywnym grafem połączeń notatek w stylu "galaxy"
    (węzły jak gwiazdy, tytuł każdego rodzaju notatki w innym kolorze).

Uruchomienie (odświeżenie dashboardu):
    python3 Dashboard/galaxy-dashboard.py

Wynik: Dashboard/Galaxy Dashboard.html  (otwórz w przeglądarce).

Domyślnie skanuje vault, w którym leży ten skrypt (katalog nadrzędny Dashboard/).
Można nadpisać ścieżką w zmiennej środowiskowej VAULT_PATH.
"""

import os
import re
import json
import glob
from collections import Counter
from datetime import datetime

# --- konfiguracja ---------------------------------------------------------

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
VAULT = os.environ.get("VAULT_PATH") or os.path.dirname(SCRIPT_DIR)
OUT = os.path.join(SCRIPT_DIR, "Galaxy Dashboard.html")

# Foldery z notatkami-węzłami grafu (Archives/Attachments/Templates pomijamy:
# Archives to duplikaty tytułów z Resources, reszta to nie-notatki).
NODE_FOLDERS = ["Resources", "Galaxy", "Projects", "Areas", "Inbox", "References"]
# Notatki luzem w korzeniu vaultu też liczymy jako węzły.
INCLUDE_ROOT_NOTES = True
# Pliki-katalogi (MOC linkujące do wszystkiego) — pomijamy jako węzły grafu,
# bo łączą się ze wszystkim i zamieniają galaktykę w jedną gwiazdę.
EXCLUDE_BASENAMES = {"index", "claude", "readme"}

# Kolejność + kolory rodzajów notatek (galaktyczna, dostępna paleta).
TYPE_COLORS = [
    ("Clippings", "#4dabf7"),   # niebieski   — webclipy / artykuły
    ("Emails",    "#69db7c"),   # zielony     — newslettery / maile
    ("Reports",   "#ffd43b"),   # żółty       — raporty PDF
    ("LinkedIn",  "#f783ac"),   # różowy      — posty LinkedIn
    ("Concept",   "#c084fc"),   # fioletowy   — Galaxy (pojęcia)
    ("Project",   "#ff922b"),   # pomarańcz   — Projects (huby)
    ("Area",      "#3bc9db"),   # cyjan       — Areas (huby)
    ("Inne",      "#adb5bd"),   # szary       — reszta
]
TYPE_COLOR_MAP = dict(TYPE_COLORS)

FM_RE = re.compile(r"^---\n(.*?)\n---", re.S)
WIKILINK_RE = re.compile(r"\[\[([^\]]+?)\]\]")


# --- parsowanie -----------------------------------------------------------

def read(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except Exception:
        return ""


def frontmatter(text):
    m = FM_RE.match(text)
    return m.group(1) if m else ""


def _clean(v):
    """Zdejmuje cudzysłowy, a z [[Cel|alias]] wyciąga 'Cel'."""
    v = v.strip().strip('"').strip("'").strip()
    m = re.search(r"\[\[([^\]]+?)\]\]", v)
    if m:
        return wikilink_target(m.group(1))
    return v


def fm_list(fm, key):
    """Wartości z YAML `key:` — obsługuje listę blokową, listę flow [a, b] i skalar."""
    # lista blokowa (- pozycje)
    m = re.search(rf"^{key}:\s*\n((?:[ \t]*-[ \t]*.*\n?)+)", fm, re.M)
    if m:
        out = []
        for line in m.group(1).splitlines():
            v = _clean(re.sub(r"^[ \t]*-[ \t]*", "", line))
            if v:
                out.append(v)
        return out
    # inline: key: [...] albo key: wartosc
    m2 = re.search(rf"^{key}:[ \t]*(.+)$", fm, re.M)
    if not m2:
        return []
    raw = m2.group(1).strip()
    if raw in ("[]", "~", ""):
        return []
    if raw.startswith("[") and raw.endswith("]"):
        # lista flow — dziel po przecinkach spoza wikilinków
        inner = raw[1:-1]
        parts = re.split(r",(?![^\[]*\]\])", inner)
        return [x for x in (_clean(p) for p in parts) if x]
    v = _clean(raw)
    return [v] if v else []


def wikilink_target(raw):
    """[[Cel|alias]] / [[Cel#nagłówek]] -> 'Cel'."""
    return raw.split("|")[0].split("#")[0].strip()


def note_type(category, folder):
    if category in TYPE_COLOR_MAP:
        return category
    mapping = {"Galaxy": "Concept", "Projects": "Project", "Areas": "Area"}
    if folder in mapping:
        return mapping[folder]
    return "Inne"


# --- skan vaultu ----------------------------------------------------------

def collect_files():
    files = []
    for folder in NODE_FOLDERS:
        base = os.path.join(VAULT, folder)
        if os.path.isdir(base):
            files += glob.glob(os.path.join(base, "**", "*.md"), recursive=True)
    if INCLUDE_ROOT_NOTES:
        files += glob.glob(os.path.join(VAULT, "*.md"))
    return [f for f in files if "/." not in f.replace(VAULT, "", 1)]


def top_folder(relpath):
    parts = relpath.split(os.sep)
    return parts[0] if len(parts) > 1 else "(korzeń)"


def main():
    files = collect_files()

    nodes = {}          # basename(lower) -> node dict
    folder_counts = Counter()
    labels = Counter()
    authors = Counter()
    wikilinks = Counter()

    raw_notes = []      # (basekey, fm, body) do drugiego przejścia po linkach

    for path in files:
        rel = os.path.relpath(path, VAULT)
        base = os.path.splitext(os.path.basename(path))[0]
        if base.lower() in EXCLUDE_BASENAMES:
            continue
        key = base.lower()
        folder_counts[top_folder(rel)] += 1

        text = read(path)
        fm = frontmatter(text)
        body = text[len(fm) + 8:] if fm else text  # po zamykającym ---

        cats = fm_list(fm, "categories")
        category = cats[0] if cats else ""
        ntype = note_type(category, top_folder(rel))

        for lab in fm_list(fm, "labels"):
            labels[lab] += 1
        for au in fm_list(fm, "authors") + fm_list(fm, "author"):
            authors[au] += 1

        if key not in nodes:
            nodes[key] = {
                "id": key,
                "label": base,
                "type": ntype,
                "folder": top_folder(rel),
                "deg": 0,
            }
        raw_notes.append((key, fm, body))

    edges = []
    edge_seen = set()
    for key, fm, body in raw_notes:
        for raw in WIKILINK_RE.findall(fm + "\n" + body):
            t = wikilink_target(raw)
            if not t:
                continue
            wikilinks[t] += 1
            tk = t.lower()
            if tk in nodes and tk != key:
                e = (key, tk) if key < tk else (tk, key)
                if e not in edge_seen:
                    edge_seen.add(e)
                    edges.append({"s": e[0], "t": e[1]})
                    nodes[key]["deg"] += 1
                    nodes[tk]["deg"] += 1

    node_list = list(nodes.values())

    data = {
        "generated": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "totalNotes": len(node_list),
        "totalEdges": len(edges),
        "folders": folder_counts.most_common(),
        "topLabels": labels.most_common(10),
        "topAuthors": authors.most_common(10),
        "topWikilinks": wikilinks.most_common(10),
        "types": TYPE_COLORS,
        "nodes": node_list,
        "edges": edges,
    }

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(render(data))
    print(f"OK — {len(node_list)} notatek, {len(edges)} polaczen -> {OUT}")


# --- render HTML ----------------------------------------------------------

def render(data):
    return HTML_TEMPLATE.replace("__DATA__", json.dumps(data, ensure_ascii=False))


HTML_TEMPLATE = r"""<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Galaxy Dashboard — vault Piotr</title>
<style>
  :root{
    --bg:#05060d; --panel:#0d1020cc; --panel2:#12162b; --border:#20264a;
    --txt:#e7ecff; --muted:#8b93c4; --accent:#7aa2ff;
  }
  *{box-sizing:border-box}
  html,body{margin:0;height:100%;background:var(--bg);color:var(--txt);
    font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
  #graph{position:fixed;inset:0;display:block;cursor:grab}
  #graph:active{cursor:grabbing}
  .overlay{position:fixed;z-index:5}
  .card{background:var(--panel);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);
    border:1px solid var(--border);border-radius:14px;box-shadow:0 10px 40px #0008}
  #header{top:16px;left:16px;padding:14px 18px;max-width:340px}
  #header h1{margin:0 0 2px;font-size:16px;letter-spacing:.3px}
  #header .sub{color:var(--muted);font-size:12px}
  #header .big{display:flex;gap:18px;margin-top:10px}
  #header .big div{font-size:12px;color:var(--muted)}
  #header .big b{display:block;font-size:22px;color:var(--txt);line-height:1.1}
  #side{top:16px;right:16px;width:300px;max-height:calc(100vh - 32px);overflow:auto;padding:4px}
  .stat{padding:12px 14px}
  .stat h2{margin:0 0 8px;font-size:12px;text-transform:uppercase;letter-spacing:1px;
    color:var(--muted);font-weight:700}
  .row{display:flex;align-items:center;gap:8px;font-size:13px;padding:3px 0}
  .row .name{flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
  .row .val{color:var(--muted);font-variant-numeric:tabular-nums}
  .bar{height:6px;border-radius:4px;display:block}
  .barwrap{flex:1;background:#ffffff10;border-radius:4px;overflow:hidden;max-width:120px}
  #legend{bottom:16px;left:16px;padding:12px 14px}
  #legend h2{margin:0 0 8px;font-size:11px;text-transform:uppercase;letter-spacing:1px;color:var(--muted)}
  #legend .item{display:flex;align-items:center;gap:8px;font-size:12px;padding:2px 0;cursor:pointer;opacity:.95;user-select:none}
  #legend .item.off{opacity:.3}
  #legend .swatch{width:11px;height:11px;border-radius:50%;box-shadow:0 0 8px currentColor;flex:none}
  #controls{bottom:16px;right:16px;padding:10px 12px;display:flex;gap:8px;align-items:center}
  #controls input{width:150px;background:var(--panel2);border:1px solid var(--border);color:var(--txt);
    border-radius:8px;padding:6px 9px;font-size:12px;outline:none}
  #controls button{background:var(--panel2);border:1px solid var(--border);color:var(--txt);
    border-radius:8px;padding:6px 10px;font-size:12px;cursor:pointer}
  #controls button:hover{border-color:var(--accent)}
  #tip{position:fixed;z-index:9;pointer-events:none;background:#0b0e1cf5;border:1px solid var(--border);
    border-radius:8px;padding:6px 10px;font-size:12px;max-width:260px;display:none;box-shadow:0 6px 20px #000a}
  #tip b{color:#fff}
  #tip .meta{color:var(--muted);font-size:11px;margin-top:2px}
  .gen{color:var(--muted);font-size:11px;margin-top:8px}
  @media (max-width:820px){#side{display:none}}
</style>
</head>
<body>
<canvas id="graph"></canvas>
<div id="tip"></div>

<div id="header" class="overlay card">
  <h1>🌌 Galaxy Dashboard</h1>
  <div class="sub">vault Piotr — połączenia notatek</div>
  <div class="big">
    <div><b id="mNotes">0</b>notatek</div>
    <div><b id="mEdges">0</b>połączeń</div>
    <div><b id="mTypes">0</b>rodzajów</div>
  </div>
  <div class="gen" id="gen"></div>
</div>

<div id="side" class="overlay">
  <div class="stat card" style="margin-bottom:12px">
    <h2>📁 Notatki wg folderu</h2><div id="folders"></div>
  </div>
  <div class="stat card" style="margin-bottom:12px">
    <h2>🏷️ Top 10 labels</h2><div id="labels"></div>
  </div>
  <div class="stat card" style="margin-bottom:12px">
    <h2>✍️ Top 10 authors</h2><div id="authors"></div>
  </div>
  <div class="stat card">
    <h2>🔗 Top 10 wikilinks</h2><div id="wikilinks"></div>
  </div>
</div>

<div id="legend" class="overlay card">
  <h2>Rodzaje notatek — kliknij, by ukryć</h2>
  <div id="legendItems"></div>
</div>

<div id="controls" class="overlay card">
  <input id="search" placeholder="szukaj notatki…" autocomplete="off">
  <button id="lonely">ukryj samotne</button>
  <button id="reset">reset widoku</button>
  <button id="freeze">pauza</button>
</div>

<script>
const DATA = __DATA__;
</script>
<script>
const typeColor = Object.fromEntries(DATA.types);
const colorOf = t => typeColor[t] || "#adb5bd";
const active = new Set(DATA.types.map(t => t[0]));

function esc(s){return String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));}
function fmtBars(el, rows, max, colorFn){
  el.innerHTML = "";
  rows.forEach(([name, val]) => {
    const w = max ? Math.max(4, Math.round(val / max * 100)) : 0;
    const c = colorFn ? colorFn(name) : "var(--accent)";
    const div = document.createElement("div");
    div.className = "row";
    div.innerHTML =
      `<span class="name" title="${esc(name)}">${esc(name)}</span>`+
      `<span class="barwrap"><span class="bar" style="width:${w}%;background:${c}"></span></span>`+
      `<span class="val">${val}</span>`;
    el.appendChild(div);
  });
}

document.getElementById("mNotes").textContent = DATA.totalNotes;
document.getElementById("mEdges").textContent = DATA.totalEdges;
document.getElementById("mTypes").textContent = DATA.types.length;
document.getElementById("gen").textContent = "zaktualizowano: " + DATA.generated;

fmtBars(document.getElementById("folders"), DATA.folders, Math.max(...DATA.folders.map(f=>f[1])));
fmtBars(document.getElementById("labels"), DATA.topLabels, Math.max(1,...DATA.topLabels.map(x=>x[1])), ()=>"#c084fc");
fmtBars(document.getElementById("authors"), DATA.topAuthors, Math.max(1,...DATA.topAuthors.map(x=>x[1])), ()=>"#4dabf7");
fmtBars(document.getElementById("wikilinks"), DATA.topWikilinks, Math.max(1,...DATA.topWikilinks.map(x=>x[1])), ()=>"#69db7c");

const legEl = document.getElementById("legendItems");
DATA.types.forEach(([t,c])=>{
  const d=document.createElement("div");
  d.className="item"; d.dataset.t=t;
  d.innerHTML=`<span class="swatch" style="background:${c};color:${c}"></span>${t}`;
  d.onclick=()=>{ if(active.has(t)){active.delete(t);d.classList.add("off");}
                  else{active.add(t);d.classList.remove("off");} };
  legEl.appendChild(d);
});

// ---------- graf ----------
const canvas = document.getElementById("graph");
const ctx = canvas.getContext("2d");
let W,H,DPR;
function resize(){
  DPR=Math.min(2,window.devicePixelRatio||1);
  W=window.innerWidth; H=window.innerHeight;
  canvas.width=W*DPR; canvas.height=H*DPR;
  canvas.style.width=W+"px"; canvas.style.height=H+"px";
  ctx.setTransform(DPR,0,0,DPR,0,0);
}
window.addEventListener("resize",resize); resize();

const nodes = DATA.nodes.map(n=>({
  ...n,
  x:(Math.random()-.5)*Math.min(W,H)*0.9,
  y:(Math.random()-.5)*Math.min(W,H)*0.9,
  vx:0, vy:0,
  r: 2.2 + Math.min(9, Math.sqrt(n.deg)*1.5)
}));
const idx = Object.fromEntries(nodes.map((n,i)=>[n.id,i]));
const links = DATA.edges.map(e=>({s:idx[e.s], t:idx[e.t]})).filter(l=>l.s!=null&&l.t!=null);
const nbr = nodes.map(()=>new Set());
links.forEach(l=>{ nbr[l.s].add(l.t); nbr[l.t].add(l.s); });

let view={x:W/2,y:H/2,k:0.85};
let alpha=1, frozen=false, hideLonely=false;
const vis = n => active.has(n.type) && (!hideLonely || n.deg>0);
const REP=380, LINK_DIST=42, LINK_K=0.02, GRAV=0.012, DAMP=0.86, CELL=48;

function tick(){
  if(frozen || alpha<0.004){ draw(); return; }
  const grid=new Map();
  const gk=(x,y)=>x+"_"+y;
  for(let i=0;i<nodes.length;i++){
    const n=nodes[i], cx=Math.floor(n.x/CELL), cy=Math.floor(n.y/CELL), k=gk(cx,cy);
    (grid.get(k)||grid.set(k,[]).get(k)).push(i);
  }
  for(let i=0;i<nodes.length;i++){
    const n=nodes[i], cx=Math.floor(n.x/CELL), cy=Math.floor(n.y/CELL);
    for(let ax=-1;ax<=1;ax++)for(let ay=-1;ay<=1;ay++){
      const cell=grid.get(gk(cx+ax,cy+ay)); if(!cell)continue;
      for(const j of cell){
        if(j<=i)continue;
        const m=nodes[j];
        let dx=n.x-m.x, dy=n.y-m.y, d2=dx*dx+dy*dy;
        if(d2<0.01){dx=Math.random()-.5;dy=Math.random()-.5;d2=1;}
        if(d2>CELL*CELL*4)continue;
        const d=Math.sqrt(d2), f=REP/d2, fx=dx/d*f, fy=dy/d*f;
        n.vx+=fx; n.vy+=fy; m.vx-=fx; m.vy-=fy;
      }
    }
  }
  for(const l of links){
    const a=nodes[l.s], b=nodes[l.t];
    let dx=b.x-a.x, dy=b.y-a.y, d=Math.sqrt(dx*dx+dy*dy)||1;
    const f=(d-LINK_DIST)*LINK_K, fx=dx/d*f, fy=dy/d*f;
    a.vx+=fx; a.vy+=fy; b.vx-=fx; b.vy-=fy;
  }
  for(const n of nodes){
    n.vx-=n.x*GRAV; n.vy-=n.y*GRAV;
    n.vx*=DAMP; n.vy*=DAMP;
    if(n!==nodes[dragNode]){ n.x+=n.vx*alpha*2; n.y+=n.vy*alpha*2; }
  }
  alpha*=0.992;
  draw();
}

function draw(){
  ctx.clearRect(0,0,W,H);
  ctx.save();
  ctx.translate(view.x,view.y); ctx.scale(view.k,view.k);
  const q=(searchTerm||"").toLowerCase();
  const hi=hoverNode!=null?nbr[hoverNode]:null;

  ctx.lineWidth=0.6/view.k;
  for(const l of links){
    const a=nodes[l.s], b=nodes[l.t];
    if(!vis(a)&&!vis(b))continue;
    let op=0.10;
    if(hoverNode!=null){ op=(l.s===hoverNode||l.t===hoverNode)?0.55:0.03; }
    ctx.strokeStyle=`rgba(150,170,255,${op})`;
    ctx.beginPath(); ctx.moveTo(a.x,a.y); ctx.lineTo(b.x,b.y); ctx.stroke();
  }
  for(let i=0;i<nodes.length;i++){
    const n=nodes[i], shown=vis(n);
    let a=shown?1:0.06;
    if(hideLonely && n.deg===0){ a=0; }
    if(hoverNode!=null){ a*=(i===hoverNode||hi.has(i))?1:0.15; }
    if(q){ a*=n.label.toLowerCase().includes(q)?1:0.12; }
    const c=colorOf(n.type);
    ctx.globalAlpha=a;
    ctx.beginPath(); ctx.fillStyle=c;
    ctx.shadowColor=c; ctx.shadowBlur=(i===hoverNode?18:8);
    ctx.arc(n.x,n.y,n.r,0,6.2832); ctx.fill(); ctx.shadowBlur=0;
  }
  ctx.globalAlpha=1;
  ctx.textAlign="left"; ctx.textBaseline="middle";
  const showAll=view.k>1.6;
  for(let i=0;i<nodes.length;i++){
    const n=nodes[i];
    if(!vis(n))continue;
    const isHi=hoverNode!=null&&(i===hoverNode||hi.has(i));
    const big=n.deg>=8;
    if(!(showAll||big||isHi))continue;
    if(q && !n.label.toLowerCase().includes(q) && !isHi)continue;
    ctx.font=`${isHi?12:11}px -apple-system,Segoe UI,Roboto,sans-serif`;
    ctx.fillStyle=colorOf(n.type);
    ctx.globalAlpha=isHi?1:(showAll?0.85:0.7);
    ctx.fillText(n.label, n.x+n.r+3, n.y);
  }
  ctx.globalAlpha=1;
  ctx.restore();
}

let hoverNode=null, dragNode=-1, panning=false, last={x:0,y:0}, searchTerm="";
const tip=document.getElementById("tip");
function toWorld(px,py){ return {x:(px-view.x)/view.k, y:(py-view.y)/view.k}; }
function pick(px,py){
  const w=toWorld(px,py); let best=null,bd=1e9;
  for(let i=0;i<nodes.length;i++){
    const n=nodes[i]; if(!vis(n))continue;
    const dx=n.x-w.x, dy=n.y-w.y, d=dx*dx+dy*dy, rr=(n.r+4)*(n.r+4);
    if(d<rr && d<bd){bd=d;best=i;}
  }
  return best;
}
canvas.addEventListener("mousemove",e=>{
  if(dragNode>=0){
    const w=toWorld(e.clientX,e.clientY);
    nodes[dragNode].x=w.x; nodes[dragNode].y=w.y;
    nodes[dragNode].vx=0; nodes[dragNode].vy=0;
    alpha=Math.max(alpha,0.3); return;
  }
  if(panning){
    view.x+=e.clientX-last.x; view.y+=e.clientY-last.y;
    last={x:e.clientX,y:e.clientY}; return;
  }
  const h=pick(e.clientX,e.clientY); hoverNode=h;
  if(h!=null){
    const n=nodes[h];
    tip.style.display="block";
    tip.style.left=Math.min(e.clientX+14,window.innerWidth-270)+"px";
    tip.style.top=(e.clientY+14)+"px";
    tip.innerHTML=`<b>${esc(n.label)}</b><div class="meta">`+
      `<span style="color:${colorOf(n.type)}">●</span> ${esc(n.type)} · ${esc(n.folder)} · ${n.deg} połączeń</div>`;
    canvas.style.cursor="pointer";
  } else { tip.style.display="none"; canvas.style.cursor="grab"; }
});
canvas.addEventListener("mousedown",e=>{
  const h=pick(e.clientX,e.clientY);
  if(h!=null){ dragNode=h; } else { panning=true; last={x:e.clientX,y:e.clientY}; }
});
window.addEventListener("mouseup",()=>{ dragNode=-1; panning=false; });
canvas.addEventListener("wheel",e=>{
  e.preventDefault();
  const s=Math.exp(-e.deltaY*0.0012);
  const wx=(e.clientX-view.x)/view.k, wy=(e.clientY-view.y)/view.k;
  view.k=Math.max(0.15,Math.min(6,view.k*s));
  view.x=e.clientX-wx*view.k; view.y=e.clientY-wy*view.k;
},{passive:false});

document.getElementById("search").addEventListener("input",e=>{ searchTerm=e.target.value.trim(); });
document.getElementById("reset").onclick=()=>{ view={x:W/2,y:H/2,k:0.85}; };
const lonelyBtn=document.getElementById("lonely");
lonelyBtn.onclick=()=>{ hideLonely=!hideLonely; lonelyBtn.textContent=hideLonely?"pokaż samotne":"ukryj samotne"; };
const freezeBtn=document.getElementById("freeze");
freezeBtn.onclick=()=>{ frozen=!frozen; freezeBtn.textContent=frozen?"start":"pauza"; if(!frozen)alpha=Math.max(alpha,0.2); };

(function loop(){ tick(); requestAnimationFrame(loop); })();
</script>
</body>
</html>"""


if __name__ == "__main__":
    main()
