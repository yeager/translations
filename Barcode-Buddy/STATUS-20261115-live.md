# Barcode Buddy – svensk status

Återläst från Hosted Weblate 15 november 2026.

Komponenten `strings` innehåller 37 enheter. Fem är införda som svenska
översättningar och 32 är fuzzy. För de 32 fuzzy-enheterna finns redan 42
väntande förslag från kontot `yeagersthlm2`; inga fler förslag skickades för
att undvika dubbletter.

Tio enheter har två konkurrerande förslag. De skiljer sig främst i ordval,
exempelvis *mängd* eller *antal*, *behandlade* eller *bearbetade* och
*tillstånd* eller *status*. De behöver väljas av en Weblate-granskare, inte
skrivas över automatiskt. De återstående 22 enheterna har ett förslag var.

De tidigare granskade råexporterna bevaras som `sv.json` och ändringsunderlag
som `sv-pending-20260918.json` respektive
`fuzzy-sv-reviewed-20260920.json`. Den senaste återläsningen bekräftar att
förslagen inte är godkända eller publicerade.

Kontroller för den här statusuppdateringen: JSON-validering av
ändringsunderlagen, `l10n-lint`, `git diff --check` och Gitleaks. `msgfmt`
är inte tillämpligt på statusfilen. Hunspell kördes inte för att begränsa
CPU-belastningen.
