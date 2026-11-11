# Batch 205: popupfönster

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 2 aktiva meddelanden i `UIPopupPane` har granskats. De är rubriker i
popupfönstrets detaljvisning, med och utan sidräknare.

## Resultat

Ingen textändring behövdes. `Detaljer` är rätt rubrik, markupen `<p><b>` är
bevarad och platshållarna `%1` och `%2` har korrekt svensk relation med `av`.

## Kontroller

- XPath-räkning: 2 aktiva meddelanden.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt granskat och arkiverat. Ingen katalogändring uppstod och därmed finns
inget nytt att skicka till PR #848 från denna batch.
