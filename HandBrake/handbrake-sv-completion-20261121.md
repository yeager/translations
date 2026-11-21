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

86 tidigare oöversatta strängar sparades via Transifex API: Mac UI 25, Windows UI 58 och Windows UI-verktygstips 3.

## Tillämpad terminologi

Den tillhörande listan `handbrake-sv-terminology-20261121.md` styr bland annat: källfil, förinställning, kö, utdata, ljudspår, undertextspår, **kodek**, kodare, genomströmning, bildfrekvens, bithastighet, omslagsbild, metadata och loggfil.

## Granskningsfynd som redan är rättade

- 174 förekomster av det äldre `förval` rättades morfologiskt till `förinställning` i Linux UI, Mac UI och Windows UI. Exempel: `förvalet` → `förinställningen`; `förvalsfil` → `förinställningsfil`.
- 16 förekomster av `bitfrekvens`/ `bildhastighet` rättades till `bithastighet`/ `bildfrekvens`.
- VFR-hjälptexten i Linux UI skrevs om för korrekt och tydlig svenska.
- Sex kontextgranskade hjälprader i Mac UI och Windows UI förbättrades: bildstorlek, anamorfisk kodning, brusreducering, avflätning och skärpning. Produktetiketter som `None`, `Custom` och `Automatic` bevarades där de är UI-värden.
- Linux UI: `Encoder Preset` rättades från `Kodningförinställning` till `Kodarförinställning`. TrueHD-hjälptexten rättades från felstavade `ThrueHD` och fick korrekt böjning av `automatisk genomströmning`.
- Mac UI: tre källkontrollerade rader rättades: `Video encoder tune` → `Videokodarjustering`, plural/böjning i `Video encoder preset` och `Keep duplicate titles` → `Behåll dubblettitlar`.
- Windows UI: ködialogen rättades från `Dubbletta jobb` till `Dubblettjobb`. GPLv2-informationen rättades mot den engelska källsträngen: bland annat `handlighet`, `fFifth Floor`, licenshänvisningen och garantifriskrivningen.

## Verifiering

- API-statistiken visar 0 oöversatta strängar i samtliga fyra resurser.
- Full kontroll av 3 186 svenska rader fann inga verkliga skillnader i platshållare eller printf-format. En träff med procenttecken i löptext identifierades som falskt positiv.
- Hunspell-scan av Linux UI, Mac UI och de rättade Windows-raderna granskades manuellt. De flesta träffar är acceleratorbokstäver, egennamn, kodek- och filtertermer; dokumenterade sakfel sparades.
- `svlang` bedömde de rättade Windows-raderna. Dess återstående varningar gäller den officiella engelska postadressen och den sammansatta tekniska termen `köfil`.
- Formatsträngar och platshållare såsom `{0}`, `%1$d`, `%@` och `%.2f` bevarades.
