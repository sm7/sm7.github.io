"""Curated scene texts for Sultanate/Sur/Mughal cards. Usage: sultanate_scenes.py <card> <kind> <png>  (writes webps + scenes.json item)"""
import json,sys,os
from PIL import Image
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ED2='Elliot & Dowson, History of India, vol. II'; ED3='Elliot & Dowson, History of India, vol. III'
ED4='Elliot & Dowson, History of India, vol. IV'; ED5='Elliot & Dowson, History of India, vol. V'
NOSEC='No scholarly account (e.g. Jackson, Kumar, Asher, Habib, Digby) could be read as an open text, so none is relied on here.'
H={
'mamluk':'Setting · Delhi under Iltutmish, c. 1229–1237 CE',
'khalji':'Setting · Siri and Delhi under ʿAlāʾ al-Dīn, c. 1303–1311 CE',
'tughluq':'Setting · Firozabad under Fīrūz Shāh, c. 1354–1388 CE',
'sayyid':'Setting · Mubārakābād on the Yamuna, 1433 CE',
'lodi':'Setting · Agra and the markets under Sikandar Lodī, 1504 CE',
'sur':'Setting · Delhi and the royal road under Sher Shāh, c. 1540–1545 CE',
'mughal':'Setting · Agra under Akbar, c. 1565–1573 CE',
}
S={}
S[('mamluk','city')]=dict(label='City',title='Delhi of the slave-sultans: the Qutb mosque precinct, the Jāmiʿ Masjid quarter and the royal kūshks',
alt='Hypothetical reconstruction of Delhi c. 1230: the Quwwat-ul-Islām mosque with its great arched screen and a red-sandstone minaret, a small domed tomb, a walled town and a dusty road with carts and camels',
attested='Iltutmish took the throne of Delhi in 607 H. (1210); his chief palace was the Kushk-i Fīrūzī, and a Jāmiʿ Masjid with a gate called the Muʿizzī stood in the city, with the clothes bazaar on one approach to it (Minhāj-i Sirāj, in '+ED2+', pp. 332–336). The Qutb group has Aibak\'s Quwwat-ul-Islām mosque with its great arched screen dated 1199 and the minar begun by Aibak and completed by Iltutmish; the mosque was built from the materials of demolished Hindu temples, with columns of different temples set one upon another; Iltutmish extended the mosque and screen, using plainer columns because the supply of carved columns had given out; a square red-sandstone tomb with a dome on squinches, banded with Qurʾānic inscription, stands in the precinct (J. A. Page, A Guide to the Qutb, ASI, 1938, pp. 1–23).',
prescribed='Page gives the only physical reconstruction read, a conjectural perspective of the mosque as it stood c. 1315, and says himself that his central bay rests on corbel and lintel fragments, not on a text. '+NOSEC,
conjecture='The wall circuit and gates of the town, the street plan, house forms (shown as flat-roofed rubble and lime-plaster houses), the position of the Jāmiʿ Masjid relative to the Qutb precinct, the form of the Kushk-i Fīrūzī (not shown separately), the minaret shown at four storeys, dress (Turkish nobles in coats and caps, townspeople in wrapped cloths), animals and carts. The painter\'s view of the minaret and screen follows the surviving monument, which was restored in later centuries.')
S[('mamluk','street')]=dict(label='Bazaar',title='The clothes bazaar by the Jāmiʿ Masjid: a documented gap',
alt='Hypothetical reconstruction of a thirteenth-century Delhi cloth bazaar beside a red-sandstone mosque gateway, with cloth merchants, porters, bullock carts and Turkish horsemen',
attested='Only two facts survive in the sources read: a clothes bazaar lay on one approach to the Jāmiʿ Masjid of Delhi, and in the riot there on 6 Rajab 634 H. (March 1237) the crowd gathered at that mosque (Minhāj-i Sirāj, in '+ED2+', p. 336); Rukn al-Dīn is said to have scattered gold through the streets and bazaars (p. 332). Nothing describes stalls, goods or traders.',
prescribed=NOSEC,
conjecture='Everything shown: the shop fronts, the stuffs on display, the people, the awnings and the mosque gateway. This scene is a painter\'s sketch of what a cloth bazaar of the period may have looked like, not a reconstruction from evidence.')
S[('khalji','city')]=dict(label='City',title='Siri and Delhi under ʿAlāʾ al-Dīn: the palace-city, the enlarged Jāmiʿ Masjid and the granaries',
alt='Hypothetical reconstruction of Delhi c. 1305: a rubble fort wall with round bastions and a pointed gateway, a pillared hall, a great mosque with an unfinished minaret under bamboo scaffolding, a tank with a domed pavilion and vaulted granaries',
attested='ʿAlāʾ al-Dīn entrenched his camp at Siri during the Mongol siege, then built a palace there and made it his capital; the fort of Siri was finished and became a populous place; he had the fort of Delhi repaired; three or four royal granaries in the city were always full (Baranī, in '+ED3+', pp. 160, 191, 200). Amīr Khusraw says he added a fourth court with lofty pillars to the Jāmiʿ Masjid, planned a second minar of double the circumference, with stone dug from the hills and from demolished temples, and cleaned the tank of Shamsu-d-dīn and \'erected a dome in the middle of it\' (pp. 69–70). The Alai Darwaza (inscribed 1311) is a square chamber of red sandstone with marble bands, horse-shoe arches and a plain dome, and only the first stage of his great minar was raised (Page, Guide to the Qutb, pp. 1–23).',
prescribed='Page offers a conjectural reconstruction of the mosque with the ʿAlāʾī additions, c. 1315. '+NOSEC,
conjecture='The circuit and bastions of Siri\'s wall, the form of the Red Palace and of the Hazār-sutūn (named, not described), the layout of the town, the granary buildings (shown as vaulted brick stores), the form of the tank\'s dome, the scaffolding, the soldiers\' dress (mail and lamellar), and the crowd. The sources also record the tower of Mongol heads at the Badaun gate; it is not shown.')
S[('khalji','street')]=dict(label='Bazaar',title='The regulated market: grain dealers, carriers and the inspector\'s scales',
alt='Hypothetical reconstruction of a regulated Delhi market c. 1305: bullock carts unloading grain, dealers with scales, a market inspector with a staff and balance, stalls of caps, shoes and combs, and mounted officials',
attested='ʿAlāʾ al-Dīn fixed grain prices by regulation; the market controller went round the markets with horse and foot, deputies and spies; the royal granaries held grain that was sold at the fixed rate when rains failed; all carriers (kārawāniyān, banjāras) were placed under the market controller and settled in villages on the Jumna; hoarding was forbidden; prices were also fixed for things sold at the stalls, \'from caps to shoes, from combs to needles\'; the Sultan tested sellers by sending boys to buy bread, which was then weighed before him (Baranī, in '+ED3+', pp. 192–197). The cloth, horse and cattle regulations are replaced by asterisks in this translation.',
prescribed='No scholar\'s account could be read. '+NOSEC,
conjecture='The market\'s physical setting (an open square with rubble and lime-plaster shop fronts and cloth awnings; no source gives a site), the shape of the scales and weights, the sacks and baskets, the dress of traders and officials, the number of people and the mosque, granary and gateway in the distance. The sources also describe the sale of slaves and a punishment for short weight; neither is shown.')
S[('tughluq','city')]=dict(label='City',title='Firozabad: the Sultan\'s new city beside the Jumna',
alt='Hypothetical reconstruction of Firozabad c. 1370: a walled palace and mosque complex of battered rubble masonry above a river landing with cargo boats, and a tall polished sandstone pillar with a gilded cupola on a stepped base',
attested='Firozabad was founded on the Jumna at the village of Gawin, five kos from Delhi; a new town took in eighteen named places; there were eight public mosques, each for 10,000 worshippers; the Delhi road swarmed with people, with carriages, mules, horses and palanquin-bearers for hire (ʿAfīf, in '+ED3+', pp. 302–303). The Kushk-i shikār had stone minarets and the Kushk-i nuzūl had domes bearing verses in gold letters (p. 316). The Ashokan pillar from Tobra came down the Jumna by boat; a building of stone and chunam was raised in stages near the Jāmiʿ Masjid to receive it, with black-and-white friezes round its capitals and a gilded copper cupola called kolas, 32 gaz long with 24 visible (pp. 351–352). The Sultan laid out 1,200 gardens near Delhi (p. 345). In his own memoir he says he had painted pictures on palace doors and walls effaced and limited gold braid on garments to four inches (Futūḥāt-i Fīrūz Shāhī, in '+ED3+', pp. 382–383).',
prescribed='No scholarly account was read, and nothing is taken from the ruins at Kotla Fīrūz Shāh, whose upper storeys are not evidence for the original. '+NOSEC,
conjecture='All building forms (the texts give names, counts and the pillar\'s height but no shapes): the palace blocks, the mosques and domes, the form of the pillar\'s base and cupola, the plaster colour, the river width, the garden layout, plain long coats and caps (following the Sultan\'s own dress restraint), the boats, the people and the cypresses.')
S[('tughluq','street')]=dict(label='Bazaar',title='A bazaar in the plentiful years of Fīrūz Shāh: documented prices, undocumented stalls',
alt='Hypothetical reconstruction of a Delhi street market c. 1370: rubble shop fronts with awnings, grain in sacks on scales, a fruit seller with grapes, a cloth merchant, a moneychanger, porters, a mule and an ox-cart',
attested='ʿAfīf records wheat at 8 jitals a man, gram and barley at 4 jitals a man, ten sirs of horse feed for one jital and grapes at one jital a sir; coins ran from one to forty-eight jitals, with half-jital (ādhā) and quarter-jital (bikh) for small change (in '+ED3+', pp. 344–346, 357–358). Offenders were exposed in the bazaars for a day or two (pp. 329–330).',
prescribed=NOSEC,
conjecture='The whole physical scene: the lane, shops and awnings, the goods and containers, the people and their dress, the sweetmeat seller, the mule and ox-cart, and the mosque in the distance. The texts give prices and coins, not a market\'s form.')
S[('sayyid','city')]=dict(label='City',title='Mubārakābād rising beside the Yamuna: a documented gap',
alt='Hypothetical reconstruction of a building site on the west bank of the Yamuna in 1433: low courses of rough stone and brick, bamboo scaffolding, labourers and bullock carts, an older fortified town in the distance',
attested='Mubārak Shāh laid the foundation of a new town, Mubārakābād, on the bank of the Yamuna on 31 October 1433, after living at Siri from 1428 and camping at the Ḥawẓ-i Khāṣṣ (Yaḥyā Sirhindī, Tārīkh-i Mubārak Shāhī, in '+ED4+', pp. 36–37). No description of the town as built was found.',
prescribed=NOSEC,
conjecture='Everything seen: a plain building site is shown because only the foundation is attested. The wall heights, scaffolding, workers\' dress, the older town in the distance and the river are the painter\'s. No finished building is shown.')
S[('lodi','city')]=dict(label='City',title='Agra chosen from the royal barge',
alt='Hypothetical reconstruction of the site of Agra in 1504: a royal barge with a canopy on a wide river, two low mounds on the bank, village huts and surveyors with rods and ropes',
attested='Sikandar left Delhi, marched to Mathura and took boat; approaching, he saw two elevated spots suited for building and asked the commander of the royal barge which was preferable; the answer \'That which is Agra, or in advance\' led him to name the city and order its foundation; he ordered a fort built; on Sunday 3 Safar 911 H. (July 1505) a violent earthquake threw down lofty buildings (Niʿmat Allāh, in '+ED5+', pp. 98–100; ʿAbd Allāh, Tārīkh-i Dāʾūdī, in '+ED4+', p. 465).',
prescribed=NOSEC,
conjecture='The bank, huts, trees and boats, the dress of the party (long tunics, sashes and small turbans), the barge\'s canopy and pennant, the shape of the mounds, which mound is chosen (the source says only \'Agra, or in advance\'), the surveyors and the season. No city or fort is yet built, as the source gives none at this moment.')
S[('lodi','street')]=dict(label='Bazaar',title='Cheap grain, cheap cloth',
alt='Hypothetical reconstruction of a north-Indian market street c. 1500: grain in sacks and baskets weighed on balances, cloth lengths hung to display, jars of ghee, a moneychanger with copper coins, bullock carts and shoppers',
attested='ʿAbd Allāh says that in Sikandar\'s reign grain, merchandise and goods of every kind were so cheap that small means sufficed to live comfortably (Tārīkh-i Dāʾūdī, in '+ED4+', p. 448). For Ibrāhīm\'s time, compared with Sikandar\'s, he gives ten mans of corn, five sirs of ghee and ten yards of cloth for one bahlolī (p. 476); these figures are Ibrāhīm\'s, not Sikandar\'s.',
prescribed=NOSEC,
conjecture='The entire physical setting: shop fronts, awnings, containers, weights, dress, crowd and animals, and the distant domed tomb (kept low and small). The source gives commodities, a coin and prices only. Women\'s dress follows the painter\'s idea of a draped garment and is not sourced.')
S[('sur','city')]=dict(label='City',title='The new city on the river bank: Sher Shāh\'s Delhi',
alt='Hypothetical reconstruction of Delhi c. 1542: a rubble and ashlar citadel with battered bastions and a high gateway, an unfinished outer wall with scaffolding and piles of cut stone, a stone mosque with a shallow dome, boats on the river',
attested='The former capital \'was at a distance from the Jumna, and Sher Shah destroyed and rebuilt it by the bank of the Jumna\' with two forts: the smaller for the governor\'s residence, the other, the wall round the whole city; in the governor\'s fort he built a Jāmiʿ mosque of stone, ornamented with much gold and lapis lazuli; the fortifications round the city were not complete when he died (ʿAbbās Sarwānī, Tārīkh-i Shēr Shāhī, in '+ED4+', p. 419). ʿAbd Allāh places the new city on the Jumna bank in the village of Indrapat, between Firozabad and Kilu Khari, after Sher Shāh destroyed the Siri fort in 947 H. (Tārīkh-i Dāʾūdī, in '+ED4+', pp. 476–477; the text is cut off in the reading made).',
prescribed=NOSEC,
conjecture='The plan, the number of gates, wall heights and finish, the look of the citadel, the form of the mosque (the source says only that it was of stone), the city fabric, the people, the boats and the stage of the work. The sources do not describe the river front.')
S[('sur','street')]=dict(label='Road halt',title='The sarāʾī on the royal road',
alt='Hypothetical reconstruction of a Sūr-period sarāʾī c. 1540: a fired-brick gateway with water pots, a courtyard with a well and a small brick mosque, merchants unloading carts, horses tethered under roadside trees and a cook at a hearth',
attested='Sher Shāh made a sarāʾī on every road at a distance of two kos, 1,700 in all; each had separate lodgings for Hindus and Muslims, pots of water at the gate, Brahmans to provide hot and cold water, beds, food and grain for horses, a well and a brick mosque in the middle with an imam, a muʾazzin and watchmen, and two horses kept for news; fruit and shade trees were planted on both sides of the highway, where travellers rested and tethered their horses; corn was cheap (ʿAbbās Sarwānī, in '+ED4+', pp. 417–418, 421, 425). Elliot notes that in his own day no trace of sarāʾī, mosque, road or tree could be found.',
prescribed=NOSEC,
conjecture='The courtyard\'s plan, the number of cells, the gate form, wall height and brick bond, the dress and goods of travellers, the tree species and the season. The source puts the well and mosque in the middle but gives no plan.')

def build(card,kind,png):
    it=dict(S[(card,kind)]); it['k']=kind
    d=f'{ROOT}/scenes/{card}'; os.makedirs(d,exist_ok=True)
    im=Image.open(png).convert('RGB')
    im.save(f'{d}/{kind}.webp',quality=82)
    for w in (480,960): im.resize((w,round(w*im.height/im.width)),Image.LANCZOS).save(f'{d}/{kind}-{w}.webp',quality=80)
    it['img']=f'scenes/{card}/{kind}.webp'; it['secondLabel']='Second source'; it['note']='Hypothetical reconstruction, painted with an AI image model from the texts above; not an archaeological finding. Colours, ornament and dress are illustrative.'
    p=f'{d}/scenes.json'
    s=json.load(open(p)) if os.path.exists(p) else {'id':card,'heading':H[card],'items':[]}
    s['items']=[x for x in s['items'] if x['k']!=kind]+[it]
    s['items'].sort(key=lambda x:{'city':0,'street':1,'temple':2}.get(x['k'],9))
    json.dump(s,open(p,'w'),ensure_ascii=False,indent=1); print('wired',card,kind)
if __name__=='__main__': build(*sys.argv[1:4])
