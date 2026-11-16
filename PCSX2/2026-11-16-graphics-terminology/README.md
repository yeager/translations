# PCSX2: svenska grafiktermer

Datum: 2026-11-16  
Tjänst: Crowdin, projekt 561203 (PCSX2 Emulator)  
Språk: `sv-SE`

## Ändringar

| Sträng-id | Källa | Svenska |
| --- | --- | --- |
| 4663 | `Anti-Blur` | `Motverka oskärpa` |
| 17269 | Hjälptext för `Anti-Blur` | `interna korrigeringar mot oskärpa` |
| 4757 | `Spin GPU During Readbacks` | `Håll GPU:n aktiv under återläsningar` |
| 4881 | `Precache Textures` | `Förinläs texturer` |
| 5027 | Förklaring av `interlacing offset` | `radsprångsförskjutningen` |

Granskningen ersätter svengelska ord som `Anti-Blur`, `hack`, `Spin` och
`förcachning` med svenska termer. `GS`, `GPU` och `PS2` behålls som synliga
tekniska beteckningar.

## Inskick och återläsning

Alla fem ändringar sparades via Crowdin API och lästes därefter tillbaka:

| Sträng-id | Crowdin-översättning |
| --- | ---: |
| 4663 | 450333 |
| 17269 | 450335 |
| 4757 | 450337 |
| 4881 | 450339 |
| 5027 | 450341 |

Detta är sparade Crowdin-förslag, inte belägg för granskning, godkännande
eller release uppströms.

## Kontroller

- XML-tolkning och l10n-lint godkände deltafilen utan fel.
- svlang markerade inga relevanta språkfel.
- Ett lågprioriterat, avgränsat Hunspell-prov fann att den etablerade
  sammansättningen `radsprångsförskjutning` saknades i ordlistan. Den lades
  till med test för grund- och bestämd form i hunspell-sv och pushades som
  commit `812ac24`; därefter godkände Hunspell de svenska orden. `GPU` och
  `PS2` bedöms som tekniska beteckningar, inte stavfel.
- Diffkontroll och Gitleaks passerade.
- `msgfmt` gäller PO-filer och är inte tillämpligt på XLIFF; XML-tolkningen
  kontrollerar i stället filformatet.
