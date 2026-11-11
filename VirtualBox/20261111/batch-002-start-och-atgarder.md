# Batch 002: start, åtgärder och uppstartsdiagnostik

Datum: 2026-11-11
Komponenter: `QApplication`, `UIAccelerationFeaturesEditor`, `UIActionPool`,
`UIBootFailureDialog`

## Granskade och ändrade områden

- Kärnmodulsdialoger: idiomatisk svenska, korrekt imperativ och tydlig
  upplysning om `root`-användaren. Kommandot `/sbin/vboxconfig` och samtliga
  modulnamn är oförändrade.
- Virtualisering: `Nested Paging` har normaliserats till `Nästlad
  sidindelning` med sammanhängande hjälptxt.
- Åtgärder och menyobjekt: rättade bland annat felaktig översättning av
  ”Rename selected virtual machine group” till borttagning, felaktiga
  sammansättningar, konsol med ett l, bestämd form för paneler och konsekvent
  VirtualBox-maskindefinitionsfil.
- Uppstartsdiagnostik: naturliga svenska felmeddelanden, korrekt ISO-fil,
  DVD, dialogruta och uppstartsmedium.

## Upstream

Ändringarna är lokala och ingår i den pågående helgranskningen. De ska pushas
till PR #848 först efter sammanlagd format-, språk- och diffkontroll.
