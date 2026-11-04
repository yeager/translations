# Blender Manual: svensk granskningsbatch 53

Datum: 4 november 2026

Källa: `exports/2026-11-04/blender-manual-manual-sv.po` samt de officiella
Blender 5.3-sidorna om Extensions, licenser och publicering.

## Kontext och omfattning

Sexton poster för dokumentation om Blenders utbyggnadssystem. Här skiljs
tre saker åt: de synliga dokumentationsorden (*tilläggsmoduler*,
*resursbibliotek*, *teman*), formella manifestvärden (till exempel
`"asset-library"` och `asset_library`) och kodidentifierare
(`PER_LIBRARY`, `FROM_REPOSITORY`). De två senare grupperna måste vara
identiska med källtexten, medan den kringliggande dokumentationstexten är
svensk.

Den synliga UI-etiketten `Allow Online Access` följer den aktuella
UI-katalogens **Tillåt nätåtkomst**. RST-mål, URL:er, API-egenskaper och
SPDX-licensnamn har bevarats exakt.

## Kontroller

- `msgfmt --check --statistics`: 16 översatta meddelanden och godkänd syntax.
- Radvis jämförelse av `(msgctxt, msgid)` mot råexporten: 16/16 träffar.
- `l10n-lint --language sv`: 0 fel och varningar. Informationsnotiser om
  oförändrad måltext gäller endast formella manifestvärden och
  kodidentifierare.
- `svlang skrivregler --enable-interpunktion`: inga skrivregelfel.
  `svlang svengelska` noterar `features` i en bevarad URL och är därför en
  falsk positiv träff.
- Hunspell `sv_SE` noterar enbart RST-roller, URL-delar, kodidentifierare,
  manifestvärden och licensnamn. De är medvetet oförändrade.
- `git diff --check` och Gitleaks: godkända, utan hemligheter.

Råexporten är orörd. Deltafilen är en lokal kandidat och är inte uppladdad
till Blender Translate.
