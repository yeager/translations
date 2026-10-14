# GDB 7.6, svensk granskning, batch 084

Granskade aktiva poster 4 151–4 200 rad för rad. Rättade fjärrspårning, avbrottssekvenser, minnespaket, fjärrprotokoll, kommandon och svensk interpunktion. Identifierare, paketnamn, parametrar och platshållare är bevarade.

Validering: `msgfmt` godkändes. `l10n-lint` rapporterade 0 fel och 570 befintliga varningar i hela katalogen. `svlang` rapporterade elva kända syntaxträffar för bevarade GDB-kommandon och `...`. Hunspell, svensk terminologi och översättningsminnet kontrollerades. Gitleaks hittade inga hemligheter.
