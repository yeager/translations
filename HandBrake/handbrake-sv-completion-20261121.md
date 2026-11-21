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

Den tillhörande listan `handbrake-sv-terminology-20261121.md` styr bland annat: källfil, förinställning, kö, utdata, ljudspår, undertextspår, **kodek**, kodare, avkodare, genomströmning, bildfrekvens, bithastighet, omslagsbild, metadata och loggfil.

## Granskningsfynd som redan är rättade

- 174 förekomster av det äldre `förval` rättades morfologiskt till `förinställning` i Linux UI, Mac UI och Windows UI. Exempel: `förvalet` → `förinställningen`; `förvalsfil` → `förinställningsfil`.
- 16 förekomster av `bitfrekvens`/ `bildhastighet` rättades till `bithastighet`/ `bildfrekvens`.
- VFR-hjälptexten i Linux UI skrevs om för korrekt och tydlig svenska.
- Sex kontextgranskade hjälprader i Mac UI och Windows UI förbättrades: bildstorlek, anamorfisk kodning, brusreducering, avflätning och skärpning. Produktetiketter som `None`, `Custom` och `Automatic` bevarades där de är UI-värden.
- Linux UI: `Encoder Preset` rättades från `Kodningförinställning` till `Kodarförinställning`. TrueHD-hjälptexten rättades från felstavade `ThrueHD` och fick korrekt böjning av `automatisk genomströmning`.
- Mac UI: tre källkontrollerade rader rättades: `Video encoder tune` → `Videokodarjustering`, plural/böjning i `Video encoder preset` och `Keep duplicate titles` → `Behåll dubblettitlar`.
- Windows UI: ködialogen rättades från `Dubbletta jobb` till `Dubblettjobb`. GPLv2-informationen rättades mot den engelska källsträngen: bland annat `handlighet`, `fFifth Floor`, licenshänvisningen och garantifriskrivningen.
- Fortsatt helgranskning: åtta rader lästes tillbaka efter API-sparning. Mac UI fick korrekt parameteretikett för vänster kant och omarbetad beskrivning av förinställningar. Windows UI fick pluralformen `Förinställningar`. Fem Windows-verktygstips rättades för oöversatta engelska ord, stavning (`Brönn`), plural/böjning, semantik och den felvända höger/vänster-anvisningen för kodarreglaget.

- Windows-verktygstips: ytterligare 36 rader rättades och sparades direkt via API efter radgranskning. Ändringarna omfattar bland annat artefakter, brusreducering, telecine, behållarformat, bildpunktsförhållande, avflätning, skärpning, förinställningar, färgrymd samt svensk böjning och ordföljd i längre hjälptexter.

- Mac UI: 25 ytterligare källkontrollerade rader rättades och sparades. Bland annat ersattes den felaktiga översättningen `sorgkant` med `kant`, förinställningsböjningar rättades och `decoder` skiljdes korrekt från `encoder` som `avkodare` respektive `kodare`.

- Mac UI: 28 ytterligare rader lästes i sammanhang och 28 tydliga språk- eller terminologifel rättades och sparades direkt via API. Detta omfattar bland annat `Ny förinställning`, svenska UI-värden i bildstorleksdialogen, korrekt ommixningsbeskrivning, konsekvent genomströmning och korrigerade måttbeskrivningar.

- Mac UI: ytterligare 12 rader rättades efter radgranskning, inklusive översatta täljare/nämnare, anamorfisk hjälptext, rotationsinstruktion, ljudavstängning och köåtgärder.

- Mac UI: 11 ytterligare rader rättades: pluralformen av förinställningar, titelval till kön, MP4/iPod-hjälptext, tidsstämplar med tomma bildrutor, behållarformat och metadata-genomströmning.

## Verifiering

- API-statistiken visar 0 oöversatta strängar i samtliga fyra resurser.
- Full kontroll av 3 186 svenska rader fann inga verkliga skillnader i platshållare eller printf-format. En träff med procenttecken i löptext identifierades som falskt positiv.
- Hunspell-scan av hela granskningsunderlaget används som urvalsstöd; tekniska termer, produktetiketter och syntax bedöms i sitt sammanhang.
- `svlang` bedömde de rättade Windows-raderna. Dess återstående varningar gäller den officiella engelska postadressen och den sammansatta tekniska termen `köfil`.
- Formatsträngar och platshållare såsom `{0}`, `%1$d`, `%@` och `%.2f` bevarades.
