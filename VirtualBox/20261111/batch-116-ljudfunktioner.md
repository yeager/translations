# Batch 116: ljudfunktioner

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 5 aktiva meddelanden i `UIAudioFeaturesEditor` har granskats radvis,
mot den C++-kod som bygger redigeraren.

## Resultat

Ingen textändring behövdes. Översättningen skiljer korrekt på ljudutgång och
ljudingång, använder `värden` och `gästen` i rätt riktning och bevarar
tangentbordsgenvägarna.

## Kontroller

- XPath-räkning: 5 aktiva meddelanden i `UIAudioFeaturesEditor`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UIAudioFeaturesEditor`-granskningen är lokalt
slutförd. Ingen upstreamändring finns för denna komponent; kataloggranskningen
fortsätter.
