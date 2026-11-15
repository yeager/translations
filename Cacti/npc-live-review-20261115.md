# Cacti `npc`: svensk livegranskning 2026-11-15

## Aktuell komponentstatus

- Tjänst: Cacti Translate / Weblate, komponent `cacti/npc`.
- Komponenten var nåbar och olåst vid kontrollen.
- Svenskan omfattar 57 av 57 strängar, utan fuzzy-poster eller fallerande
  Weblate-kontroller.
- Färsk PO-export klarar `msgfmt --check`; källfilens revisionsmetadata är
  inte översättningsfel.

## Radgranskning och delta

Samtliga 57 befintliga svenska poster kontrollerades mot källa och
filreferenser. En hjälptext för tidsformat har en tydligare, naturligare
formulering:

| Källa | Tidigare svensk text | Rekommenderad svensk text |
| --- | --- | --- |
| `Select the format you want for displaying times.` | `Välj formatet som tider ska visas med.` | `Välj det format du vill använda för att visa tider.` |

Den separata deltafilen `cacti-npc-sv-delta-20261115.po` innehåller enbart
denna rättning. Rättningen sparades i Cacti Translates Weblate-redigerare och
lästes sedan tillbaka direkt i samma redigerarvy. Deltat är därmed **lokalt
granskat, arkiverat, inskickat och verifierat mottaget**. Projektets fortsatta
granskning och en eventuell releasepublicering är inte verifierade.

## Kontroller

- `msgfmt --check`: godkänd.
- `l10n-lint`: inga fel eller varningar; en längdkvotsnotis för `N/A` är inte
  ett översättningsfel.
- Hunspell svenska: inga träffar i måltexterna.
- `svlang`: tekniska namn och korrekta sammansättningar gav heuristiska
  träffar; de är inte automatiska språkfel.
- Gitleaks och `git diff --check`: godkända för deltafilen.
