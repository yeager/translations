# PCSX2: dödzon i helskärmsgränssnittet

Datum: 2026-11-16  
Tjänst: Crowdin, projekt 561203 (PCSX2 Emulator)  
Språk: `sv-SE`

## Ändring och kontroll

| Sträng-id | Källa | Tidigare svenska | Svenska |
| --- | --- | --- | --- |
| 10492 | `Deadzone` | `Dödläge` | `Dödzon` |

Strängen är en etikett i PCSX2:s helskärmsgränssnitt. `Dödzon` följer de
närliggande kontrollinställningarna och den etablerade termen i projektets
svenska terminologi.

Översättningen sparades via Crowdin API och lästes tillbaka som
Crowdin-översättning 450321. Detta är ett sparat förslag, inte belägg för
granskning, godkännande eller release uppströms.

## Kontroller

- XML-tolkning och l10n-lint godkände deltafilen utan fel.
- svlang markerade inga språkfel.
- Hunspell kördes inte för denna enradiga, termgranskade ändring medan en
  separat Hunspell-körning belastar processorn. Den används fortsatt med
  avgränsad omfattning och CPU-kontroll.
- Diffkontroll och Gitleaks passerade.
- `msgfmt` gäller PO-filer och är inte tillämpligt på XLIFF; XML-tolkningen
  kontrollerar i stället filformatet.
