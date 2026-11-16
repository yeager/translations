# Cataclysm-DDA, svenska: batch 29

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De gäller sortering, vätsketömning och
reparation av föremål.

Källkontexten kontrollerades i `src/activity_actor.cpp` och
`src/activity_handlers.cpp`. `refit` betyder här att anpassa ett föremåls
passform, inte att montera om teknisk utrustning. Den dynamiska benämningen
på vätskepumpen sätts ihop med bindestreck som `%s-pumpen`.

## Kontroller före API-inskick

- Platsmarkörer, inklusive `%s`, `%d`, `%1$s` och `%2$s`, ska stämma mellan
  källa och mål.
- `l10n-lint --language sv --json-format auto` ska passera utan varningar eller fel.
- Hunspell-SV och svlang ska granskas manuellt för sammansättningar,
  platshållare och projektspecifika termer.
- Ingen otillåten em dash får tillföras. `msgfmt` är inte tillämpligt eftersom
  Transifex API tar enskilda JSON-översättningar, inte en PO-katalog.

## Inskick och återläsning

Den 16 november 2026 sparades samtliga tio översättningar via Transifex API.
En ny, oberoende GET-återläsning jämförde sedan varje målsträng med denna
batch. Alla 10 av 10 stämde exakt.

svlang markerade två förväntade falska träffar i en korrekt `eftersom`-bisats
och imperativfraser. Hunspell-SV rapporterade inga avvikelser.
