# Eden Android: färgdesign för överlägg

Datum: 16 november 2026

## Omfattning

En färsk Transifex-avläsning visade att Android-resursen hade 53 oöversatta
svenska strängar. Samtliga hör till den nya funktionen för färgdesign av
skärmöverlägg: skapa, importera, exportera, spara och hantera egna
färgdesigner och förinställningar.

Måltexterna följer den befintliga Eden-terminologin med **överlägg**,
**inmatningsöverlägg** och **förinställning**. Produktnamn, spelplattformar
och filändelsen `.edenovl` är bevarade. Formuleringen "Läs in" används när
en sparad färgdesign öppnas från fil.

## Kontroller

- 53 av 53 måltexter har samma `%1$s`-platshållare som källan.
- Ingen ny em dash har införts.
- `l10n-lint` rapporterar inga fynd i batchfilen.
- Hunspell-SV träffar endast avsiktliga namn och termer: `.edenovl`,
  Famicom, GameCube, Hexfärg, Joy-Con, NES och spakklick.
- `svlang` gav bara falska V2-träffar i korrekta satser samt samma avsiktliga
  produkt- och facktermer. En verklig böjningsmiss, "din egna design",
  rättades till **din egen design** före uppladdningen.
- `git diff --check` och Gitleaks passerar.

## Uppladdning och återläsning

Samtliga 53 översättningar skickades med `PATCH` till Transifex API och
svarade med exakt sparad måltext. Därefter lästes varje enhet tillbaka med
`GET`; återläsningen gav 53 av 53 exakta matchningar.

Transifex rapporterar nu Android-resursen som **1 137 av 1 137** svenska
strängar, med **0 oöversatta** och **0 oöversatta ord**. Detta bekräftar
sparandet i Transifex, inte upstream-granskning, källsynk eller release.
