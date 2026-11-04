# Blender Manual: svensk granskningsbatch 54

Datum: 4 november 2026

Källa: `exports/2026-11-04/blender-manual-manual-sv.po` och den officiella
Blender 5.3-manualens avsnitt om tilläggens bygg-, validerings- och
publiceringsflöde.

## Omfattning

Fem rubriker och en tagg. *Building* är avsnittsnamnet för processen och
återges som **Bygga**. De närliggande korta kommandoradsrubrikerna är
uppmaningar och återges därför **Bygg**, **Validera** och **Publicera**.
Taggen *Model* är innehållskategorin **Modell**, inte användargränssnittets
*läge*.

## Kontroller

- `msgfmt --check --statistics`: 5 översatta meddelanden och godkänd syntax.
- Radvis jämförelse av `(msgctxt, msgid)` mot råexporten: 5/5 träffar.
- `l10n-lint --language sv`, svlang, Hunspell, `git diff --check` och
  Gitleaks körs före arkivering.

Råexporten är orörd. Deltafilen är lokalt validerad men inte uppladdad till
Blender Translate.
