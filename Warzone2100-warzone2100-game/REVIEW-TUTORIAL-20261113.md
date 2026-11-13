# Warzone 2100 – svensk granskning: introduktionshandledning

Datum: 2026-11-13

## Omfattning

42 steg i spelets introduktionshandledning. Strängarna kommer från data/base/script/tutorial.js och har granskats i sin instruktionella skärmkontext, inklusive namnen på blinkande UI-ikoner.

## Terminologibeslut

- *truck* → **konstruktionsfordon**.
- *oil derrick* → **oljetorn** och *power generator* → **energigenerator**.
- *recover an artifact* → **bärga en artefakt**.
- *delivery point* → **leveranspunkt**.
- Synliga funktionsetiketter följer UI-kontexten: **BYGG**, **FORSKNING**, **DESIGN**, **TILLVERKNING** och **STÄNG**.

## Lokal kontroll

- msgfmt --check --statistics: godkänd; huvudkatalogen hade 657 översatta och 3 290 oöversatta meddelanden.
- git diff --check: godkänd.
- gitleaks detect --no-git --source po/sv.po: godkänd, inga läckor.
- Trippelkonsonantkontroll: endast engelska källhänvisningar, inga svenska översättningar.

## Status

Arkiverad lokalt granskad kopia. Ingen uppladdning till Crowdin och inget upstream-inskick har gjorts.
