# Batch 037: GRASS-parametrar och systemfel

Datum: 2026-11-10

Omfattning: sex kontextbevarade korrigeringskandidater, poster 268 till 273.
De omfattar GRASS-parametrar, numeriska lösare, positionsvalidering och fel
för kommandorad och miljövariabeln PATH.

Särskilt kontrollerat:

- Den falska vännen *inferior* avser positionsordning och översätts därför
  med `mindre än`, inte `sämre`.
- `solver`, `shell` och `binary` har fastställts som `lösare`,
  `kommandorad` och `binärfil` för denna GRASS-kontext.
- GRASS, PATH och båda platshållarna i binärfilfelet bevaras exakt.

Validering: `msgfmt --check`, `xmllint --noout`, 12 pytest-tester, Gitleaks
och `git diff --check` godkändes.

Status: lokalt granskat och publicerat i
[`yeager/swedish-tm` commit `0bd5bda`](https://github.com/yeager/swedish-tm/commit/0bd5bda).
Inte uppladdat till Transifex. Tidigare försök mot den dokumenterade
bulkändpunkten gav HTTP 500 utan observerad partiell tillämpning.
