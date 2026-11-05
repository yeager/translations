# Blender Manual: svensk granskningsbatch 43

Datum: 4 november 2026

Källa: `exports/2026-11-04/blender-manual-manual-sv.po`.

## Omfattning

Sjutton poster ur Inställningar › Gränssnitt. Batchen återställer korrekta
svenska beskrivningar för dolda datablock, hörnhandtag, numeriska pilar,
Inställningar-fönstret, minskad rörelse och menystängning.

`Preferences` följer den svenska UI-beteckningen *Inställningar*. I tekniska
förklaringar används den etablerade sammansättningen *datablock*; RST-roller
och deras mål är bevarade. *Minska rörelse* återger tillgänglighetsfunktionen
`Reduce Motion` utan att felaktigt ge intryck av att själva animationen ska
upprepas.

En efterkontroll mot UI-exporten den 5 november bekräftade den exakta
etiketten *Numeriska inmatningspilar*, som används i batchen i stället för en
fri omskrivning.

## Kontroller

- `msgfmt --check --statistics`: 17 översatta meddelanden och godkänd syntax.
- Radvis jämförelse av `(msgctxt, msgid)` mot råexporten: 17/17 träffar.
- `l10n-lint --language sv`: inga träffar.
- `svlang skrivregler --enable-interpunktion` och `svlang svengelska`: inga
  träffar i måltexterna.
- Hunspell `sv_SE`: endast RST-markeringar, kodmålen och etablerade
  Blender-sammansättningar träffade; inga stavfel.
- `git diff --check`: godkänd.
- Gitleaks: inga hemligheter hittades.

Råexporten är orörd. Deltafilen är redo att ingå i en senare samlad, högst
100-strängars uppladdningsbatch för den generiska Manual-komponenten.
