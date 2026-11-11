# QGIS: etikettskala och dubbletter 274

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen behandlar etikettens synlighet efter skala och hanteringen av
dubblettetiketter. Radbrytningarna i de två skalhjälptexterna behålls, och
`inclusive` respektive `exclusive` återges som inkluderande och exkluderande
för att bevara regelns exakta innebörd.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Maximum scale, i.e. most "zoomed in".\nThis limit is inclusive, that means the label will be displayed on this scale.` | `Största skala, dvs. mest "inzoomad".\nGränsen är inkluderande. Etiketten kommer alltså att visas vid denna skala.` | `Största skala, det vill säga den mest inzoomade skalan.\nGränsen är inkluderande, vilket innebär att etiketten visas vid denna skala.` |
| `Minimum scale, i.e. most "zoomed out".\nThis limit is exclusive, that means the label will not be displayed on this scale.` | `Minsta skala, dvs. mest "utzoomad".\nGränsen är exkluderande. Etiketten kommer alltså inte visas vid denna skala.` | `Minsta skala, det vill säga den mest utzoomade skalan.\nGränsen är exkluderande, vilket innebär att etiketten inte visas vid denna skala.` |
| `Label spacing is not available on this QGIS installation` | `Etikettavstånd är inte tillgängligt på denna QGIS-installation` | `Etikettavstånd är inte tillgängligt i den här QGIS-installationen` |
| `Duplicate Labels` | `Duplicerade etiketter` | `Dubblettetiketter` |
| `Avoid duplicate labels` | `Undvik duplicerade etiketter` | `Undvik dubblettetiketter` |
| `Duplicate label removal is not available on this QGIS installation` | `Borttagning av duplicerade etiketter är inte tillgängligt på denna QGIS-installation` | `Borttagning av dubblettetiketter är inte tillgänglig i den här QGIS-installationen` |
| `Ignore label whitespace when detecting collisions` | `Ignorera etiketters blanksteg när kollisioner detekters` | `Ignorera blanksteg i etiketter när kollisioner upptäcks` |

Ingen extern ändring har gjorts. De rekommenderade texterna är lokala
kandidater tills de jämförts mot aktuella Transifex-enheter i en senare
uppladdningsbatch.
