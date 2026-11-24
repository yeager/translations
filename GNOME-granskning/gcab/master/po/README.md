# gcab — master/po (sv)

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/gcab/master/po/sv/>
- Granskad och inskickad: 2026-11-23
- Aktuell POT: 34 aktiva meddelanden, 0 oöversatta och 0 fuzzy efter granskningen.

## Ändringar och validering

Sex poster är rättade. Kommandoradsidentifierarna `DIR`, `FILE` och
`INPUT_FILES` återställs exakt från källan; återstående rättningar förbättrar
svensk formulering. `msgfmt --check`, `msgcmp --use-fuzzy` och `l10n-lint` är
felfria. Filen laddades upp med kommentaren `Granskad och klar`; API:t svarade
`{"result":"OK"}`.

## Korrigering av kommandoradsmetavariabler (2026-11-24)

- 3 befintliga strängar korrigerade: beskrivande kommandoradsargument översatta till svenska.
- Validering: `msgfmt --check`; `l10n-lint`-regeln `metavariable-translation` ger inga kvarvarande träffar i de 295 granskade huvudgrenarnas kataloger.
- Ändringen är lokal och har inte skickats till GNOME.
