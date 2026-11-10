# Batch 036: autentisering och relationswidgetar

Datum: 2026-11-10

Omfattning: fyra kontextbevarade korrigeringskandidater, poster 264 till 267.
De omfattar två separata relationredigeringswidgetar, MapTiler HMAC
SHA256-signatur och en autentiseringstext med extern länk.

Särskilt kontrollerat:

- Två skilda Transifex-enheter har samma källtext men olika UI-kontexter.
- MapTiler, HMAC SHA256 och den externa URL:en bevaras exakt.
- HTML-strukturen i autentiseringstexten och sammansättningen
  `MapTiler-kontouppgifter`.

Validering: `msgfmt --check`, `xmllint --noout`, 12 pytest-tester, Gitleaks
och `git diff --check` godkändes.

Status: lokalt granskat och publicerat i
[`yeager/swedish-tm` commit `87c5118`](https://github.com/yeager/swedish-tm/commit/87c5118).
Inte uppladdat till Transifex. Tidigare försök mot den dokumenterade
bulkändpunkten gav HTTP 500 utan observerad partiell tillämpning.
