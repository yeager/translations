# Batch 019: fjärr- och ögonblicksbildsinställningar

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

- `UIVisoCreatorWidget`: 25 aktiva meddelanden.
- `UIVRDESettingsEditor`: 13 aktiva meddelanden.
- `UIMachineSettingsGeneral`: 8 aktiva meddelanden.
- `UISnapshotDetailsWidget`: 19 aktiva meddelanden.
- `UISnapshotPane`: 4 aktiva meddelanden.

Samtliga 69 aktiva meddelanden har granskats radvis. Den efterfrågade
`UIMachineSettingsEditor` och `UISnapshotDetailsEditor` saknas i den aktuella
katalogen; deras befintliga motsvarigheter granskades i stället. Säkra
korrigeringar infördes i lokal commit `5da8d7a`.

## Ändringar

- VISO-trädets underobjekt och hjälpvisaren har naturliga svenska namn.
- VRDE/RDP använder konsekvent virtuell maskin och tydligare anslutningstext.
- Chiffertyp för diskkryptering är idiomatiskt formulerad.
- Ögonblicksbildsredigeraren har korrekt bestämdhet och naturliga instruktioner.

## Kontroller

- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Ändringarna är verifierade lokalt och ännu inte pushade till PR #848 medan
den fullständiga radvisa granskningen fortsätter.
