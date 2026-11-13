# Warzone 2100 – svensk granskning: pansrade försvar och cyborgvapen

Datum: 2026-11-13

## Omfattning

57 namn och beskrivningar för cyborgvapen, pansrade försvar, värn, bunkrar och artilleribatterier. Källhänvisningarna anger både vapen och byggnadsobjekt.

## Terminologibeslut

- *bunker* → **bunker**, *guard tower* → **vakttorn**, *hardpoint* → **värn** och *strongpoint* → **starkt värn**.
- *battery pit* → **batterigrop**.
- *rail gun* → **skenkanon**, *assault cannon* → **automatkanon**.
- Produktnamnen Lancer, Scourge, Tank Killer, Flashlight, Firestorm och Novastorm behålls.

## Lokal kontroll

- msgfmt --check --statistics: godkänd; huvudkatalogen hade 1 173 översatta och 2 774 oöversatta meddelanden.
- git diff --check: godkänd.
- gitleaks detect --no-git --source po/sv.po: godkänd, inga läckor.
- Trippelkonsonantkontroll: endast engelska källhänvisningar, inga svenska översättningar.

## Status

Arkiverad lokalt granskad kopia. Ingen uppladdning till Crowdin och inget upstream-inskick har gjorts.
