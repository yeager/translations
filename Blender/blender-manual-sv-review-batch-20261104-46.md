# Blender Manual: svensk granskningsbatch 46

Datum: 4 november 2026

Källa: `exports/2026-11-04/blender-manual-manual-sv.po`.

## Omfattning

Tio poster i Inställningar › Gränssnitt › Statusrad och närliggande
översättningsinställningar. Batchen rättar bland annat:

- `Collection` → *Samling* enligt Blenders projektspecifika terminologi;
- `vertices` → *hörnpunkter* i meshgeometrisk kontext;
- `System Memory` → *Systemminne*;
- synlig dokumentationslänk `extensions` → *tillägg*;
- `New Data` → *Nya data*, alltså nya Blender-datablock, inte uppgifter.

RST-roller och deras API-mål bevaras. `3D Viewport` följer den etablerade
formen *3D-vyport*.

## Kontroller

- `msgfmt --check --statistics`: 10 översatta meddelanden och godkänd syntax.
- Radvis jämförelse av `(msgctxt, msgid)` mot råexporten: 10/10 träffar.
- `l10n-lint --language sv`: inga träffar.
- `svlang skrivregler --enable-interpunktion` och `svlang svengelska`: inga
  träffar i måltexterna.
- Hunspell `sv_SE`: endast avsiktliga RST- och API-identifierare samt
  facktermer träffade; inga stavfel.
- `git diff --check`: godkänd.
- Gitleaks: inga hemligheter hittades.

Råexporten är orörd. Deltafilen ingår i nästa körning av den reproducerbara
generatorn för Weblate-batcher med högst 100 poster per fil.
