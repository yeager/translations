# VirtualBox, svensk granskning 2026-11-11

## Källa och avgränsning

- Officiell källgren: `VirtualBox/virtualbox` `main`, revision
  `b6bea72111fcff48f31c57c9f66365b1d3301bb9` (20 oktober 2026).
- Granskningsunderlag: den öppna PR:n [#848](https://github.com/VirtualBox/virtualbox/pull/848),
  ursprunglig huvudrevision `7b2f494a0b0301f6f85423d1f4d4abc30222c5df`.
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
- 2026-11-11, batch 004: maskinväljaren, molnkonsoler, färgtema,
  detaljer för virtuella maskiner och virtuella medier har granskats radvis.
  Ändringarna är fortfarande endast lokala.
- 2026-11-11, batch 005: nätverksinställningar, delade mappar,
  ögonblicksbilder, virtuellt tangentbord, filhanterare och global proxy har
  granskats radvis. Ändringarna är fortfarande endast lokala.
- 2026-11-11, batch 006: indikatorer, maskininställningar, lagring,
  nätverksfunktioner och proxyfel har granskats radvis. Ändringarna är
  fortfarande endast lokala.
- 2026-11-11, batch 007: delat urklipp, lagringsvyn, seriella portar,
  avslut av virtuella maskiner och den nya maskinguiden har granskats radvis.
  Ändringarna är fortfarande endast lokala.
- 2026-11-11, batch 008: loggvisaren, CPU- och USB-etiketter samt
  kloningsguiden har granskats radvis. Ändringarna är fortfarande endast
  lokala.
- 2026-11-11, batch 009: konsoltexter, återstående systemmeddelanden och
  terminologin har normaliserats. Ändringarna är fortfarande endast lokala.
- 2026-11-11, batch 010: virtuell mediehantering har granskats och
  normaliserats till svensk singular och plural. Ändringarna är fortfarande
  endast lokala.
- 2026-11-11, batch 011: maskinåtgärder, fångsthjälp, moln- och
  kloningsguider samt uppdateringsinställningar har granskats radvis.
- 2026-11-11, batch 012: slutgranskningen av katalogen är klar. Startsidan
  rättades där konfigurationen felaktigt angavs som ett sätt att använda
  datorn, i stället för att få VirtualBox Manager att fungera med den.
- PR #848 uppdaterades 2026-11-11 till huvudrevision
  `9ec705ee28c949c8faf7b7d6b187216dfaedda37` med samtliga tio
  granskningscommitar. GitHub har bekräftat mottagandet.
- PR:n är öppen och ännu inte granskad eller mergad. GitHubs enda externa
  kontroll, `oca/oracle`, misslyckas för huvudrevisionen. Det är Oracle
  Contributor Agreement-kontrollen och inte ett fel i översättningsfilerna.
- Råfilerna i `../VirtualBox/` är historiska och har inte skrivits över.

## Kontroller för batch 001

- `lupdate`: 3 589 aktuella källsträngar.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `l10n-lint` med `lupdate`-mallen som referens: inga verkliga fel efter
  granskningen. Två tomma `--`-värden är avsiktliga språkmetadata.
- `git diff --check`: godkänd.
- `svlang consistency`: godkänd.
- `hunspell-sv`: granskad manuellt; återstående träffar är produktnamn,
  kommandon, format och tekniska identifierare.
- `gitleaks detect --no-git --redact`: inga läckta hemligheter.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är formatets motsvarande
  kompileringskontroll.
