# Calls — gnome-51/po

- **GNOME-katalog:** [calls/gnome-51/po/sv](https://l10n.gnome.org/vertimus/calls/gnome-51/po/sv/)
- **Källor:** aktuell PO, POT och API-statistik hämtade 2026-11-28. POT-datum: 2026-10-12 18:00+0000.
- **Före granskning:** 122/122 aktiva poster översatta, 0 fuzzy, 0 oöversatta.
- **Efter granskning:** 122/122 aktiva poster översatta, 0 fuzzy, 0 oöversatta. 0 nya översättningar och 42 ändrade befintliga poster.
- **Omfattning:** samtliga 122 aktiva poster granskade mot senaste POT. Obsoleta poster lämnades orörda. `Last-Translator` uppdaterat till Daniel Nylander <gnome@danielnylander.se>.
- **Inskickning:** inte inskickad till GNOME.

## Validering

- `msgfmt --check --check-format`: godkänd.
- `msgcmp --use-fuzzy` mot aktuell POT: godkänd; samma 122 aktiva nycklar.
- Platshållare, radbrytningar och markup kontrollerade; inga avvikelser. `translator-credits` undantaget från strukturell markupkontroll eftersom e-postadresserna innehåller vinkelparenteser.
- Acceleratorer granskade; inga nordiska tecken används som acceleratorer.
- `l10n-lint --language sv`: 0 fel, 0 varningar. Informationsnotiserna gäller oförändrade personnamn, citattecken kring `%s` och att acceleratorn i `_Close` flyttats till `T` i `S_täng`.
- `hunspell -d sv_SE -l`: flaggade personnamn (`Julian Sparber`, `Evangelos Ribeiro Tzaras`), produkt-/protokollnamn (`ModemManager`, `PSTN`, `SIP`, `TLS`, `USSD`, `VoIP`, `D-Bus`) och giltiga sammansättningar/termer (`Mediakryptering`, `orsakskod`, `tel-URI`) granskades manuellt. `true` bevaras som booleskt konfigurationsvärde. Inga ord lades till i ordlistan.

## Filer

- Original: `calls.gnome-51.sv.original.po`
- Granskad: `calls.gnome-51.sv.reviewed.po`
- Diff: `calls.gnome-51.sv.diff`
- POT: `calls.gnome-51.pot`
