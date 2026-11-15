# Home Assistant Core, Lokalise, svenska

Datum: 2026-11-15

De senaste sparade batcherna är `core-sofar-grid-batch-101.json` och
`core-sofar-thermal-input-batch-102.json` och
`core-sofar-input-inverter-batch-103.json`. De omfattar 45 fel- och
skyddsetiketter för Sofar-växelriktarens nätövervakning, kylflänsar och
ingångssäkringar.

Lokalise API-sparningen har återlästs: samtliga 45 strängar är markerade som
översatta och inte overifierade. Arbetet är arkiverat i detta repo. Det finns
ingen verifierad upstream-granskning, merge eller publicerad Home Assistant-
release kopplad till batchen.

`msgfmt` är inte tillämpligt på Lokalise-JSON. JSON-, l10n-lint-,
svlang-, Hunspell-, diff- och Gitleaks-kontroller dokumenteras tillsammans med
batchens arkivering.
