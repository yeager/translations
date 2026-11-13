# Warzone 2100 – svensk granskning: fabriker, sensorer och EMP

Datum: 2026-11-13

## Omfattning

50 namn och forskningsbeskrivningar för fabrikstillverkning, sensorer, EMP-vapen och snabbskjutande robotar.

## Terminologibeslut

- *factory module* → **fabriksmodul** och *factory output* → **fabrikens produktionstakt**.
- *EMP cannon*, *EMP mortar* och *EMP missile launcher* → **EMP-kanon**, **EMP-granatkastare** och **EMP-robotlavett**.
- *sensor range* → **sensorräckvidd** och *counter-battery range* → **motbatteriräckvidd**.
- Hardcrete, Dragon, Cobra, Python och Viper behålls som synliga egennamn eller materialnamn.

## Lokal kontroll

- `msgfmt --check --statistics`: godkänd; huvudkatalogen har 1 426 översatta och 2 521 oöversatta meddelanden.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --source po/sv.po`: godkänd, inga läckor.
- Kontroll av trippelkonsonanter: inga svenska träffar; de enda träffarna är engelska källreferenser.

## Status

Arkiverad lokalt granskad kopia. Ingen uppladdning till Crowdin och inget upstream-inskick har gjorts.
