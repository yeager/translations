# Foundation – Drakens skatt II, svensk granskningsbatch 2026-11-19

Tio oöversatta strängar i `ks_content.json` har granskats via Crowdin API. Förslagen är utkast och har inte sparats i Crowdin.

| ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 26482 | If food is at stake, Hunters will be on the lookout. | — | Om det finns mat på spel håller jägarna utkik. |
| 26484 | A bounty of food will keep Hunters on the lookout. | — | En riklig mängd mat får jägarna att fortsätta hålla utkik. |
| 26486 | Led by their best … | — | Under ledning av sin bästa kommer dina jägare att söka efter skatten på sin fritid. |
| 26488 | Your well-fed Hunters find the treasure. | — | Dina välmätta jägare hittar skatten. |
| 26490 | Your well-fed Hunters come back empty-handed. | — | Dina välmätta jägare kommer tillbaka tomhänta. |
| 26492 | I will deploy a Company to scour the region. | — | Jag skickar ut ett sällskap för att genomsöka trakten. |
| 26494 | Let’s have a Company pursue the search. | — | Låt ett sällskap fortsätta sökandet. |
| 26496 | You will be able to deploy a company … | — | Du kommer att kunna skicka ut ett sällskap för att söka efter skatten. |
| 26498 | The company finds the treasure. | — | Sällskapet hittar skatten. |
| 26500 | The company wastes its time. | — | Sällskapet slösar bort sin tid. |

## Kontroller

- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` passerade utan anmärkningar.
- Terminologin *Company* → *sällskap* används genomgående i batchen.
