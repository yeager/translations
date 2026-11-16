# Cataclysm-DDA, svenska: batch 56

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De gäller syrebrist, anfall och skjutvapen.

Källkontexten kontrollerades i `src/avatar_action.cpp`. ”Tur” används för
spelets enskilda *turn*, och ”räckviddsattack” för ett anfall som utnyttjar ett
vapens räckvidd. Platsmarkörerna i skjutvapenmeddelandena är bevarade och den
engelska utelämningen i källtexten är behållen.

## Kontroller före API-inskick

- Platsmarkörer ska stämma mellan källa och mål.
- `l10n-lint --language sv --json-format auto` ska passera utan varningar eller fel.
- Hunspell-SV och svlang ska granskas manuellt för sammansättningar och
  projektspecifika termer.
- Ingen otillåten em dash får tillföras. `msgfmt` är inte tillämpligt eftersom
  Transifex API tar enskilda JSON-översättningar, inte en PO-katalog.

## Inskick och återläsning

Den 16 november 2026 sparades samtliga tio översättningar via Transifex API.
En ny, oberoende GET-återläsning jämförde sedan varje målsträng med denna
batch. Alla 10 av 10 stämde exakt.

svlang rapporterade en naturlighetspoäng på 10 av 10 utan språkvarningar.
Hunspell-SV gav bara normal analysutmatning och inga stavningsfel.
