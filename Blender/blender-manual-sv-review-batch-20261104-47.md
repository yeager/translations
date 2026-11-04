# Blender Manual: svensk granskningsbatch 47

Datum: 4 november 2026

Källa: `exports/2026-11-04/blender-manual-manual-sv.po`.

## Omfattning

Elva poster för textåtergivning och teckensnitt i Inställningar › Gränssnitt.
Batchen ersätter bland annat blandningen av engelska och svenska i
teckensnittsinställningarna och den missvisande formen *Mono-space Font*.

Terminologin har lagts till i projektets lista:

- `Anti-Aliasing` → *Kantutjämning*
- `Subpixel Anti-Aliasing` → *Subpixelutjämning*
- `font hinting` → *teckensnittshintning*

Länkmålet till den engelska Wikipediaartikeln är en URL och ska vara
oförändrat. RST-termen i texten har däremot svensk synlig text.

## Kontroller

- `msgfmt --check --statistics`: 11 översatta meddelanden och godkänd syntax.
- Radvis jämförelse av `(msgctxt, msgid)` mot råexporten: 11/11 träffar.
- `l10n-lint --language sv`: inga träffar.
- `svlang skrivregler --enable-interpunktion` och `svlang svengelska`: inga
  träffar i måltexterna.
- Hunspell `sv_SE`: endast de dokumenterade tekniska facktermerna och
  RST-markeringen träffade; inga stavfel.
- `git diff --check`: godkänd.
- Gitleaks: inga hemligheter hittades.

Råexporten är orörd. Deltafilen ingår i nästa körning av generatorn för
Weblate-batcher med högst 100 poster per fil.
