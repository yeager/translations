# Blender Manual: svensk granskningsbatch 48

Datum: 4 november 2026

Källa: `exports/2026-11-04/blender-manual-manual-sv.po`.

## Omfattning

Sex poster för upplösningsskala och tillfälliga redigerare i Inställningar ›
Gränssnitt. Den felaktigt tillagda parentesfrasen efter *Upplösningsskala*
tas bort. Blender-områden använder den etablerade termen *område*, och
`File Browser` följer den befintliga svenska UI-termen *filbläddrare*.

`DPI` bevaras som teknisk förkortning och blir i löpande text
*DPI-värdet*. Inga filvägar, kodidentifierare eller formatnamn ändras.

## Kontroller

- `msgfmt --check --statistics`: 6 översatta meddelanden och godkänd syntax.
- Radvis jämförelse av `(msgctxt, msgid)` mot råexporten: 6/6 träffar.
- `l10n-lint --language sv`: inga träffar.
- `svlang skrivregler --enable-interpunktion` och `svlang svengelska`: inga
  träffar i måltexterna.
- Hunspell `sv_SE`: endast produktnamnet Blender och `DPI` träffade; inga
  stavfel.
- `git diff --check`: godkänd.
- Gitleaks: inga hemligheter hittades.

Råexporten är orörd. Deltafilen ingår i nästa körning av generatorn för
Weblate-batcher med högst 100 poster per fil.
