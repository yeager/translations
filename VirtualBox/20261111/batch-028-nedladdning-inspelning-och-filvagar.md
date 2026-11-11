# Batch 028: nedladdning, inspelning och filvägar

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

- Nedladdare för tilläggspaket, Gästtillägg och manual: 7 aktiva meddelanden.
- Inspelningsinställningar: 31 aktiva meddelanden utan ändringsbehov.
- Fil- och standardsökvägsfält: 13 aktiva meddelanden.

Samtliga 51 aktiva meddelanden granskades radvis.

## Ändringar

- `VirtualBox-tilläggspaket` skrivs med korrekt bindestreck.
- Fil- och standardsökvägshjälp har naturlig bestämdhet och tydligare
  händelseföljd.

Ändringarna infördes i lokal commit `73a9742`.

## Kontroller

- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt verifierad och arkiverad. Ändringarna inväntar fullständig radvis
granskning före samlad push till PR #848.
