# Batch 035: CRS- och biblioteksetiketter

Datum: 2026-11-10

Omfattning: tre kontextbevarade korrigeringskandidater, poster 261 till 263.
De omfattar information om EPSG-registret, en äldre Proj-sträng och
GeographicLib-versionen i bearbetningsåterkoppling.

Särskilt kontrollerat:

- EPSG, Proj och GeographicLib är produkt- eller biblioteksnamn och behålls.
- Svensk sammansättning i `Proj-sträng` och `GeographicLib-version`.
- Versionsplatshållarna `%1.%2.%3` bevaras exakt.

Validering: `msgfmt --check`, `xmllint --noout`, 12 pytest-tester, Gitleaks
och `git diff --check` godkändes.

Status: lokalt granskat och publicerat i
[`yeager/swedish-tm` commit `64b13f6`](https://github.com/yeager/swedish-tm/commit/64b13f6).
Inte uppladdat till Transifex. Tidigare försök mot den dokumenterade
bulkändpunkten gav HTTP 500 utan observerad partiell tillämpning.
