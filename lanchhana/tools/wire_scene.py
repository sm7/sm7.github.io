#!/usr/bin/env python3
"""wire_scene.py <card-id> <kind> <webp> [--append-conj TEXT]
Merges a draft item (from /tmp/claude-0/drafts/<id>.json) into scenes/<id>/scenes.json, copies image."""
import json,sys,shutil,os
cid,kind,webp=sys.argv[1:4]
extra=sys.argv[5] if len(sys.argv)>5 and sys.argv[4]=='--append-conj' else ''
d=json.load(open(f'/tmp/claude-0/drafts/{cid}.json'))
it=[x for x in d['items'] if x['k']==kind][0]
it={k:v for k,v in it.items() if k!='prompt'}
if extra: it['conjecture']=it['conjecture'].rstrip()+' '+extra
os.makedirs(f'scenes/{cid}',exist_ok=True)
dst=f'scenes/{cid}/{kind}.webp'; shutil.copy(webp,dst); it['img']=dst
p=f'scenes/{cid}/scenes.json'
s=json.load(open(p)) if os.path.exists(p) else {'id':cid,'heading':d['heading'],'items':[]}
s['items']=[x for x in s['items'] if x['k']!=kind]+[it]
order={'city':0,'street':1,'temple':2}
s['items'].sort(key=lambda x:order.get(x['k'],-1))
json.dump(s,open(p,'w'),ensure_ascii=False,indent=1)
print('wired',cid,kind,[x['k'] for x in s['items']])
