# Blender Manual: svensk granskningsbatch 44

Datum: 4 november 2026

Källa: `exports/2026-11-04/blender-manual-manual-sv.po`.

## Omfattning

Tjugotre poster för datum- och tidsformat i Inställningar › Gränssnitt.
Batchen rättar felkopplade svenska måltexter och kompletterar de tidigare
tomma beskrivningarna. Formatmönstren `dd/mm/yyyy`, `yyyy-mm-dd` och
motsvarande varianter lämnas avsiktligt oförändrade: de är konkreta
formatsträngar, inte svensk löptext. Däremot är deras synliga förklaringar
översatta till exempelvis *dag/månad/år* och *år-månad-dag*.

`24-Hour` och `12-Hour` blir *24-timmarsformat* respektive
*12-timmarsformat*. Tal- och klockexemplen bevaras exakt.

## Terminologiverifiering, 5 november 2026

De svenska UI-etiketterna i den aktuella Blender 5.3-exporten bekräftar
*Datumformat*, *Tidsformat*, *24-timmarsformat* och *12-timmarsformat*.
Översättningsminnet använder samma huvudtermer. Det gäller däremot inte som
skäl att lokalisera själva exemplen: `yyyy-mm-dd`, `dd/mm/yyyy`, `23:59` och
`11:59 PM` visar valbara format och ska därför återges bokstavligt.

## Kontroller

- `msgfmt --check --statistics`: 23 översatta meddelanden och godkänd syntax.
- Radvis jämförelse av `(msgctxt, msgid)` mot råexporten: 23/23 träffar.
- `l10n-lint --language sv`: 0 fel och 3 varningar. Två
  `date-format`-varningar gäller de bevarade literalformaten i exemplen;
  `number-range-dash` misstolkar datumformatet `27-02-2019` som ett
  talintervall. Alla tre är avsiktliga falska positiva träffar.
- `svlang skrivregler --enable-interpunktion` och `svlang svengelska`: inga
  träffar i måltexterna.
- Hunspell `sv_SE`: endast formatmönster och etablerade
  `12`-/`24-timmarsformat` träffade; inga stavfel.
- `git diff --check`: godkänd.
- Gitleaks: inga hemligheter hittades.

Råexporten är orörd. Deltafilen är redo att ingå i en senare samlad, högst
100-strängars uppladdningsbatch för den generiska Manual-komponenten.
