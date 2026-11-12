# Widelands – svensk granskning

Datum: 2026-11-12  
Projekt: `o:widelands:p:widelands`  
Komponent: `appdata`  
Källa: Transifex API, befintliga svenska översättningar.

## Status

- Widelands v1.3.1 släpptes 2026-02-22.
- Alla 34 komponenter har 0 oöversatta svenska strängar.
- Samtliga saknar dock Transifex granskningsmarkering; full språkgranskning sker komponentvis.
- `appdata`: 14 strängar granskade rad för rad, 6 verkliga språkfel rättade och uppladdade i en API-batch (HTTP 200). Läsning av varje enskild uppdatering via API bekräftade att den sparats.
- `editor`: 20 strängar granskade rad för rad, 8 verkliga språkfel rättade och uppladdade i en API-batch (HTTP 200). Läsning av varje enskild uppdatering via API bekräftade att den sparats.
- `map_plateau`: 25 strängar granskade rad för rad, 10 verkliga språkfel rättade och uppladdade via API. Kontroll av enskilda uppdateringar bekräftade att de sparats.
- `map_river`: 86 strängar granskade rad för rad, 21 verkliga språkfel rättade och uppladdade i en API-batch (HTTP 200). Kontroll av varje uppdatering via API bekräftade att den sparats. Varningarna från l10n-lint och svlang gäller procentplatshållarna `%1%`, `%2%` och `%3%`, som måste bevaras exakt.
- `mp_scenario_island_hopping`: 27 strängar granskade rad för rad, 12 verkliga språkfel rättade och uppladdade i en API-batch (HTTP 200). Kontroll av varje uppdatering via API bekräftade att den sparats.
- `mp_scenario_smugglers`: 19 strängar granskade rad för rad, 7 verkliga språkfel rättade och uppladdade i en API-batch (HTTP 200). Kontroll av varje uppdatering via API bekräftade att den sparats. l10n-lint missar siffran 10 när den skrivs idiomatiskt som ”tionde”; detta är en falsk positiv informationsnotis.
- `scenario_dummy`: 2 strängar granskade rad för rad, 2 idiomatiska korrigeringar uppladdade i en API-batch (HTTP 200) och verifierade via API.
- `training_wheels`: 46 strängar granskade rad för rad, 8 korrigeringar uppladdade i en API-batch (HTTP 200) och verifierade via API.
- `win_conditions`: 70 strängar granskade rad för rad, 10 korrigeringar uppladdade i en API-batch (HTTP 200) och verifierade via API. Hunspell-träffen `skogsgnom` är projektspecifik terminologi.
- `scenario_emp01`: 70 strängar granskade rad för rad, 4 säkra korrigeringar uppladdade i en API-batch (HTTP 200) och verifierade via API. Deltafilen var först felmärkt som `scenario_atl01`; API:t avvisade den före ändringar sparades, och komponent-ID:t rättades innan den godkända uppladdningen.
- `scenario_atl02`: 150 strängar granskade rad för rad, 16 korrigeringar uppladdade i en API-batch (HTTP 200) och verifierade via API.
- `scenario_bar01`: 150 strängar granskade rad för rad. 9 korrigeringar uppladdade i rätt komponent och verifierade via API. Tre felmärkta rader hörde till `scenario_emp01`; de laddades upp och verifierades där separat.
- `scenario_emp02`: 88 strängar granskade rad för rad, 17 verkliga språkfel rättade och uppladdade i en API-batch (HTTP 200). Direkt läsning av samtliga uppdateringar via API bekräftade att de sparats. Hunspell-träffarna är egennamnen Amalea, Fremil, Malac och Saledus. l10n-lints enda varning är en medveten, idiomatisk omformulering som inte bevarar källans kolon. Svlangs V2- och anglicismmarkeringar har bedömts i sitt berättelse- och spelsammanhang.
- `scenario_emp03`: 150 strängar granskade rad för rad, 40 verkliga språkfel rättade och uppladdade i en API-batch (HTTP 200). Direkt läsning av samtliga uppdateringar via API bekräftade att de sparats. l10n-lint hittade inga fel; svlangs V2-markeringar är kontextberoende. Hunspell-träffarna är egennamnen Amalea, Fremil, Lutius och Saledus.
- `scenario_emp04`: 292 strängar granskade rad för rad, 54 verkliga språkfel rättade och uppladdade i en API-batch. Direkt läsning av samtliga uppdateringar via API bekräftade att de sparats. l10n-lint, JSON-/plural- och em-dash-kontroller, diffkontroll och Gitleaks passerade. Svlangs V2-markeringar är kontextberoende; Hunspell-träffarna är egennamnen Amalea, Lutius och Saledus samt projektspråkets `rustningsdelar`.
- `scenario_fri01`: 150 strängar granskade rad för rad, 44 verkliga språkfel rättade och uppladdade i en API-batch (HTTP 200). Direkt läsning av samtliga uppdateringar via API bekräftade att de sparats. l10n-lint har två kontextuella varningar för källans kolon, medan svlangs V2-markeringar gäller berättelsetext. Hunspell-träffarna är egennamn och projektspecifika sammansättningar.
- `scenario_fri02`: 141 strängar granskade rad för rad, 38 verkliga språkfel rättade och uppladdade i en API-batch. Direkt läsning av samtliga uppdateringar via API bekräftade att de sparats. l10n-lint, JSON-/plural- och em-dash-kontroller, diffkontroll och Gitleaks passerade. Svlangs V2-markeringar är berättelsekontext och Hunspell-träffarna är egennamn (Langeneß, Murilius, Reebaud/Reebaude och Terrae Septentrionalis).
- `scenario_fri03`: 93 strängar granskade rad för rad, 37 verkliga språkfel rättade och uppladdade i en API-batch. Direkt läsning av samtliga uppdateringar via API bekräftade att de sparats. Terminologin kompletterades med `port space` → `hamnplats` och `diking` → `dikning`. l10n-lint, JSON-/plural- och em-dash-kontroller, diffkontroll och Gitleaks passerade; svlangs och Hunspells träffar är berättelsekontext respektive egennamn.

## Kontroller

- `git diff --check` och `gitleaks` passerade för varje uppladdad batch. Resultat från l10n-lint, svlang och hunspell har bedömts i kontext och dokumenterats per komponent när de inte är verkliga fel.
- `msgfmt` är inte tillämpligt på denna Transifex JSON-deltafil; ingen rå PO-export har ändrats.
