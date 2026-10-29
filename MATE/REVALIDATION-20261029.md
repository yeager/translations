# MATE: omvalidering av väntande uppladdningar 29 oktober 2026

De tre lokala kandidaterna kontrollerades på nytt innan Fedora Weblate har
låsts upp.

| Kandidat | Syntax | l10n-lint | Bedömning |
| --- | --- | --- | --- |
| `mate-control-center-sv-pending-unlock-20261011.po` | `msgfmt --check` godkänd | 0 fel, 0 varningar | Redo för en ny exportjämförelse efter upplåsning. |
| `mate-control-center-help-sv-pending-unlock-20261011.po` | `msgfmt --check` godkänd; bara en oförändrad standardvarning i PO-huvudet | 0 fel, 1 varning | Varningen gäller årtalet `2015-2021` i upphovsrättstexten och är inte en kandidatändring. |
| `mate-terminal-sv-pending-unlock-20261019.po` | `msgfmt --check` godkänd | 0 fel, 2 varningar | Varningarna gäller källbevarade adress- och upphovsrättsintervall med tankstreck, inte de 15 svenska rättningarna. |

Informationssignaler om kortkommandons understreck, produktnamn och avvikande
sluttecken har lästs. De är normala följder av GTK-markörer, oförändrade namn
eller källans formatering. Ingen automatisk ändring har gjorts.

Innan import ska en färsk export från respektive komponent användas och endast
fortfarande relevanta rättningar återappliceras. Fedora Weblate var låst vid
den här kontrollen; ingen uppladdning gjordes.
