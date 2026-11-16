# PCSX2: uppdatering och sparade tillstånd

Datum: 2026-11-16  
Tjänst: Crowdin, projekt 561203 (PCSX2 Emulator)  
Språk: `sv-SE`

## Ändringar

| Sträng-id | Källa | Svenska |
| --- | --- | --- |
| 5653 | Fel om inofficiell version | Rättar `Tyvärr` och `inkompatibilitet`, med HTML och länk bevarade. |
| 5703 | Fel vid borttagning av tillståndsfil | `tillståndsfilen` i korrekt bestämd form. |
| 5731 | `Save Slot %1 (%2)` | `Sparplats %1 (%2)`. |
| 6273 | Varning om inkompatibla sparade tillstånd | Tydlig svensk rubrik och naturlig instruktion, med HTML bevarad. |

`Save state` översätts konsekvent som `sparat tillstånd` i användartext,
medan en enskild fil blir `tillståndsfil`. Platshållarna `%1` och `%2`, HTML
och länkmålet är oförändrade.

## Inskick och återläsning

Alla fyra ändringar sparades via Crowdin API och lästes därefter tillbaka:

| Sträng-id | Crowdin-översättning |
| --- | ---: |
| 5653 | 450353 |
| 5703 | 450355 |
| 5731 | 450357 |
| 6273 | 450359 |

Detta är sparade Crowdin-förslag, inte belägg för granskning, godkännande
eller release uppströms.

## Kontroller

- XML-tolkning och l10n-lint godkände deltafilen utan fel.
- svlang markerade `PCSX2` och `GitHub` som sällsynta produktnamn samt
  tre falska V2-varningar. Satsinledningarna `Tyvärr försöker`,
  `För att förhindra ... är` och `Om du installerar ... blir` följer svensk
  ordföljd.
- Ett lågprioriterat, avgränsat Hunspell-prov godkände de svenska orden.
  `PCSX2`, `GitHub` och länkadressen är avsiktliga produkt- och nätverksnamn.
- Diffkontroll och Gitleaks passerade.
- `msgfmt` gäller PO-filer och är inte tillämpligt på XLIFF; XML-tolkningen
  kontrollerar i stället filformatet.
