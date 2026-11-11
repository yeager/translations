# Batch 122: bildfrekvens

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Samtliga 6 aktiva meddelanden i `UIRecordingVideoFrameRateEditor` har
granskats radvis mot reglagekoden för videoinspelning.

## Resultat

Tre strängar har förtydligats: `Additional frames` är nu `Ytterligare
bildrutor`, och den korta enheten för fps är konsekvent `bildrutor/s`.
Tangentbordsgenväg och `%1` är bevarade.

## Kontroller

- XPath-räkning: 6 aktiva meddelanden i `UIRecordingVideoFrameRateEditor`.
- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Den fullständiga aktuella `UIRecordingVideoFrameRateEditor`-granskningen är
lokalt slutförd i commit `771bbd8` och ännu inte pushad till PR #848.
