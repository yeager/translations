# Audacity: formatkorrigeringar i projekt- och moduldialoger

Den här batchen innehåller fem radgranskade poster från `au3/locale/sv.po`.
Den rättar radbrytningar så att de stämmer med källtexten och förenklar
svenskan i projekt- och moduldialoger.

Källcommit: [`94490ee`](https://github.com/yeager/audacity/commit/94490eeab51c35e45458db3fd89834c1922994f2).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt --check --statistics`, Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks kördes. `msgfmt`, diffkontroll och Gitleaks passerade; katalogomfattande språkträffar är äldre eller formatmässigt irrelevanta för denna batch.

PR:n är öppen och väntar på obligatorisk upstreamgranskning. Den är inte mergad.
