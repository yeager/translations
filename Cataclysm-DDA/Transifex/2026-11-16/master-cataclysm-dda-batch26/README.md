# Cataclysm-DDA, svenska: batch 26

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De gäller spelets mekanik för att krossa lik,
vilket förhindrar att de återuppstår, samt medlet som används vid rengöring.

Källkontexten kontrollerades mot aktuell upstream-källkod. Den mekaniska
betydelsen av `pulp` är **krossa lik**, inte ett lånord. Svenska pluralformer
har separata mål för singular och plural där Transifex-resursen kräver det.

## Kontroller före API-inskick

- Platsmarkörer, inklusive `<npcname>` och `%1$s`/`%1$i`, ska stämma mellan
  källa och mål.
- `l10n-lint --language sv --json-format auto` ska passera utan varningar eller fel.
- Hunspell-SV och svlang ska granskas manuellt för projektspecifika termer och
  platshållare.
- Ingen otillåten em dash får tillföras. `msgfmt` är inte tillämpligt eftersom
  Transifex API tar enskilda JSON-översättningar, inte en PO-katalog.

## Inskick och återläsning

Den 16 november 2026 sparades samtliga tio översättningar via Transifex API.
En ny, oberoende GET-återläsning jämförde därefter målvärdena, inklusive båda
pluralformerna, med denna batch. Alla 10 av 10 stämde exakt.
