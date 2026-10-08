"""Append the Delhi Sultanate + Mughal cards from /tmp/claude-0/newcards into data.js (idempotent)."""
import json,subprocess,os,shutil
from PIL import Image
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); N='/tmp/claude-0/newcards'
LR=json.loads(subprocess.check_output(['node','-e',f"global.window={{}};require('{ROOT}/data.js');console.log(JSON.stringify(window.LR))"]))
ORIG=open(f'{ROOT}/data.js').read(); TAIL=ORIG[ORIG.index('\n/* approximate reign'):]
cards=json.load(open(f'{N}/cards.json'))
SRC={}
for f in ['mamluk_khalji','tughluq_sur','mughal']: SRC.update(json.load(open(f'{N}/{f}.json'))['SRC'])
M=[c for c in cards if c['id'].startswith('mughal-')]; cards=[c for c in cards if not c['id'].startswith('mughal-')]
names={'mughal-akbar':'Akbar (1556–1605)','mughal-jahangir':'Jahāngīr (1605–1627)','mughal-aurangzeb':'Aurangzīb (1658–1707)'}
mg={'id':'mughal','tab':'later','n':'Mughal Empire','d':'1556–1707 CE','r':'North','k':'coin','e':'Akbar\'s formula, Jahāngīr\'s zodiac coins, Aurangzīb\'s couplets','nat':'','nc':'',
 'motifs':['bull','sky'],'t':' '.join(f"{names[c['id']]}: {c['t']}" for c in M),
 'brief':'three medallions: '+' | '.join(c['brief'] for c in M),'prompt':'Composite of three single-emblem medallions (Akbar, Jahāngīr, Aurangzīb), see mughal-akbar/jahangir/aurangzeb prompts in earlier drafts.',
 'review':' '.join(f"{names[c['id']]}: {c['review']}" for c in M)}
cards.append(mg)
IMG={'mamluk':'l19-mamluk','khalji':'l20-khalji','tughluq':'l21-tughluq','sayyid':'l22-sayyid','lodi':'l23-lodi','sur':'l24-sur','mughal':'l25-mughal'}
have={c['id'] for c in LR['cards']}
for c in cards:
    if c['id'] in have: continue
    shutil.copy(f'{N}/{c["id"]}.webp',f'{ROOT}/later/{IMG[c["id"]]}.webp'); c['img']=f'later/{IMG[c["id"]]}.webp'
    ev=c.get('ev')
    if ev:
        p=f'/mnt/user-data/uploads/Downloads/ev_{c["id"]}.jpg'
        if os.path.exists(p):
            im=Image.open(p).convert('RGB'); im.thumbnail((800,800)); im.save(f'{ROOT}/{ev["img"]}',quality=82)
        else: del c['ev']; print('no ev photo for',c['id'])
    for k in ('prompt',):
        c.setdefault(k,'')
    LR['cards'].append(c); print('added',c['id'])
LR['SRC'].update(SRC)
LR['LEFTOUT']['mughal-flag']='<b>Mughal flag, crest and lion-and-sun.</b> The Āʾīn-i Akbarī (I.19) lists the imperial ensigns (throne, parasol, standards) but the text read gives no colour or device for any of them; no scholarly or period source for a fixed Mughal state flag or crest was found, so none is carded.'
LR['LEFTOUT']['mughal-couplet']='<b>Aurangzīb\'s coin couplet.</b> The couplet quoted in popular accounts is not printed in the Elliot &amp; Dowson passage read, so its wording is not given.'
span={'mamluk':[1206,1290],'khalji':[1290,1320],'tughluq':[1320,1414],'sayyid':[1414,1451],'lodi':[1451,1526],'sur':[1540,1555],'mughal':[1556,1707]}
HEAD='/* Lāñchhana Register data. Text uses {key} after a sentence to cite SRC[key]. */\nwindow.LR='
T=TAIL
import re
for k,v in span.items():
    if f'"{k}":' not in T: T=T.replace('"travancore": [1729, 1949]',f'"travancore": [1729, 1949], "{k}": {json.dumps(v)}')
open(f'{ROOT}/data.js','w').write(HEAD+json.dumps(LR,ensure_ascii=False,indent=0)+';\n'+T)
