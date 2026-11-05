# Blender Manual: svensk granskningsbatch 45

Datum: 4 november 2026

Källa: `exports/2026-11-04/blender-manual-manual-sv.po`.

## Omfattning

Nitton poster ur Inställningar › Gränssnitt för färgväljare, sidhuvudens
placering och faktorvisning. Batchen ersätter flera semantiskt felaktiga
svenska måltexter, bland annat *Sidhuvuds position*, *Procentdel* och felaktig
översättning av flyttal.

`Color Space` följer den redan verifierade Blender-terminologin
*färgrymd*. `HSV`, `HSL`, `SV`, `HS` och `HV` bevaras som etablerade
färgmodellsförkortningar. RST-roller och destinationsmål är intakta.

## Kontroller

- `msgfmt --check --statistics`: 19 översatta meddelanden och godkänd syntax.
- Radvis jämförelse av `(msgctxt, msgid)` mot råexporten: 19/19 träffar.
- `l10n-lint --language sv`: inga träffar.
- `svlang skrivregler --enable-interpunktion` och `svlang svengelska`: inga
  träffar i måltexterna.
- Hunspell `sv_SE`: endast avsiktliga RST-roller och etablerade tekniska
  förkortningar träffade; inga stavfel.
- `git diff --check`: godkänd.
- Gitleaks: inga hemligheter hittades.

Batch 1–45 omfattar nu 505 verifierade manualdelta-poster enligt den samlade
`msgfmt`-kontrollen. Råexporten är orörd; den samlade uppladdningen måste ändå
delas i högst 100-strängars batcher enligt Weblate-flödet.

## Terminologisk efterkontroll 5 november

UI-katalogen belägger **Färgväljarens typ**, **Rubrikposition**,
**Behåll befintligt**, **Visningstyp för faktor** och **Procentandel**.
Manualens rubriktexter och den förklarande texten följer nu samma termval.
Särskilt har den tvetydiga formuleringen om placeringen överst skrivits om
så att den beskriver rubrikens beteende direkt.
