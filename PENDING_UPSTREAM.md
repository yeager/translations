# Väntande upstream-importer

Följande filer är granskade mot respektive senaste lokala export och pushade till
`main`. De har ännu inte importerats under den här arbetsomgången.

| Projekt | Fil | Omfattning | Verifiering |
| --- | --- | ---: | --- |
| Hosted Weblate Application | `Weblate/Application/weblate-application-sv-reviewed-delta-20261023-live.po` | 40 ändringar: 15 tidigare rättningar, 15 tomma strängar, 10 inaktuella strängar | l10n-lint, svlang, Hunspell, msgfmt och Gitleaks |
| Hosted Weblate Website | `Weblate/Website/weblate-website-sv-reviewed-delta-20261023.po` | 7 ändringar | l10n-lint, svlang, msgfmt och Gitleaks |
| GitLab EE i Crowdin | `GitLab/gitlab-sv-current-strings-orbit-delta-20261023.xliff` | 53 Orbit-strängar | XML-parser, l10n-lint, svlang och Gitleaks |

Varje fil är en deltafil: den innehåller bara aktuella enheter som skiljer sig
från den export den granskades mot. Importresultatet behöver kontrolleras i
tjänsten efter uppladdning innan arbetet kan räknas som inskickat.
