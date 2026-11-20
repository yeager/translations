# Foundation — svensk granskningsrapport

Datum: 2026-11-20  
Komponent: `buildings.release.json` (del 2)

| Engelsk källsträng | Tidigare svensk text | Föreslagen/sparad svensk text | Lint och stavning |
|---|---|---|---|
| Stone Tower | Stentorn, mindre | Stentorn | Inga anmärkningar. |
| Stone Bell Tower, Spired | Klocktornet av sten, spetsigt | Spetsigt klocktorn av sten | Inga anmärkningar. |
| Stone Bell Tower, Sloped | Klocktornet av sten, sluttande | Klocktorn av sten med sluttande tak | Inga anmärkningar. |
| Rustic Upper Gate, Balcony | Rustik övre grind, balkong | Rustik övre port, balkong | Inga anmärkningar. |
| Rustic Upper Gate, Balustrade | Rustik övre grind, balustrad | Rustik övre port, balustrad | Inga anmärkningar. |
| Rustic Upper Gate, Roof | Rustik Övre grind, Tak | Rustik övre port, tak | Inga anmärkningar. |
| Rustic Upper Gate, Open | Rustik övre grind, öppen | Rustik övre port, öppen | Inga anmärkningar. |

`l10n-lint --language sv` godkände filen och `hunspell-sv` fann inga stavningsanmärkningar. Alla granskade ändringar skapades i Crowdin via API (HTTP 201). `Stone Tower` förekommer flera gånger i källan; den granskade förekomsten skickades därför explicit till sträng-ID 14772. Hunspell gav endast Gettext-varningen om PO-huvudets teckenuppsättning; den gäller inte översättningarna.