# Batch 030: diskar och aktivitetsöversikt

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

- Diskvarianter, diskettverktyg, ny virtuell disk och mediesökning: 39
  aktiva meddelanden.
- Aktivitetsöversikt, maskinförhandsvisning och maskinlogik: 45 aktiva
  meddelanden.

Samtliga 84 aktiva meddelanden granskades radvis.

## Ändringar

- Disketiketter och guideinstruktioner är naturligare och skiljer på disk,
  fil och fysisk lagring.
- Aktivitetsöversikten har konsekventa CPU- och RAM-etiketter samt begripliga
  mått för diskläsning och diskskrivning.
- `Molnmaskin` används konsekvent.

De två längre guidetexterna med avvikande källmarkup lämnades oförändrade
tillsammans med sin markup.

Ändringarna infördes i lokal commit `18da0a4`.

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
