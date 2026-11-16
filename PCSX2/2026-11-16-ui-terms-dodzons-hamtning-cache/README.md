# PCSX2 – svenska UI-termer för dödzoner, hämtning och cache

Datum: 2026-11-16  
Tjänst: Crowdin, projekt 561203 (PCSX2 Emulator)  
Språk: `sv-SE`

## Ändringar

| Sträng-id | Källa | Svenska |
| --- | --- | --- |
| 7117 | `Steering Deadzone` | `Styrningens dödzon` |
| 7789 | `Button/Trigger Deadzone` | `Dödzon för knappar/avtryckare` |
| 11494 | `Toggle Hardware Mipmapping` | `Växla maskinvarumipmapping` |
| 7311 | Fel om `Hardware Download Mode` | `Hårdvaruhämtningsläge` med den synliga inställningen `Accurate` bevarad |
| 7349 | Fel om `Texture Preloading` | `Förinläsning av texturer` med den synliga inställningen `Full` bevarad |
| 8495 | `Disable Shader Cache` | `Inaktivera shadercache` |

`dödzon`, `förinläsning av texturer`, `maskinvaruhämtningsläge` och
`shadercache` följer PCSX2:s redan granskade svenska kataloger. `Accurate`
och `Full` är synliga värden i programmets inställningar och lämnas därför
oförändrade.

## Inskick och återläsning

Alla sex översättningar sparades via Crowdin API och lästes därefter tillbaka:

| Sträng-id | Crowdin-översättning |
| --- | ---: |
| 7117 | 450303 |
| 7789 | 450305 |
| 11494 | 450307 |
| 7311 | 450309 |
| 7349 | 450311 |
| 8495 | 450313 |

Detta är sparade Crowdin-förslag, inte belägg för granskning, godkännande
eller release uppströms.

## Kontroller

- XML-tolkning och l10n-lint godkände deltafilen utan fel.
- Hunspell accepterade de svenska facktermerna och markerade endast
  `Accurate`, som är ett synligt inställningsvärde från programmet.
- svlang saknar anglicism- och skrivregelsvarningar. Dess enda V2-markering
  gäller imperativet `Växla` och är en falsk positiv.
- Diffkontroll och Gitleaks passerade.
- `msgfmt` gäller PO-filer och är inte tillämpligt på XLIFF; XML-tolkningen
  kontrollerar i stället filformatet.
