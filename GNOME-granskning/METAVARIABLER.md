# GNOME: granskning av kommandoradsmetavariabler

Granskningsdatum: 2026-11-24.

Gick igenom samtliga 307 arkiverade `*.reviewed.po`-kataloger med l10n-lints svenska regel för beskrivande metavariabler: 107 324 poster kontrollerades. Efter rättningarna återstår 0 träffar.

## Rättade kataloger

- [fwupd/main/po](fwupd/main/po/README.md): `METAINFO` översattes till `METADATA` i två strängar. Den aktuella Damned Lies-katalogen har 1 054 översatta, 6 fuzzy och 3 oöversatta av 1 063; den äldre arkiverade katalogen måste uppdateras mot senaste POT innan modulen kan markeras klar.
- [NetworkManager/main/po](networkmanager/main/po/README.md): tre förekomster av den beskrivande etiketten `ARGUMENTS` ändrades till `ARGUMENT` i hjälpsyntaxen. Aktuell status är 2 520 översatta, 15 fuzzy och 31 oöversatta av 2 566; den arkiverade filen behöver fortsatt omgranskning mot senaste POT.

## Bevarade värden

Flaggor, miljövariabler, formatmarkörer, protokollnamn, produktnamn och faktiska kommandon/identifierare lämnas oförändrade. Där engelska och svenska metavariabler har samma etablerade form, exempelvis `ID`, `URI`, `DATA` och `VERSION`, är oförändrad stavning inte ett översättningsfel. Se även [GNOME-terminologin](TERMINOLOGI.md#kommandoradsmetavariabler).

## Validering

`msgfmt --check` godkänd för båda ändrade katalogerna. `l10n-lint --language sv --checks metavariables` rapporterade 0 fel och 0 varningar i samtliga 307 arkiverade granskade kataloger. Inget har skickats till GNOME.
