# Batch 003: appliance, ljud och maskininställningar

Datum: 2026-11-11
Komponenter: `UIApplianceEditorWidget`,
`UIApplianceUnverifiedCertificateViewer`, `UIAudio*`,
`UIAutoCaptureKeyboardEditor`, `UIBaseMemoryEditor`, `UIBootOrderEditor`

## Granskade och ändrade områden

- Appliance- och certifikatdialoger: korrekt plural, tydligare referens till
  appliance-filen och idiomatisk text för overifierade certifikat.
- Ljud: förtydligad riktning mellan gäst och värd, korrekt verb för inspelning
  och konsekvent `Null-ljuddrivrutin`.
- Tangentbordsfångst: bestämd form, konsekventa termer för den virtuella
  maskinen och naturlig beskrivning av vart tangenttryckningar skickas.
- Minne och uppstart: enhetliga RAM-etiketter samt korrekt BIOS/UEFI-text och
  ordningsföljd för startenheter.

## Upstream

Ändringarna är lokala och inte pushade till PR #848. Full radvis granskning
och samlad slutkontroll återstår innan PR:n uppdateras.
