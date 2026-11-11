# Batch 007: lagring och maskinguiden

Datum: 2026-11-11
Komponenter: `UISharedClipboardEditor`, `UISnapshotFolderEditor`,
`UIStorageSettingsEditor`, `UISerialSettingsEditor`, `UIVMCloseDialog` och
`UIWizardNewVM`.

## Granskade och ändrade områden

- Delat urklipp och ögonblicksbilder: idiomatisk betydelse för
  behovsstyrd delning och konsekvent benämning av virtuella maskiner.
- Lagring: rättade medium-, SSD- och inkopplingstexter samt naturlig svenska
  i val av virtuella och fysiska enheter.
- Seriella portar: källkommandon och exempel som `myvbox`, `/tmp/myvbox` och
  `hostname:port` bevarades oförändrade.
- Avslutsdialog och maskinguiden: korrigerade saknade källsträngar under
  kontrollen, avstängnings- och återställningstext samt stavfelet
  `hårrdisk`.

## Delkontroll

- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `git diff --check`: godkänd.

## Upstream

Ändringarna är lokala och inte pushade till PR #848. Full radvis granskning
och samlad slutkontroll återstår innan PR:n uppdateras.
