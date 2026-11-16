# PCSX2: minneskort i mapp

Datum: 2026-11-16  
Tjänst: Crowdin, projekt 561203 (PCSX2 Emulator)  
Språk: `sv-SE`

## Ändring

| Sträng-id | Källa | Tidigare svenska | Ny svenska |
| --- | --- | --- | --- |
| 7537 | Dialog för att skapa minneskort | `Vi rekommenderar att använda 8MB ellerMapp för bästa kompatibilitet.` | `För bästa kompatibilitet rekommenderar vi antingen minneskort på 8 MB eller minneskort som lagras i en mapp.` |

Den tidigare texten saknade både innehåll och mellanrum efter `eller`.
Den nya formuleringen beskriver funktionen utan en otydlig ny sammansättning.

## Kontroller

- Deltafilen är välformad XML och godkändes av l10n-lint.
- Hunspell-sv kördes med låg prioritet på de berörda svenska orden. Ingen
  kvarvarande Hunspell-process upptäcktes efter körningen.
- svlang används som kompletterande språkkontroll.
- `msgfmt` gäller PO-filer och är inte tillämpligt på XLIFF.

## Inskick och återläsning

Ändringen sparades via Crowdin API och lästes därefter tillbaka som
översättning `450369`. Det är ett sparat Crowdin-förslag, inte belägg för
granskning, godkännande eller release uppströms.
