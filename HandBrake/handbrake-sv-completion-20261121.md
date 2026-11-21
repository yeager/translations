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

- Mac UI: 11 nya korrigeringar omfattar förinställningspluraler, målbläddring, kodningsjobb, förhandsbilders kvalitetstext och VideoToolbox-hårdvaruavkodare.

- Mac UI: 13 rader rättades i inställningar och undertexter: skivformat, processorkärnor, förinställningsböjning, måldiskens fria utrymme, Closed Caption-undertexter och språkligt korrekt inbränning.

- Mac UI: 18 rader rättades i videokodnings- och undertextvyerna. Åtgärderna omfattar DVD/Blu-ray, Closed Captions, flerpasskodning, datahastighet, spårval, pluraler och `%lu`-strängars svenska böjning utan att påverka platshållarna.

- Mac UI: 13 rader i dialoger och köhantering rättades, bland annat förinställningsplural, CSV-kapitelfel, titelval, åtgärd vid stopp samt kodningsslutförande. Platshållaren `%@` bevarades i de två statusmeddelandena.

- Mac UI: slutblocket innehöll åtta tydliga rättelser: lagrings-/visningsmått, främmande ljudsökning, filteretiketten `Skärpa` samt grammatiskt korrekta felmeddelanden för förinställningar. Berörda API-rader lästes tillbaka efter sparning; `DRC` kontrollerades särskilt efter återställning.

- Linux UI: radgranskning påbörjad. 22 rader rättades, inklusive förinställningsgenus och -plural, tvingade undertexter, SRT-förskjutning, ködetaljer, DVD-vinkel, iPod Atom och metadata-genomströmning.

- Linux UI: ytterligare 23 rader rättades i bild-, filter-, video- och undertextvyer. Förbättringarna omfattar bildpunktsförhållande, fyllningskanter, telecine, färgrymd/-omfång, bithastighet, Closed Captions och genomströmningsspårnamn.

- Linux UI: 28 ytterligare rader rättades: konsekvent automatiskt genomströmningsval för tolv ljudformat, dubblettitlar, skiftlägesokänsliga filändelser, HandBrake-namn, förhandsgranskning, tvingade undertexter och DRC-hjälptext.

- Linux UI: 15 nya radkorrigeringar omfattar ommixning, kapiteltermer, tvingade/inbrända undertexter, bildpunkts- och visningsförhållande, urvalsformuleringar samt korrekta filter- och bildkantsetiketter.

- Linux UI: slutblocket i den manuella genomgången gav 18 korrigeringar, bland annat avflätning, ljudkodek, oskarp mask, batterimeddelande, förinställningsplural, bildpunktsförhållande, bildfrekvensstatus, tidsenheter och målfilssystemets varning.

- Windows UI: radgranskning påbörjad. 29 källkontrollerade rader rättades, med fokus på förinställningars genus/plural, automatisk filnamngivning, kvalitets- och bildinställningar, felmeddelanden, WebM-undertexter och förklaringen för saknade källtitlar.

- Windows UI: ytterligare 24 rader rättades i system-, ljud- och filtervyer. Exempel är 64-bitarskravet, urklippet, automatisk genomströmning, reservkodare, avflätning, brusreducering, skärpning, DirectX-avkodning och förinställningspluraler.

- Windows UI: fem ytterligare inställningsrader rättades och sparades: enskilda kodningsloggar, DVD-läsning och systemfältsterminologi.

- Windows UI: 18 ytterligare rader rättades i video-, kö- och undertextvyer. Bland annat snabb avkodning, tvingade och Closed Caption-undertexter, förinställningsplural, åtgärder vid slutförande, mörkt tema, batteri-/diskutrymmesnotiser och språkvalsformuleringar.

## Verifiering

- API-statistiken visar 0 oöversatta strängar i samtliga fyra resurser.
- Full kontroll av 3 186 svenska rader fann inga verkliga skillnader i platshållare eller printf-format. En träff med procenttecken i löptext identifierades som falskt positiv.
- Hunspell-scan av hela granskningsunderlaget används som urvalsstöd; tekniska termer, produktetiketter och syntax bedöms i sitt sammanhang.
- `svlang` bedömde de rättade Windows-raderna. Dess återstående varningar gäller den officiella engelska postadressen och den sammansatta tekniska termen `köfil`.
- Formatsträngar och platshållare såsom `{0}`, `%1$d`, `%@` och `%.2f` bevarades.
