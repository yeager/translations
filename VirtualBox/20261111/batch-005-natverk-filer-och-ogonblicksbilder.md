# Batch 005: nätverk, filer och ögonblicksbilder

Datum: 2026-11-11
Komponenter: `UINetworkAttachmentEditor`, `UINetworkManager`,
`UINotificationProgress`, `UISharedFolderDetailsEditor`, `UISharedFoldersEditor`,
`UISnapshot*`, `UISoftKeyboard`, `UIDisplayFeaturesEditor`, `UIDownloader*`,
`UIErrorString`, `UIExecutionCapEditor`, `UIFileManager`, `UIFontScaleEditor`
och `UIGlobalSettingsProxy`.

## Granskade och ändrade områden

- Nätverk: konsekventa begrepp för värdoperativsystem,
  endast-värd-nätverk och DHCP samt omformulerade hjälptester för begriplig
  svensk syntax.
- Delade mappar: det tekniska kommandot `mount -t vboxsf share mount_point`
  återställdes oförändrat; parameter- och produktnamn bevaras.
- Ögonblicksbilder och virtuellt tangentbord: rättade bestämd form, plural,
  engelskt layoutnamn och skanningskod.
- Filhanteraren: korrigerade felstavningen `Resultatdetaij`, status- och
  metadataetiketter samt filhanterings- och proxytext.

## Delkontroll

- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `git diff --check`: godkänd.

## Upstream

Ändringarna är lokala och inte pushade till PR #848. Full radvis granskning
och samlad slutkontroll återstår innan PR:n uppdateras.
