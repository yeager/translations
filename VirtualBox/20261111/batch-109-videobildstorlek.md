# Batch 109: videobildstorlek

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 5 aktiva meddelanden i `UIRecordingVideoFrameSizeEditor` har
granskats radvis mot `UIRecordingVideoFrameSizeEditor.cpp`.

## Resultat

Ingen textändring behövdes. `Bildstorlek`, `användardefinierad`, upplösning,
bildbredd och bildhöjd har korrekt betydelse i inställningen för inspelad
video. Tangentbordsgenvägen är bevarad.

## Kontroller

- XPath-räkning: 5 aktiva meddelanden i `UIRecordingVideoFrameSizeEditor`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UIRecordingVideoFrameSizeEditor`-granskningen är
lokalt slutförd. Ingen upstreamändring finns för denna komponent;
kataloggranskningen fortsätter.
