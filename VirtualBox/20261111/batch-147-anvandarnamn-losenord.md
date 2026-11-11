# Batch 147: användarnamn och lösenord

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 14 aktiva meddelanden i `UIUserNamePasswordEditor` har granskats
radvis i inmatningsdialogen för gästoperativsystemets användarkonto.

## Resultat

Det otydliga `Ogiltigt lösenordspar` har ersatts med det konkreta
felmeddelandet `Lösenorden stämmer inte överens`.

Ändringen finns i lokal commit `078d202` och är ännu inte pushad till PR:n.

## Kontroller

- XPath-räkning: 14 aktiva meddelanden.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt granskat och arkiverat. Upstream-inskick väntar tills den fullständiga
kataloggranskningen är klar.
