"""Convert a ChatGPT emblem PNG (square, medallion on plain ground) into the site's 640px circular RGBA webp.
Usage: emblem_to_webp.py <in.png> <out.webp> [radius_fraction=0.492]"""
import sys
from PIL import Image, ImageDraw
src,dst=sys.argv[1],sys.argv[2]; r=float(sys.argv[3]) if len(sys.argv)>3 else 0.492
im=Image.open(src).convert('RGB'); W=im.width
S=4; m=Image.new('L',(W*S,W*S),0); ImageDraw.Draw(m).ellipse([W*S*(0.5-r),W*S*(0.5-r),W*S*(0.5+r),W*S*(0.5+r)],fill=255)
m=m.resize((W,W),Image.LANCZOS); im.putalpha(m)
c=im.crop((int(W*(0.5-r)),int(W*(0.5-r)),int(W*(0.5+r))+1,int(W*(0.5+r))+1)).resize((640,640),Image.LANCZOS)
c.save(dst,quality=90)
