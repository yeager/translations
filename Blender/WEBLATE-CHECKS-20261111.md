# Blender UI: Weblate-kontroller 11 november 2026

Den aktuella Weblate-vyn för Blender UI/Svenska visade 31 aktiva, fallerande
kontroller. Varje post är redan översatt. De två kontrollgrupperna nedan har
lästs i den inloggade komponentvyn och bedömts i sin UI- och teknikkontext.

## Oförändrad översättning: 19 poster

Kontrollen träffar synliga Blender-namn, etablerade färg- och
codec-/formatnamn eller språk-/kodidentifierare som avsiktligt behålls:
`B-Bone`, `Filmic Log`, `Filmic sRGB`, `BT.2020 2.4 Exponent EOTF Display`,
`ProRes 422 Proxy`, `Curl`, `Spray`, `Initial`, `Ping Pong`, `Disk`,
`Boids 2D`, `Cinema (48)`, `Cinema`, `Sampling`, `Bendy Bones`,
`Swahili - Kiswahili`, `Power`, `%sAction` och `AgX - SDR`.

De ska inte ändras enbart för att undvika kontrollen. Flera är synliga
funktionsnamn, andra är standardiserade namn på färgrymd, format eller språk.
`%sAction` innehåller dessutom en kodplatshållare.

## Flera versaler: 12 poster

Kontrollen utlöses av nödvändiga tekniska förkortningar och bevarade
UI-/kodnamn, inte av svensk rubrikstil. De berör bland annat `UI`, `PO`,
`ID`, `UV`, `URL`, `ZIP` och `VR` i följande texter:

- Deklaration av uttag och UI-paneler för en nodgrupp
- Uppdatera i18n-arbetsförrådet (PO-filer)
- Nästlad nod-ID för noden
- Packa UV-öar
- Lägg till eller ta bort extern funktionsuppsättning (..., UI-mallar)
- Använd fjärr-URL
- En ZIP-fil `{!r}` förväntades
- Tre UV-uppackningsfeltexter
- Visa vyporten med VR-glasögon (huvudmonterade skärmar)

Versalerna är semantiskt korrekta. De ska därför behållas; att skriva ut
förkortningarna eller förvanska dem skulle göra UI:t mindre igenkännbart och
strida mot källans API- och formatnamn.

## Status

Detta är en lokal bedömning av den aktuella Weblate-vyn. Inga Weblate-
kontroller har avfärdats och ingen översättning har ändrats som följd av
genomgången. De 31 aktiva kontrollerna är därmed dokumenterade som sakliga
falsklarm för den aktuella katalogen.
