# RetroArch – varning för svarta bildrutor, svensk QA-rättning 2026-11-19

En befintlig svensk översättning i `msg_hash_us.json` har granskats via Crowdins QA-API. Förslaget är inte sparat eller skickat till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 5757604 | WARNING: Rapid flickering may cause image persistence on some displays. Use at your own risk // Insert black frame(s) between frames. Can greatly reduce motion blur by emulating CRT scan out, but at cost of brightness. | VARNING: Snabbt flimmer kan orsaka kvarstående bild på vissa skärmar. Använd på egen risk // Infoga svarta ramar mellan bildrutorna. Kan kraftigt minska rörelseoskärpa genom att emulera CRT-scanning, men på bekostnad av ljusstyrkan. | VARNING: Snabbt flimmer kan orsaka kvarstående bild på vissa skärmar. Använd på egen risk // Infoga svarta bildrutor (en eller flera) mellan bildrutorna. Kan kraftigt minska rörelseoskärpa genom att emulera CRT-scanning, men på bekostnad av ljusstyrkan. |

## Kontroller

- Källans parentesmarkering för `frame(s)` är återställd som ”bildrutor (en eller flera)”; Crowdins ursprungliga parentes-QA-träff är därmed löst.
- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` och Crowdins slutliga QA markerar endast CRT-scanning, en teknisk term.
- Avgränsaren `//` och varningsformatet är bevarade.
