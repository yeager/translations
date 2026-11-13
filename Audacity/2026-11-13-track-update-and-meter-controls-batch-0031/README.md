# Audacity: spår-, uppdaterings- och mätarkontroller

Den här batchen innehåller 36 radgranskade poster från `au3/locale/sv.po`.
Den omfattar sammanslagning av spår, klipp- och amplitudkurvverktyg,
uppdateringsdialoger, mätarinställningar och berörda effekter.

Ändringarna finns i källcommit [`986943d`](https://github.com/yeager/audacity/commit/986943d90ffcbee61f5b7b6118f1d043aca835d4)
på den öppna upstream-PR:n [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

Kontroller före arkivering:

- `msgfmt --check --statistics` passerade: 4 443 översatta poster.
- Avgränsad Hunspell-sv-kontroll gav endast produktnamnet Audacity och tekniska förkortningar.
- `l10n-lint` och `svlang` kördes; kvarvarande träffar är befintliga katalogvarningar och inte nya formatfel i batchen.
- `git diff --check` och Gitleaks passerade.

Upstreamstatus: committen är pushad till PR-grenen. PR:n är öppen och väntar på obligatorisk upstreamgranskning; den är inte mergad.
