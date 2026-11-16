# PCSX2: ljud, återgivning och URL

Datum: 2026-11-16  
Tjänst: Crowdin, projekt 561203 (PCSX2 Emulator)  
Språk: `sv-SE`

## Ändringar

| Sträng-id | Källa | Svenska |
| --- | --- | --- |
| 10912 | Fel vid öppning av URL | `URL:en` |
| 11078 | Fel vid skapande av renderingsenhet | `återgivningsenhet` och `återgivningsmetod` |
| 11116 | Blending Accuracy | `Blandningsnoggrannheten` |
| 11244 | `Audio Backend` | `Ljudutdatametod` |
| 11246 | Förklaring av Audio Backend | Svensk förklaring av Cubeb, SDL och Null |
| 11398 | Stereo till surround | `flerkanalsljud` |

`Ljudutdatametod` beskriver användarens val av ljudkomponent utan den
svengelska formen `ljudbakände`. Cubeb, SDL och Null är komponentnamn och
bevaras. `URL:en` följer svensk böjning av förkortningar.

## Kontroller

- Deltafilen är välformad XML och kontrolleras med l10n-lint.
- svlang körs på måltexterna.
- Hunspell-sv körs lågprioriterat för ett begränsat urval och processlistan
  kontrolleras efteråt.
- `msgfmt` gäller PO-filer och är inte tillämpligt på XLIFF.

svlang markerade komponentnamnen `Basic`, `Cubeb`, `SDL` och `Null` som
ovanliga i frekvenslistan samt gav en falsk positiv V2-varning i bisatsen
efter `att GPU:n`. Inget av detta är ett svenskt språkfel.

## Inskick och återläsning

Alla sex ändringar sparades via Crowdin API och lästes därefter tillbaka:

| Sträng-id | Crowdin-översättning |
| --- | ---: |
| 10912 | 450425 |
| 11078 | 450427 |
| 11116 | 450429 |
| 11244 | 450431 |
| 11246 | 450433 |
| 11398 | 450435 |

Detta är sparade Crowdin-förslag, inte belägg för godkännande eller release
uppströms.
