# Foundation – agenter: release, full radgranskning 2026-11-19

Samtliga 64 strängar i `agents.release.json` granskades via Crowdin API. Fyra förbättringsförslag identifierades; övriga 60 bedömdes korrekta.

| ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 14028 | Your villager ate a delicious meal at the tavern! This Happiness bonus will fade over time. | Din bybo åt en utsökt måltid på värdshuset! Denna Lyckobonus kommer att försvinna med tiden. | Din bybo åt en utsökt måltid på värdshuset! Den här lyckobonusen avtar med tiden. |
| 14034 | Merry Fair | Munter Mässa | Munter mässa |
| 14036 | The fair lived up to expectations! … | Mässan levde upp till förväntningarna! … Lyckobonusen kommer gradvis försvinna. | Mässan levde upp till förväntningarna! Ditt folk gläder sig över det lyckade evenemanget, men lyckobonusen avtar gradvis. |
| 14116 | The King's retinue consists of their favourite advisors, courtiers, valets, and guardsmen. | Kungens följe består av dess favoritrådgivare, hovmän, betjänter och vakter. | Kungens följe består av hans favoritrådgivare, hovmän, betjänter och vakter. |

## Kontroller

- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` passerade utan anmärkningar.
- Förslagen har inte skickats till Crowdin.
