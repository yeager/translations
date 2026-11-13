# Warzone 2100 – svensk granskning: automatiserade system och målprioriteringar

Datum: 2026-11-13

## Omfattning

50 strängar för automatvapen, automatiserad produktion och reparation, VTOL-styrning, Avenger-luftvärn och målprioriteringar.

## Terminologibeslut

- *assault gun* → **automatvapen** och *assault cannon* → **automatkanon**.
- *rearming pad* → **omladdningsplatta**.
- *SAM site* → **SAM-ställning**.
- *best targets* → **bästa mål** i vapnens forskningsbeskrivningar.

## Lokal kontroll

- msgfmt --check --statistics: godkänd; huvudkatalogen hade 1 223 översatta och 2 724 oöversatta meddelanden.
- git diff --check: godkänd.
- gitleaks detect --no-git --source po/sv.po: godkänd, inga läckor.
- Trippelkonsonantkontroll: endast engelska källhänvisningar, inga svenska översättningar.

## Status

Arkiverad lokalt granskad kopia. Ingen uppladdning till Crowdin och inget upstream-inskick har gjorts.
