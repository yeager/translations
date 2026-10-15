# Devscripts, svensk granskning, batch 7

Granskade poster 401–450 rad för rad. Rättade naturligt språk i kommandobeskrivningar, ersatte förkortningen `ej`, och tog bort svenska tankstreck där de inte behövdes.

Validering: `msgfmt` och `l10n-lint` godkändes utan fel. `svlang`, Hunspell, svensk terminologi, översättningsminne och Gitleaks kontrollerades. `l10n-lint` rapporterar 284 redan befintliga varningar utanför batchens ändringar. En `svlang` träff kommer från ett oförändrat CLI-exempel där mellanslaget före kommat är betydelsebärande kommandoformatering.
