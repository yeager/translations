# QGIS: åtgärder och HTTP-överföring 062

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`  
Källkod: `src/core/actions/qgsaction.cpp`

QGIS-åtgärder kan skicka data som en URL-kodad begäran, JSON eller HTTP
`multipart`. Den befintliga svenska texten blandar engelsk och svensk form i
den första etiketten, gör HTTP-termen alltför allmän i den andra och beskriver
felaktigt hela åtgärden som ett kommando i informationsrutan. `multipart`
behålls som synlig HTTP- och MIME-term.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Submit URL (urlencoded or JSON)` | `URL att skicka (urlencoded eller JSON)` | `Skicka URL (URL-kodad eller JSON)` |
| `Submit URL (multipart)` | `URL att skicka (flerdelad)` | `Skicka URL (multipart)` |
| HTML-rutan `Action Details` | `Kommandodetaljer` och `Kommando` | `Åtgärdsdetaljer` och `Åtgärd` |

I HTML-strängen bevaras markup, radbrytningar och platshållarna `%1`, `%2`,
`%3`, `%4` och `%6` exakt. Ingen extern ändring har gjorts; aktuella
Transifex-enhetsidentifierare behöver hämtas innan en deltafil kan skapas.
