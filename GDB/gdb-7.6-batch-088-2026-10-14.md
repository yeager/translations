# GDB 7.6, svensk granskning, batch 088

Granskade aktiva poster 4 351–4 400 rad för rad. Rättade seriella portar, fjärrsessionsinspelning, underprocesser, socketanslutningar, hårdvaruflödeskontroll, register och svenska böjningar. Kodidentifierare, kommandon, platshållare och radbrytningar är bevarade.

Validering: `msgfmt` godkändes. `l10n-lint` rapporterade 0 fel och 566 befintliga varningar i hela katalogen. `svlang` rapporterade elva kända syntaxträffar för bevarade GDB-kommandon och `...`. Hunspell och svensk terminologi kontrollerades. Gitleaks hittade inga hemligheter.
