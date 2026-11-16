# PCSX2: tydligare svenska UI-texter

Datum: 2026-11-16  
Tjänst: Crowdin, projekt 561203 (PCSX2 Emulator)  
Språk: `sv-SE`

## Ändringar

| Sträng-id | Källa | Svenska |
| --- | --- | --- |
| 5117 | `Texture Preloading` | `Förinläsning av texturer` |
| 5249 | Hjälptext om GS-synkronisering | GS-hämtningar och naturlig svensk förklaring av riskerna |
| 5327 | `Render To Separate Window` | `Återge i separat fönster` |
| 5391 | Pausa och återuppta emulatorn | `återupptar` i stället för `avpausar` |
| 5479 | `Support &Forums...` | `&Supportforum...` |

`Återge` är den naturliga verbformen för den här UI-åtgärden. I den tekniska
GS-hjälptexten används `hämtningar`, vilket beskriver intern dataöverföring
och inte en nedladdning från internet. Ampersanden i `&Supportforum...` är en
bevarad tangentbordsmarkering från källtexten.

## Inskick och återläsning

Alla fem ändringar sparades via Crowdin API och lästes därefter tillbaka:

| Sträng-id | Crowdin-översättning |
| --- | ---: |
| 5117 | 450343 |
| 5249 | 450345 |
| 5327 | 450347 |
| 5391 | 450349 |
| 5479 | 450351 |

Detta är sparade Crowdin-förslag, inte belägg för granskning, godkännande
eller release uppströms.

## Kontroller

- XML-tolkning och l10n-lint godkände deltafilen utan fel.
- svlang markerade inga relevanta språkfel.
- Ett lågprioriterat, avgränsat Hunspell-prov godkände de svenska orden.
  `GS` och `GPU` bedöms som tekniska beteckningar, inte stavfel.
- Diffkontroll och Gitleaks passerade.
- `msgfmt` gäller PO-filer och är inte tillämpligt på XLIFF; XML-tolkningen
  kontrollerar i stället filformatet.
