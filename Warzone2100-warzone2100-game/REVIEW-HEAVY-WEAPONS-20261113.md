# Warzone 2100 – svensk granskning: tunga vapen och chassin

Datum: 2026-11-13

## Omfattning

50 namn och beskrivningar för tunga vapen, chassin, robotförsvar och fordonsmallar.

## Terminologibeslut

- *heavy body* → **tungt chassi** och *body points* → **skrovpoäng**.
- *heavy cannon*, *heavy machinegun* och *heavy plasma launcher* → **tung kanon**, **tung kulspruta** och **tung plasmakanon**.
- *rocket array*, *rocket bastion* och *rocket battery* → **robotlavett**, **robotbastion** och **robotbatteri**.
- Produktnamnen Mantis, Python, Tiger, Vengeance, Wyvern, Inferno, Ground Shaker och Bombard behålls.

## Lokal kontroll

- `msgfmt --check --statistics`: godkänd; huvudkatalogen har 1 576 översatta och 2 371 oöversatta meddelanden.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --source po/sv.po`: godkänd, inga läckor.
- Kontroll av trippelkonsonanter: inga svenska träffar; de enda träffarna är engelska källreferenser.

## Status

Arkiverad lokalt granskad kopia. Ingen uppladdning till Crowdin och inget upstream-inskick har gjorts.
