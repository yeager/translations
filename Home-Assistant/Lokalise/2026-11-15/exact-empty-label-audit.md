# Home Assistant Core, svenska: kontroll av tomma etiketter

## Omfattning

En fullständig läsning via Lokalise API av projektet **Home Assistant - Core**
(projekt-ID `130246255a974bd3b5e8a1.51616605`). Sökningen omfattade samtliga
150 API-sidor och 74 564 svenska översättningar som returnerades under
genomgången.

## Resultat

Inga svenska översättningar innehåller något av orden `Tom`, `Tomt` eller
`Tomma`. Inga ändringar behövde sparas.

Det är viktigt att skilja en synlig etikett med innebörden *empty* från ett
avsiktligt tomt strängvärde. De senare ska även fortsättningsvis vara tomma,
inte översättas till "Tom".

## Verifiering

- Lokalise API:s paginering gick igenom sidorna 1--150.
- Varje returnerad svensk översättning kontrollerades med ordgränser för
  `Tom`, `Tomt` och `Tomma`.
- Träffar: 0.

## Status

Ingen uppladdning behövdes. Detta är en läsverifiering av den aktuella
upstream-statusen i Lokalise, inte ett påstående om att hela den svenska
lokaliseringen i övrigt är språkgranskad.
