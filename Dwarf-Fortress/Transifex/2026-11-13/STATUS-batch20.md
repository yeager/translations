# Dwarf Fortress 50 `text_set`, batch 20

Datum: 13 november 2026

10 tidigare oöversatta rader har granskats och skickats i ett gemensamt
Transifex API-anrop. Batchen omfattar äventyrstext och namnmallar.
`[CONTEXT:…]`- och `[…]`-platshållarna är kontrollerade mot källan; flera
namnmallar är avsiktligt källika därför att de bara innehåller spelmotorns
variabler.

Kontroller: JSON, l10n-lint, platshållarparitet, Hunspell-sv, svlang,
Gitleaks och `git diff --check`. Hunspell- och svlangträffar gäller enbart
bevarade spelvariabler. `msgfmt` är inte tillämpligt på JSON-deltat.

Upstream: Transifex returnerade HTTP 200 med 10 uppdaterade poster 13
november 2026 18:24:15 UTC. Den omedelbara statistikåterläsningen var ännu
cachelagrad på 156/354; API-svaret bekräftar dock samtliga 10 exakta
måltexter med `origin: API`. Projektets ordinarie granskning återstår.
