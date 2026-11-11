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
- 2026-11-11, batch 049: första delen av `UIActionPool` har granskats
  radvis. Ändringarna är verifierade lokalt i commit `0b9825d` och ännu inte
  pushade till PR:n.
- 2026-11-11, batch 050: nästa del av `UIActionPool` har granskats radvis.
  Ändringarna är verifierade lokalt i commit `0a323f7` och ännu inte pushade
  till PR:n.
- 2026-11-11, batch 051: nästa del av `UIActionPool` har granskats radvis.
  Ändringarna är verifierade lokalt i commit `5cff19e` och ännu inte pushade
  till PR:n.
- 2026-11-11, batch 052: samtliga 511 aktiva meddelanden i `UIActionPool`
  är granskade radvis. Delbatcherna 049–052 är verifierade lokalt och ännu
  inte pushade till PR:n.
- 2026-11-11, batch 053: samtliga 76 aktiva meddelanden i `UIWizardNewVM`
  är granskade radvis. Ändringarna är verifierade lokalt i commit `82733f4`
  och ännu inte pushade till PR:n.
- 2026-11-11, batch 054: samtliga 84 aktiva meddelanden i
  `UINotificationProgress` är granskade radvis. Ändringarna är verifierade
  lokalt i commit `f65ab27` och ännu inte pushade till PR:n.
- 2026-11-11, batch 055: samtliga 97 aktiva meddelanden i `UIFileManager`
  är granskade radvis. Ändringarna är verifierade lokalt i commit `c2f49f1`
  och ännu inte pushade till PR:n.
- 2026-11-11, batch 056: samtliga 85 aktiva meddelanden i
  `UIVMInformationDialog` är granskade radvis. Ändringarna är verifierade
  lokalt i commit `3e6854f` och ännu inte pushade till PR:n.
- 2026-11-11, batch 057: samtliga 111 aktiva meddelanden i `UINetworkManager`
  är granskade radvis. Ändringarna är verifierade lokalt i commit `cead0d7`
  och ännu inte pushade till PR:n.
- 2026-11-11, batch 058: samtliga 278 aktiva meddelanden i `UICommon` är
  granskade radvis. De tidigare 281 posterna omfattade tre `vanished`-poster.
  Ändringarna är verifierade lokalt i commit `e3a131b` och ännu inte pushade
  till PR:n.
- 2026-11-11, batch 059: samtliga 52 aktiva meddelanden i
  `UIHelpBrowserWidget` är granskade radvis. Ändringarna är verifierade lokalt
  i commit `d9961d7` och ännu inte pushade till PR:n.
- 2026-11-11, batch 060: samtliga 107 aktiva meddelanden i `UIDetails` är
  granskade radvis. Ändringarna är verifierade lokalt i commit `6a23a06` och
  ännu inte pushade till PR:n.
- 2026-11-11, batch 061: samtliga 49 aktiva meddelanden i
  `UIWizardExportApp` är granskade radvis. Ändringarna är verifierade lokalt
  i commit `5405d76` och ännu inte pushade till PR:n.
- 2026-11-11, batch 062: samtliga 45 aktiva meddelanden i `UIMediumManager`
  är granskade radvis. Ändringarna är verifierade lokalt i commit `c50614d`
  och ännu inte pushade till PR:n.
- 2026-11-11, batch 063: samtliga 43 aktiva meddelanden i
  `UIWizardImportApp` är granskade radvis. Ändringarna är verifierade lokalt
  i commit `7cc27ec` och ännu inte pushade till PR:n.
- 2026-11-11, batch 064: samtliga 18 aktiva meddelanden i `UIMediumSelector`
  är granskade radvis. Ändringarna är verifierade lokalt i commit `eb32cfc`
  och ännu inte pushade till PR:n.
- 2026-11-11, batch 065: samtliga 17 aktiva meddelanden i `UIHostComboEditor`
  är granskade radvis. Ändringen är verifierad lokalt i commit `e265627` och
  ännu inte pushad till PR:n.
- 2026-11-11, batch 066: samtliga 16 aktiva meddelanden i `UIUSBFiltersEditor`
  är granskade radvis. Ändringarna är verifierade lokalt i commit `746b4f6`
  och ännu inte pushade till PR:n.
- 2026-11-11, batch 067: samtliga 18 aktiva meddelanden i
  `UITakeSnapshotDialog` är granskade radvis. Ändringarna är verifierade
  lokalt i commit `766be4d` och ännu inte pushade till PR:n.
- 2026-11-11, batch 068: samtliga 15 aktiva meddelanden i
  `UIFDCreationDialog` är granskade radvis. Ändringarna är verifierade lokalt
  i commit `dc64857` och ännu inte pushade till PR:n.
- 2026-11-11, batch 069: samtliga 14 aktiva meddelanden i
  `UIUserNamePasswordEditor` är granskade radvis. Ändringen är verifierad
  lokalt i commit `1525891` och ännu inte pushad till PR:n.
- 2026-11-11, batch 070: samtliga 14 aktiva meddelanden i `UIToolsItem` är
  granskade radvis. Ändringarna är verifierade lokalt i commit `5da26bf` och
  ännu inte pushade till PR:n.
- 2026-11-11, batch 071: samtliga 12 aktiva meddelanden i
  `UIAdvancedSettingsDialogMachine` är granskade radvis. Ändringen är
  verifierad lokalt i commit `be45645` och ännu inte pushad till PR:n.
- 2026-11-11, batch 072: samtliga 11 aktiva meddelanden i
  `UIMediumSizeAndPathGroupBox` är granskade radvis. Ändringarna är
  verifierade lokalt i commit `f26489a` och ännu inte pushade till PR:n.
- 2026-11-11, batch 073: samtliga 11 aktiva meddelanden i `UIMediumItem` är
  granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 074: samtliga 11 aktiva meddelanden i
  `UIFilePathSelector` är granskade radvis. Ändringen är verifierad lokalt i
  commit `a1ef75b` och ännu inte pushad till PR:n.
- 2026-11-11, batch 075: samtliga 10 aktiva meddelanden i
  `UIHostnameDomainNameEditor` är granskade radvis. Ändringen är verifierad
  lokalt i commit `699cb54` och ännu inte pushad till PR:n.
- 2026-11-11, batch 076: samtliga 10 aktiva meddelanden i
  `UISharedClipboardProviderThread` är granskade radvis. Ingen textändring
  behövdes.
- 2026-11-11, batch 077: samtliga 10 aktiva meddelanden i `UIMediumTools` är
  granskade radvis. Ändringarna är verifierade lokalt i commit `3430207` och
  ännu inte pushade till PR:n.
- 2026-11-11, batch 078: samtliga 7 aktiva meddelanden i
  `UISharedClipboardProvider` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 079: samtliga 10 aktiva meddelanden i `UISnapshotItem`
  är granskade radvis. Ändringarna är verifierade lokalt i commit `07f89e7`
  och ännu inte pushade till PR:n.
- 2026-11-11, batch 080: samtliga 9 aktiva meddelanden i
  `UIMenuBarEditorWidget` är granskade radvis. Ändringen är verifierad lokalt
  i commit `d0dea3a` och ännu inte pushad till PR:n.
- 2026-11-11, batch 081: samtliga 9 aktiva meddelanden i
  `UIIndicatorKeyboard` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 082: samtliga 8 aktiva meddelanden i
  `UIMediumSearchWidget` är granskade radvis. Ändringen är verifierad lokalt
  i commit `8fff2fb` och ännu inte pushad till PR:n.
- 2026-11-11, batch 083: samtliga 8 aktiva meddelanden i
  `UIIndicatorNetwork` är granskade radvis. Ändringen är verifierad lokalt i
  commit `49c7f6f` och ännu inte pushad till PR:n.
- 2026-11-11, batch 084: samtliga 8 aktiva meddelanden i
  `UIMachinePreview` är granskade radvis. Ändringen är verifierad lokalt i
  commit `a19576b` och ännu inte pushad till PR:n.
- 2026-11-11, batch 085: samtliga 8 aktiva meddelanden i
  `UIIndicatorFeatures` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 086: samtliga 8 aktiva meddelanden i
  `UIImportLicenseViewer` är granskade radvis. Ändringarna är verifierade
  lokalt i commit `b6d2379` och ännu inte pushade till PR:n.
- 2026-11-11, batch 087: samtliga 19 aktiva meddelanden i `UITranslator` är
  granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 088: samtliga 7 aktiva meddelanden i
  `UIMachineSettingsStorage` är granskade radvis. Ändringen är verifierad
  lokalt i commit `43ea1fa` och ännu inte pushad till PR:n.
- 2026-11-11, batch 089: samtliga 10 aktiva meddelanden i
  `UIMachineSettingsNetwork` är granskade radvis. Ändringarna är verifierade
  lokalt i commit `a3345c0` och ännu inte pushade till PR:n.
- 2026-11-11, batch 090: samtliga 6 aktiva meddelanden i
  `UIMachineSettingsSerial` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 091: samtliga 8 aktiva meddelanden i
  `UIMachineSettingsGeneral` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 092: samtliga 4 aktiva meddelanden i
  `UIBootOrderEditor` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 093: samtliga 4 aktiva meddelanden i
  `UIExecutionCapEditor` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 094: det enda aktiva meddelandet i
  `UIIndicatorHardDrive` är granskat radvis. Ingen textändring behövdes.
- 2026-11-11, batch 095: samtliga 7 aktiva meddelanden i `UIIndicatorMouse`
  är granskade radvis. Ändringarna är verifierade lokalt i commit `7d3fba7`
  och ännu inte pushade till PR:n.
- 2026-11-11, batch 096: samtliga 7 aktiva meddelanden i
  `UIIndicatorRecording` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 097: samtliga 4 aktiva meddelanden i `UIIndicatorAudio`
  är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 098: samtliga 6 aktiva meddelanden i
  `UINotificationCenter` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 099: samtliga 4 aktiva meddelanden i `UIIndicatorUSB`
  är granskade radvis. Ändringen är verifierad lokalt i commit `73085cd` och
  ännu inte pushad till PR:n.
- 2026-11-11, batch 100: samtliga 3 aktiva meddelanden i
  `UIIndicatorDisplay` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 101: samtliga 3 aktiva meddelanden i
  `UIDisplayScreenFeaturesEditor` är granskade radvis. Ingen textändring
  behövdes.
- 2026-11-11, batch 102: samtliga 11 aktiva meddelanden i
  `UIMachineSettingsDisplay` är granskade radvis. Ändringen är verifierad
  lokalt i commit `2d07e90` och ännu inte pushad till PR:n.
- 2026-11-11, batch 103: samtliga 2 aktiva meddelanden i
  `UIIndicatorFloppyDisks` är granskade radvis. Ändringarna är verifierade
  lokalt i commit `884442f` och ännu inte pushade till PR:n.
- 2026-11-11, batch 104: samtliga 2 aktiva meddelanden i
  `UIIndicatorOpticalDisks` är granskade radvis. Ändringarna är verifierade
  lokalt i commit `f9051f9` och ännu inte pushade till PR:n.
- 2026-11-11, batch 105: samtliga 4 aktiva meddelanden i
  `UIVirtualMachineItemCloud` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 106: samtliga 9 aktiva meddelanden i
  `UIAdvancedSettingsDialogGlobal` är granskade radvis. Ingen textändring
  behövdes.
- 2026-11-11, batch 107: samtliga 7 aktiva meddelanden i
  `UIRecordingVideoBitrateEditor` är granskade radvis. Ingen textändring
  behövdes.
- 2026-11-11, batch 108: samtliga 5 aktiva meddelanden i
  `UIMediumSizeEditor` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 109: samtliga 5 aktiva meddelanden i
  `UIRecordingVideoFrameSizeEditor` är granskade radvis. Ingen textändring
  behövdes.
- 2026-11-11, batch 110: båda aktiva meddelandena i
  `UIAudioSettingsEditor` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 111: samtliga 3 aktiva meddelanden i
  `UIAccelerationFeaturesEditor` är granskade radvis. Ingen textändring
  behövdes.
- 2026-11-11, batch 112: samtliga 6 aktiva meddelanden i
  `UIVideoMemoryEditor` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 113: samtliga 6 aktiva meddelanden i `UIErrorString` är
  granskade radvis. Ändringarna är verifierade lokalt i commit `52ae590` och
  ännu inte pushade till PR:n.
- 2026-11-11, batch 114: båda aktiva meddelandena i
  `UIGraphicsControllerEditor` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 115: samtliga 11 aktiva meddelanden i
  `UIBootFailureDialog` är granskade radvis. Ändringen är verifierad lokalt i
  commit `7509366` och ännu inte pushad till PR:n.
- 2026-11-11, batch 116: samtliga 5 aktiva meddelanden i
  `UIAudioFeaturesEditor` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 117: samtliga 3 aktiva meddelanden i
  `UINetworkReplyPrivateThread` är granskade radvis. Ingen textändring
  behövdes.
- 2026-11-11, batch 118: båda aktiva meddelandena i
  `UISettingsSerializerProgress` är granskade radvis. Ingen textändring
  behövdes.
- 2026-11-11, batch 119: samtliga 6 aktiva meddelanden i
  `UIAcquirePublicKeyDialog` är granskade radvis. Terminologin har rättats
  till `offentlig nyckel` i lokal commit `633f115`; ändringen är ännu inte
  pushad till PR:n.
- 2026-11-11, batch 120: samtliga 5 aktiva meddelanden i
  `UIAddDiskEncryptionPasswordDialog` är granskade radvis. Ingen textändring
  behövdes.
- 2026-11-11, batch 121: samtliga 5 aktiva meddelanden i
  `UIRecordingAudioProfileEditor` är granskade radvis. Ingen textändring
  behövdes.
- 2026-11-11, batch 122: samtliga 6 aktiva meddelanden i
  `UIRecordingVideoFrameRateEditor` är granskade radvis. Bildfrekvenstexten
  har förtydligats i lokal commit `771bbd8` och är ännu inte pushad till PR:n.
- 2026-11-11, batch 123: samtliga 7 aktiva meddelanden i
  `UIScaleFactorEditor` är granskade radvis. Grammatiken har rättats i lokal
  commit `b21621e` och ändringen är ännu inte pushad till PR:n.
- 2026-11-11, batch 124: samtliga 6 aktiva meddelanden i
  `UIShortcutConfigurationEditor` är granskade radvis. Etiketterna har
  förbättrats i lokal commit `f7d90f7` och är ännu inte pushade till PR:n.
- 2026-11-11, batch 125: samtliga 6 aktiva meddelanden i
  `UIMaximumGuestScreenSizeEditor` är granskade radvis. Hjälptexterna har
  förtydligats i lokal commit `28cb328` och är ännu inte pushade till PR:n.
- 2026-11-11, batch 126: samtliga 4 aktiva meddelanden i `UIMiniToolBar` är
  granskade radvis. Verktygsfältsterminologin har rättats i lokal commit
  `2786bae` och ändringen är ännu inte pushad till PR:n.
- 2026-11-11, batch 127: samtliga 3 aktiva meddelanden i
  `UIFormEditorWidget` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 128: samtliga 6 aktiva meddelanden i
  `UIGuestControlTreeWidget` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 129: samtliga 11 aktiva meddelanden i
  `UIGuestProcessControlWidget`, `UIGuestProcessTreeItem` och
  `UIGuestSessionTreeItem` är granskade radvis. Etiketterna har rättats i
  lokal commit `3ba2a5c` och är ännu inte pushade till PR:n.
- 2026-11-11, batch 130: samtliga 4 aktiva meddelanden i
  `UIStatusBarEditorWidget` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 131: samtliga 72 aktiva meddelanden i
  `UIStorageSettingsEditor` är granskade radvis. Två språkfel har rättats i
  lokal commit `1058a35` och ändringarna är ännu inte pushade till PR:n.
- 2026-11-11, batch 132: samtliga 18 aktiva meddelanden i
  `UITakeSnapshotDialog` är granskade radvis. Tre åtgärdstexter har rättats i
  lokal commit `99647ee` och ändringarna är ännu inte pushade till PR:n.
- 2026-11-11, batch 133: samtliga 5 aktiva meddelanden i `UITextEditor` är
  granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 134: det enda aktiva meddelandet i `UIToolBox` är
  granskat radvis. Verktygstipset har rättats i lokal commit `3a7a2e5` och är
  ännu inte pushat till PR:n.
- 2026-11-11, batch 135: samtliga 14 aktiva meddelanden i `UIToolsItem` är
  granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 136: det enda aktiva meddelandet i `UIToolsView` är
  granskat radvis. Ingen textändring behövdes.
- 2026-11-11, batch 137: samtliga 2 aktiva meddelanden i `UITpmEditor` är
  granskade radvis. Verktygstipset har rättats i lokal commit `0bf25fc` och
  är ännu inte pushat till PR:n.
- 2026-11-11, batch 138: samtliga 19 aktiva meddelanden i `UITranslator` är
  granskade radvis. Relativ tid har rättats i lokal commit `b87eebc` och är
  ännu inte pushad till PR:n.
- 2026-11-11, batch 139: samtliga 6 aktiva meddelanden i
  `UIUSBControllerEditor` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 140: samtliga 19 aktiva meddelanden i
  `UIUSBFilterDetailsEditor` är granskade radvis. Tre strängar har rättats i
  lokal commit `49d5fbe` och är ännu inte pushade till PR:n.
- 2026-11-11, batch 141: samtliga 16 aktiva meddelanden i
  `UIUSBFiltersEditor` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 142: samtliga 2 aktiva meddelanden i `UIUSBMenu` är
  granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 143: samtliga 2 aktiva meddelanden i
  `UIUSBSettingsEditor` är granskade radvis. Terminologin har rättats i lokal
  commit `8054e3e` och är ännu inte pushad till PR:n.
- 2026-11-11, batch 144: samtliga 13 aktiva meddelanden i `UIUSBTools` är
  granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 145: samtliga 11 aktiva meddelanden i `UIUpdateManager`
  är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 146: samtliga 13 aktiva meddelanden i
  `UIUpdateSettingsEditor` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 147: samtliga 14 aktiva meddelanden i
  `UIUserNamePasswordEditor` är granskade radvis. Felmeddelandet har rättats
  i lokal commit `078d202` och är ännu inte pushat till PR:n.
- 2026-11-11, batch 148: samtliga 6 aktiva meddelanden i
  `UIVMActivityMonitorPaneContainer` är granskade radvis. Knapptexten har
  rättats i lokal commit `f97dffa` och är ännu inte pushad till PR:n.
- 2026-11-11, batch 149: samtliga 30 aktiva meddelanden i
  `UIVMActivityOverviewWidget` är granskade radvis. Ingen textändring
  behövdes.
- 2026-11-11, batch 150: samtliga 12 aktiva meddelanden i `UIVMCloseDialog`
  är granskade radvis. Två texter har rättats i lokal commit `b00b984` och är
  ännu inte pushade till PR:n.
- 2026-11-11, batch 151: samtliga 2 aktiva meddelanden i
  `UIVRDEAuthLibraryEditor` är granskade radvis. Verktygstipset har rättats i
  lokal commit `5f1cf89` och är ännu inte pushat till PR:n.
- 2026-11-11, batch 152: samtliga 5 aktiva meddelanden i
  `UIVirtualBoxManager` är granskade radvis. Tre texter har rättats i lokal
  commit `c761881` och är ännu inte pushade till PR:n.
- 2026-11-11, batch 153: samtliga 3 aktiva meddelanden i
  `UIVirtualMachineItemLocal` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 154: samtliga 2 aktiva meddelanden i `UIVisualStateEditor`
  är granskade radvis. Verktygstipset har rättats i lokal commit `0287650` och
  är ännu inte pushat till PR:n.
- 2026-11-11, batch 155: samtliga 3 aktiva meddelanden i `VBoxAboutDlg` är
  granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 156: samtliga 3 aktiva meddelanden i `VBoxLicenseViewer`
  är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 157: samtliga 2 aktiva meddelanden i
  `QIArrowButtonPress` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 158: samtliga 5 metadatafält i `@@@` är granskade
  radvis. Ingen textändring behövdes.
- 2026-11-11, batch 159: samtliga 2 aktiva meddelanden i `QIArrowSplitter`
  är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 160: det enda aktiva meddelandet i `QIDialogContainer`
  är granskat radvis. Ingen textändring behövdes.
- 2026-11-11, batch 161: det enda aktiva meddelandet i `QIInputDialog` är
  granskat radvis. Ingen textändring behövdes.
- 2026-11-11, batch 162: det enda aktiva meddelandet i `QILabel` är granskat
  radvis. Ingen textändring behövdes.
- 2026-11-11, batch 163: det enda aktiva meddelandet i `QILineEdit` är
  granskat radvis. Ingen textändring behövdes.
- 2026-11-11, batch 164: samtliga 7 aktiva meddelanden i `QIMessageBox` är
  granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 165: det enda aktiva meddelandet i `QIRichTextLabel` är
  granskat radvis. Ingen textändring behövdes.
- 2026-11-11, batch 166: samtliga 4 aktiva meddelanden i `SFTreeViewItem`
  är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 167: samtliga 4 aktiva meddelanden i
  `UIAdvancedSettingsDialog` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 168: samtliga 2 aktiva meddelanden i
  `UIAudioControllerEditor` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 169: samtliga 2 aktiva meddelanden i
  `UIAudioHostDriverEditor` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 170: det enda aktiva meddelandet i
  `UIChooserAbstractModel` är granskat radvis. Ingen textändring behövdes.
- 2026-11-11, batch 171: samtliga 9 aktiva meddelanden i
  `UIChooserItemGroup` är granskade radvis. Två pluralformer har rättats
  lokalt och inväntar den samlade uppdateringen av PR #848.
- 2026-11-11, batch 172: det enda aktiva meddelandet i `UIChooserNodeGroup`
  är granskat radvis. Benämningen har förtydligats lokalt och inväntar den
  samlade uppdateringen av PR #848.
- 2026-11-11, batch 173: det enda aktiva meddelandet i
  `UIChooserNodeMachine` är granskat radvis. Ingen textändring behövdes.
- 2026-11-11, batch 174: samtliga 4 aktiva meddelanden i
  `UIChooserSearchWidget` är granskade radvis. Fyra verktygstips har rättats
  lokalt och inväntar den samlade uppdateringen av PR #848.
- 2026-11-11, batch 175: det enda aktiva meddelandet i `UIChooserView` är
  granskat radvis. Ingen textändring behövdes.
- 2026-11-11, batch 176: samtliga 2 aktiva meddelanden i
  `UICloudMachineSettingsDialog` är granskade radvis. Ingen textändring
  behövdes.
- 2026-11-11, batch 177: samtliga 2 aktiva meddelanden i
  `UIDefaultMachineFolderEditor` är granskade radvis. Etiketten har rättats
  lokalt och inväntar den samlade uppdateringen av PR #848.
- 2026-11-11, batch 178: det enda aktiva meddelandet i
  `UIDescriptionEditor` är granskat radvis. Ingen textändring behövdes.
- 2026-11-11, batch 179: samtliga 2 aktiva meddelanden i `UIDetailsElement`
  är granskade radvis. Två menyåtgärder har rättats lokalt och inväntar den
  samlade uppdateringen av PR #848.
- 2026-11-11, batch 180: det enda aktiva meddelandet i `UIDetailsItem` är
  granskat radvis. Tillgänglighetsnamnet har rättats lokalt och inväntar den
  samlade uppdateringen av PR #848.
- 2026-11-11, batch 181: det enda aktiva meddelandet i `UIDetailsView` är
  granskat radvis. Tillgänglighetsbeskrivningen har rättats lokalt och
  inväntar den samlade uppdateringen av PR #848.
- 2026-11-11, batch 182: samtliga 3 aktiva meddelanden i `UIDownloader` är
  granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 183: samtliga 2 aktiva meddelanden i
  `UIDownloaderExtensionPack` är granskade radvis. Ingen textändring
  behövdes.
- 2026-11-11, batch 184: samtliga 2 aktiva meddelanden i
  `UIDownloaderGuestAdditions` är granskade radvis. Spartexten har rättats
  lokalt och inväntar den samlade uppdateringen av PR #848.
- 2026-11-11, batch 185: samtliga 2 aktiva meddelanden i
  `UIEmptyFilePathSelector` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 186: det enda aktiva meddelandet i
  `UIGlobalSettingsGeneral` är granskat radvis. Ingen textändring behövdes.
- 2026-11-11, batch 187: samtliga 2 aktiva meddelanden i
  `UIGuestProcessControlDialog` är granskade radvis. Ingen textändring
  behövdes.
- 2026-11-11, batch 188: det enda aktiva meddelandet i `UIHelpButton` är
  granskat radvis. Ingen textändring behövdes.
- 2026-11-11, batch 189: samtliga 4 aktiva meddelanden i `UIHomePane` är
  granskade radvis. Två HTML-texter har rättats lokalt och inväntar den
  samlade uppdateringen av PR #848.
- 2026-11-11, batch 190: samtliga 2 aktiva meddelanden i `UIHotKeyEditor`
  är granskade radvis. Två verktygstips har rättats lokalt och inväntar den
  samlade uppdateringen av PR #848.
- 2026-11-11, batch 191: samtliga 2 aktiva meddelanden i
  `UIIndicatorKeyboardExtension` är granskade radvis. Statusradstexterna har
  rättats lokalt och inväntar den samlade uppdateringen av PR #848.
- 2026-11-11, batch 192: samtliga 2 aktiva meddelanden i
  `UIIndicatorSharedFolders` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 193: samtliga 4 aktiva meddelanden i `UILanguageItem` är
  granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 194: samtliga 3 aktiva meddelanden i
  `UILanguageSettingsEditor` är granskade radvis. Fältetiketten har rättats
  lokalt och inväntar den samlade uppdateringen av PR #848.
- 2026-11-11, batch 195: det enda aktiva meddelandet i `UILineTextEdit` är
  granskat radvis. Ingen textändring behövdes.
- 2026-11-11, batch 196: det enda aktiva meddelandet i `UIMachineLogic` är
  granskat radvis. Ingen textändring behövdes.
- 2026-11-11, batch 197: det enda aktiva meddelandet i `UIMachineView` är
  granskat radvis. Tillgänglighetsbeskrivningen har rättats lokalt och
  inväntar den samlade uppdateringen av PR #848.
- 2026-11-11, batch 198: det enda aktiva meddelandet i `UIMachineWindow` är
  granskat radvis. Fönstertiteln har rättats lokalt och inväntar den samlade
  uppdateringen av PR #848.
- 2026-11-11, batch 199: samtliga 5 aktiva meddelanden i
  `UIMiniToolbarSettingsEditor` är granskade radvis. Ingen textändring
  behövdes.
- 2026-11-11, batch 200: samtliga 4 aktiva meddelanden i
  `UIMonitorCountEditor` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 201: samtliga 2 aktiva meddelanden i
  `UINotificationDownloader` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 202: samtliga 3 aktiva meddelanden i `UIPaneContainer`
  är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 203: samtliga 2 aktiva meddelanden i
  `UIParavirtProviderEditor` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 204: det enda aktiva meddelandet i `UIPopupCenter` är
  granskat radvis. Popuptexten har rättats lokalt och inväntar den samlade
  uppdateringen av PR #848.
- 2026-11-11, batch 205: samtliga 2 aktiva meddelanden i `UIPopupPane` är
  granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 206: samtliga 2 aktiva meddelanden i
  `UIRecordingFilePathEditor` är granskade radvis. Ingen textändring
  behövdes.
- 2026-11-11, batch 207: samtliga 2 aktiva meddelanden i
  `UIRecordingModeEditor` är granskade radvis. Ingen textändring behövdes.
- 2026-11-11, batch 208: samtliga 2 aktiva meddelanden i
  `UIRecordingScalingModeEditor` är granskade radvis. Ingen textändring
  behövdes.
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
