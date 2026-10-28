# Skyrim Community Shaders: svensk port

Den aktuella utvecklingsrevisionen `d3099b19f79f62d12bebbcaae4b3aa1ec1d3b28a`
har 4 237 engelska nycklar. Den tidigare arkiverade porten innehöll 2 132
svenska nycklar från en äldre katalog. Av dessa matchar 2 081 fortfarande
nyckel för nyckel i den aktuella katalogen. De 308 utgångna eller omdöpta
nycklarna är inte med i den nya språkfilen.

`skyrim-community-shaders-sv-current-port-20261028.json` är den rena,
nyckelordnade svenska porten. Den innehåller 2 188 översatta nycklar och
utelämnar 2 049 nya nycklar, vilka enligt projektets dokumenterade i18n-regel
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
