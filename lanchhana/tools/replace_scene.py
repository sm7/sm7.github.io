#!/usr/bin/env python3
"""Replace an existing scene image and thumbnails; optionally patch its notes.
usage: replace_scene.py <card> <kind> <webp> [--conj-replace OLD NEW] [--conj-append TEXT]
Run from lanchhana/. Afterwards run tools/add_scenes.py and bump the ?v= image cache param in register.html."""
import sys,json,shutil
from PIL import Image
a=sys.argv[1:]; cid,kind,webp=a[0],a[1],a[2]
dst=f'scenes/{cid}/{kind}.webp'; shutil.copy(webp,dst)
im=Image.open(dst).convert('RGB')
for w in (480,960):
    im.resize((w,round(im.height*w/im.width)),Image.LANCZOS).save(dst[:-5]+f'-{w}.webp',quality=80,method=6)
p=f'scenes/{cid}/scenes.json'; s=json.load(open(p))
it=[x for x in s['items'] if x['k']==kind][0]
i=3
while i<len(a):
    if a[i]=='--conj-replace':
        assert a[i+1] in it['conjecture'], 'old text not found'
        it['conjecture']=it['conjecture'].replace(a[i+1],a[i+2]); i+=3
    elif a[i]=='--conj-append':
        it['conjecture']=it['conjecture'].rstrip()+' '+a[i+1]; i+=2
    else: raise SystemExit('bad arg '+a[i])
json.dump(s,open(p,'w'),ensure_ascii=False,indent=1)
print('replaced',cid,kind,im.size)
