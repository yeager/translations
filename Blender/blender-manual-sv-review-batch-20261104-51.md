# Blender Manual: svensk granskningsbatch 51

Datum: 4 november 2026

Källa: `exports/2026-11-04/blender-manual-manual-sv.po`.

## Kontext och omfattning

Tjugofem poster i referensmanualen för Blenders kommandorad. Den här batchen
rättar i första hand felaktigt återanvända flaggor: exempelvis
`--no-window-focus` i stället för `--no-window-frame`, gamla
`--cycles-device` i stället för `--gpu-device`, samt fel GPU-felsökningsflaggor.
Kommandon, kortflaggor, miljövariabler, platshållare och filnamn är
maskinläsbara värden och ska därför vara identiska med källtexten.

De svenska beskrivningarna har lästs mot respektive kommandoradsalternativ i
den aktuella Blender-manualen. *Loggningsnivå*, *miljövariabel*, *datablock*
och *åtgärd* följer den fastställda terminologin.

## Kontroller

- `msgfmt --check --statistics`: 25 översatta meddelanden och godkänd syntax.
- Radvis jämförelse av `(msgctxt, msgid)` mot råexporten: 25/25 träffar.
- `l10n-lint --language sv`: 0 fel och varningar. Informationsnotiser om
  identisk mål- och källtext gäller enbart kommandon och miljövariabler.
- `svlang skrivregler --enable-interpunktion`: inga skrivregelfel.
  `svlang svengelska` noterar bara kodliteralens `startup` i
  `startup.blend`; filnamnet får inte översättas.
- Hunspell `sv_SE` noterar enbart kommandon, formatnamn, miljövariabler,
  platshållare och produktnamn. De är medvetet oförändrade.
- Identiska mål för flaggor och miljövariabler är medvetna: de är kod- och
  kommandovärden, inte oöversatta användartexter.
- `git diff --check` och Gitleaks: godkända, utan hemligheter.

Råexporten är orörd. Deltafilen är en lokal kandidat och är inte uppladdad
till Blender Translate.
