# Batch 111: processorfunktioner

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 3 aktiva meddelanden i `UIAccelerationFeaturesEditor` har granskats
radvis mot `UIAccelerationFeaturesEditor.cpp`.

## Resultat

Ingen textändring behövdes. `Hårdvaruvirtualisering` och `nästlad
sidindelning` är korrekta VirtualBox-termer. Beskrivningen behåller både
Intel VT-x och AMD-V samt rätt funktion som kryssrutan aktiverar.

## Kontroller

- XPath-räkning: 3 aktiva meddelanden i `UIAccelerationFeaturesEditor`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UIAccelerationFeaturesEditor`-granskningen är
lokalt slutförd. Ingen upstreamändring finns för denna komponent;
kataloggranskningen fortsätter.
