# QGIS: punktmolnshöjd och vertikalt CRS 093

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar punktmolnets höjdinställningar. Den följer QGIS etablerade
term `koordinatreferenssystem (CRS)` och skiljer lagrets egenskaper från
projektets. HTML-struktur, listpunkter och platshållarna `%1` och `%2`
bevaras.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Not set` | `Inte satt` | `Inte angivet` |
| `Layer coordinate reference system is set to a compound CRS (%1), so the layer's vertical CRS is the vertical component of this CRS (%2).` | `Lagrets koordinatsystem är satt till ett sammansatt koordinatsystem (%1), så lagrets vertikala koordinatsystem är den vertikala komponenten av detta (%2).` | `Lagrets koordinatreferenssystem är ett sammansatt CRS (%1), så lagrets vertikala CRS är den vertikala komponenten i detta CRS (%2).` |
| `Layer coordinate reference system is set to a geographic 3D CRS (%1), so the vertical CRS cannot be manually specified.` | `Lagrets koordinatsystem är satt till ett geografiskt 3D-koordinatsystem (%1), så projektets vertikala koordinatsystem kan inte anges manuellt.` | `Lagrets koordinatreferenssystem är ett geografiskt 3D-CRS (%1), så det vertikala CRS:et kan inte anges manuellt.` |
| `Layer coordinate reference system is set to a geocentric CRS (%1), so the vertical CRS cannot be manually specified.` | `Lagrets koordinatsystem är satt till ett geocentriskt koordinatsystem (%1), så projektets vertikala koordinatsystem kan inte anges manuellt.` | `Lagrets koordinatreferenssystem är ett geocentriskt CRS (%1), så det vertikala CRS:et kan inte anges manuellt.` |
| `Layer coordinate reference system is set to a projected 3D CRS (%1), so the vertical CRS cannot be manually specified.` | `Lagrets koordinatsystem är satt till ett projicerat 3D-koordinatsystem (%1), så projektets vertikala koordinatsystem kan inte anges manuellt.` | `Lagrets koordinatreferenssystem är ett projicerat 3D-CRS (%1), så det vertikala CRS:et kan inte anges manuellt.` |
| `Automatically sets the offset so that the lowest point in the cloud sits at an elevation of 0.` | `Ställer automatiskt in förskjutning så att lägsta punkten i molnet finns på en höjd av 0.` | `Anger automatiskt förskjutningen så att den lägsta punkten i punktmolnet hamnar på höjden 0.` |
| HTML-hjälpen för höjdskalning och förskjutning | Delvis korrekt, men saknar idiomatisk svensk ordföljd | `<html><head/><body><p><span style=" font-weight:600;">Höjdskalning och höjdförskjutning kan användas för att korrigera höjdvärdena i punktmolnet manuellt vid rendering.</span></p><p>Skalningen tillämpas på punktmolnets höjdvärden innan förskjutningen läggs till.</p></body></html>` |
| `Respect layer's coloring` | `Används lagrets färgsättning` | `Respektera lagrets färgsättning` |
| HTML-hjälpen för `Vertical Reference System` | Språkligt tung sista instruktion | `<html><head/><body><p>Vertikala referenssystem stöds för punktmolnslager av:</p><ul><li>höjdprofiler</li><li>resultat från identifieringsverktyget</li><li>3D-kartvyer, när 3D-vyn har ett vertikalt referenssystem</li></ul><p><i>Andra verktyg eller tillägg kan ignorera det vertikala referenssystemet. Validera därför resultaten noga.</i></p></body></html>` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
