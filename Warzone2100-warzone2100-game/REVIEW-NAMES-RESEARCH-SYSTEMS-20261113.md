# Warzone 2100 – svensk granskning: namn, system och forskning

Datum: 2026-11-13

## Omfattning

65 synliga enhets-, försvars-, byggnads- och forskningsnamn från stats- och UI-filer. Varje namn har kontrollerats mot sina referenser för att skilja egennamn från generiska funktioner.

## Terminologibeslut

- *sensor tower* → **sensortorn**, *command turret* → **befälstorn** och *command center* → **ledningscentral**.
- *missile silo* → **robotsilo**; målsöknings- och avfyrningskoder skrivs som sammansättningar.
- *propulsion* → **framdrivning** med typangivelse, exempelvis *banddriven framdrivning*.
- Produktnamnen Tornado, Cyclone, Lancer, Scourge, Tank Killer och HPV behålls när de är synliga namn.
- Fraktionsnamnen New Paradigm, The Collective och NEXUS behålls i sammansatta byggnadsnamn.

## Lokal kontroll

- msgfmt --check --statistics: godkänd; huvudkatalogen hade 927 översatta och 3 020 oöversatta meddelanden.
- git diff --check: godkänd.
- gitleaks detect --no-git --source po/sv.po: godkänd, inga läckor.
- Trippelkonsonantkontroll: endast engelska källhänvisningar, inga svenska översättningar.

## Status

Arkiverad lokalt granskad kopia. Ingen uppladdning till Crowdin och inget upstream-inskick har gjorts.
