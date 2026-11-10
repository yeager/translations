# Batch 033: installerare för Python-tillägg

Datum: 2026-11-10

Omfattning: tre kontextbevarade korrigeringskandidater, poster 254 till 256.
De omfattar två dialogtitlar och ett meddelande om ett föråldrat tillägg som
döljer en nyare medföljande version.

Särskilt kontrollerat:

- Den projektspecifika UI-termen `tillägg` används konsekvent; den tidigare
  rekommendationen `insticksmodul` har begränsats till teknisk dokumentation.
- Skillnaden mellan att dölja en version och att göra den synlig igen.
- Produktnamnen QGIS, Python och filformatet ZIP bevaras.

Validering: `msgfmt --check`, `xmllint --noout`, 12 pytest-tester, Gitleaks
och `git diff --check` godkändes.

Status: lokalt granskat och publicerat i
[`yeager/swedish-tm` commit `be66562`](https://github.com/yeager/swedish-tm/commit/be66562).
Inte uppladdat till Transifex. Tidigare försök mot den dokumenterade
bulkändpunkten gav HTTP 500 utan observerad partiell tillämpning.
