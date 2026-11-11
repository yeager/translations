# Batch 022: globala, system- och skärminställningar

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

- `UIGlobalSettingsInput`: 2 aktiva meddelanden.
- `UIAdvancedSettingsDialogGlobal`: 9 aktiva meddelanden.
- `UIMachineSettingsDisplay`: 11 aktiva meddelanden.
- `UIMachineSettingsSystem`: 14 aktiva meddelanden.
- `UIMachineSettingsGeneral`: 8 aktiva meddelanden.
- `UIAudioSettingsEditor`: 2 aktiva meddelanden utan ändringsbehov.

Samtliga 46 aktiva meddelanden granskades radvis. Den saknade contexten
`UIDisplaySettingsEditor` ersattes av den faktiska `UIMachineSettingsDisplay`.

## Ändringar

- Globala inställningar använder `kortkommandon`,
  `värdtangentkombination` och tydlig navigeringstext.
- VRDE-serverport, helskärmsläge och operativsystemtyp har naturliga och
  tekniskt exakta formuleringar.
- Systemvarningarna för RAM och I/O APIC är tydligare utan att ändra
  tekniska benämningar.

Ändringarna infördes i lokal commit `6d88175`.

## Kontroller

- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt verifierad och arkiverad. Ändringarna är ännu inte pushade till PR
#848 eftersom den kompletta radvisa granskningen fortsätter.
