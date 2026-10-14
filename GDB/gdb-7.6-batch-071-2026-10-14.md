# GDB 7.6, svensk granskning, batch 071

Granskade aktiva poster 3 501–3 550 rad för rad. Rättade OS-data, expressionsparser, registerdiagnostik, decimala flyttal och svensk stil. Identifierare, platshållare och syntax är bevarade.

Validering: `msgfmt` godkändes. `l10n-lint` rapporterade 0 fel och 653 befintliga varningar i hela katalogen. `svlang` rapporterade nio kända syntaxträffar för bevarade GDB-kommandon och `...`. Hunspell, svensk terminologi och översättningsminnet kontrollerades. Gitleaks hittade inga hemligheter.
