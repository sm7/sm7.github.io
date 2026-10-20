"""Apply the Pramana source pass (20 Oct 2026) to data.js. Idempotent. Run: python3 tools/pramana_pass.py

Every sentence added here rests on text read in Pramana (https://indike.org/pramana/): the BORI critical edition,
the vulgate and the southern recension of the Mahabharata, the Baroda critical edition of the Ramayana,
inscription texts with their printed-edition references, and its coin catalogue. Queries are in
experiments/pramana-audit.md."""
import json, subprocess, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LR = json.loads(subprocess.check_output(['node', '-e', f"global.window={{}};require('{ROOT}/data.js');console.log(JSON.stringify(window.LR))"]))
ORIG = open(f'{ROOT}/data.js').read()
TAIL = ORIG[ORIG.index('\n/* approximate reign'):] if '\n/* approximate reign' in ORIG else ''
BY = {c['id']: c for c in LR['cards']}
SRC = LR['SRC']
PM = 'https://indike.org/pramana/'

def src(key, cite, url):
    SRC[key] = [cite, url]

def add(cid, text):
    c = BY[cid]
    c['t'] = c['t'].rstrip() + ' ' + text

def has(cid, key):
    return '{' + key + '}' in BY[cid]['t']

# ---- sources -------------------------------------------------------------------------------------------------
src('pmRam290', 'Rāmāyaṇa 2.90.13–16, Baroda critical edition (text as held in Pramana, indike.org); the same verses stand at 2.90.13–16 in its southern recension', PM + 'in.lit.ramayana.valmiki*crit.2.90.14')
src('pmRam278', 'Rāmāyaṇa 2.78.1–4, Baroda critical edition (text as held in Pramana, indike.org)', PM + 'in.lit.ramayana.valmiki*crit.2.78.3')
src('pmVS7_105', 'Mahābhārata 7.105.8–30 in the vulgate (Nīlakaṇṭha\'s text) and the southern recension, collated line by line against critical-edition 7.80.8–27 (texts as held in Pramana, indike.org)', PM + 'in.lit.mahabharata.vyasa*vulgate.7.105')
src('pm6_44_48', 'Mahābhārata 6.44.48, critical edition (BORI), text as held in Pramana (indike.org); vulgate 6.46.50, southern 6.46.49', PM + 'in.lit.mahabharata.vyasa*crit.6.44.48')
src('pm6_17_18v', 'Mahābhārata 6.17.18 in the critical edition, the vulgate and the southern recension (texts as held in Pramana, indike.org)', PM + 'in.lit.mahabharata.vyasa*vulgate.6.17.18')
src('pmV7_23_84', 'Mahābhārata 7.23.84–85, vulgate (Nīlakaṇṭha\'s text); southern recension 7.23.85–86 (texts as held in Pramana, indike.org)', PM + 'in.lit.mahabharata.vyasa*vulgate.7.23.84')
src('pmV7_23_83', 'Mahābhārata 7.23.83, vulgate (Nīlakaṇṭha\'s text); southern recension 7.23.84 (texts as held in Pramana, indike.org)', PM + 'in.lit.mahabharata.vyasa*vulgate.7.23.83')
src('pmV7_23_86', 'Mahābhārata 7.23.86, vulgate (Nīlakaṇṭha\'s text); southern recension 7.23.87 (texts as held in Pramana, indike.org)', PM + 'in.lit.mahabharata.vyasa*vulgate.7.23.86')
src('pmV7_23_87', 'Mahābhārata 7.23.87, vulgate (Nīlakaṇṭha\'s text); southern recension 7.23.88 (texts as held in Pramana, indike.org)', PM + 'in.lit.mahabharata.vyasa*vulgate.7.23.87')
src('pmV7_23_89', 'Mahābhārata 7.23.89, vulgate (Nīlakaṇṭha\'s text); southern recension 7.23.90 (texts as held in Pramana, indike.org)', PM + 'in.lit.mahabharata.vyasa*vulgate.7.23.89')
src('pmV7_23_90', 'Mahābhārata 7.23.75 and 7.23.90, vulgate (Nīlakaṇṭha\'s text); southern recension 7.23.76 and 7.23.91 (texts as held in Pramana, indike.org)', PM + 'in.lit.mahabharata.vyasa*vulgate.7.23.90')
src('pmMW', 'Monier-Williams, Sanskrit–English Dictionary, s.v. śārṅga (\'a kind of bird, MBh.\'), as shown by Pramana\'s word lookup', PM + 'api/word?w=%C5%9B%C4%81r%E1%B9%85ga')

src('pmSirur', 'Sirur stone inscription of Amoghavarṣa I, Śaka 788 (866 CE), Indian Antiquary 12 (1883), p. 218, locator 25 — text as held in Pramana (indike.org)', PM + 'inp.epigraphy.deccan.rastrakuta.sirur-stone-inscription-of-amoghavarsha-i-saka-788')
src('pmNilgund', 'Nilgund inscription of the time of Amoghavarṣa I, 866 CE, Epigraphia Indica 6, no. 11, locator 16 — text as held in Pramana (indike.org)', PM + 'inp.epigraphy.deccan.rastrakuta.nilgund-inscription-of-the-time-of-amoghavarsha-i-a-d-866')
src('pmJavakheda', 'Javakheda plates of Amoghavarṣa I, Śaka 742, Epigraphia Indica 32 (Sircar 1958), plate III, seal enlarged — scan listed in Pramana (indike.org)', PM + 'inp.epigraphy.deccan.rastrakuta.javakheda-plates-of-amoghavarsha-i-saka-742')
src('pmJambgaon', 'Jambgaon plates of Indra III, Śaka 836, Epigraphia Indica 36 (Sircar 1965), seal from a photograph — listed in Pramana (indike.org)', PM + 'inp.epigraphy.deccan.rastrakuta.jambgaon-plates-of-indra-iii-saka-836')
src('pmUndika', 'Untikavāṭikā grant of Abhimanyu, Epigraphia Indica 8 (Hultzsch 1906), no. 16, seal captioned as showing a lion — listed in Pramana (indike.org)', PM + 'inp.epigraphy.deccan.rastrakuta.undikavatika-grant-of-abhimanyu')
src('pmKopparam', 'Kopparam plates of Pulakeśin II, Epigraphia Indica 18, p. 257 — text as held in Pramana (indike.org); the same formula recurs in nine further Bādāmi Chālukya grants there, eight of them dated c. 660–713 CE', PM + 'inp.epigraphy.deccan.badami-calukya.kopparam-plates-of-pulakesin-ii')
src('pmKailasa', 'Lists of birudas, Kailāsanātha temple, Kāñcīpuram, South Indian Inscriptions 1, nos. 25–26 — text as held in Pramana (indike.org)', PM + 'inp.epigraphy.south.pallava.kancipuram-kailasanatha-temple-lists-of-birudas')
src('pmVijayawada', 'Pallava slab found at Vijayawāḍā, South Indian Inscriptions 10, p. 8 — text as held in Pramana (indike.org)', PM + 'inp.epigraphy.south.pallava.vijayawada-on-a-mutilated-slab-dug-up-in-the-court-yard-of')
src('pmNadagam', 'Nadagam plates of Vajrahasta, Śaka 979, Epigraphia Indica 4, no. 24 — text as held in Pramana (indike.org)', PM + 'inp.epigraphy.east.eastern-ganga.nadagam-plates-of-vajrahasta-saka-samvat-979')
src('pmMadrasMus', 'Madras Museum plates of Vajrahasta III, Śaka 984, Epigraphia Indica 9, no. 11 — text as held in Pramana (indike.org)', PM + 'inp.epigraphy.east.eastern-ganga.madras-museum-plates-of-vajrahasta-iii-saka-samvat-984')
src('pmTagarti', 'Tagarti agrahāra copper-plate grant of a Western Gaṅga king, Epigraphia Carnatica 7, Sk 52 (dated c. 358 CE in Pramana; the wording, not the date, is cited) — text as held in Pramana (indike.org)', PM + 'inp.epigraphy.deccan.western-ganga.tagarti-agrahara-copper-plate-grant-of-western-ganga')
src('pmSalem', 'Salem plates of Gaṅga Śrīpuruṣa, Śaka 693, Epigraphia Indica 27, no. 25, seal from a photograph — listed in Pramana (indike.org)', PM + 'inp.epigraphy.deccan.western-ganga.salem-plates-of-ganga-sripurusha-saka-693')
src('pmAllahabad', 'Allahabad pillar inscription of Samudragupta, Corpus Inscriptionum Indicarum 3 (Fleet 1888), line 24 (garutmad-aṅka) and Fleet\'s translation — text as held in Pramana (indike.org)', PM + 'inp.epigraphy.north.gupta.allahabad-posthumous-stone-pillar-inscription-of')
src('pmGwalior', 'Gwalior (Vaillabhaṭṭasvāmin temple) inscription, Vikrama 933 (876 CE), Epigraphia Indica 1, p. 156, verse 22, with Hultzsch\'s translation — as held in Pramana (indike.org)', PM + 'inp.epigraphy.west.pratihara.first-inscription-of-the-vaillabhattasvamin-temple-at')
src('pmSarnathEdict', 'Sārnāth pillar (Schism) edict of Aśoka, Sircar, Select Inscriptions 1.36 — text as held in Pramana (indike.org)', PM + 'inp.epigraphy.north.maurya.sarnath-pillar-edict')
src('pmMaitraka', 'Pramana, Maitraka inscriptions (147, of which 132 have text), searched on 20 October 2026 for seal, bull, vṛṣabha, ṛṣabha and nandin; the queries are in experiments/pramana-audit.md', PM + 'inp.epigraphy.west.maitraka')
src('pmCoinCat', 'Pramana coin and specimen catalogue (tables obj and mark_occ), counted by dynasty and motif on 20 October 2026; the queries are in experiments/pramana-audit.md', PM + 'api/marks')

# ---- itihasa -------------------------------------------------------------------------------------------------
c = BY['ikshvaku']
if not has('ikshvaku', 'pmRam290'):
    c['t'] = ("Lakṣmaṇa sees an army approach and concludes that Bharata is coming against them.{ram} He points to its ensign: a very large, glorious, "
              "branching kovidāra tree with raised trunk, shining on the chariot.{ram} The verse names only the tree.{ram} In the Baroda critical edition "
              "these are verses 2.90.13–16.{pmRam290} Guha, the Niṣāda king, also names Bharata's army by the 'kovidāra banner on the chariot' at 2.78.3.{pmRam278}")
    c['ref'] = 'Rāmāyaṇa 2.90.14 in the Baroda critical edition and in Pramana\'s southern recension (2.96.18 in the numbering of valmikiramayan.net); also 2.78.3'

SEEN = {  # card -> (text, key); 7.105 = vulgate and southern numbering of critical-edition 7.80
    'arjuna': 'The vulgate and southern recensions give the Kurukṣetra banner as the same emblem (7.105.8–9).',
    'ashvatthaman': 'The vulgate and southern recensions give the same emblem (7.105.10–11).',
    'karna': 'The vulgate and southern recensions give the same emblem (7.105.12–13).',
    'kripa': 'The vulgate and southern recensions give the same emblem (7.105.14–15).',
    'vrishasena': 'The vulgate and southern recensions give the same emblem (7.105.16–17).',
    'shalya': 'The vulgate and southern recensions give the same emblem (7.105.18–19).',
    'bhurishravas': 'The vulgate and southern recensions give the same emblem (7.105.22–23).',
    'duryodhana': 'The vulgate and southern recensions give the same emblem (7.105.26–27).',
}
for cid, s in SEEN.items():
    if not has(cid, 'pmVS7_105'):
        add(cid, s + '{pmVS7_105}')
if not has('jayadratha', 'pmVS7_105'):
    add('jayadratha', "The vulgate agrees with the critical edition. The southern recension has lohitāṅgābhaḥ, 'of red-limbed splendour', where the critical edition has alohitārkābhaḥ, so it does not describe the boar's brightness in the same way (7.105.20).{pmVS7_105}")
if not has('shala', 'pmVS7_105'):
    add('shala', "The vulgate and southern recensions also read śalasya, 'of Śala' (7.105.24), so the name is not peculiar to the critical edition.{pmVS7_105}")
if not has('bhishma', 'pm6_17_18v'):
    add('bhishma', "The critical edition, the vulgate and the southern recension all read this verse alike at 6.17.18.{pm6_17_18v} The critical edition describes the banner again at 6.44.48, now as a lofty silver palm with five stars, and says Bhīṣma shone with it like the moon on Mount Meru.{pm6_44_48}")
    BY['bhishma']['ref'] = 'Mahābhārata 6.17.18; 6.44.48'

c = BY['ghatotkaca']
if not has('ghatotkaca', 'pmV7_23_90'):
    c['t'] = ("Horses of many colours, with faces of many shapes, carried the hero Ghaṭotkaca, whose banner was a chariot-wheel.{mbs7022} The verse gives no material or colour for the wheel.{mbs7022} "
              "The vulgate and southern texts have that verse too (7.23.75; 7.23.76), and then add a second banner in a verse the critical edition does not have: a vulture on his standard (vulgate 7.23.90; southern 7.23.91).{pmV7_23_90}{gan7023}")
    c['ref'] = 'Mahābhārata 7.22.60 (critical edition); the vulture is vulgate 7.23.90, southern 7.23.91'

PAND = {
 'yudhishthira': ("The vulgate Sanskrit (7.23.84–85) names a golden moon with a host of planets, and two large divine drums, Nanda and Upananda, 'being struck by a device' (yantra); Ganguli's 'tied to it' is his rendering. The southern recension has the same verses (7.23.85–86).{pmV7_23_84}",
   'dhvajaṃ tu kururājasya pāṇḍavasya mahaujasaḥ | dṛṣṭavānasmi sauvarṇaṃ somaṃ grahagaṇānvitam | mṛdaṅgau cātra vipulau divyau nandopanandakau | yantreṇāhanyamānau ca susvanau harṣavardhanau',
   'Vulgate 7.23.84–85 (grahagaṇānvitam as in the southern text 7.23.85; the vulgate e-text prints anvatam); southern 7.23.85–86; not in the critical edition',
   'Vulgate only, not in the critical edition. The painting ties the drums to the staff, as Ganguli does; the Sanskrit says they are struck by a device.', None),
 'bhima': ("The vulgate Sanskrit (7.23.83) names a great shining lion with eyes of vaiḍūrya gems. Ganguli adds 'in silver', but the Sanskrit as read in Pramana's vulgate and southern texts has rājantam, 'shining', and not rājatam, 'silver', so the silver is not confirmed here. The southern recension has the verse at 7.23.84.{pmV7_23_83}",
   'dhvajaṃ tu bhīmasenasya vaiḍhūryamaṇilocanam | bhrājamānaṃ mahāsiṃhaṃ rājantaṃ dṛṣṭavānaham',
   'Vulgate 7.23.83, southern 7.23.84; not in the critical edition',
   "Vulgate only, not in the critical edition. 'Silver' is Ganguli's rendering; the Sanskrit reads rājantam, 'shining'. The painting follows Ganguli.", 'Lion with vaiḍūrya-gem eyes'),
 'nakula': ("The vulgate Sanskrit (7.23.86) says the great standard on Nakula's chariot bore a śarabha with a golden back, 'very fierce' (atyugra); the southern recension has it at 7.23.87.{pmV7_23_86}",
   'śarabhaṃ pṛṣṭhasauvarṇaṃ nakulasya mahādhvajam | apaśyāma rathe\'tyugraṃ bhīṣayāṇamavasthitam',
   'Vulgate 7.23.86, southern 7.23.87; not in the critical edition', None, None),
 'sahadeva': ("The vulgate Sanskrit (7.23.87) gives a silver (rājata) swan with a bell and a pennant on Sahadeva's standard; the southern recension has it at 7.23.88.{pmV7_23_87}",
   'haṃsastu rājataḥ śrīmān dhvaje ghaṇṭāpatākavān | sahadevasya durdharṣo dviṣatāṃ śokavardhanaḥ',
   'Vulgate 7.23.87, southern 7.23.88; not in the critical edition', None, None),
 'abhimanyu': ("The Sanskrit (vulgate 7.23.89; southern 7.23.90) says śārṅga-pakṣī hiraṇmayaḥ, 'a golden śārṅga bird', bright as heated gold.{pmV7_23_89} Pramana's dictionary lookup lists śārṅga only as 'a kind of bird'.{pmMW} The same catalogue uses mayūra, 'peacock', for Vṛṣasena's banner (7.80.16), so 'peacock' is Ganguli's identification and not the text's.",
   'abhimanyoḥ kumārasya śārṅgapakṣī hiraṇmayaḥ | rathe dhvajavaro rājaṃstaptacāmīkarojjvalaḥ',
   'Vulgate 7.23.89, southern 7.23.90; not in the critical edition',
   "Vulgate only, not in the critical edition. The painting follows Ganguli's 'peacock'; the Sanskrit names a śārṅga bird, not a mayūra.", 'Golden śārṅga bird (Ganguli: peacock)'),
}
for cid, (txt, san, ref, warn, e) in PAND.items():
    c = BY[cid]
    first_key = txt.split('{')[1].split('}')[0]
    if not has(cid, first_key):
        c['t'] = c['t'].rstrip() + ' ' + txt
        c['san'] = san
        c['ref'] = ref
        if warn: c['warn'] = warn
        if e: c['e'] = e

# ---- early dynasties -----------------------------------------------------------------------------------------
c = BY['rashtrakuta']
if not has('rashtrakuta', 'pmSirur'):
    c['t'] = ("Amoghavarṣa I's inscriptions of 866 CE call the Rāṣṭrakūṭa king 'born in the Raṭṭa line, Garuḍa-marked' (Raṭṭa-vaṁśōdbhavaṁ Garuḍa-lāñchanaṁ), at Sirur and again at Nilgund.{pmSirur}{pmNilgund} "
              "So Garuḍa is attested as the dynasty's mark in its own record, not only by later report. "
              "The printed seal impressions of the Javakheda plates of Amoghavarṣa I (820 CE) and the Jambgaon plates of Indra III (914 CE) show a seated figure, winged in the Javakheda impression, which fits Garuḍa; the pose cannot be read in detail from the plates.{pmJavakheda}{pmJambgaon} "
              "A grant of Abhimanyu from Untikavāṭikā, earlier than 753, has a seal captioned in Epigraphia Indica as showing a lion.{pmUndika} "
              "The seal of the early Rāṣṭrakūṭa plates from Jamkhed carries only a short inscription, with no recognisable picture.{balogh2014}")
    c.pop('review', None)

if not has('maitraka', 'pmMaitraka'):
    c = BY['maitraka']
    c['t'] = ("Maitraka grants carry the dynasty's seal, usually described with a seated bull above the legend 'Śrī-Bhaṭakkaḥ'. "
              "That description has not been confirmed from any text or readable plate. The charters name the founder as 'senāpati Bhaṭakka' but none describes a seal.{pmMaitraka}")
    c['review'] = ("Documented gap: Pramana holds 147 Maitraka inscriptions, 132 with text. In those texts the words seal, bull, vṛṣabha, ṛṣabha and nandin never occur. "
                   "Their 'lāñchana' is the idiom for the mark on the king's forehead from bowing at his father's feet, and their 'dhvaja' is the banner of dharma, not an emblem. "
                   "Three seal impressions are printed in Pramana's scans (Corpus Inscriptionum Indicarum 3; Epigraphia Indica 21), but they are too worn to read here. The bull stays unconfirmed.")

if not has('chalukya', 'pmKopparam'):
    add('chalukya', "The Bādāmi Chālukya grants name it in words. Pulakeśin II's Kopparam plates describe the family as having obtained, by the favour of the blessed Nārāyaṇa, the boar crest (varāha-lāñchana), at the sight of which all kings were subdued in an instant; the formula recurs in nine further grants, eight of them dated c. 660–713 CE.{pmKopparam}")

if not has('pallava', 'pmKailasa'):
    add('pallava', "The Pallavas' own titles confirm the bull: the list of birudas engraved at the Kailāsanātha temple in Kāñcīpuram includes 'ṛṣabha-lāñchana', 'bull-marked'.{pmKailasa} A Pallava slab from Vijayawāḍā gives 'khaṭvāṅga-dhvaja', 'vṛṣabha-lāñchana' and 'lord of Kāñcīpura' as titles in a row.{pmVijayawada} In Pramana's coin catalogue 82 of 133 Pallava coin types and specimens show a bull and 27 a lion.{pmCoinCat}")

if not has('eastern-ganga', 'pmNadagam'):
    add('eastern-ganga', "Eleventh-century charters name the bull in words: the Nadagam plates (Śaka 979) and the Madras Museum plates of Vajrahasta III (Śaka 984) list 'vara-vṛṣabha-lāñchana', the excellent bull crest, among the king's royal insignia beside the white parasol and the golden fly-whisk.{pmNadagam}{pmMadrasMus}")

if not has('western-ganga', 'pmTagarti'):
    add('western-ganga', "A Western Gaṅga grant from Tagarti styles the king 'Gaṅga-kuḷa-mārttaṇḍa, mada-gajēndra-lāñcana', 'marked with the elephant lord in rut'.{pmTagarti} The photographed seal of the Salem plates of Śrīpuruṣa (Śaka 693) appears to show an elephant.{pmSalem}")

if not has('gupta', 'pmAllahabad'):
    add('gupta', "The Allahabad pillar inscription lists the services by which rulers near and far attached themselves to Samudragupta, among them 'garutmad-aṅka'; Fleet translates it 'Garuḍa-tokens'.{pmAllahabad} In Pramana's coin catalogue Garuḍa appears on 77 of 591 Gupta coin types and specimens, Lakṣmī on 120.{pmCoinCat}")

if not has('pratihara', 'pmGwalior'):
    add('pratihara', "The title is attested in the Gwalior inscription of the Vaillabhaṭṭasvāmin temple (Vikrama 933, 876 CE), which says the illustrious Ādivarāha, wishing to conquer the three worlds, appointed a man to guard Gopādri.{pmGwalior}")

if not has('maurya', 'pmSarnathEdict'):
    add('maurya', "The same Sārnāth pillar carries Aśoka's Schism Edict, which orders that a monk or nun who splits the Saṅgha be made to wear white robes and to live outside the monastery.{pmSarnathEdict}")

if not has('satavahana', 'pmCoinCat'):
    add('satavahana', "In Pramana's coin catalogue the commonest motif among 264 Sātavāhana coin types and specimens is the elephant (100), ahead of the Ujjain symbol (62) and the hill (37); the evidence photograph shows an elephant type.{pmCoinCat}")

# ---- check and write -----------------------------------------------------------------------------------------
missing = set()
for cd in LR['cards']:
    for k in re.findall(r'\{(\w+)\}', cd['t']):
        if k not in SRC: missing.add((cd['id'], k))
assert not missing, missing
HEAD = '/* Lāñchhana Register data. Text uses {key} after a sentence to cite SRC[key]. */\nwindow.LR='
open(f'{ROOT}/data.js', 'w').write(HEAD + json.dumps(LR, ensure_ascii=False, indent=0) + ';\n' + TAIL)
print('ok; SRC', len(SRC), 'cards', len(LR['cards']))
