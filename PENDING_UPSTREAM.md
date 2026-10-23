# Väntande upstream-importer

Följande filer är granskade mot respektive senaste lokala export och pushade till
`main`. De har ännu inte importerats under den här arbetsomgången.

| Projekt | Fil | Omfattning | Verifiering |
| --- | --- | ---: | --- |
| GitLab EE i Crowdin | `GitLab/gitlab-sv-current-strings-orbit-delta-20261023.xliff` | 53 Orbit-strängar | XML-parser, l10n-lint, svlang och Gitleaks |

Varje fil är en deltafil: den innehåller bara aktuella enheter som skiljer sig
från den export den granskades mot. Importresultatet behöver kontrolleras i
tjänsten efter uppladdning innan arbetet kan räknas som inskickat.
