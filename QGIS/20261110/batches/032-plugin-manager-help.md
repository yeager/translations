# Batch 032: pluginhanterarens hjälptexter

Datum: 2026-11-10

Omfattning: tre kontextbevarade korrigeringskandidater, poster 251 till 253.
De omfattar hjälpen för ogiltiga, experimentella och föråldrade tillägg.

Särskilt kontrollerat:

- Alla HTML-taggar och den exakta externa länken
  `https://plugins.qgis.org`.
- Betydelseskillnaden mellan ogiltigt, trasigt, inkompatibelt,
  experimentellt och föråldrat.
- Att varningarna behåller saklig ton och instruktionernas innebörd.

Validering: `msgfmt --check`, `xmllint --noout`, 12 pytest-tester, Gitleaks
och `git diff --check` godkändes.

Status: lokalt granskat och publicerat i
[`yeager/swedish-tm` commit `bc615c1`](https://github.com/yeager/swedish-tm/commit/bc615c1).
Inte uppladdat till Transifex. Tidigare försök mot den dokumenterade
bulkändpunkten gav HTTP 500 utan observerad partiell tillämpning.
