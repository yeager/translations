# msitools — master/po (sv)

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/msitools/master/po/sv/>
- Granskad och inskickad: 2026-11-23
- Aktuell POT: 34 aktiva meddelanden, 0 oöversatta och 0 fuzzy efter granskningen.

## Ändringar och validering

I den tidigare inskickade katalogen var `MSI_FILE` redan korrekt översatt som
`MSI-FIL`. Den aktuella rättelsen översätter `INPUT_FILE1 [INPUT_FILE2]` till
`INDATAFIL1 [INDATAFIL2]`. `msgfmt --check`, `msgcmp --use-fuzzy` och
`l10n-lint` är felfria. Filen laddades upp med kommentaren
`Granskad och klar`; API:t svarade `{"result":"OK"}`.

## Korrigering av kommandoradsmetavariabler (2026-11-24)

- 2 befintliga strängar korrigerade: beskrivande kommandoradsargument översatta till svenska.
- Validering: `msgfmt --check`; `l10n-lint`-regeln `metavariable-translation` ger inga kvarvarande träffar i de 295 granskade huvudgrenarnas kataloger.
- Den aktuella API-filen matchar den granskade PO-filen exakt; metavariabelrättelsen är redan publicerad. Ingen ny uppladdning behövs.
