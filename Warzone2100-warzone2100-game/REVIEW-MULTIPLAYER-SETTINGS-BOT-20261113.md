# Warzone 2100 – svensk granskning: flerspelarinställningar och botchatt

Datum: 2026-11-13

## Omfattning

38 strängar för flerspelarlobbyns regler, matchslut, svårighetsgrader och AI-bottens chattmeddelanden. Källhänvisningarna visar respektive lobby- och skriptkontext.

## Terminologibeslut

- *Scavengers* → **skrotare**.
- *power level* → **energinivå** i lobbyinställningarna.
- *locked teams* → **låsta lag** och *shared research* → **delad forskning**.
- *beacon* → **fyr** i bottens hjälpförfrågan.
- *truck* → **konstruktionsfordon** även i bottens svar.

## Lokal kontroll

- msgfmt --check --statistics: godkänd; huvudkatalogen hade 965 översatta och 2 982 oöversatta meddelanden.
- git diff --check: godkänd.
- gitleaks detect --no-git --source po/sv.po: godkänd, inga läckor.
- Trippelkonsonantkontroll: endast engelska källhänvisningar, inga svenska översättningar.

## Status

Arkiverad lokalt granskad kopia. Ingen uppladdning till Crowdin och inget upstream-inskick har gjorts.
