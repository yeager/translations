# PCSX2: återgivning och färgkartor

Datum: 2026-11-16  
Tjänst: Crowdin, projekt 561203 (PCSX2 Emulator)  
Språk: `sv-SE`

## Ändringar

| Sträng-id | Källa | Svenska |
| --- | --- | --- |
| 9905 | `Disable Render Fixes` | `Inaktivera korrigeringar för återgivning` |
| 9911 | Hjälptext om `colormap-textures` | `texturer med färgkarta` |
| 9929 | `Use Software Renderer For FMVs` | `Använd programvaruåtergivning för FMV:er` |

`Återgivning` används konsekvent för den synliga grafiska funktionen, medan
`texturer med färgkarta` beskriver `colormap-textures` utan en onödigt svår
sammansättning. `GPU` och `CPU` är etablerade tekniska beteckningar och får
svensk böjning som `GPU:n` och `CPU:n` i löpande text.

## Kontroller

- Deltafilen är välformad XML och kontrolleras med l10n-lint.
- svlang körs på måltexterna.
- Hunspell-sv körs lågprioriterat för ett begränsat urval och processlistan
  kontrolleras efteråt.
- `msgfmt` gäller PO-filer och är inte tillämpligt på XLIFF.

svlang markerade endast förkortningen `FMV` som ovanlig i sin frekvenslista.
Det är en etablerad beteckning för förinspelad video och inte ett språkfel.

## Inskick och återläsning

Alla tre ändringar sparades via Crowdin API och lästes därefter tillbaka:

| Sträng-id | Crowdin-översättning |
| --- | ---: |
| 9905 | 450399 |
| 9911 | 450401 |
| 9929 | 450403 |

Detta är sparade Crowdin-förslag, inte belägg för godkännande eller release
uppströms.
