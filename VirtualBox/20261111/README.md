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

- Batch 001–011 omfattar radvis granskning av angivna gränssnittsområden,
  bland annat start, maskinåtgärder, nätverk, lagring, media, loggar,
  guider och uppdateringsinställningar. De sammanlagda ändringarna är
  inskickade i PR #848.
- Den tekniska helkontrollen av katalogen är klar: 3 589 aktiva strängar,
  giltig XML och en kompilerbar QM-fil.
- **Den manuella radvisa granskningen av samtliga 3 589 strängar är inte
  klar.** Den fortsätter från den aktuella PR-katalogen i avgränsade,
  dokumenterade batcher. Tidigare formulering om en fullständig
  slutgranskning har korrigerats.
- 2026-11-11, batch 013: alla 281 aktiva meddelanden i `UICommon` har
  granskats radvis. Ändringarna är verifierade lokalt och ännu inte pushade
  till PR:n.
- 2026-11-11, batch 014: alla 102 aktiva meddelanden i `UIDetails` har
  granskats radvis. Ändringarna är verifierade lokalt och ännu inte pushade
  till PR:n.
- 2026-11-11, batch 015: alla 72 aktiva meddelanden i
  `UIStorageSettingsEditor` har granskats radvis. Ändringarna är verifierade
  lokalt och ännu inte pushade till PR:n.
- 2026-11-11, batch 016: `UIMediumManager` (44), `UINetworkManager` (111),
  USB-filterredigerarna (36) och `UIWizardCloneVM` (50) har granskats radvis.
  Ändringarna är verifierade lokalt i commit `69933e4` och ännu inte pushade
  till PR:n.
- 2026-11-11, batch 017: `UIVMLogViewerWidget` (47) och
  `UICloudProfileManager` (29) har granskats radvis. Ändringarna är
  verifierade lokalt i commit `172a7ce` och ännu inte pushade till PR:n.
- 2026-11-11, batch 018: `UISharedFolderDetailsEditor` (18),
  `UINameAndSystemEditor` (14), `UISerialSettingsEditor` (14) och
  `UINetworkFeaturesEditor` (13) har granskats radvis. Ändringarna är
  verifierade lokalt i commit `e652cc0` och ännu inte pushade till PR:n.
- 2026-11-11, batch 019: VISO (25), VRDE (13), generella
  maskininställningar (8), ögonblicksbildsuppgifter (19) och
  ögonblicksbildspanelen (4) har granskats radvis. Ändringarna är verifierade
  lokalt i commit `5da8d7a` och ännu inte pushade till PR:n.
- 2026-11-11, batch 020: `UICloudConsoleManager` (24) har granskats radvis.
  Ändringarna är verifierade lokalt i commit `8eb3507` och ännu inte pushade
  till PR:n.
- 2026-11-11, batch 021: `UIStorageSettingsEditor` (72) och
  `UINetworkSettingsEditor` (2) har granskats radvis. Ändringarna är
  verifierade lokalt i commit `1cc8397` och ännu inte pushade till PR:n.
- 2026-11-11, batch 022: globala inmatnings- och inställningsdialoger (11),
  skärminställningar (11), system- och generella maskininställningar (22)
  samt ljudinställningar (2) har granskats radvis. Ändringarna är verifierade
  lokalt i commit `6d88175` och ännu inte pushade till PR:n.
- 2026-11-11, batch 023: tilläggspakethanteraren (14), uppdateringshanteraren
  (11) och guiden för ny virtuell maskin (75) har granskats radvis.
  Ändringarna är verifierade lokalt i commit `bc91842` och ännu inte pushade
  till PR:n.
- 2026-11-11, batch 024: delade mappar, urklipp och dra-och-släpp (19),
  indikatorer (23) samt nätverksanslutning och portomdirigering (22) har
  granskats radvis. Ändringarna är verifierade lokalt i commit `92c0bde` och
  ännu inte pushade till PR:n.
- 2026-11-11, batch 025: medieväljare och mediestorlek (44), gästprocesser
  och sessioner (13) samt hjälpfönster och startsida (57) har granskats
  radvis. Ändringarna är verifierade lokalt i commit `4aab66c` och ännu inte
  pushade till PR:n.
- 2026-11-11, batch 026: kryptering, TPM och startfel (27) samt
  startordning, moderkort och processor (20) har granskats radvis.
  Ändringarna är verifierade lokalt i commit `b9a465d` och ännu inte pushade
  till PR:n.
- 2026-11-11, batch 027: guider för att lägga till och skapa molnmaskiner
  samt molnklonens namn (32) har granskats radvis. Ändringarna är verifierade
  lokalt i commit `cba0297` och ännu inte pushade till PR:n.
- 2026-11-11, batch 028: nedladdare (7), inspelningsinställningar (31) och
  fil-/sökvägsfält (13) har granskats radvis. Ändringarna är verifierade
  lokalt i commit `73a9742` och ännu inte pushade till PR:n.
- 2026-11-11, batch 029: USB-kontroller, menyer, inställningar och verktyg
  (23) har granskats radvis. Ändringarna är verifierade lokalt i commit
  `99e657b` och ännu inte pushade till PR:n.
- PR #848 uppdaterades 2026-11-11 till huvudrevision
  `f11f1d7cb7cd85ced4377bb8d3b329d68b30fa36` med samtliga tio
  granskningscommitar. GitHub har bekräftat mottagandet.
- Commithistoriken rättades därefter till `po@danielnylander.se` utan att
  kataloginnehållet ändrades. `oca/oracle` är godkänd för den aktuella
  huvudrevisionen.
- PR:n är öppen och ännu inte granskad eller mergad.
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
