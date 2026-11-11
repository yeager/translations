# Batch 026: start och säkerhet

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

- Krypteringslösenord, diskkryptering, TPM och startfel: 27 aktiva meddelanden.
- Startordning, kretsuppsättning, moderkort och processor: 20 aktiva
  meddelanden.

Samtliga 47 aktiva meddelanden granskades radvis.

## Ändringar

- Krypteringsvarningens pluralformer är grammatiskt korrekta.
- TPM-emulering har naturlig referens till den virtuella maskinen.
- Uppstartsordning, RTC, PAE och nästlad hårdvaruvirtualisering har
  tekniskt exakta formuleringar.

Ändringarna infördes i lokal commit `b9a465d`.

## Kontroller

- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt verifierad och arkiverad. Ändringarna väntar på fortsatt radvis
granskning före samlad push till PR #848.
