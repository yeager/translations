# Batch 006: maskininställningar och indikatorer

Datum: 2026-11-11
Komponenter: `UIIndicator*`, `UIMachineSettings*`, `UIMedium*`,
`UIMotherboardFeaturesEditor`, `UINativeWizard`, `UINetworkFeaturesEditor`,
`UINetworkReplyPrivate`, `UIPointingHIDEditor`, `UIPortForwardingTable`,
`UIProcessorFeaturesEditor` och `UIProxyFeaturesEditor`.

## Granskade och ändrade områden

- Statusindikatorer: korrekt böjning för in- och utmatning samt tydliga
  tangentbordsstatusar för fångst och värdtangentkombinationer.
- Maskininställningar: rättad betydelse för `at most one`, kretsuppsättning,
  processor- och USB-varningar samt konsekvent maskinvaru- och nätverksspråk.
- Nätverk och proxy: rättade `postomdirigeringar`, URL-fel, nästlad
  virtualisering och tydligare formuleringar för proxyinställningar.
- Lagring och visning: rättade saknade bestämningar, stavfel i helskärmsläge
  och naturliga svenska etiketter.

## Delkontroll

- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga läckta hemligheter.
- `l10n-lint`: endast de två avsiktligt tomma språkmetadatafälten (`--`) är
  felklassade som oöversatta.

## Upstream

Ändringarna är lokala och inte pushade till PR #848. Full radvis granskning
och samlad slutkontroll återstår innan PR:n uppdateras.
