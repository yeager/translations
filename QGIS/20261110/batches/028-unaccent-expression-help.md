# Batch 028: uttryckshjälp för unaccent()

Datum: 2026-11-10

Omfattning: två kontextbevarade korrigeringskandidater, poster 236 och 237.
De är den fullständiga hjälpen till uttrycksfunktionen `unaccent()` och den
efterföljande förklaringen av användningsfall.

Särskilt kontrollerat:

- HTML-taggar och liststruktur.
- PostgreSQL-funktionen `unaccent()`, Unicode-normalisering enligt NFC och
  termen `Unicode`.
- Samtliga diakritiska och andra Unicode-exempel, inklusive ligaturer,
  kyrilliska tecken och fullbreddstecken.

Validering: `msgfmt --check`, `xmllint --noout`, 12 pytest-tester, Gitleaks
och `git diff --check` godkändes.

Status: lokalt granskat och publicerat i
[`yeager/swedish-tm` commit `855a5a5`](https://github.com/yeager/swedish-tm/commit/855a5a5).
Inte uppladdat till Transifex. Tidigare försök mot den dokumenterade
bulkändpunkten gav HTTP 500 utan observerad partiell tillämpning.
