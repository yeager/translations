# Batch 120: diskkrypteringslösenord

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 5 aktiva meddelanden i `UIAddDiskEncryptionPasswordDialog` har
granskats radvis mot dialogen som efterfrågar lösenord för krypterade medier.

## Resultat

Ingen textändring behövdes. Singular och plural för hårddiskar är korrekta,
`krypteringslösenord` fungerar för båda svenska numerusformerna och
HTML-markering samt `%n` och `%1` är bevarade.

## Kontroller

- XPath-räkning: 5 aktiva meddelanden i `UIAddDiskEncryptionPasswordDialog`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UIAddDiskEncryptionPasswordDialog`-granskningen är
lokalt slutförd. Ingen ytterligare upstreamändring finns för denna komponent;
kataloggranskningen fortsätter.
