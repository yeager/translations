# Batch 030: validering, filnamn och Unicode

Datum: 2026-11-10

Omfattning: fem kontextbevarade korrigeringskandidater, poster 242 till 246.
De omfattar en filterkärna, oändlig filterrektangel, Unicode-kod,
utdatafilnamn och projektion i en lagerdialog.

Särskilt kontrollerat:

- Att `projektion` ska behållas eftersom källan uttryckligen använder
  *projection*, inte *CRS*.
- Termen `Unicode-kod` och versaliseringen `Unicode`.
- Att den tekniska teckenregeln och alla valalternativ bevaras utan
  meningsförändring.

Validering: `msgfmt --check`, `xmllint --noout`, 12 pytest-tester, Gitleaks
och `git diff --check` godkändes.

Status: lokalt granskat och publicerat i
[`yeager/swedish-tm` commit `717f08b`](https://github.com/yeager/swedish-tm/commit/717f08b).
Inte uppladdat till Transifex. Tidigare försök mot den dokumenterade
bulkändpunkten gav HTTP 500 utan observerad partiell tillämpning.
