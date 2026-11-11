# Batch 125: gästskärmsstorlek

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 6 aktiva meddelanden i `UIMaximumGuestScreenSizeEditor` har
granskats radvis mot inställningsreglaget för högsta gästskärmsstorlek.

## Resultat

Tre hjälptexter har gjorts naturligare och tydligare. De beskriver nu direkt
att gästen får använda den angivna högsta bredden och höjden, utan den
engelskspråkiga konstruktionen `vi vill`. Policyns etikett är också omformad
på svenska.

## Kontroller

- XPath-räkning: 6 aktiva meddelanden i `UIMaximumGuestScreenSizeEditor`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UIMaximumGuestScreenSizeEditor`-granskningen är
lokalt slutförd i commit `28cb328` och ännu inte pushad till PR #848.
