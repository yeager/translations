# PCSX2: avflätning, återgivning och konsoler

Datum: 2026-11-16  
Tjänst: Crowdin, projekt 561203 (PCSX2 Emulator)  
Språk: `sv-SE`

## Ändringar

| Sträng-id | Källa | Svenska |
| --- | --- | --- |
| 10496 | CPU-konvertering av framebuffer | `4- och 8-bitarsbildbuffertar` |
| 10502 | `No Deinterlacing` | `Ingen avflätning` |
| 10694 | Växla till Software Renderer | `Växlar till programvaruåtergivning...` |
| 10696 | Växla till Hardware Renderer | `Växlar till maskinvaruåtergivning...` |
| 10834 | Log To System Console | `Logga till &systemkonsol` |
| 10836 | Log To Debug Console | `Logga till &felsökningskonsol` |

`Återgivning` används för den synliga växlingen av återgivningsmetod.
`Systemkonsol` och `felsökningskonsol` får korrekt svensk enkelkonsonant.
Ampersanden i de två menyvalen är bevarad som tangentbordsmarkering.

## Kontroller

- Deltafilen är välformad XML och kontrolleras med l10n-lint.
- svlang körs på måltexterna.
- Hunspell-sv körs lågprioriterat för ett begränsat urval och processlistan
  kontrolleras efteråt.
- `msgfmt` gäller PO-filer och är inte tillämpligt på XLIFF.

svlang markerade endast den tekniska sammansättningen `bitarsbildbuffertar`
som ovanlig i frekvenslistan. Det är inte ett stavnings- eller grammatikfel.

## Inskick och återläsning

Alla sex ändringar sparades via Crowdin API och lästes därefter tillbaka:

| Sträng-id | Crowdin-översättning |
| --- | ---: |
| 10496 | 450413 |
| 10502 | 450415 |
| 10694 | 450417 |
| 10696 | 450419 |
| 10834 | 450421 |
| 10836 | 450423 |

Detta är sparade Crowdin-förslag, inte belägg för godkännande eller release
uppströms.
