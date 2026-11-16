# PCSX2: interna GS-hämtningar

Datum: 2026-11-16  
Tjänst: Crowdin, projekt 561203 (PCSX2 Emulator)  
Språk: `sv-SE`

## Ändringar

| Sträng-id | Källa | Svenska |
| --- | --- | --- |
| 8471 | `Hardware Download Mode` | `Hårdvaruhämtningsläge` |
| 8473 | `Changes synchronization behavior for GS downloads.` | `Ändrar synkroniseringsbeteendet för GS-hämtningar.` |
| 5245 | `GS Download Mode` | `GS-hämtningsläge` |

I dessa grafikinställningar betyder `download` intern hämtning av GS-data,
inte att användaren hämtar något från internet. `Hämtningsläge` följer den
redan granskade PCSX2-termen `Hårdvaruhämtningsläge` och förtydligar
funktionen i gränssnittet.

## Inskick och återläsning

Ändringarna sparades via Crowdin API och lästes därefter tillbaka:

| Sträng-id | Crowdin-översättning |
| --- | ---: |
| 8471 | 450323 |
| 8473 | 450325 |
| 5245 | 450327 |

Detta är sparade Crowdin-förslag, inte belägg för granskning, godkännande
eller release uppströms.

## Kontroller

- XML-tolkning och l10n-lint godkände deltafilen utan fel.
- svlang markerade inga språkfel.
- Ett avgränsat Hunspell-prov med låg prioritet godkände de svenska orden.
  Endast `GS` markerades, vilket är väntat eftersom det är en
  programförkortning och inte ett stavfel i sin UI-kontext.
- Diffkontroll och Gitleaks passerade.
- `msgfmt` gäller PO-filer och är inte tillämpligt på XLIFF; XML-tolkningen
  kontrollerar i stället filformatet.
