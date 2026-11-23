# Obfuscate — master/po (sv)

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/obfuscate/master/po/sv/>
- Granskad och inskickad: 2026-11-23
- Aktuell POT: 50 aktiva meddelanden, 0 oöversatta och 0 fuzzy efter granskningen.

## Ändringar och validering

Två svenska formuleringar är rättade: varningen om osparade ändringar har
korrekt grammatik och procenttalet följer svensk typografi. `msgfmt --check`
och `msgcmp --use-fuzzy` är felfria; `l10n-lint` rapporterar 0 fel och 0
varningar. Informationsanmärkningen om acceleratorn gäller medvetet
`Ö_ppna fil`: `_Ö` får inte användas som nordisk accelerator. Filen laddades
upp med kommentaren `Granskad och klar`; API:t svarade `{"result":"OK"}`.
