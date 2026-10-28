# Skyrim Community Shaders: svensk port

Den aktuella utvecklingsrevisionen `d3099b19f79f62d12bebbcaae4b3aa1ec1d3b28a`
har 4 237 engelska nycklar. Den tidigare arkiverade porten innehöll 2 132
svenska nycklar från en äldre katalog. Av dessa matchar 2 081 fortfarande
nyckel för nyckel i den aktuella katalogen. De 308 utgångna eller omdöpta
nycklarna är inte med i den nya språkfilen.

`skyrim-community-shaders-sv-current-port-20261028.json` är den rena,
nyckelordnade svenska porten. Den innehåller 2 081 översatta nycklar och
utelämnar 2 156 nya nycklar, vilka enligt projektets dokumenterade i18n-regel
faller tillbaka till engelska. Den är därför en säker partiell första
upstreaminsändning, inte en komplett svensk katalog.

Kontroller 2026-10-28:

- Projektets `extract-i18n.py --check` och `--orphans` passerar.
- Projektets `sort-i18n.py --check` passerar.
- Alla platshållare i de 2 081 svenska posterna matchar engelskan.
- `l10n-lint` rapporterar inga fel och en avgränsad Gitleaks-körning rapporterar
  inga fynd.
- svlangs enda skrivregelträff är den bevarade spelvariabeln
  `fGrassStartFadeDistance`; Hunspell-träffarna är spel-, shader-, fil- och
  API-termer som har granskats i kontext.

Projektets senaste release, v1.9.1, publicerades 2026-09-24 och uppfyller
48-månaderskravet. Nästa steg är en upstream-PR med den partiella svenska
filen; den återstående katalogen behöver delas upp i granskningsbara satser.
