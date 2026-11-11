# QGIS: geobearbetningens parametrar och objektfilter 106

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar parametrar, enumval, utbredning och filter för objekt i
geobearbetningen. Syntaxvärdena `x min,x max,y min,y max` och exempelvärdet
`1,3` bevaras, liksom hakparenteserna i statusetiketten.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| ` [overridden name: %1]` | `[åsidosatt namn: %1]` | ` [åsidosatt namn: %1]` |
| `Clear Selection` | `Rensa valda` | `Rensa markering` |
| `[Not selected]` | `[Ej vald]` | `[Inte valt]` |
| `selected option index (starting from 0), array of indices, or comma separated string of options (e.g. '1,3')` | `valt alternativs index (med början på 0), array av index, eller kommaseparerad textsträng med alternativ (t.ex. '1,3')` | `index för valt alternativ (med början på 0), en matris med index eller en kommaseparerad sträng med alternativ (till exempel '1,3')` |
| `string representation of an expression` | `textrepresentation av uttryck` | `strängrepresentation av ett uttryck` |
| `string of the format 'x min,x max,y min,y max' or a geometry value (bounding box is used)` | `textsträng med formatet 'x min,x max,y min,y max' eller ett geometrivärde (begränsningsboxen används)` | `sträng med formatet 'x min,x max,y min,y max' eller ett geometrivärde (begränsningsrutan används)` |
| `path to layer destination` | `sökväg till lagrets destination` | `sökväg till lagerdestinationen` |
| `If set, allows the default method for handling features with invalid geometries to be overridden` | `Om inställt, tillåts standardmetoden för hantering av objekt med ogiltig geometri att åsidosättas` | `Om alternativet är valt kan standardmetoden för hantering av objekt med ogiltiga geometrier åsidosättas` |
| `If set, limits the maximum number of features which will be processed from this source` | `Om inställt, begränsas antal objekt som kommer att processas från denna källa` | `Om alternativet är valt begränsas det maximala antalet objekt som bearbetas från den här källan` |
| `Limit features processed` | `Begränsa processade objekt` | `Begränsa antalet bearbetade objekt` |
| `Geometry Not Required` | `Geometri krävs ej` | `Geometri krävs inte` |
| `Stop Algorithm Execution When a Geometry is Invalid` | `Stoppa algoritmexekvering när en geometri är felaktig` | `Stoppa algoritmen om en geometri är ogiltig` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
