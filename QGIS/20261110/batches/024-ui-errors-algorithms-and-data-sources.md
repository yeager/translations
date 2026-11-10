# Batch 024: UI-fel, algoritmer och datakällor

Datum: 2026-11-10

Omfattning: 30 kontextbevarade korrigeringskandidater, poster 153 till 182,
i den aktuella svenska Transifex-resursen `qgis-application`.

| Område | Antal | Exempel på kontroller |
|---|---:|---|
| Datatermer, licenser och hjälptext | 5 | Punktmoln, Nominatim och Python-konsol med HTML-markup. |
| Projekt, WMS och felmeddelanden | 9 | GNU GPL, REPACK, `.qgd`, temporal inställning och GetCapabilities. |
| Geobearbetning och datafel | 6 | Hargreaves, överlagringslager, rankningsvärden, OGR och fältnamn. |
| Befintlighets- och anslutningsfel | 10 | Befintliga datakällor, anslutningar, utbredningsbuffert och punktmoln. |

Kontroller:

- Källtext och UI-kontext kontrollerades rad för rad i råexporten.
- API-sökning gav exakt Transifex-enhet före varje kandidats registrering.
- `msgfmt --check` och `xmllint --noout` godkändes för genererade TM-filer.
- `pytest -q` godkändes: 12 tester.
- Gitleaks och `git diff --check` godkändes.

Status: lokalt granskat och publicerat i
[`yeager/swedish-tm` commit `4833104`](https://github.com/yeager/swedish-tm/commit/4833104).
Inte uppladdat till Transifex. Den dokumenterade bulkändpunkten har tidigare
svarat HTTP 500 och återläsning har inte visat någon delvis tillämpad ändring.
