# Batch 042: appliancemetadata

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

Appliance-redigerarens 32 aktiva meddelanden har granskats radvis.

## Ändringar

Produktens och leverantörens URL använder idiomatisk svensk genitiv.
Terminologin för gästoperativsystem, styrkort, diskavbildning, IDE, SATA,
SCSI, SAS, VirtioSCSI och NVMe är bevarad. Ändringarna finns i lokal commit
`a61aa5a`.

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
