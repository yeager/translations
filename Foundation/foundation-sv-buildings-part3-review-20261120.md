# Foundation — svensk granskningsrapport

Datum: 2026-11-20  
Komponent: `buildings.json` (del 3)

| Engelsk källsträng | Tidigare svensk text | Föreslagen svensk text | Lint och stavning |
|---|---|---|---|
| Provides Faith to the villagers. | Ger tro till byborna. | Ger tro åt byborna. | Inga anmärkningar. |
| Fisher's hut | Fiskehydda | Fiskarstuga | Inga anmärkningar; redan registrerad i Crowdin. |
| Bailiff Office | Fogdehus | Fogdekontor | Inga anmärkningar. |

`l10n-lint --language sv` godkände filen och `hunspell-sv` fann inga stavningsanmärkningar. Två förslag skapades med HTTP 201; ett identiskt förslag fanns redan i Crowdin. Hunspell gav endast Gettext-varningen om PO-huvudets teckenuppsättning; den gäller inte översättningarna.