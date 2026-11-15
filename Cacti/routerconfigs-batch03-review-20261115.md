# Cacti RouterConfigs, svensk granskningsbatch 03

Datum: 2026-11-15  
Källa: `cacti/routerconfigs`, svensk Weblate-export efter batch 02  
Omfattning: 13 strängar markerade *behöver åtgärdas*

## Inriktning

Samtliga återstående fuzzy-strängar hade felaktiga maskinöversättningar eller orelaterad svensk text. De ersätts med kontextkorrekta UI-termer.

## Granskningsbeslut

- *Schedule Type*, *Days of Month*, *Dated Subdirectory* och *Context Lines* följer samma terminologi som batch 01 och 02.
- *Post-Login Prompts* är *Inloggningsfrågor*, vilket stämmer med beskrivningen av fråga/svar-par efter inloggning.
- *Disabled* är en status och översätts därför till *Inaktiverad*, inte uppmaningen *Inaktivera*.
- `%d line` saknar pluralform i källformatet. `%d rad` bevarar platshållaren och följer källans singularstruktur.
- Månadsnamnen skrivs med gemen enligt svensk standard.

## Kontroller

- `msgfmt --check`
- `l10n-lint`
- `svlang`
- `hunspell-sv`
- `git diff --check`
- `gitleaks detect --no-git --source … --redact`

Resultat och importstatus läggs till efter validering och uppladdning.
