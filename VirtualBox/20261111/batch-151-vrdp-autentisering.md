# Batch 151: VRDP-autentisering

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 2 aktiva meddelanden i `UIVRDEAuthLibraryEditor` har granskats i
de globala inställningarna för VRDP-autentiseringsbiblioteket.

## Resultat

Verktygstipset använder nu `fjärrskrivbordsklienter (VRDP)` i stället för den
engelska frasen `Remote Display (VRDP)-klienter`.

Ändringen finns i lokal commit `5f1cf89` och är ännu inte pushad till PR:n.

## Kontroller

- XPath-räkning: 2 aktiva meddelanden.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt granskat och arkiverat. Upstream-inskick väntar tills den fullständiga
kataloggranskningen är klar.
