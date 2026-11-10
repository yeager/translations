# Batch 025: Int8-datatyper i GDAL-verktyg

Datum: 2026-11-10

Omfattning: 17 separata Transifex-enheter med den identiska källsträngen
`Int8 data type requires GDAL version 3.7 or later`.

Varje enhet hämtades och kontrollerades med sin egen Transifex-kontext. De
omfattar klippning, interpolering, sammanslagning, närhet, rasterisering och
övriga GDAL-verktyg. Den svenska formen är konsekvent
`Int8-datatyp kräver GDAL version 3.7 eller senare`.

Validering:

- `msgfmt --check` och `xmllint --noout` godkändes.
- `pytest -q` godkändes: 12 tester.
- Gitleaks och `git diff --check` godkändes.

Status: lokalt granskat och publicerat i
[`yeager/swedish-tm` commit `cb86a96`](https://github.com/yeager/swedish-tm/commit/cb86a96).
Inte uppladdat till Transifex. Den tidigare verifierade bulk-API-vägen svarade
HTTP 500 och tillämpade inga ändringar.
