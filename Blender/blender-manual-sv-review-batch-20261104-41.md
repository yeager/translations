# Blender Manual: svensk granskningsbatch 41

Datum: 4 november 2026

Källa: `exports/2026-11-04/blender-manual-manual-sv.po`.

## Omfattning

Sju poster i `editors/preferences/asset_libraries.rst` om hur ett tillägg
hittas för en resurs samt det inbyggda grundresursbiblioteket. Kontexten
kontrollerades mot den svenska Blender-katalogens faktiska UI-beteckningar:

- `View Extension...` → *Visa tillägg…*
- `Get Extensions` → *Skaffa tillägg*
- `Essentials` → *Grundresurser*
- `Include Online Essentials` → *Inkludera grundresurser online*
- `Online Access` → *Nätåtkomst*

I den längre, förklarande brödtexten används *resursbibliotek*, i linje med
den närliggande UI-kontexten. RST-roller, RST-mål och produktnamnet Blender
är bevarade. `bpy.types.PreferencesSystem.use_online_access` är ett
programmeringsidentifierare och ska därför inte översättas.

En förnyad kontroll mot UI-exporten den 5 november bekräftar både den
fristående etiketten *Grundresurser* och rubrikformen
*Grundresursbiblioteket*. De betecknar olika syntaktiska sammanhang och ska
inte mekaniskt ersätta varandra.

## Kontroller

- `msgfmt --check --statistics`: 7 översatta meddelanden och godkänd syntax.
- Radvis jämförelse av `(msgctxt, msgid)` mot råexporten: 7/7 träffar.
- `l10n-lint --language sv`: inga träffar. Referenskatalogkontrollen används
  inte för denna avsiktligt partiella deltafil, eftersom den annars felaktigt
  rapporterar samtliga poster utanför batchen som saknade.
- `svlang skrivregler --enable-interpunktion` och `svlang svengelska`: inga
  träffar i de svenska måltexterna.
- Hunspell `sv_SE`: endast RST-markeringar och den bevarade
  `bpy.types`-identifieraren träffade; inga stavfel.
- `git diff --check`: godkänd.
- Gitleaks: inga hemligheter hittades.

Råexporten är orörd. Deltafilen är arkiverad och väntar på en samlad
uppladdningsbatch för den generiska Manual-komponenten.
