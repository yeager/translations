# PCSX2: svenska etiketter för dödzoner

Datum: 2026-11-16  
Tjänst: Crowdin, projekt 561203 (PCSX2 Emulator)  
Språk: `sv-SE`

## Ändringar

| Sträng-id | Källa | Svenska |
| --- | --- | --- |
| 6753 | `Deadzone:` | `Dödzon:` |
| 6879 | `Analog Deadzone` | `Analog dödzon` |
| 7815 | `Whammy Bar Deadzone` | `Whammybarens dödzon` |

`dödzon` är den redan etablerade termen i de närliggande svenska
inställningarna. Formuleringarna följer etikettens konkreta styrdon i stället
för att använda det missvisande `dödläge`.

## Inskick och återläsning

Alla tre ändringar sparades via Crowdin API och lästes därefter tillbaka:

| Sträng-id | Crowdin-översättning |
| --- | ---: |
| 6753 | 450315 |
| 6879 | 450317 |
| 7815 | 450319 |

Sträng 7733 har samma källa som 6753 men kan inte få samma korrigering
inskickad igen. Crowdin returnerar dubblett eftersom korrekt historisk
översättning 119861 (`Dödzon:`) redan finns, samtidigt som en senare felaktig
översättning 251616 (`Dödläge:`) konkurrerar. Inga röster eller historiska
översättningar ändrades utan en projektgodkänd metod.

Detta är sparade Crowdin-förslag, inte belägg för granskning, godkännande
eller release uppströms.

## Kontroller

- XML-tolkning och l10n-lint godkände deltafilen utan fel.
- svlang markerade inga relevanta språkfel.
- Ett lågprioriterat Hunspell-prov med hunspell-sv godkände `dödzon` och
  `analog`. `Whammybarens` saknas som förväntat eftersom det är ett synligt
  produktnamn. Körningen begränsades till berörda ord och lämnade ingen
  Hunspell-process kvar.
- Diffkontroll och Gitleaks passerade.
- `msgfmt` gäller PO-filer och är inte tillämpligt på XLIFF; XML-tolkningen
  kontrollerar i stället filformatet.
