# Batch 031: projektnamn och vågformsuttryck

Datum: 2026-11-10

Omfattning: fyra kontextbevarade korrigeringskandidater, poster 247 till 250.
De omfattar en konfliktdialog för projektets rotnamn och tre parallella
uttryckshjälptexter om fyrkantsvågor, triangulära vågor och vågor.

Särskilt kontrollerat:

- `projektets rotnamn` används konsekvent i två sammanhörande
  valideringsmeddelanden.
- Den fackspråkliga termen `våglängd` och den svenska formen `maximal
  våglängd`.
- Kodnära värden och parameteretiketter, `strict` och `true`, bevaras exakt.

Validering: `msgfmt --check`, `xmllint --noout`, 12 pytest-tester, Gitleaks
och `git diff --check` godkändes.

Status: lokalt granskat och publicerat i
[`yeager/swedish-tm` commit `1e41f23`](https://github.com/yeager/swedish-tm/commit/1e41f23).
Inte uppladdat till Transifex. Tidigare försök mot den dokumenterade
bulkändpunkten gav HTTP 500 utan observerad partiell tillämpning.
