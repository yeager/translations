# RetroArch – kärntaggar i spellistor, svensk QA-rättning 2026-11-19

En befintlig svensk översättning i `msg_hash_us.json` har granskats via Crowdins QA-API. Förslaget är inte sparat eller skickat till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 6140021 | Specify when to tag playlist entries with the currently associated core (if any). This setting is ignored when playlist sublabels are enabled. | Ange när spellisteposter ska märkas med den för närvarande kopplade kärnan, om någon. Den här inställningen ignoreras när spellisteunderrubriker är aktiverade. | Ange när spellisteposter ska märkas med den för närvarande kopplade kärnan (om någon). Den här inställningen ignoreras när spellisteunderrubriker är aktiverade. |

## Kontroller

- Källans parenteser runt `if any` är återställda som ”(om någon)”; Crowdins ursprungliga parentes-QA-träff är därmed löst.
- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` passerade utan anmärkningar.
- Crowdins QA-validering returnerade inga träffar.
