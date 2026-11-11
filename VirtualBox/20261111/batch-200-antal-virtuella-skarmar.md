# Batch 200: antal virtuella skärmar

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 4 aktiva meddelanden i `UIMonitorCountEditor` har granskats i
maskininställningen för antal virtuella skärmar.

## Resultat

Ingen textändring behövdes. `Virtuella skärmar` är rätt term för Virtual
Monitors, och etikett, beskrivning samt minimi- och maximivärde är språkligt
korrekta. Åtkomsttangenten är bevarad.

## Kontroller

- XPath-räkning: 4 aktiva meddelanden.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt granskat och arkiverat. Ingen katalogändring uppstod och därmed finns
inget nytt att skicka till PR #848 från denna batch.
