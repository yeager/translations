# Cataclysm-DDA, svenska: batch 31

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De gäller reparation och hantering av
föremål med behållarinnehåll eller fordonsförvaring.

Källkontexten kontrollerades i `src/activity_handlers.cpp` och
`src/activity_item_handling.cpp`. Fordonsdelar uttrycks som `%3$s på %2$s`
i stället för en dynamisk engelsk genitivkedja. Reparationstexten formuleras
utan fast genus framför den dynamiska föremålsplatshållaren.

## Kontroller före API-inskick

- Platsmarkörer, formattaggar och pluralformer ska stämma mellan källa och mål.
- `l10n-lint --language sv --json-format auto` ska passera utan varningar eller fel.
- Hunspell-SV och svlang ska granskas manuellt för sammansättningar,
  platshållare och projektspecifika termer.
- Ingen otillåten em dash får tillföras. `msgfmt` är inte tillämpligt eftersom
  Transifex API tar enskilda JSON-översättningar, inte en PO-katalog.

## Inskick och återläsning

Den 16 november 2026 sparades samtliga tio översättningar via Transifex API.
En ny, oberoende GET-återläsning jämförde sedan måltexten, inklusive samtliga
pluralformer, med denna batch. Alla 10 av 10 stämde exakt.

svlang och Hunspell-SV rapporterade endast förväntade tekniska former:
formattaggarna, `<npcname>` och den formaterade decimalprocenten.
