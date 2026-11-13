# Audacity: radbrytningar i dialoger

Fem radgranskade poster återställer källtextens radbrytningar och indrag i
projekt-, konfigurations-, kortkommando- och spårdialoger. Detta tar bort de
sista felen för avvikande escape-tecken från `l10n-lint`.

Källcommit: [`749ea11`](https://github.com/yeager/audacity/commit/749ea114dd65a95fb63acbd61de27760e6993ae7).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt --check --statistics`, Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks kördes. `msgfmt`, diffkontroll och Gitleaks passerade. `l10n-lint` rapporterar inga kvarvarande fel för escape-tecken.

PR:n är öppen och väntar på obligatorisk upstreamgranskning. Den är inte mergad.
