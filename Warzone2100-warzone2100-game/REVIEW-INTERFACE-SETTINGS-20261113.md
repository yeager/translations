# Warzone 2100 – svensk granskning: inställningsgränssnitt

Datum: 2026-11-13

## Omfattning

32 synliga inställningsetiketter för gränssnitt, radar, video och grafik.

## Terminologibeslut

- *interface* → **gränssnitt**, *game UI* → **spelgränssnitt**.
- *graphics backend* → **grafikrutin** och *display scale* → **visningsskala**.
- *tracked* → **följer** i radarläget.
- *fullscreen* → **helskärm**.

## Lokal kontroll

- `msgfmt --check --statistics`: godkänd; huvudkatalogen har 1 658 översatta och 2 289 oöversatta meddelanden.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --source po/sv.po`: godkänd, inga läckor.

## Speltest

Texten har kompilerats in i en lokal, modifierad testkopia av 4.7.0. Den officiella binären saknar svensk språkpost; testet använder därför en tillfällig lokal aliaspost och är inte ett upstream-stöd för svenska.

## Status

Arkiverad lokalt granskad kopia. Ingen uppladdning till Crowdin och inget upstream-inskick har gjorts.
