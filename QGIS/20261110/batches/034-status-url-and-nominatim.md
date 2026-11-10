# Batch 034: status, URL och Nominatim-attribution

Datum: 2026-11-10

Omfattning: fyra kontextbevarade korrigeringskandidater, poster 257 till 260.
De omfattar en GRASS-statusetikett, URL-inmatning för plugin-katalog,
jämförelsevarning och Nominatim-geokodarens licensinformation.

Särskilt kontrollerat:

- Vinkelparenteser och `%1` i statusetiketten.
- URL-prefixen `http://` och `file:///`.
- OpenStreetMap Foundation, ODbL och länken till Nominatim.
- Att `delning på lika villkor` används endast som licensvillkor.

Validering: `msgfmt --check`, `xmllint --noout`, 12 pytest-tester, Gitleaks
och `git diff --check` godkändes.

Status: lokalt granskat och publicerat i
[`yeager/swedish-tm` commit `5e39498`](https://github.com/yeager/swedish-tm/commit/5e39498).
Inte uppladdat till Transifex. Tidigare försök mot den dokumenterade
bulkändpunkten gav HTTP 500 utan observerad partiell tillämpning.
