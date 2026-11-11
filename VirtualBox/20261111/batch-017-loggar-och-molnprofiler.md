# Batch 017: loggar och molnprofiler

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

- `UIVMLogViewerWidget`: 47 aktiva meddelanden.
- `UICloudProfileManager`: 29 aktiva meddelanden.

Alla aktiva meddelanden har lästs radvis med källtext och sammanhang.
De säkra korrigeringarna infördes i lokal commit `172a7ce`.

## Ändringar

- Loggvisarens filtertexter är idiomatiska och konsekventa.
- HTML-markeringen för sökvägen till loggmappen är nu korrekt avgränsad.
- `Bädda in` används konsekvent i loggvisaren.
- Molnprofilhanteraren har korrekt verktygsnamn, naturlig bestämdhet och
  tydligare information om den aktuella profilen.

## Kontroller

- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Ändringarna är verifierade lokalt och arkiveras här. De är ännu inte pushade
till PR #848, eftersom den fullständiga radvisa granskningen fortsatt pågår.
