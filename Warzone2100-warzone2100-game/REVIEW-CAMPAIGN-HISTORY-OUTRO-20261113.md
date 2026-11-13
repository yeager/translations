# Warzone 2100 – svensk granskning: bakgrundshistoria och slutsekvens

Datum: 2026-11-13

## Omfattning

44 strängar från bakgrunden om Reed Corporation och NEXUS, Kollapsens historiska sekvens, nödsändningar och slutsekvensen. Berättelsetexten har översatts som sammanhängande svenska med bibehållen ton och etablerade egennamn.

## Terminologibeslut

- *Cyberspace* → **cyberrymden** och *immersion tanks* → **immersionskammare**.
- *NEXUS Intruder Program* → **NEXUS Intruder-program**.
- *nuclear winter* → **kärnvapenvinter**.
- *nuclear deterrent* → **kärnvapenavskräckning**.
- *The Collapse* → **Kollapsen**.

## Lokal kontroll

- msgfmt --check --statistics: godkänd; huvudkatalogen hade 862 översatta och 3 085 oöversatta meddelanden.
- git diff --check: godkänd.
- gitleaks detect --no-git --source po/sv.po: godkänd, inga läckor.
- Trippelkonsonantkontroll: endast engelska källhänvisningar, inga svenska översättningar.

## Status

Arkiverad lokalt granskad kopia. Ingen uppladdning till Crowdin och inget upstream-inskick har gjorts.
