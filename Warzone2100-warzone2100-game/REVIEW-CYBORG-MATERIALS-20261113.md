# Warzone 2100 – svensk granskning: cyborger och material

Datum: 2026-11-13

## Omfattning

50 namn och forskningsbeskrivningar för cyborger, kompositlegeringar, termiskt pansar, konstruktion och ammunition.

## Terminologibeslut

- *cyborg factory* → **cyborgfabrik** och *cyborg propulsion* → **cyborgframdrivning**.
- *composite alloys* → **kompositlegeringar**, med **täta** och **supertäta** för respektive materialnivå.
- *thermal armor* → **termiskt pansar**; de mer beskrivande forskningsnamnen använder **värmetåligt pansar**.
- Produktnamnen Lancer och Tank Killer behålls i sammansättningar.

## Lokal kontroll

- `msgfmt --check --statistics`: godkänd; huvudkatalogen har 1 376 översatta och 2 571 oöversatta meddelanden.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --source po/sv.po`: godkänd, inga läckor.
- Kontroll av trippelkonsonanter: inga svenska träffar; de enda träffarna är engelska källreferenser.

## Status

Arkiverad lokalt granskad kopia. Ingen uppladdning till Crowdin och inget upstream-inskick har gjorts.
