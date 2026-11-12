# Nextcloud – svenska småkomponenter

6 tidigare oöversatta svenska strängar granskades i Nextclouds UI- och säkerhetskontext och skickades 2026-11-12: `client`, `end_to_end_encryption`, `files_pdfviewer`, `ios-plurals`, `tvshownamer` och `user_ldap`.

Varje resurs validerades med l10n-lint, svlang, Hunspell, `git diff --check` och Gitleaks. `msgfmt` är inte tillämpligt för Transifex JSON-resurser; l10n-lint och Transifex API:s godkända import är formatvalideringen. Hunspell-träffar avser produktnamn, format, filändelser eller platshållare. En separat Transifex API-batch per resurs gav HTTP 200, och ny API-läsning visade 0 återstående strängar i alla sex resurser.
