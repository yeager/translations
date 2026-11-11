# Batch 179: åtgärder för detaljvärdet

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 2 aktiva meddelanden i `UIDetailsElement` har granskats i
snabbmenyn för redigerbara värden på informationspanelen.

## Resultat

Båda åtgärderna har fått bestämd form: `Kopiera värdet` och `Redigera
värdet`. Menyåtgärderna verkar på det aktuella enskilda värdet, vilket gör
bestämd form både idiomatisk och tydlig. Platshållaren `%1` har bevarats.

## Kontroller

- XPath-räkning: 2 aktiva meddelanden.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt granskat och arkiverat. Katalogändringen är verifierad lokalt och
avvaktar den samlade uppdateringen av PR #848 efter fullständig granskning.
