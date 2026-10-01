"""One-off migration (Oct 2026): built data.js from the old single-page register, the fact-check results,
recorded prompts and the new Pāṇḍava entries. Paths under /tmp were session scratch files; data.js is now the source of truth."""
import json, re, subprocess, sys
SC='/tmp/claude-0/-home-claude-sm7-github-io/997c0891-c63e-51d7-a902-fd3eed4555e9/scratchpad/fc'
OLD='/tmp/claude-0/-home-claude/997c0891-c63e-51d7-a902-fd3eed4555e9/scratchpad'
ROOT='/home/claude/sm7.github.io/lanchhana'
legacy=json.loads(subprocess.check_output(['node','-e',f"const m=require('{SC}/data_mod.js');console.log(JSON.stringify(m))"]))
S=dict(legacy['S']); S.update(legacy['MBH'])
outs={k:json.load(open(f'{SC}/out_{k}.json')) for k in ['epic','early_a','early_b','later']}
for o in outs.values(): S.update(o.get('sourcesNew',{}))
pv=json.load(open(f'{SC}/pandava.json'))
S.update({'mbs7022':pv['sourceUrls']['mbs7022'],'gan7023':["Mahābhārata, Droṇa Parva, Section XXIII, tr. K. M. Ganguli (vulgate) — sacred-texts.com","https://www.sacred-texts.com/hin/m07/m07023.htm"],
 'mbsIndex':["The Mahābhārata in Sanskrit: source note (BORI critical edition, Tokunaga/Smith) — sacred-texts.com","https://sacred-texts.com/hin/mbs/index.htm"],
 'ganSarabha':["Mahābhārata, Śānti Parva, Section CXVII, tr. K. M. Ganguli — sacred-texts.com","https://sacred-texts.com/hin/m12/m12a116.htm"],
 'sampathMysore':["Vikram Sampath, Splendours of Royal Mysore: The Untold Story of the Wodeyars (Rupa, 2008) — Internet Archive","https://archive.org/details/splendoursofroya0000vikr"]})
# prompts
modern=json.load(open(f'{ROOT}/prompts/modern.json'))
ep=json.load(open(f'{OLD}/epic/prompts.json')); epr=json.load(open(f'{OLD}/epic/prompts_run.json')); eretry=json.load(open(f'{ROOT}/prompts/epic-retry.json'))
STYLE=modern['05-gupta'].split('No human figures. ')[1]
def eprompt(no,img):
    if img in eretry: return eretry[img]
    if no in epr: v=epr[no]; return 'Create an image. '+(v if isinstance(v,str) else v[1])
    if no in ep: return 'Create an image. '+ep[no][1]
    return None
PV=json.load(open(f'{ROOT}/prompts/pandava.json'))
lq={a:(b,c) for a,b,c in json.load(open(f'{OLD}/later_q.json'))}
def slug(img): return re.sub(r'^[lm]?\d+[ab]?-','',img)
MOT={
 'lion':('Lion',['maurya','kadamba','vishnukundina','tripura','bhima']),
 'bull':('Bull',['magadha','kripa','pallava','maitraka','maukhari','pushyabhuti','gauda','eastern-ganga','shahi','chauhan']),
 'boar':('Boar (Varāha)',['jayadratha','chalukya','pratihara','kakatiya','vijayanagara']),
 'garuda':('Garuḍa',['krishna','gupta','panduvamshi','rashtrakuta','paramara']),
 'bird':('Peacock, swan and other birds',['vrishasena','shala','marwar','mysore','sahadeva','abhimanyu']),
 'elephant':('Elephant',['duryodhana','karna','shala','kamarupa','western-ganga','chaulukya','sharabhapuriya','yadava']),
 'fish':('Fish',['saindhava','pandya','chola']),
 'tiger':('Tiger',['chola','hoysala']),
 'goddess':('Lakṣmī and the goddess',['sharabhapuriya','kalachuri','gahadavala','karkota']),
 'gods':('Gods and avatars',['sena','pratihara']),
 'ape':('Ape and Hanumān',['arjuna','chandela']),
 'mythic':('Composite beasts',['ahom','nakula','mysore']),
 'sky':('Sun, moon and stars',['magadha-coin','bhishma','bhurishravas','mewar','sikh','yudhishthira','kshatrapa','vijayanagara']),
 'plant':('Tree, palm and furrow',['ikshvaku','bhishma','shalya']),
 'weapon':('Bow, sword and wheel',['drona','chera','chola','vijayanagara','ghatotkaca']),
 'ritual':('Altar, post, conch and sign',['drona','bhurishravas','travancore','satavahana','kushan','pala','yadava']),
 'flag':('Plain and coloured flags',['maratha','jaipur','marwar','pandava-colours']),
}
def motifs(i): return [k for k,(l,ids) in MOT.items() if i in ids]
def fix(e,o,fields):
    for f in fields:
        if f in o and o[f] is not None: e[f]=o[f]
        elif f in o and o[f] is None and f in ('warn',): e.pop(f,None)
    return e
cards=[]
# EPIC
eo={c['no']:c for c in outs['epic']['cards']}
for x in legacy['EPIC']:
    img=x.get('img') or ('02a-magadha-coin')
    i='magadha-coin' if x['no']=='2a' else ('magadha' if x['no']=='2b' else slug(img))
    o=eo[x['no']]
    e=dict(id=i,tab='itihasa',no=x['no'],n=x['n'],who=x['who'],e=o.get('e',x['e']),k='coin' if x['k']=='coin' else 'epic',
           img=f'epic/{img}.webp',san=o.get('san',x['san']),ref=o.get('ref',x['ref']),t=o['t'],motifs=motifs(i))
    if x['no']=='2a': e['t']=e['t'].replace(' Painted in JavaScript from the documented marks.','')
    pr=eprompt(x['no'],img)
    if pr: e['prompt']=pr
    if x['no']=='14': e['model']='Google Gemini'
    if x['no']=='2a': e['model']='Drawn in code from the documented punch marks'
    cards.append(e)
# PANDAVA (new)
B={b['who']:b for b in pv['banners']}
def gq(w): return B[w]['ganguli'].strip("'")
new=[
 dict(id='ghatotkaca',no='16',n='Rākṣasa ally',who='Ghaṭotkaca',e='Chariot-wheel',k='epic',san=B['Ghaṭotkaca']['san'],ref='Mahābhārata 7.22.60',
  t="Horses of many colours, with faces of many shapes, carried the hero Ghaṭotkaca, whose banner was a chariot-wheel.{mbs7022} The verse gives no material or colour for the wheel.{mbs7022} The vulgate text that Ganguli translated puts a vulture on his standard instead.{gan7023}"),
 dict(id='pandava-colours',no='17',n='Pāṇḍava allies',who='Kekayas, Śukla, Nīla, Citra and others',e='Banners known by colour',k='epic',
  san="ekavarṇena sarveṇa dhvajena kavacena ca / aśvaiś ca dhanuṣā caiva śuklaiḥ śuklo nyavartata",ref='Mahābhārata 7.22.49; also 7.22.11, 36, 54–56, 62',
  t="In the critical edition, Droṇa Parva 7.22 describes the Pāṇḍava host mostly by its horses, and names banners only by colour.{mbs7022}{mbsIndex} The five Kekaya brothers have red banners, the Prabhadraka Pāñcālas banners worked with gold, Śukla a banner as white as his armour, horses and bow, and Nīla one all blue.{mbs7022} Citra's banner is set with gems, Citrāyudha's is variegated, and the troops around Bhīma carry golden banners.{mbs7022} No device is named for any of them, so the painting shows plain banners in these colours.{mbs7022}"),
]
VUL=[('yudhishthira','Yudhiṣṭhira','Golden moon with planets','Yudhiṣṭhira'),('bhima','Bhīmasena','Silver lion with lapis eyes','Bhīmasena'),
     ('nakula','Nakula','Śarabha with a golden back','Nakula'),('sahadeva','Sahadeva','Silver swan with bells','Sahadeva'),('abhimanyu','Abhimanyu','Golden peacock','Abhimanyu')]
for idx,(i,who,lab,key) in enumerate(VUL):
    new.append(dict(id=i,no=str(18+idx),n='Pāṇḍava',who=who,e=lab,k='vulgate',san='',ref='Vulgate, Droṇa Parva 23 (Ganguli); not in the critical edition',
      quote=gq(key),t=f"Ganguli's translation, made from the vulgate text, describes this standard in Droṇa Parva section 23.{{gan7023}} The critical edition does not have the passage: its chapter 7.22 describes the Pāṇḍava warriors' horses and names no such device.{{mbs7022}}{{mbsIndex}}",warn='Vulgate only, not in the critical edition'))
new[-1]['t']+=" Ganguli renders the bird as a peacock; the vulgate Sanskrit has not been checked here.{gan7023}"
for e in new:
    if e['id']=='nakula':
        e['t']+=" The standard names only a śarabha with a golden back. The painting follows the epic's own description of the śarabha in the Śānti Parva: a beast that kills lions, with eight legs and eyes on the top of its head.{ganSarabha}"

for e in new:
    e.update(tab='itihasa',img=f"epic/{e['id']}.webp",motifs=motifs(e['id']))
    if not __import__('os').path.exists(f"{ROOT}/epic/{e['id']}.webp"): e['pending']=True
    e['prompt']=PV.get(e['id'])
cards.extend(new)
# EARLY
eao={c['n']:c for c in outs['early_a']['cards']+outs['early_b']['cards']}
for x in legacy['D']:
    o=eao[x['n']]; i=slug(x['img'])
    e=dict(id=i,tab='early',n=x['n'],d=o.get('d',x['d']),r=x['r'],k=o.get('k',x['k']),e=o.get('e',x['e']),nat=x['nat'],nc=x['nc'],
           img=f"modern/m{x['img']}.webp",t=o['t'],motifs=motifs(i))
    pr=modern.get(x['img'])
    if pr: e['prompt']=pr
    cards.append(e)
# LATER
lo={c['n']:c for c in outs['later']['cards']}
for x in legacy['LATER']:
    o=lo[x['n']]; i=slug(x['img'])
    e=dict(id=i,tab='later',n=x['n'],d=o.get('d',x['d']),r=x['r'],k=o.get('k',x['k']),e=o.get('e',x['e']),nat=x['nat'],nc=x['nc'],
           img=f"later/{x['img']}.webp",t=o['t'],motifs=motifs(i))
    if o.get('warn'): e['warn']=o['warn']
    if x.get('flag'):
        f=dict(legacy['FLAGS'][x['flag']]); 
        if o.get('flagCap'): f['cap']=o['flagCap']
        e['flag']=f
    q=lq.get(x['img'])
    if q: e['brief']=q[0]+' '+q[1]
    if i=='mysore': e['read']=['sampathMysore']
    cards.append(e)
# Kadamba: lion is not on Banavasi coins -> tradition
for e in cards:
    if e['id']=='kadamba': e['k']='tradition'; e['warn']='Emblem known from later tradition; not on Banavāsi coins'
# evidence photos: Wikimedia Commons files, checked by eye; see tools/evidence_meta.json
EVM=json.load(open(f'{ROOT}/tools/evidence_meta.json')); EVC=json.load(open(f'{ROOT}/tools/evidence_captions.json'))
import os
for e in cards:
    if e['id'] in EVC and os.path.exists(f"{ROOT}/evidence/{e['id']}.webp"):
        m=EVM[e['id']]; art=re.sub(r'\s+',' ',m['art'] or '').strip()
        art=re.sub(r'\(uploader\)|Unknown author|\(talk\)|\(Uploads\)|User:','',art).strip() or ('Los Angeles County Museum of Art' if e['id']=='chola' else 'Unknown author')
        e['ev']=dict(img=f"evidence/{e['id']}.webp",caption=EVC[e['id']],file=m['page'],credit=f"{art[:60]} · {m['lic']}",licurl=m.get('licurl'))
# evidence candidates (unverified until checked)
ev={}
for o in outs.values():
    for c in o['cards']:
        if c.get('evidence'):
            ev[c.get('n') or c.get('no')]=c['evidence']
json.dump(ev,open(f'{SC}/evidence_candidates.json','w'),ensure_ascii=False,indent=1)
# check citations
used=set()
for e in cards:
    for k in re.findall(r'\{(\w+)\}',e['t']): used.add(k)
missing=[k for k in used if k not in S]
if missing: sys.exit('missing sources: '+str(missing))
SRC={k:S[k] for k in sorted(used|{'sampathMysore'})}
MOTIFS={k:v[0] for k,v in MOT.items()}
ids=[e['id'] for e in cards]; assert len(ids)==len(set(ids)),[i for i in ids if ids.count(i)>1]
for k,(l,lst) in MOT.items():
    for i in lst: assert i in ids,(k,i)
out='/* Lāñchhana Register data. Text uses {key} after a sentence to cite SRC[key]. */\n'
out+='window.LR='+json.dumps(dict(SRC=SRC,MOTIFS=MOTIFS,STYLE=STYLE,cards=cards),ensure_ascii=False,indent=0)+';\n'
open(f'{ROOT}/data.js','w').write(out)
print(len(cards),'cards',len(SRC),'sources',len(ev),'evidence candidates')
