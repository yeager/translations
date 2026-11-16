# Home Assistant Core: MeteoAlarm

Datum: 16 november 2026

Fjorton MeteoAlarm-strängar med engelsk källtext har granskats, sparats via
Lokalise API och lästs tillbaka. YAML, `configuration.yaml`, `EMMA_ID` samt
platshållarna `{province}` och `{country}` är bevarade.

Efter återläsningen återstår 33 markerade Core-poster. De har tom källtext
eller tomma pluralstrukturer och är inte översättningsbara. Kontroller:
JSON, svlang, Hunspell-sv, diffkontroll och Gitleaks. `msgfmt` är inte
tillämpligt på JSON-resursen.
