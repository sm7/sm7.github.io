# Scene coverage audit (city / street / temple)

Generated from scenes/*/scenes.json. "-" = no honest source found yet; left blank rather than invented.

| card | city | street | temple |
|---|---|---|---|
| ahom | ✓ | ✓ | - |
| ayodhya | ✓ | - | - |
| chalukya | ✓ | - | ✓ |
| chandela | - | - | ✓ |
| chauhan | ✓ | ✓ | - |
| chera | ✓ | - | ✓ |
| chola | ✓ | ✓ | ✓ |
| eastern-ganga | - | - | ✓ |
| gahadavala | - | - | - |
| gauda | - | - | - |
| gupta | ✓ | ✓ | ✓ |
| hoysala | ✓ | - | ✓ |
| ikshvaku | - | - | ✓ |
| jaipur | - | - | - |
| kakatiya | - | - | - |
| kalachuri | - | - | - |
| kamarupa | ✓ | - | - |
| karkota | ✓ | - | ✓ |
| kshatrapa | ✓ | - | ✓ |
| kushan | - | - | ✓ |
| magadha | ✓ | ✓ | ✓ |
| maitraka | ✓ | - | - |
| maratha | ✓ | - | - |
| maukhari | - | - | - |
| maurya | ✓ | ✓ | ✓ |
| mewar | ✓ | - | - |
| mysore | ✓ | - | ✓ |
| pala | - | - | - |
| pallava | ✓ | ✓ | ✓ |
| panduvamsi | - | - | - |
| pandya | ✓ | - | ✓ |
| paramara | ✓ | - | - |
| pratihara | ✓ | ✓ | - |
| pushyabhuti | ✓ | ✓ | ✓ |
| rashtrakuta | ✓ | - | - |
| satavahana | - | - | ✓ |
| sena | ✓ | - | ✓ |
| shahi | - | - | - |
| sharabhapuriya | - | - | - |
| sikh | ✓ | ✓ | ✓ |
| travancore | - | - | ✓ |
| tripura | - | - | - |
| vijayanagara | ✓ | ✓ | ✓ |
| vishnukundina | - | - | - |
| western-ganga | - | - | ✓ |
| yadava | - | - | - |

## Notes
- Deviations between experiments/prompts.json and the prompts actually sent: pandya/city (composition-first), pandya/temple, gupta/city (muted documentary wording), magadha/street (softened after a policy block), pallava/street (Sanskrit line was garbled and abridged when typed; the image carries no legible text).
- Single-source scenes (Hügel for Sikh; Aiya for Travancore) say so in their conjecture notes.
- western-ganga/temple shows the Gommaṭa statue in its traditional unclothed convention; veto if unwanted.
- Dropped for lack of an honest scene: maukhari/temple, panduvamsi/temple; gauda, panduvamsi and vishnukundina city judged too thin.

## Image QA pass (Oct 2026)
Criteria: true to source; not anachronistic; looks like its era.
Replaced with era-anchored regenerations (explicit negatives for jharokha, jali, chhatri, cusped arches, domes, Mangalore tiles, bastions): chalukya army/city, gupta city/charity/temple, kshatrapa city, pallava street/city, pandya city, maitraka city, magadha street/city, sena city, chauhan city/street, paramara city, hoysala city, maurya temple, rashtrakuta court, chola city.
Each replaced scene's conjecture note now says what in the picture is the painter's rather than the source's.
Not yet re-reviewed: Ayodhya precinct/festival/road/entry scenes (domes and jharokhas flagged).
