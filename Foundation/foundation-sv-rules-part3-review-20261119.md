# Foundation – regler III, svensk granskning 2026-11-19

Den tredje delen av `rules.json` har granskats via Crowdin API. Förslagen är utkast och har inte skickats till Crowdin.

| ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 22416 | {1} and {2} mutual Splendour negative impact is increased by {3}. | {1} och {2} ömsesidig negativ inverkan på Prakt ökas med {3}. | Den ömsesidiga negativa inverkan på {1}s och {2}s prakt ökar med {3}. |
| 22418 | {1} and {2} mutual Splendour negative impact is reduced by {3}. | {1} och {2} ömsesidig negativ påverkan på Prakt minskas med {3}. | Den ömsesidiga negativa inverkan på {1}s och {2}s prakt minskar med {3}. |
| 22420 | Combatant recovery speed is increased by {IMG1}. | Stridandes återhämtningshastighet ökas med {IMG1}. | Återhämtningshastigheten för stridande ökar med {IMG1}. |
| 22422 | Combatant recovery speed is reduced by {IMG1}. | Stridandes återhämtningshastighet minskas med {IMG1}. | Återhämtningshastigheten för stridande minskar med {IMG1}. |
| 22430 | Because of Privilege: {1} | På grund av privilegier: {1} | På grund av privilegiet: {1} |
| 22432 | Every time you trade with a village of {1} allegiance, you gain {2} Influence with its Estate. | Varje gång du handlar med en by med {1} lojalitet får du {2} inflytande med dess gods. | Varje gång du handlar med en by med {1} lojalitet får du {2} inflytande hos dess stånd. |
| 22434 | Taxation cumulation speed is increased by {1}. | Kumuleringshastigheten för beskattning ökas med {1}. | Kumuleringshastigheten för beskattning ökar med {1}. |
| 22448 | Upkeep of {1} Building Parts are increased by {2} | Underhållet av {1} byggnadsdelar ökade med {2} | Underhållet av {1} byggnadsdelar ökar med {2} |
| 22450 | Upkeep of {1} Building Parts are decreased by {2} | Underhållet av {1} byggnadsdelar minskade med {2} | Underhållet av {1} byggnadsdelar minskar med {2} |

## Kontroller

- `l10n-lint --language sv`: inga fel eller varningar; två informationsnoteringar eftersom svensk ordföljd börjar före platshållarna i 22416 och 22418.
- `hunspell -d sv_SE` passerade utan anmärkningar.
- Samtliga bild- och textplatshållare är bevarade.
