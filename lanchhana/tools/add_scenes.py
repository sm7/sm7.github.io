"""Merge scenes/<id>/scenes.json into data.js as card.scenes. Run from anywhere: python3 tools/add_scenes.py"""
import json,subprocess,glob,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LR=json.loads(subprocess.check_output(['node','-e',f"global.window={{}};require('{ROOT}/data.js');console.log(JSON.stringify(window.LR))"]))
ORIG=open(f'{ROOT}/data.js').read(); TAIL=ORIG[ORIG.index('\n/* approximate reign'):] if '\n/* approximate reign' in ORIG else ''
BY={c['id']:c for c in LR['cards']}
for f in sorted(glob.glob(f'{ROOT}/scenes/*/scenes.json')):
    s=json.load(open(f)); c=BY[s['id']]
    for it in s['items']:
        assert os.path.exists(f"{ROOT}/{it['img']}"), it['img']
        assert all(it.get(k) for k in ('title','alt','attested','prescribed','conjecture')), it['k']
    c['scenes']={'heading':s['heading'],'items':s['items']}; print('scenes ->',s['id'],len(s['items']))
HEAD='/* Lāñchhana Register data. Text uses {key} after a sentence to cite SRC[key]. */\nwindow.LR='
open(f'{ROOT}/data.js','w').write(HEAD+json.dumps(LR,ensure_ascii=False,indent=0)+';\n'+TAIL)
