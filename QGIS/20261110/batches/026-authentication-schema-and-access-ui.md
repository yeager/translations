# Batch 026: autentisering, scheman och åtkomst-UI

Datum: 2026-11-10

Omfattning: 25 kontextbevarade korrigeringskandidater, poster 202 till 226.
De omfattar befintlighetsfel, Cesium/Ion, CRS, autentisering, Planetary
Computer, GRASS och SQL/CREATE SCHEMA.

Särskilt kontrollerat:

- QGIS-termerna `utdata`, `målreferenskoordinatsystem` och `datakälla`.
- Bevarade produktnamn, SQL-nyckelord, URI, `authcfg` och platshållare.
- Att svenska felmeddelanden använder `finns` där källans *exists* avser
  förekomst, inte den engelsknära formen `existerar`.

Validering: `msgfmt --check`, `xmllint --noout`, 12 pytest-tester, Gitleaks
och `git diff --check` godkändes för respektive delbatch.

Status: lokalt granskat och publicerat i
[`yeager/swedish-tm` commit `2151a3d`](https://github.com/yeager/swedish-tm/commit/2151a3d).
Inte uppladdat till Transifex. Tidigare försök mot den dokumenterade
bulkändpunkten gav HTTP 500 utan observerad partiell tillämpning.
