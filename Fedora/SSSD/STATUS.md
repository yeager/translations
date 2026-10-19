# SSSD, svenska

## Status 2026-10-19

Den aktuella svenska PO-filen hämtades från Fedora Weblate-komponenten
`sssd/sssd-master`. Den har 745 aktiva, översatta strängar och inga tomma
eller luddiga poster.

- En loggsträng rättades: källans bindestrecksformatering bevaras i stället
  för svenska tankstreck.
- `sssd-sv-reviewed-delta-20261019.po` innehåller endast den rättade strängen
  och kan importeras i Weblate.
- Ändringen skickades till Fedora Weblate och lästes tillbaka från enhet
  `12331660` med tillståndet Översatt. Fullfilen är en lokal granskningskopia.

## Kontroll

`msgfmt --check` passerar. `l10n-lint` ger 0 fel och 0 varningar.
`svlang skrivregler` ger inga skrivregelfel. Återstående l10n-lint-information
är avsiktlig: svensk sifferskrift, platshållarens flyttade plats och
PAM-funktionsnamn som måste bevaras ordagrant.

## Manuell språkgranskning, grupp 2

De första 50 aktiva strängarna har granskats i sin källordning. Sju
formuleringar har förbättrats och skrivits till Fedora Weblate. Varje
uppdaterad enhet lästes tillbaka via API efter ändringen.

## Manuell språkgranskning, grupp 3

Sträng 51–100 har granskats i källordning. Fem rättningar har skrivits till
Fedora Weblate och lästs tillbaka från respektive enhet via API.

## Manuell språkgranskning, grupp 4

Sträng 101–150 har granskats i källordning. Sju rättningar har skrivits till
Fedora Weblate och lästs tillbaka från respektive enhet via API.
