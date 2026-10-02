"""Scholarly re-sourcing pass (Oct 2026): replaces Wikipedia, dealer, blog, news and portal citations
with papers, books, epigraphic editions and museum records whose passages were read; drops entries
whose emblem has no scholarly attestation; flags entries still awaiting a readable scholarly source."""
import json, re, subprocess
ROOT='/home/claude/sm7.github.io/lanchhana'
SC='/tmp/claude-0/-home-claude-sm7-github-io/997c0891-c63e-51d7-a902-fd3eed4555e9/scratchpad/src2'
LR=json.loads(subprocess.check_output(['node','-e',f"global.window={{}};require('{ROOT}/data.js');console.log(JSON.stringify(window.LR))"]))
SRC=LR['SRC']; cards=LR['cards']; BY={c['id']:c for c in cards}
out={}
NEWSRC={}
for g in ['early_a','early_b','later_a','later_b']:
    d=json.load(open(f'{SC}/out_{g}.json')); NEWSRC.update(d['sources'])
    for c in d['cards']: out[c['id']]=c
for f in ['pass2_early','pass2_south','pass2_later']:
    NEWSRC.update(json.load(open(f'{SC}/{f}.json'))['sources'])
for k in ['gahUnverified','none','mewUnverified','hansIndiaLEAD','borgohain2022quest']: NEWSRC.pop(k,None)
NEWSRC['brownCoins']=["C. J. Brown, The Coins of India (1922), keys to Plates V–VI — Project Gutenberg","https://www.gutenberg.org/ebooks/75542"]
NEWSRC['brown']=NEWSRC['brownCoins']
NEWSRC['asherSarnath'][0]="Frederick M. Asher, 'Lion capital, Sarnath Museum', Asher Collection, American Institute of Indian Studies — VMIS"
NEWSRC['borgohain2023'][0]="T. Borgohain & K. Bhuyan, 'A Study on the Tai-Ahom Dragon Ngi Ngao Kham', IJRAR 10(1) (2023), pp. 461–463 (low-impact journal)"
SRC.update(NEWSRC)

REVIEW="A readable scholarly source for this emblem has not yet been found. The emblem is shown as it is usually given, pending that check."
T={}  # text overrides
for i in ['maurya','satavahana','kushan','kshatrapa','kamarupa','western-ganga','pallava','maukhari','chalukya','pushyabhuti',
          'gauda','karkota','panduvamshi','eastern-ganga','pratihara','pala','paramara','kalachuri','shahi',
          'hoysala','kakatiya','yadava','sena','chandela','chauhan','jaipur','vijayanagara','maratha','sikh','travancore']:
    T[i]=out[i]['text']
T['maurya']=T['maurya'].replace(" The painting shows three of the four lions, over a wheel and the horse.","")+" The painting shows three of the four lions, over a wheel and the horse."
T['gupta']=out['gupta']['text']+" The revised Corpus of Gupta inscriptions lists a copper-silver seal of Kumāragupta III from Bhitarī.{cii3rev_toc} On the Nālandā clay seal of Viṣṇugupta, Garuḍa is flanked by the sun and the crescent.{cii3rev_no48}"
T['vishnukundina']="Viṣṇukuṇḍin coins show a lion in a circle on the obverse, and on the reverse a conch (śaṅkha) flanked by lampstands inside a rayed circle.{vijayakumar1987} Their coinage followed the motifs of Pallava coins, which carry a bull or a lion.{rathAnimal}"
T['sharabhapuriya']="Śarabhapurīya seals show the goddess Lakṣmī standing on a lotus, bathed with water poured from vessels held up by an elephant on either side, with a two-line verse legend naming the king below.{pradhan2011} Their gold repoussé coins show a standing Garuḍa with spread wings, flanked by a crescent and a wheel on one side and the sun and a conch on the other.{sarkar2020}"
T['chola']="On the seal of the Velañjeri plates of Parāntaka I, two fish and a seated tiger rest on a bow, flanked by two lampstands and topped by a parasol and two fly-whisks, with a Sanskrit legend.{nagaswamyVelanjeri} The Los Angeles County Museum of Art holds the seal of a copper-plate charter of Rājendra I (1012–1044), with an inscribed band round the rim.{lacmaSeal} Coins of Uttama Chola show the tiger seated under a canopy facing a pair of fish; the bow joins the group on the coins of Rājendra I.{chennaiChola}"
T['pandya']="The special cognizance of the Pāṇḍyas was the fish, in various combinations.{jackson} Between the 7th and 10th centuries their coins bear the fish, sometimes single and sometimes in a pair.{chennaiIntro} Some coins show two fishes with a sceptre or an inscription between them.{jackson} Later Pāṇḍya copper-plate seals have the fish in the centre, flanked by the tiger and the bow.{aiyerEI27}"
T['chera']="The cognizance of the Cheras was a bow.{jackson} Chera coins of the early historic period carry a bow and arrow on the reverse.{nmDelhiSangam} On the Kollippurai copper coin from Karur, the prominence of the bow is what identifies it as Chera.{nagaswamyKolli}"
T['ahom']="The earliest known Ahom coin is dated 1648 and was issued by Jayadhvaja Siṃha.{dutta2019} Ahom coins were struck on octagonal blanks, with legends generally in Assamese-Bengali characters.{dutta2019} The ngi-ngao-kham, a dragon-lion of Tai-Ahom belief, is described as the royal emblem, as carved on the Kareng Ghar, Rang Ghar and Talatal Ghar, and as painted on the war flag called the khring fra, only in short papers in low-impact journals that cite no earlier evidence.{borgohain2023}"
T['tripura']="Ratna Māṇikya (1464–1489) struck the first Tripura silver coins in his own name.{dutta2019} A lion is the usual device on Tripura coins, and later Krishna-type coins show the flute-playing god standing above the Tripura lion.{triSarma}{dutta2019}"
T['mysore']="The gaṇḍabheruṇḍa, a two-headed bird, is described as the royal insignia of Mysore.{srikantaSastri} When the Woḍeyars adopted it has not yet been checked against a scholarly source."
T['mewar']="Tod records that the audience hall of the Udaipur palace was called the Sūrya Mahal, the hall of the sun, after a sun medallion in relief on its wall.{tod1829_bk4ch18} A scholarly account of the sun as the Mewar royal device or on its standard has not yet been checked."
T['gahadavala']="The seated four-armed goddess on gold coins was struck by the Kalachuri Gāṅgeyadeva and by the Chandela Hallakṣaṇavarman.{brownCoins} Govindacandra's coins of this type have not yet been checked against a scholarly catalogue."
T['maitraka']="Maitraka grants carry the dynasty's seal, usually described with a seated bull above the legend 'Śrī-Bhaṭakkaḥ'. That description has not yet been checked against a readable edition."
T['rashtrakuta']="Garuḍa is usually given as the Rāṣṭrakūṭa seal emblem, but no edition describing it could yet be read. The seal of the early Rāṣṭrakūṭa plates from Jamkhed carries only a short inscription, with no recognisable picture.{balogh2014}"
REVIEWED={'maitraka','rashtrakuta','gahadavala','mewar','mysore','ahom'}
DROP={'kadamba':"<b>Kadamba of Banavāsi.</b> The lion often given as their emblem is attested on the coins of the later Kadambas of Goa, not on those of Banavāsi.",
      'saindhava':"<b>Saindhava of Ghumli.</b> The fish emblem given in popular sources was not found in any scholarly edition of their grants.",
      'chaulukya':"<b>Chaulukya (Solaṅkī) of Gujarat.</b> The charging-elephant coins are attributed to Jayasiṃha Siddharāja only by dealers; no scholarly attribution of a coin type or seal was found.",
      'marwar':"<b>Rāṭhoṛ of Marwar.</b> Tod names the clan goddess as winged, but no scholarly or period source describing the Jodhpur flag or a bird on it was found."}
EV={'kshatrapa':"The usual reverse of their silver coins is a three-arched hill"}
REPAINT={
 'kshatrapa':"the Western Kṣatrapa coin reverse: a hill of three arches stacked like a pyramid (one arch on top of two), with a wavy line beneath it, a small crescent moon to the LEFT of the hill and a small rayed sun to the RIGHT, in silver relief. No crescent on top of the hill.",
 'gupta':"Garuḍa, the divine eagle of Viṣṇu, facing front with both wings spread wide and a bird's hooked beak, flanked by a small sun on one side and a crescent moon on the other, as on a Gupta royal seal. No serpent, no crown.",
 'sharabhapuriya':"the goddess Lakṣmī STANDING on a lotus, frontal, while an elephant on either side holds up a water-vessel in its trunk and pours water over her, as on Śarabhapurīya royal seals.",
 'chalukya':"a wild boar (varāha) running in profile, bristles along the back and tusks showing, with a small sun and a crescent moon above it on either side and two fly-whisks (chauris), as on a Chalukya grant seal.",
 'paramara':"Garuḍa flying to the right in HUMAN form: a crowned human figure with a beak-like nose, wings springing from the shoulders, holding a hooded cobra in his left hand and raising his right hand to strike it, as engraved on Paramāra copper plates.",
 'kakatiya':"a humped bull couchant (lying down, legs folded) in profile, between two standing lamp-stands (candelabra), with a small royal umbrella above it.",
 'yadava':"the Yādava gold padmaṭaṅka device: a large eight-petalled lotus at the centre of a cup-shaped gold disc, surrounded by small separate punch-marks: a conch and the syllable 'Śrī'. No elephant.",
 'chandela':"a four-armed goddess seated frontally, cross-legged, as on Chandela gold drammas, rendered in gold.",
 'jaipur':"the Jaipur panchrangā: a single flag of five horizontal coloured stripes (red, yellow, white, green, blue) on a short golden staff, with no small second flag above it.",
 'vijayanagara':"the Vijayanagara seal device: a wild boar standing in profile, with a crescent moon and a rayed sun above it. No sword.",
 'sikh':"a single stylised leaf with veins and a short stalk, as stamped on Sikh rupees of Ranjit Singh's reign, in silver.",
 'travancore':"a single conch shell (śaṅkha) in silver-white, shown upright, as on Travancore silver chakrams. No garland and no crescent.",
}
LABEL={'kakatiya':"Couchant bull between candelabra",'yadava':"Lotus punch coin (padmaṭaṅka)",'chandela':"Seated four-armed goddess",
 'vijayanagara':"Boar with sun and moon",'sikh':"Leaf mark of the Khalsa rupee",'travancore':"Conch (śaṅkha)",'sharabhapuriya':"Gajalakṣmī",
 'kshatrapa':"Three-arched hill with sun and crescent",'paramara':"Flying Garuḍa in human form, with cobra",'chola':"Seated tiger, two fish and bow",
 'gauda':"Nandi with the moon",'kamarupa':"Elephant",'western-ganga':"Elephant"}
KIND={'vijayanagara':'seal','sikh':'coin','travancore':'coin','mysore':'tradition','mewar':'tradition','kakatiya':'coin'}
WARN={'kakatiya':"Jackson (1912) gives a couchant bull; the boar and Garuḍa named in later writing have not yet been checked",
      'tripura':"The lion as the standard device rests on Sarma's catalogue index",
      'ahom':"Emblem and flag rest only on low-impact journal papers",
      'yadava':None,'chandela':"The Hanumān copper coins often cited have not yet been checked",
      'vijayanagara':None,'kshatrapa':None,'sikh':None,'travancore':None,'jaipur':None,'mysore':None,'mewar':None}
FLAGDROP={'sikh','travancore','mysore','mewar','ahom'}
FLAGCAP={'jaipur':"Panchrangā, the five-coloured flag of Amber, recorded by Lethbridge (1893).",
         'maratha':"Bhagwā jhenḍā: deep orange and swallow-tailed, as Grant Duff (1826) describes it."}
for c in cards:
    i=c['id']
    if i in T: c['t']=T[i]
    if i in LABEL: c['e']=LABEL[i]
    if i in KIND: c['k']=KIND[i]
    if i in WARN:
        if WARN[i]: c['warn']=WARN[i]
        else: c.pop('warn',None)
    if i in REVIEWED: c['review']=REVIEW
    else: c.pop('review',None)
    if i in FLAGDROP: c.pop('flag',None)
    if i in FLAGCAP and c.get('flag'): c['flag']['cap']=FLAGCAP[i]
    if i=='jaipur' and c.get('flag'):
        c['flag']['svg']=''.join(f'<rect x="2" y="{2+n*7.2}" width="56" height="7.2" fill="{col}"/>' for n,col in enumerate(["#c8102e","#f2c200","#ffffff","#2e8b3a","#1f4fa0"]))
    if i in REPAINT: c['repaint']=REPAINT[i]
    if i=='kadamba': c.pop('ev',None)
# epic: drop Wikipedia citations
for c in cards:
    if c['id']=='ikshvaku':
        c['t']=re.sub(r"\s*The verse names only the tree;.*$","",c['t'])+" The verse names only the tree.{ram}"
    if c['id']=='magadha-coin':
        c['t']="The Purāṇic king-lists of Magadha name these kings but give no emblems.{parg} Their silver punch-marked coins carry several separately punched marks; the five shown here, with a sun and a six-armed sign, are illustrative."
        c['review']="The description of the punch marks has not yet been checked against a scholarly catalogue."
# motifs follow the new paintings
def setm(i,ms): BY[i]['motifs']=ms
setm('kakatiya',['bull']); setm('chandela',['goddess']); setm('vijayanagara',['boar','sky']); setm('sikh',['plant'])
setm('yadava',['ritual']); setm('gupta',['garuda','sky']); setm('chalukya',['boar','sky']); setm('kshatrapa',['sky','ritual'])
dropped=[c for c in cards if c['id'] in DROP]
cards=[c for c in cards if c['id'] not in DROP]
used=set()
for c in cards:
    used|=set(re.findall(r'\{(\w+)\}',c['t'])); used|=set(c.get('read',[]))
missing=[k for k in used if k not in SRC]
assert not missing, missing
WEAK=re.compile(r'wikipedia|mintageworld|numista|blogspot|fotw|crwflags|indianetzone|iasgyan|thehansindia|deccanchronicle|outlook|worldhistory|sikhnet|coinindia\.com/galleries|virasat|spink|sarmaya|indica\.today|livehistoryindia|puratattva|monidipa|braintor|arvindsinghmewar|inhcrf|x\.com',re.I)
weak=[(k,SRC[k][1]) for k in used if WEAK.search(SRC[k][1]) and k not in ('tandon2014',)]
print('weak still used:',weak)
LR['SRC']={k:SRC[k] for k in sorted(used)}; LR['cards']=cards
LR['LEFTOUT']=DROP
open(f'{ROOT}/data.js','w').write('/* Lāñchhana Register data. Text uses {key} after a sentence to cite SRC[key]. */\nwindow.LR='+json.dumps(LR,ensure_ascii=False,indent=0)+';\n')
print(len(cards),'cards;',len(LR['SRC']),'sources; dropped',list(DROP)); print('repaint:',[c['id'] for c in cards if c.get('repaint')])
