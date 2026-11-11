# Batch 212: statusradsindikatorer och validering

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

De sista 4 aktiva meddelandena i `UISessionStateStatusBarIndicator`,
`UISessionTextStatusBarIndicator` och `UISettingsPageValidator` har
granskats radvis. De används för tillgänglighetsnamn på statusradsindikatorer
respektive rubriker i inställningsvalideringens felrapport.

## Resultat

Båda statusradsindikatorerna har skrivits om från den svårtolkade dynamiska
sammansättningen `%1-statusradsindikator` till `%1-indikator på statusraden`.
Valideringsrubrikerna har fått svensk ordföljd: `Sidan <b>%1</b>:`. Markup och
platshållare är bevarade.

## Kontroller

- XPath-räkning: 4 aktiva meddelanden.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt granskat och arkiverat. Katalogändringarna är verifierade lokalt och
avvaktar den samlade uppdateringen av PR #848 efter fullständig granskning.
