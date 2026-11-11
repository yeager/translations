# Batch 004: maskin, moln och virtuella medier

Datum: 2026-11-11
Komponenter: `UIChipsetEditor`, `UIChooser*`, `UICloudConsoleManager`,
`UICloudProfileManager`, `UIColorThemeEditor`, `UICommon`, `UIDetails`,
`UIDiskEncryptionSettingsEditor`, `UIDiskVariantWidget`, `UIMedium` och
`UIMediumManager`.

## Granskade och ändrade områden

- Kretsuppsättning och maskinväljare: svenska sammansättningar, korrekt
  söktext och idiomatisk beskrivning av maskinträdet.
- Molnkonsoler: rättad felstavning av `konsol` i de nygranskade strängarna och
  konsekvent benämning av molnkonsollhanteraren.
- Färgtema, status och detaljvyer: naturliga tillståndsnamn, konsekvent
  `endast-värd-nätverkskort` och svenska sammansättningar för portar och
  kretsuppsättningar.
- Diskkryptering och virtuella medier: rättad grammatik, korrekt referens till
  anslutna diskar och tydlig skillnad mellan bas-, differens- och övriga
  medier.

## Kontroller

- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga läckta hemligheter.
- `l10n-lint`: två avsiktligt tomma metadatafält (`--`) rapporteras som
  oöversatta. Övriga återstående varningar är tekniska litteraler eller
  verktygets falska positiva träffar och granskas i slutkontrollen.

## Upstream

Ändringarna är lokala och inte pushade till PR #848. Full radvis granskning
och samlad slutkontroll återstår innan PR:n uppdateras.
