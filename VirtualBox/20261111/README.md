# VirtualBox, svensk granskning 2026-11-11

## Källa och avgränsning

- Officiell källgren: `VirtualBox/virtualbox` `main`, revision
  `b6bea72111fcff48f31c57c9f66365b1d3301bb9` (20 oktober 2026).
- Granskningsunderlag: den öppna PR:n [#848](https://github.com/VirtualBox/virtualbox/pull/848),
  huvudrevision `7b2f494a0b0301f6f85423d1f4d4abc30222c5df`.
- Senaste stabila utgåva enligt projektets nedladdningssida är 7.2.22 och
  ligger väl inom 48 månader.

## Källkontroll

`lupdate` kördes mot hela `src/VBox/Frontends/VirtualBox` i PR-huvudet.
Den fann 3 589 källsträngar, exakt lika många som i PR:ns `VirtualBox_sv.ts`.
Den versionerade mallen `VirtualBox_xx_YY.ts` innehåller däremot 3 458
strängar och är alltså 131 strängar efter den aktuella koden. Det är en
källunderhållsbrist i mallen, inte ett bortfall i PR:ns svenska katalog.

PR #848 innehåller dessutom en separat rättning av macOS-paketeringen: även
`VirtualBoxVM.app` får `.lproj`-kataloger. Utan dem lokaliseras inte
hjälpprogrammets programmeny trots att TS- och QM-filerna finns.

## Status

- 2026-11-11, batch 001: 18 svenska strängar radvis granskade och korrigerade
  lokalt ovanpå PR #848.
- 2026-11-11, batch 002: `QApplication`, `UIAccelerationFeaturesEditor`,
  `UIActionPool` och `UIBootFailureDialog` har granskats radvis i den aktuella
  genomgången. Ändringarna är fortfarande endast lokala.
- 2026-11-11, batch 003: `UIApplianceEditorWidget`,
  `UIApplianceUnverifiedCertificateViewer`, ljudinställningar,
  tangentbordsfångst och uppstartsordning har granskats radvis. Ändringarna är
  fortfarande endast lokala.
- Kvar: radvis granskning av återstående aktiva strängar i `VirtualBox_sv.ts`.
- Råfilerna i `../VirtualBox/` är historiska och har inte skrivits över.

## Kontroller för batch 001

- `lupdate`: 3 589 aktuella källsträngar.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `l10n-lint` med `lupdate`-mallen som referens: inga verkliga fel efter
  granskningen. Två tomma `--`-värden är avsiktliga språkmetadata.
- `git diff --check`: godkänd.
- Återstående kontroller redovisas per batch efter manuell bedömning.
