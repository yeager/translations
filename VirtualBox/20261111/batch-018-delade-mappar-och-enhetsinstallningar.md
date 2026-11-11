# Batch 018: delade mappar och enhetsinställningar

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

- `UISharedFolderDetailsEditor`: 18 aktiva meddelanden.
- `UINameAndSystemEditor`: 14 aktiva meddelanden.
- `UISerialSettingsEditor`: 14 aktiva meddelanden.
- `UINetworkFeaturesEditor`: 13 aktiva meddelanden.

Samtliga 59 aktiva meddelanden granskades radvis. Säkra korrigeringar
infördes i lokal commit `e652cc0`.

## Ändringar

- Delade mappar och maskinnamn har naturlig bestämdhet och korrekt
  systemterminologi.
- Seriell port används konsekvent och rör respektive uttag skrivs ut i
  gränssnittet.
- Portomdirigering är den enhetliga nätverkstermen.
- Nätverkskabelns status och förklaringar är idiomatiska och tydliga.

## Kontroller

- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt verifierad och arkiverad. Innehållet väntar tillsammans med övriga
lokala batcher på att den fullständiga radvisa granskningen ska slutföras
innan PR #848 uppdateras.
