# iD Editor, presets routing, svenska

Datum: 2026-11-12
Projekt: iD Editor 2.42.3
Komponent: `presets`, delbatch för väg- och parkeringsförinställningar

10 kontextgranskade väg-, korsnings- och parkeringsposter skickades i en
Transifex API-batch och bekräftades i API-svaret. Efter inventeringen återstår
53 oöversatta poster i hela `presets`-resursen; de omfattar bland annat
kraftledningskonstruktioner och behandlas separat.

Kontroller: l10n-lint, svlang, hunspell-sv, `git diff --check` och Gitleaks
godkända. `msgfmt` är inte tillämpligt för JSON-resursen.
