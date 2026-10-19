# SSSD, svenska

## Status 2026-10-19

Den aktuella svenska PO-filen hämtades från Fedora Weblate-komponenten
`sssd/sssd-master`. Den har 745 aktiva, översatta strängar och inga tomma
eller luddiga poster.

- En loggsträng rättades: källans bindestrecksformatering bevaras i stället
  för svenska tankstreck.
- `sssd-sv-reviewed-delta-20261019.po` innehåller endast den rättade strängen
  och kan importeras i Weblate.
- Fullfilen är en lokal granskningskopia. Den är inte ett påstående om att
  ändringen är inskickad eller godkänd i Fedora Weblate.

## Kontroll

`msgfmt --check` passerar. `l10n-lint` ger 0 fel och 0 varningar.
`svlang skrivregler` ger inga skrivregelfel. Återstående l10n-lint-information
är avsiktlig: svensk sifferskrift, platshållarens flyttade plats och
PAM-funktionsnamn som måste bevaras ordagrant.
