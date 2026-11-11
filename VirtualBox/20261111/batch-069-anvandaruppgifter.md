# Batch 069: användaruppgifter

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 14 aktiva meddelanden i `UIUserNamePasswordEditor` har granskats
radvis.

## Ändringar

Förkortade och förtydligade felmeddelandet för ett tomt användarnamn. Övriga
lösenords-, tecken- och längdbegränsningar är giltiga i sin dialogkontext.
Ändringen finns i lokal commit `1525891`.

## Kontroller

- XPath-räkning: 14 aktiva meddelanden i `UIUserNamePasswordEditor`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UIUserNamePasswordEditor`-granskningen är lokalt
slutförd. Ändringarna är ännu inte pushade till PR #848, eftersom
kataloggranskningen fortsätter.
