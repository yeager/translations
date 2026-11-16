# Cataclysm-DDA, svenska: batch 34

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De gäller zonuppgifter, insamling av verktyg,
stockhuggning och arbetsplatser som är för mörka.

Källkontexten kontrollerades i `src/activity_item_handling.cpp`. `task`
översätts konsekvent som `uppgift`. Den ovanliga formatmarkören `%1s` bevaras
oförändrad eftersom den finns så i upstream-källan och får sitt namnargument i
anropet.

## Kontroller före API-inskick

- Platsmarkörer, inklusive den ovanliga `%1s`, ska stämma mellan källa och mål.
- `l10n-lint --language sv --json-format auto` ska passera utan varningar eller fel.
- Hunspell-SV och svlang ska granskas manuellt för sammansättningar,
  platshållare och projektspecifika termer.
- Ingen otillåten em dash får tillföras. `msgfmt` är inte tillämpligt eftersom
  Transifex API tar enskilda JSON-översättningar, inte en PO-katalog.

## Inskick och återläsning

Den 16 november 2026 sparades samtliga tio översättningar via Transifex API.
En ny, oberoende GET-återläsning jämförde sedan varje målsträng med denna
batch. Alla 10 av 10 stämde exakt.

svlang rapporterade inga språkvarningar. Hunspell-SV markerade endast den
avsiktligt bevarade formatmarkören `%1s`.
