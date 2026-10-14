# GDB 7.6, svensk granskning, batch 030

Granskade aktiva poster 1 451–1 500 rad för rad. Återställde felsaktigt översatta interna Darwin- och Mach-etiketter till källidentifierarna, rättade COW, lade till saknade kolon och behöll svenska för den synliga diagnostiktexten.

Validering: `msgfmt --check` godkändes. `l10n-lint` rapporterade 0 fel och 919 kvarvarande katalogvarningar. `svlang` rapporterar en kontextmedvetet godkänd varning för den bevarade GDB-syntaxen `...` i en kommandoanvisning. Hunspell-resultaten består av projektspecifika identifierare och tekniska termer som kontrollerades mot källtexten. Swedish FOSS Terminology exporterades och dess metadata kontrollerades. Gitleaks fann inga hemligheter i katalogen.
