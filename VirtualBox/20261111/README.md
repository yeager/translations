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
- 2026-11-11, batch 030: diskvarianter, diskettverktyg, ny virtuell disk och
  mediesökning (39) samt aktivitetsöversikt och maskinförhandsvisning (45)
  har granskats radvis. Ändringarna är verifierade lokalt i commit `18da0a4`
  och ännu inte pushade till PR:n.
- 2026-11-11, batch 031: visningskontroller (21) samt statusrad, menyrad och
  miniverktygsfält (22) har granskats radvis. Ändringarna är verifierade
  lokalt i commit `478dc34` och ännu inte pushade till PR:n.
- 2026-11-11, batch 032: tangentbordsfångst, kortkommandon, pekdon och
  visuellt tangentbord (76) har granskats radvis. Den verifierade delbatchen
  finns lokalt i commit `1fa7a09` och är ännu inte pushad till PR:n.
- 2026-11-11, batch 033: globala inställningar för allmänt, proxy, språk och
  uppdateringar (25) har granskats radvis. Den verifierade delbatchen finns
  lokalt i commit `1523f64` och är ännu inte pushad till PR:n.
- 2026-11-11, batch 034: notifieringscenter, nedladdare, förlopp och
  inställningsserialisering (10) har granskats radvis. Den verifierade
  delbatchen finns lokalt i commit `02c13e7` och är ännu inte pushad till PR:n.
- 2026-11-11, batch 035: startsida samt nätverkssvar, portomdirigering och
  proxy (35) har granskats radvis. Ändringarna är verifierade lokalt i commit
  `fdd91c3` och ännu inte pushade till PR:n.
- 2026-11-11, batch 036: skärmtangentbordets layoutmetadata, knappar,
  färgteman och filåtgärder (76) har granskats radvis. Ändringarna är
  verifierade lokalt i commit `004479e` och ännu inte pushade till PR:n.
- 2026-11-11, batch 037: applianceguider för import och export (92) har
  granskats radvis. Ändringarna är verifierade lokalt i commit `ad4d5ca` och
  ännu inte pushade till PR:n.
- 2026-11-11, batch 038: guiden för virtuell hårddisk (11) har granskats
  radvis. Ändringarna är verifierade lokalt i commit `6a6739a` och ännu inte
  pushade till PR:n.
- 2026-11-11, batch 039: uppdateringsinställningar, uppdateringsintervall och
  miniverktygsfält (31) har granskats radvis. Ändringarna är verifierade
  lokalt i commit `91fc31c` och ännu inte pushade till PR:n.
- 2026-11-11, batch 040: aktivitetsöversikten för värd och virtuella
  maskiner (38) har granskats radvis. Ändringarna är verifierade lokalt i
  commit `dc5663f` och ännu inte pushade till PR:n.
- 2026-11-11, batch 041: medier, användarnamn och lösenord, seriella portar
  samt nätverksfunktioner (73) har granskats radvis. Ändringarna är
  verifierade lokalt i commit `aedd069` och ännu inte pushade till PR:n.
- 2026-11-11, batch 042: appliance-redigerarens metadata (32) har granskats
  radvis. Ändringarna är verifierade lokalt i commit `a61aa5a` och ännu inte
  pushade till PR:n.
- 2026-11-11, batch 043: första delen av meddelandecentralens fel-,
  uppdaterings- och tilläggspakettexter har granskats radvis. Ändringarna är
  verifierade lokalt i commit `5e4ed58` och ännu inte pushade till PR:n.
- 2026-11-11, batch 044: nästa del av meddelandecentralen, med installation,
  skärmtangentbord, inspelning och lagringsbussar, har granskats radvis.
  Ändringarna är verifierade lokalt i commit `32dc311` och ännu inte pushade
  till PR:n.
- 2026-11-11, batch 045: ytterligare en del av meddelandecentralen, med
  USBFS, medier, offentliga nycklar, IP, DHCP och portomdirigering, har
  granskats radvis. Ändringarna är verifierade lokalt i commit `16e46d2` och
  ännu inte pushade till PR:n.
- 2026-11-11, batch 046: ytterligare en del av meddelandecentralen, med
  USB-enheter, medier, moln- och nätverksresurser, tilläggspaket,
  ögonblicksbilder och säker start, har granskats radvis. Ändringarna är
  verifierade lokalt i commit `4e854e8` och ännu inte pushade till PR:n.
- 2026-11-11, batch 047: ytterligare en del av meddelandecentralen, med
  endast-värd-nätverk, gästtillägg, USB-behörighet, styrkort, delat urklipp
  och avstängning, har granskats radvis. Ändringarna är verifierade lokalt i
  commit `6bb42b5` och ännu inte pushade till PR:n.
- 2026-11-11, batch 048: samtliga 569 aktiva meddelanden i
  `UIMessageCenter` är granskade radvis. Delbatcherna 043–047 är verifierade
  lokalt och ännu inte pushade till PR:n.
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
