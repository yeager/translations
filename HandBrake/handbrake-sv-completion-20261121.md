# HandBrake — komplettering och svensk radgranskning

Datum: 2026-11-21  
Plattform: Transifex API  
Språk: `sv_SE`

## Status efter komplettering

| Projekt/resurs | Svenska strängar | Oöversatta |
|---|---:|---:|
| Linux UI — ghb.pot | 801 | 0 |
| Mac UI — en.xliff | 1 281 | 0 |
| Windows UI — Resources.resx | 1 013 | 0 |
| Windows UI — ResourcesTooltips.resx | 91 | 0 |

86 tidigare oöversatta strängar sparades via Transifex API:

- Mac UI: 25
- Windows UI: 58
- Windows UI-verktygstips: 3

## Tillämpad terminologi

Den tillhörande listan `handbrake-sv-terminology-20261121.md` styr bland annat: källfil, förinställning, kö, utdata, ljudspår, undertextspår, genomströmning, bildfrekvens, bithastighet, omslagsbild, metadata och loggfil.

## Granskningsfynd som redan är rättade

- 174 förekomster av det äldre `förval` rättades morfologiskt till `förinställning` i Linux UI, Mac UI och Windows UI. Exempel: `förvalet` → `förinställningen`; `förvalsfil` → `förinställningsfil`.
- 16 förekomster av `bitfrekvens`/ `bildhastighet` rättades till `bithastighet`/ `bildfrekvens`.
- VFR-hjälptexten i Linux UI skrevs om för korrekt och tydlig svenska.

Formatsträngar och platshållare såsom `{0}`, `%1$d`, `%@` och `%.2f` bevarades.
