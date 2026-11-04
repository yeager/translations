# Blender Manual: svensk granskningsbatch 37

Datum: 4 november 2026

Källa: `exports/2026-11-04/blender-manual-manual-sv.po`.

## Omfattning

Nio grundposter för Resursbibliotek i Blender-inställningarna har
granskats: lokala och nätbaserade bibliotek, kataloger, URL-fält och
resursväljare.

Den oberoende kandidatgranskningen använde först *tillgångsbibliotek*, men
huvudgranskningen korrigerade detta till UI-katalogens etablerade
`Asset Libraries` → *Resursbibliotek*. Samma kontroll bekräftar `Asset
Browser` → *Resursbläddrare*. RST-målen `editors-asset_browser` och
`ui-list-view` är oförändrade.

## Kontroller

- `msgfmt --check --statistics`: 9 översatta meddelanden, godkänd syntax.
- Radvis jämförelse av `(msgctxt, msgid)` mot råexporten: 9/9 träffar.
- Hunspell `sv_SE`: endast PO-huvudets fält och bevarade RST-identifierare.
- `git diff --check`: godkänd.
- Gitleaks: inga hemligheter hittades.

Råexporten är orörd. Deltafilen arkiveras för en senare samlad uppladdning.
