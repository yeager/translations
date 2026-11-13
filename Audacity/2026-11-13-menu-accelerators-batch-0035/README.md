# Audacity: svenska menygenvägar

Åtta radgranskade poster flyttar acceleratormarkören från `å`, `ä` och `ö`
till fungerande bokstäver i respektive meny. Samma genomgång kompletterar en
saknad markör för Markera allt.

Källcommit: [`b1706fd`](https://github.com/yeager/audacity/commit/b1706fd88b9ba7c053abb523ff7b4ee4433751e3).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt --check --statistics`, Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks kördes. `msgfmt`, diffkontroll och Gitleaks passerade. `l10n-lint` bekräftar att de berörda nordiska acceleratorfelen är åtgärdade; två informationsnotiser om teckenpositionen för Ångra återstår och kräver ingen ändring.

PR:n är öppen och väntar på obligatorisk upstreamgranskning. Den är inte mergad.
