# Foundation — svensk granskningsrapport

Datum: 2026-11-20  
Komponent: `buildings.json` (del 10)

| Engelsk källsträng | Tidigare svensk text | Föreslagen svensk text | Lint och stavning |
|---|---|---|---|
| Rock Holder | Stenhållare | Stenställ | Inga anmärkningar. |
| Candle | Stearinljus | Ljus | Inga anmärkningar; redan registrerad i Crowdin. |
| Buttress | Stödpelare | Strävpelare | Inga anmärkningar. |

`l10n-lint --language sv` godkände filen och `hunspell-sv` fann inga stavningsanmärkningar. Två förslag skapades med HTTP 201; `Ljus` fanns redan identiskt i Crowdin. Hunspell gav endast Gettext-varningen om PO-huvudets teckenuppsättning; den gäller inte översättningarna.