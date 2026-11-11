# Batch 025: medier, gästprocesser och hjälp

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

- Medieväljare och mediestorleksverktyg: 44 aktiva meddelanden.
- Gästprocess- och sessionsvyer: 13 aktiva meddelanden.
- Hjälpbläddrare, hjälpknapp, startsida och välkomstvy: 57 aktiva meddelanden.

Samtliga 114 aktiva meddelanden granskades radvis. Den saknade
`UIWelcomePane` har 0 aktiva meddelanden.

## Ändringar

- Hårddiskfilens plats, diskstorlek och virtuell enhet har naturliga
  formuleringar.
- Process- och sessionsidentifierare använder konsekvent `ID`.
- Hjälpbläddraren använder `sidofält`, `verktygsfält` och idiomatiska
  sökkommandon.

Ändringarna infördes i lokal commit `4aab66c`.

## Kontroller

- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt verifierad och arkiverad. Ändringarna inväntar samlad push till PR #848
när den fullständiga radvisa granskningen är klar.
