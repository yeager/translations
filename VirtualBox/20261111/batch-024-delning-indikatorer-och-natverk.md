# Batch 024: delning, indikatorer och nätverk

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

- `UISharedFoldersEditor`: 15 aktiva meddelanden.
- `UISharedClipboardEditor`: 2 aktiva meddelanden.
- `UIDragAndDropEditor`: 2 aktiva meddelanden.
- Fem indikatorcontexts: 23 aktiva meddelanden.
- `UINetworkAttachmentEditor`, `UIMachineSettingsNetwork` och
  `UIMachineSettingsPortForwardingDlg`: 22 aktiva meddelanden.

Samtliga 64 aktiva meddelanden granskades radvis.

## Ändringar

- `Tillfälliga mappar` är konsekvent med VirtualBox terminologi.
- Ljudindikatorns in- och utgångar är tydligt namngivna.
- MAC-adressfelet, endast-värd-nätverk och portomdirigering använder
  idiomatisk och konsekvent svenska.

Ändringarna infördes i lokal commit `92c0bde`.

## Kontroller

- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Lokalt verifierad och arkiverad. Ändringarna inväntar fortsatt radvis
granskning innan den samlade uppdateringen av PR #848.
