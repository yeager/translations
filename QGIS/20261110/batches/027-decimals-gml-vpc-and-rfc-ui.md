# Batch 027: decimaler, GML, VPC och RFC-gränssnitt

Datum: 2026-11-10

Omfattning: nio kontextbevarade korrigeringskandidater, poster 227 till 235.
De omfattar decimalavskiljare, felmeddelanden för GML och datamängder,
höjdintervall, GPSBabel, virtuella punktmoln samt hjälptips för RFC 7946 och
RFC 8142.

Särskilt kontrollerat:

- QGIS-termerna `datamängd`, `utbredning`, `utdata` och
  `decimalavskiljare`.
- Bevarade standard- och formatnamn: GML, GPSBabel, GPX, VPC, COPC, LAZ/LAS,
  GeoJSON, RFC 7946, RFC 8142 och RS=0x1E.
- Radbrytning och osynliga blanksteg i RFC 8142-källan. Det avslutande
  blanksteget före radbrytningen normaliserades endast i TM-posten för att
  den genererade TMX-filen ska vara fri från efterföljande blanksteg.

Validering: `msgfmt --check`, `xmllint --noout`, 12 pytest-tester, Gitleaks
och `git diff --check` godkändes.

Status: lokalt granskat och publicerat i
[`yeager/swedish-tm` commit `1beb24c`](https://github.com/yeager/swedish-tm/commit/1beb24c).
Inte uppladdat till Transifex. Tidigare försök mot den dokumenterade
bulkändpunkten gav HTTP 500 utan observerad partiell tillämpning.
