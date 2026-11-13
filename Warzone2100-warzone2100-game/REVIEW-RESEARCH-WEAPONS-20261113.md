# Warzone 2100 – svensk granskning: vapenforskning

Datum: 2026-11-13

## Omfattning

Deltafilen innehåller 267 redan lokalt granskade svenska strängar som saknades i arkivet. Den omfattar bland annat vapensystem, försvar, enhetsrörlighet och forskningsmeddelanden. Den senaste delbatchen täcker bombning, kanoner, eldkastare, haubitsar, kulsprutor, granatkastare och robotar.

## Terminologibeslut

- *turret* → **torn**, *emplacement* → **ställning** och *sensor* → **sensor**.
- *howitzer* → **haubits**, *mortar* → **granatkastare**, *machinegun* → **kulspruta**.
- *rocket* → **robot** i spelets vapen- och uppdragskontext; *mini-rocket* → **minirobot**.
- Fysiska egenskaper uttrycks med **skrovpoäng** och **eldhastighet**.
- Namn, förkortningar och identifierare behålls när de är synliga produktspecifika namn.

## Lokal kontroll

- msgfmt --check --statistics: godkänd; huvudkatalogen hade 573 översatta och 3 374 oöversatta meddelanden.
- git diff --check: godkänd.
- gitleaks detect --no-git --source po/sv.po: godkänd, inga läckor.
- Trippelkonsonantkontroll: endast två träffar i engelska källhänvisningar (Cannon375mmMk1), inga svenska översättningar.

## Status

Arkiverad lokalt granskad kopia. Ingen uppladdning till Crowdin och inget upstream-inskick har gjorts, eftersom svenska ännu inte är aktiverat i Warzone 2100:s Crowdin-projekt.
