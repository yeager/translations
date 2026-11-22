# Audacity 4 – svensk komplettering i Transifex

Den 22 november 2026 kompletterades Audacity 4-resursen direkt med
Transifex API.

## Resultat

- Resurs: `o:audacity:p:audacity:r:audacity4`
- 227 tidigare oöversatta svenska strängar granskades i kontext och sparades.
- Qt-platshållare (`%1`, `%2`, `%3`, `%n`), markup och radbrytningar bevarades.
- Den pluraliserade makrosträngen fick separata svenska `one`- och
  `other`-former via API.

## Liveverifiering

Transifex resursstatistik efter avslutat arbete:

| Mått | Antal |
| --- | ---: |
| Totala strängar | 4 147 |
| Översatta strängar | 4 147 |
| Oöversatta strängar | 0 |
| Totala ord | 15 130 |
| Oöversatta ord | 0 |

Den direkta API-listan för `filter[translated]=false` var också tom efter
slutlig återläsning.
