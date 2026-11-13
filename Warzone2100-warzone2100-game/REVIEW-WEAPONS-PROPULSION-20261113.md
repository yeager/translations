# Warzone 2100 – svensk granskning: vapen och framdrivning

Datum: 2026-11-13

## Omfattning

50 namn och forskningsbeskrivningar för eldkastare, laserprodukter, gasturbiner, Gausskanoner och halvband.

## Terminologibeslut

- *flamer* → **eldkastare**, med **automatladdare**, **snabbladdare** och **omladdning** i forskningsnamn.
- *fuel injection engine* → **bränsleinsprutningsmotor** och *gas turbine generator* → **gasturbingenerator**.
- *Gauss cannon* → **Gausskanon**; *emplacement* och *hardpoint* följer etablerade termerna **ställning** och **värn**.
- Produktnamnen Flashlight, Ground Shaker, Gamma och Retribution behålls.

## Lokal kontroll

- `msgfmt --check --statistics`: godkänd; huvudkatalogen har 1 476 översatta och 2 471 oöversatta meddelanden.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --source po/sv.po`: godkänd, inga läckor.
- Kontroll av trippelkonsonanter: inga svenska träffar; de enda träffarna är engelska källreferenser.

## Status

Arkiverad lokalt granskad kopia. Ingen uppladdning till Crowdin och inget upstream-inskick har gjorts.
