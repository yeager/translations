# PCSX2: avflätning och återgivning

Datum: 2026-11-16  
Tjänst: Crowdin, projekt 561203 (PCSX2 Emulator)  
Språk: `sv-SE`

## Ändringar

| Sträng-id | Källa | Svenska |
| --- | --- | --- |
| 6413 | Varning för `Spin GPU During Readbacks` | Svensk alternativtext och tydligare prestandavarning. |
| 6627 | `Cycle Deinterlace Mode` | `Växla avflätningsläge`. |
| 6629 | Status för `Deinterlace mode` | `Avflätningsläget är inställt till ...`. |
| 6489 | `Disable Render Fixes` | `Inaktivera korrigeringar för återgivning`. |

`Avflätning` och `återgivning` ersätter engelska UI-ord. Den bokstavliga
platshållaren `{}` och den omgivande apostrofsentiteten är bevarade.

## Inskick och återläsning

Alla fyra ändringar sparades via Crowdin API och lästes därefter tillbaka:

| Sträng-id | Crowdin-översättning |
| --- | ---: |
| 6413 | 450361 |
| 6627 | 450363 |
| 6629 | 450365 |
| 6489 | 450367 |

Detta är sparade Crowdin-förslag, inte belägg för granskning, godkännande
eller release uppströms.

## Kontroller

- XML-tolkning och l10n-lint godkände deltafilen utan fel.
- svlang markerade två falska V2-varningar eftersom den synliga alternativtexten
  `Håll GPU:n aktiv under återläsningar` ingår i en sats. Ordföljden är korrekt
  med hela alternativtexten som subjekt och `är` som finit verb.
- Ett lågprioriterat, avgränsat Hunspell-prov fann att
  `avflätningsläge` saknades. Grund- och bestämd form lades till i
  hunspell-sv och pushades som commit `53dac42`; därefter godkände Hunspell
  de svenska orden. `GPU` bedöms som en teknisk beteckning, inte stavfel.
- Diffkontroll och Gitleaks passerade.
- `msgfmt` gäller PO-filer och är inte tillämpligt på XLIFF; XML-tolkningen
  kontrollerar i stället filformatet.
