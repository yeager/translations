# Cataclysm-DDA, svenska: batch 30

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De omfattar reparationsmenyn och dess
resurs- och sannolikhetsinformation.

Källkontexten kontrollerades i `src/activity_handlers.cpp`. `refit` är samma
åtgärd som i föregående batch och syftar på ett föremåls passform. `bionic
power` är energiresursen för bionik och översätts som `bionisk energi`.

## Kontroller före API-inskick

- Platsmarkörer, formattaggar och radbrytningar ska stämma mellan källa och mål.
- `l10n-lint --language sv --json-format auto` ska passera utan varningar eller fel.
- Hunspell-SV och svlang ska granskas manuellt för sammansättningar,
  platshållare och projektspecifika termer.
- Ingen otillåten em dash får tillföras. `msgfmt` är inte tillämpligt eftersom
  Transifex API tar enskilda JSON-översättningar, inte en PO-katalog.

Transifex API normaliserar bort avslutande radbrytningar i tre gränssnittssträngar.
Målvärdena i `candidates.json` följer därför den serverkanoniska formen;
platshållare och färgtaggar är bevarade exakt.

## Inskick och återläsning

Den 16 november 2026 sparades samtliga tio översättningar via Transifex API.
En ny, oberoende GET-återläsning jämförde därefter varje serverkanoniskt
målvärde med denna batch. Alla 10 av 10 stämde exakt.

svlang markerade förväntade falska träffar i menyfraserna och färgtaggarna.
Hunspell-SV markerade endast den projektspecifika termen `bionisk`.
