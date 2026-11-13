# Warzone 2100 – svensk granskning: kampanjmål och huvud-UI

Datum: 2026-11-13

## Omfattning

42 strängar för kampanjmål, resultatmarkörer och huvudfunktionerna i spelgränssnittet. Varje sträng har granskats mot det angivna skriptet och sin konkreta UI-roll.

## Terminologibeslut

- *HQ* → **högkvarter** när förkortningen inte behöver vara synlig.
- *manufacture* → **tillverkning** som UI-funktion; verbformen är **tillverka**.
- *constructor droid* → **konstruktionsdroid**.
- *intelligence display* → **underrättelsevy**.
- Fraktionsnamnen The Collective, New Paradigm och NEXUS behålls; NEXUS skrivs konsekvent med versaler.

## Lokal kontroll

- msgfmt --check --statistics: godkänd; huvudkatalogen hade 615 översatta och 3 332 oöversatta meddelanden.
- git diff --check: godkänd.
- gitleaks detect --no-git --source po/sv.po: godkänd, inga läckor.
- Trippelkonsonantkontroll: endast engelska källhänvisningar, inga svenska översättningar.

## Status

Arkiverad lokalt granskad kopia. Ingen uppladdning till Crowdin och inget upstream-inskick har gjorts.
