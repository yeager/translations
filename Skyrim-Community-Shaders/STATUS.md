# Skyrim Community Shaders: svensk port

Den aktuella utvecklingsrevisionen `d3099b19f79f62d12bebbcaae4b3aa1ec1d3b28a`
har 4 237 engelska nycklar. Den tidigare arkiverade porten innehöll 2 132
svenska nycklar från en äldre katalog. Av dessa matchar 2 081 fortfarande
nyckel för nyckel i den aktuella katalogen. De 308 utgångna eller omdöpta
nycklarna är inte med i den nya språkfilen.

`skyrim-community-shaders-sv-current-port-20261028.json` är den rena,
nyckelordnade svenska porten. Den innehåller 2 573 översatta nycklar och
utelämnar 1 664 nya nycklar, vilka enligt projektets dokumenterade i18n-regel
faller tillbaka till engelska. Den är därför en säker partiell första
upstreaminsändning, inte en komplett svensk katalog.

Kontroller 2026-10-28:

- Projektets `extract-i18n.py --check` och `--orphans` passerar.
- Projektets `sort-i18n.py --check` passerar.
- De 89 nytillagda TM-posterna har entydig svensk måltext, exakt samma aktuella
  engelska källa och bevarade klammerplatshållare.
- `l10n-lint` rapporterar inga fel och en avgränsad Gitleaks-körning rapporterar
  inga fynd.
- svlangs enda skrivregelträff är den bevarade spelvariabeln
  `fGrassStartFadeDistance`; Hunspell-träffarna är spel-, shader-, fil- och
  API-termer som har granskats i kontext.

Efter den första porten jämfördes även de lokala Open Shaders-arkiven mot den
aktuella engelska källan. Endast 18 poster hade både oförändrad källa och en
entydig tidigare granskad svensk måltext; de lades till i PR:n. Hundra poster
med ändrad engelsk källa lämnades avsiktligt för manuell granskning.

Ytterligare 89 poster valdes ur `swedish-tm` efter exakt jämförelse med den
aktuella engelska källan och manuell kontextkontroll. Tvetydiga, felkodade och
oförändrade kandidater lämnades utanför. I samma genomgång återställdes `%s` i
ett äldre Nsight Perf-felmeddelande, eftersom programkoden skickar ett dynamiskt
byggtips till den strängen.

Sju ytterligare etiketter översattes därefter efter kontroll av deras exakta
användningsställen i koden: färggraderingsreglage, manuellt fokus,
uppskalningsförinställningen, ett inläsningsfilter och palettens Esc-hjälp.

CS-redigerarens grundetiketter har därefter granskats i en sats om 28 poster:
statusbrickor, filter, kopieringsåtgärder, baslager och grundinställningar.
Projektets termer `Editor ID`, `Form ID`, Effects 11 och Community Shaders
har behållits där de identifierar egna format eller komponenter.

En följande sats om 21 poster täcker navigering, kategorier, förinställningar,
sparade JSON-åsidosättningar och felmeddelanden i CS-redigeraren. Den befintliga
tekniktermen `Linsöverstrålning` har behållits konsekvent också i plural.

CS-redigerarens felsökningsvy har kompletterats med 38 korta statusfält för
celler, väder, scenposter, lager, platsdata och förinställningar. Tekniska
diagnostikbegrepp med oklarare funktionell innebörd har avsiktligt lämnats till
en senare kontextgranskning.

Ytterligare 42 generella diagnostikfält har översatts: tillstånd, tid, väder,
scendata, övergångar och resolverns status. Hunspell markerar endast de
projektspecifika sammansättningarna `Resolverns` och `Scentypposter`; de är
granskade i kod- och gränssnittskontext.

Sparning och förinställningar i CS-redigeraren har kompletterats med 19
strängar. Katalogen omfattar nu återställning, JSON-åsidosättningar,
felhantering och lokala sparåtgärder med samtliga platshållare bevarade.

Platsbläddraren i CS-redigeraren har kompletterats med 40 strängar för
platstyper, filter, redigering, borttagning och platsprioritet. `Form ID` och
`Editor ID` följer den befintliga svenska terminologin som formulär-ID och
redigerar-ID.

Scenkopieringsvyn har kompletterats med 36 korta kontroller, räknare och
hjälptexter för urval, mål, perioder och överskrivning. Alla
klammerplatshållare i satsen har jämförts med den engelska källan.

Exportdialogens 37 etiketter, räknare och korta resultatmeddelanden är
översatta. Produktförkortningen CS är medvetet bevarad i `CS-förinställning`.

Scenhanterarens grundetiketter och dess korta hjälptexter har kompletterats
med 17 poster. Interna ID:n efter `##` och tekniska namn som `Baseline` har
bevarats, medan gränssnittstexten använder den etablerade terminologin
`förinställning` och `åsidosättning`.

Exportpanelens första 23 poster har också granskats: spärrmeddelanden,
filstatus, räknare, kolumnrubriker och korta hjälptexter. Alla
klammerplatshållare och kortkommandot `Ctrl+Shift+S` har bevarats.

Scenhanterarens nästa 23 poster omfattar exportpaketens status,
funktionsåsidosättningar samt tids- och väderövergångar. Även här har interna ID:n,
klammerplatshållare och kortkommandon bevarats exakt.

Den avslutande scenhanterarsatsen med 15 poster täcker exportpanelen helt,
inklusive dess flerradiga arbetsflödeshjälp. Därmed har samtliga
`feature.scene_manager`-nycklar en svensk måltext i den aktuella katalogen.

Förinställningsmenyn har kompletterats med 21 poster för aktiva paket och
teman, Baseline-inställningar samt kompatibilitetsvarningar. De dynamiska
klammerplatshållarna för versioner, funktioner och insticksmoduler är
bevarade oförändrade.

Projektets senaste release, v1.9.1, publicerades 2026-09-24 och uppfyller
48-månaderskravet. Den partiella filen skickades som
[PR #3051](https://github.com/community-shaders/skyrim-community-shaders/pull/3051)
2026-10-28. PR:n är öppen och väntar på CI och uppströmsgranskning. Den
återstående katalogen behöver delas upp i granskningsbara satser.

PR:n riktades först felaktigt mot `main`, vilket gav en orelaterad
versionsgranskningsvarning. Den riktades om till projektets standardgren
`dev`; diffen omfattar nu endast `sv.json`. GitHub väntar på att en
underhållare godkänner arbetsflödeskörning för forken. Ingen lokalt eller
upstream påvisad översättningskontroll har felat.
