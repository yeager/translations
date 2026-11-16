# Inläsning av innehåll, batch 122

En API-baserad genomgång av samtliga 74 593 nycklar identifierade 84 svenska
översättningar med en form av `ladda` där den engelska källtexten innehöll
`load`. Varje träff bedömdes i sitt sammanhang. Den här batchen omfattar bara
de tio där *load* faktiskt betyder att läsa in innehåll eller data.

Elektrisk last, laddning, uppladdning och en integrations livscykel lämnades
orörda. Där är `ladda` eller `last` rätt ord.

Yoto-strängen rättar även ett överflödigt `{error}` i målet. Källtexten saknar
motsvarande platshållare.

## Resultat

Batchen skickades via Lokalise API den 16 november 2026. Samtliga 10
översättningar sparades och hämtades därefter på nytt från API:t. Återläsningen
matchade de granskade texterna för varje nyckel.

`l10n-lint` godkände JSON-deltat. Platshållarna kontrollerades separat mot
källtexterna; inga avvikelser återstod. Hunspell-SV markerade bara egennamnet
Yoto, medan svlang inte hittade några anglicismer. Svlangs radbaserade
interpunktionsvarningar gällde kontrollens sammanslagna indata, inte de
enskilda översättningarna.
