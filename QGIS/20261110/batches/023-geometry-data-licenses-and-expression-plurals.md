# Batch 023: geometri, data, licens och uttrycksparametrar

Datum: 2026-11-10

Omfattning: nio kontextbevarade korrigeringskandidater i den aktuella
Transifex-resursen `qgis-application` för svenska.

| Område | Antal | Kontroll |
|---|---:|---|
| Befintlig databas- och geometri-UI | 2 | `existing` till `befintlig`; uttrycksbeskrivning för giltig geometri. |
| Data- och licenstext | 2 | Jämförelseattribut utan geometri samt Nominatim/ODbL. |
| CRS och intern UI-text | 2 | Destination CRS med bevarade avslutande blanksteg samt genvägskonflikt. |
| Uttrycksfunktioner med plural | 3 | `attribute`, `map_to_html_table` och `map_to_html_dl`. |

För pluralsträngarna används `har angetts` i båda svenska pluralformerna. Det
är idiomatiskt och antalneutralt, samtidigt som `%n` och funktionsnamnen
bevaras exakt.

Validering:

- `msgfmt --check` godkändes för den genererade QGIS-PO-filen.
- XML-validering med `xmllint --noout` godkändes för TMX-filen.
- `pytest -q` godkändes: 12 tester.
- `gitleaks detect --no-git --source reviewed/data/qgis.jsonl --redact`
  godkändes utan träffar.
- `git diff --check` godkändes.

Publicering: lokalt granskat och publicerat i
[`yeager/swedish-tm` commit `52f4dc2`](https://github.com/yeager/swedish-tm/commit/52f4dc2).
Inte uppladdat till Transifex. Den dokumenterade bulkändpunkten har tidigare
svarat HTTP 500 och inga delvisa ändringar har observerats vid återläsning.
