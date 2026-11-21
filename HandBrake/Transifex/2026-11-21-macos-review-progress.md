# HandBrake – macOS UI: pågående svensk radgranskning

Datum: 2026-11-21  
Plattform: Transifex API  
Resurs: `o:HandBrakeProject:p:mac-ui:r:enxliff`

## Aktuell inventering

Den aktuella svenska XLIFF-exporten innehåller 1 285 trans-units och inga tomma målsegment. Exporten hämtades via Transifex API före granskningen. Synliga tekniska filternamn jämfördes med den redan kontrollerade Linux-resursen och HandBrake-terminologilistan; filformat, kodeker och algoritmnamn lämnades oförändrade där de ska fungera som egennamn.

## Sparade och API-återlästa ändringar

| Fullständig Transifex-resurssträng | Engelska | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- | --- |
| `o:HandBrakeProject:p:mac-ui:r:enxliff:s:27727a36fae59b5260d01ed20d0abd73` | Chroma Smooth | Chroma Smooth | Kromautjämning | Synligt generiskt filternamn, redan etablerat i Linux UI. |
| `o:HandBrakeProject:p:mac-ui:r:enxliff:s:535f806857e989b59118dec6e43ddc35` | Comb Detect | Comb Detect | Comb-identifiering | Synligt generiskt filternamn, konsekvent med Linux UI. |
| `o:HandBrakeProject:p:mac-ui:r:enxliff:s:993aec0efffb6db77f0b96ea16f20175` | Deblock | Deblock | Blockborttagning | Synligt generiskt filternamn, konsekvent med Linux UI. |
| `o:HandBrakeProject:p:mac-ui:r:enxliff:s:725b7fcf22ffb8b8ff01c7ea3b2f4334` | Deinterlace | Deinterlace | Avflätning | Generiskt filternamn; svensk terminologi används i Linux UI. |
| `o:HandBrakeProject:p:mac-ui:r:enxliff:s:81416eb1f1248dbb22687f93b8547b74` | Denoise | Denoise | Brusreducering | Generiskt filternamn; svensk terminologi används i Linux UI. |

Varje ändring skickades via Transifex REST API och lästes tillbaka från sitt `resource_translation`-objekt.

## Verktyg

`l10n-lint --language sv` gav inga anmärkningar för ändringsmängden. Hunspell markerar `Kromautjämning` och `Comb-identifiering` som domänord, men inte som upptäckta stavfel; den manuella jämförelsen mot HandBrakes Linux UI har företräde. `svlang check` gav 10,0/10 och markerade samma två tekniska termer som ovanliga.

## Status

Inventering och de första säkra, synliga filterrättningarna är gjorda. Den semantiska radgranskningen av återstående macOS-strängar fortsätter. Rapporten innebär inte att macOS UI eller HandBrake som helhet är färdiggranskade.

## Fortsatt radgranskning – 2026-11-21

Färsk Transifex-hämtning omfattade 1 281 aktuella macOS-strängar. Nio ändringar sparades och återlästes via API:

| Engelska | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| Passthru Common Metadata | Genomström vanliga metadata | För över vanliga metadata | Begriplig svensk åtgärdsform. |
| Bottom/Top/Left/Right edge cropping amount in pixels (åtta punkt- och icke-punktvarianter) | Beskäring … | Beskärning … | Rätt svenskt ord; enhetlig formulering och bevarad interpunktion. |

l10n-lint med språk=sv gav 0 fel i den samlade aktuella katalogen. Hunspell-sv markerade inte de sparade texterna.


### Fortsatt semantisk kontroll

Sparade och API-återlästa: **Passthru Fallback:** → **Reservkodning vid genomströmning:**; två **Forced Only** → **Endast tvingade**; två längre hjälpposter för *Track Selection Behavior* med korrekta alternativnamn, utan dubbel negation och med bevarade radbrytningar; **Muxing…** → **Muxning…**.
