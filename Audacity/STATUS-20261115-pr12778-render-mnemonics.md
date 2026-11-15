# Audacity PR #12778: renderingsrättning, 15 november 2026

CodeRabbits genomgång uppmärksammade två kvarvarande svenska kortkommandovarianter av *Mix and Render*. De är nu rättade i samma, sammanslagna PR-commit:

* `Mi&x and Render` → `M&ixa och rendera`
* `Mix and Render to Ne&w Track` → `Mixa och rendera till &nytt spår`

Commit `937cbb9a5ef6db87fc0e7e1ec5fb0258981ff730` är pushad med force-with-lease till grenen `l10n-sv-ui-catalog-review-20261115`. PR #12778 är fortsatt öppen och väntar på projektgranskning. Ingen merge eller release är verifierad.

Kontroller för denna rättning:

* `msgfmt --check` passerade.
* Hunspell-sv gav inga träffar för de två ändrade svenska texterna.
* svlang kontrollerade texterna utan rapporterade träffar.
* `git diff --check` passerade.
* Gitleaks kontrollerade den indexerade ändringen utan hemlighetsträffar.
* l10n-lint rapporterar äldre katalogvarningar vid helkatalogskörning; de berör inte dessa två strängar.
