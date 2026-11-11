# QGIS: etikettrotations- och visningsval 273

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen behandlar etikettmotorns rotationshantering och etikettens
visningsinställningar. Verben `fästa` och `lossa` används för `pin` och
`unpin`, i enlighet med etablerad svensk UI-terminologi för fästa objekt.
Den tekniska konstanten `NULL` bevaras.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Uncheck to write labeling engine derived rotation on pin and NULL on unpin` | `Avmarkera för att skriva etikettmotorns rotationsvärden vid fästning av etiketter och NULL vid lösgörning av etiketter` | `Avmarkera för att skriva etikettmotorns beräknade rotation när etiketten fästs och NULL när den lossas` |
| `Data defined` | `Datadefinierat` | `Datadefinierad` |
| `Preserve data rotation values` | `Bevara datadefinierade rotationsvärden` | `Bevara datadefinierade rotationsvärden` |
| `No repeat` | `Ingen upprepning` | `Upprepa inte` |
| `Label options` | `Etikettinställningar` | `Etikettalternativ` |
| `Text orientation` | `Riktning för text` | `Textriktning` |
| `General Settings` | `Generella inställningar` | `Allmänna inställningar` |
| `Maximum distance` | `Största avstånd` | `Maximalt avstånd` |

Raden `Preserve data rotation values` har kontrollerats rad för rad och
bedömts korrekt. Den dokumenteras här för att skilja avsiktligt bevarad text
från korrigeringskandidater. Ingen extern ändring har gjorts.
