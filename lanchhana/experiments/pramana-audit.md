# Pramana source pass — 20 October 2026

Source: https://indike.org/pramana/ (JSON API: `/pramana/api/...`, read-only SQL at `POST /pramana/api/sql`).
Scope: the 23 itihasa cards and the 27 early-dynasty cards. Code: `tools/pramana_pass.py` (idempotent; applies every edit below).

Method note. The build shell cannot reach indike.org (egress policy returns 403), so every query was run from a browser tab on the site. Pramana's texts are transcriptions with their printed-edition references (`refs`, e.g. EI 18 p257); the register cites the printed edition and gives the Pramana page as the place the text was read. No printed volume was consulted directly.

## Itihasa

| Check | Result |
|---|---|
| Banner catalogue, critical edition (CE) 7.80.8–27, against vulgate and southern 7.105.8–30, line by line | Every emblem is the same in all three. Only substantive variant: Jayadratha's boar, CE `alohitārkābhaḥ`, southern `lohitāṅgābhaḥ`. `śalasya` (Śala) is also the vulgate and southern reading. |
| Pāṇḍava standards (Yudhiṣṭhira, Bhīma, Nakula, Sahadeva, Abhimanyu, Ghaṭotkaca's vulture) | Present in vulgate 7.23.83–90 and southern 7.23.84–91. Absent from the whole of CE book 7 (phrase search). Only Ghaṭotkaca's wheel is in CE (7.22.60). Sanskrit now quoted on the cards. |
| Bhīma "silver lion" | Not in the Sanskrit as Pramana has it: vulgate and southern read `rājantam` ("shining"), not `rājatam`. "Silver" is Ganguli's. Painting unchanged, flagged on the card. |
| Abhimanyu "golden peacock" | Sanskrit is `śārṅgapakṣī hiraṇmayaḥ`, "a golden śārṅga bird" (Monier-Williams: "a kind of bird"). The same catalogue says `mayūra` for Vṛṣasena. "Peacock" is Ganguli's. Painting unchanged, flagged: needs re-rendering if the text is to rule. |
| Yudhiṣṭhira drums | Sanskrit: Nanda and Upananda are `mṛdaṅga`s "struck by a device (yantra)"; Ganguli: "tied". Painting follows Ganguli, flagged. |
| Rāmāyaṇa kovidāra banner | Baroda CE 2.90.14 (Lakṣmaṇa) and 2.78.3 (Guha, Niṣāda king); same numbers in Pramana's southern recension. `2.96.18` is the numbering of valmikiramayan.net, which Pramana does not hold. |
| Bhīṣma | CE 6.17.18 reads alike in CE, vulgate, southern. CE 6.44.48 adds a silver palm. |

## Early dynasties

Changed, with primary text:

| Card | What Pramana gave |
|---|---|
| Rāṣṭrakūṭa | Gap closed. Sirur (IA 12 p218) and Nilgund (EI 6.11), both 866 CE: `Raṭṭa-vaṁśōdbhavaṁ Garuḍa-lāñchanaṁ`. Bagali (SII 9.1, undated) also `garuḍa-lāñchana`. Seal scans (Javakheda EI 32, Jambgaon EI 36) show a seated, winged figure; pose not readable. Pre-753 Abhimanyu grant has a lion seal (EI 8.16 caption). |
| Chālukya | `varāha-lāñchana` in Kopparam plates of Pulakeśin II (EI 18 p257) and nine more grants. |
| Pallava | `ṛṣabha-lāñchana` (Kailāsanātha birudas, SII 1.25–26); `vṛṣabha-lāñchana` (Vijayawāḍā slab, SII 10 p8). Coins: bull on 82 of 133. |
| Eastern Gaṅga | `vara-vṛṣabha-lāñchana` among royal insignia (Nadagam EI 4.24; Madras Museum plates EI 9.11), 1057 and 1062 CE. |
| Western Gaṅga | `mada-gajēndra-lāñcana` (Tagarti, EC 7 Sk 52; Pramana's date c. 358 CE not relied on). Salem plates seal appears to show an elephant. |
| Gupta | `garutmad-aṅka` (Allahabad pillar, CII 3), Fleet: "Garuḍa-tokens". Coins: Garuḍa on 77 of 591. |
| Pratīhāra | `śrīmad-ādivarāha` in the Gwalior Vaillabhaṭṭasvāmin inscription, EI 1 p156 v.22. |
| Maurya | Schism Edict on the Sārnāth pillar (SI 1.36). |
| Sātavāhana | Elephant is the commonest motif (100 of 264), Ujjain symbol 62. The card's choice of the Ujjain symbol is defensible only because the card already says it was shared. |

Still a documented gap: **Maitraka**. In 147 inscriptions (132 with text) none of `seal`, `bull`, `vṛṣabh`, `ṛṣabh`, `nandin` occurs. `lāñchana` is the forehead-callus idiom; `dhvaja` is `dharma-dhvaja`. Three seal scans (CII 3; EI 21) are too worn to read. The bull is unconfirmed.

No change, nothing decisive in Pramana: Kuṣāṇa, Kṣatrapa, Kāmarūpa, Viṣṇukuṇḍina (no coin entries in Pramana), Maukhari, Puṣyabhūti, Gauḍa, Karkoṭa, Pāṇḍuvaṃśī, Śarabhapurīya, Pāla, Kalacuri, Śāhi, Chola, Pāṇḍya, Chera, Paramāra. Coin counts agree with the cards where checked (Śāhi horseman 347 and bull 338 of 427; Gauḍa Śiva-bull and Lakṣmī 6 each of 11; Kalacuri Lakṣmī 13 of 44; Chola tiger 27 of 117; Pāṇḍya garuḍa coins are 15th-century, the fish is the early emblem). The Sonpat seal scan (CII 3.52) shows no emblem at the crop Pramana provides, so the Puṣyabhūti bull still rests on Vats.

## Reproduce

```js
const q = sql => fetch('/pramana/api/sql', {method:'POST', headers:{'content-type':'application/json'}, body: JSON.stringify({sql})}).then(r => r.json());
// emblem words in a dynasty's inscriptions
q("SELECT i.path, s.loc, substr(s.text,1,260) FROM inscription i JOIN segment s ON s.doc_id=i.doc_id WHERE i.dynasty='rastrakuta' AND s.text LIKE '%lāñc%'")
// phrase in the three Mahābhārata recensions
q("SELECT d.path, s.loc FROM segment s JOIN doc d ON d.id=s.doc_id WHERE d.path IN ('in.lit.mahabharata.vyasa*crit','in.lit.mahabharata.vyasa*vulgate','in.lit.mahabharata.vyasa*southern') AND s.loc LIKE '7.%' AND s.text LIKE '%pṛṣṭhasauvarṇ%'")
// coin motifs by dynasty
q("SELECT m.mark, count(DISTINCT m.doc_id) n FROM mark_occ m JOIN obj o ON o.doc_id=m.doc_id WHERE o.dynasty='pallava' AND o.kind IN ('coin','specimen') GROUP BY m.mark ORDER BY n DESC LIMIT 9")
// Maitraka negative search (use a word, not 'nandi': it matches '-ānandi-')
q("SELECT count(DISTINCT i.doc_id) FROM inscription i JOIN segment s ON s.doc_id=i.doc_id WHERE i.dynasty='maitraka' AND lower(s.text) LIKE '%vṛṣabh%'")
```

## Open

- Re-render Abhimanyu (śārṅga bird, not peacock) and decide on Bhīma (silver) and Yudhiṣṭhira (drums struck, not tied).
- Pramana's figures carry a licence line (those read here: 'Public domain (Fleet 1888)', 'Public domain (Burgess 1878)'). They could replace Commons photos as seal evidence, once downloaded with that line kept.
- The later dynasties were not covered. Pramana's inscription counts for them: Hoysala 1,855, Yadava 556, Kakatiya 265, Gahadavala 79, Candella 49.
