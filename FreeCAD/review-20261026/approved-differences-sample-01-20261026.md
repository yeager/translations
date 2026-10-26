# FreeCAD: första urvalet av godkända avvikelser

Den 26 oktober 2026 jämfördes det egna, redan uppladdade förslaget med den
valda översättningen i den aktuella Crowdin-exporten för de första 20 godkända
avvikelserna. Granskningen är läsande; inga röster eller ändringar skickades
till Crowdin.

## Bedömning

- De valda texterna för `Export styles to json file`, fyra Draft-matrisnamn,
  arbetsplanerna och `Font file` är mindre konsekventa än förslagen: bland
  annat används `json` i stället för `JSON` och flera svenska sammansättningar
  skrivs isär.
- De valda texterna för sträng-id 6630598, 6681242 och 6681290 innehåller
  dubblerade ord eller led: `visas`, `som`, `importeras` respektive `objekt`.
- Flera Draft-strängar återger produktnamnet som `Släppning` i stället för
  `Draft`, till exempel sträng-id 6496878, 6689600, 6689612 och 6689616.
  Det är sakligt fel i FreeCADs gränssnitt.
- Förslagen `Måttdetaljer`, `Standardarbetsplan`, `Radie för val av
  redigeringsnoder`, `OCA-områden` och `Förhandsgranskning` följer svensk
  sammansättnings- och fackterminologi bättre än de valda alternativen.

## Slutsats

Urvalet visar att godkänd status i Crowdin inte är en kvalitetsgaranti. De
berörda 20 posterna bör rättas individuellt i Crowdin efter kontextkontroll.
Massröstning är olämplig: tidigare försök har varken ersatt godkända texter
eller kunnat röstas på eget förslag.
