# Warzone 2100 – svensk granskning: kommando och motbatteri

Datum: 2026-11-13

## Omfattning

53 namn och forskningsbeskrivningar för kanoner, kommando, motbatteri, kompositlegeringar och konstruktion.

## Terminologibeslut

- *command center* → **ledningscentral**, *command relay center* → **ledningsreläcentral** och *command turret* → **befälstorn**.
- *counter-battery* → **motbatteri**; radarn, sensorn och tornen får konsekventa sammansättningar.
- *cannon* → **kanon**, *chaingun* → **kedjekanon** och *construction unit* → **konstruktionsenhet**.
- Egennamnen Cobra, Mantis, Python, Scorpion, Viper och The Collective behålls.

## Lokal kontroll

- `msgfmt --check --statistics`: godkänd; huvudkatalogen har 1 326 översatta och 2 621 oöversatta meddelanden.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --source po/sv.po`: godkänd, inga läckor.
- Kontroll av trippelkonsonanter: inga svenska träffar; de enda träffarna är engelska källreferenser.

## Status

Arkiverad lokalt granskad kopia. Ingen uppladdning till Crowdin och inget upstream-inskick har gjorts.
