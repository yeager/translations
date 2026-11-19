# RetroArch – säkerhetskopiering av kärna, svensk QA-rättning 2026-11-19

En befintlig svensk översättning i `msg_hash_us.json` har granskats via Crowdins QA-API. Förslaget är inte sparat eller skickat till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 6221901 | A backup or restore of this core is already running: ␠ | En säkerhetskopiering eller återställning av denna kärna pågår redan: | En säkerhetskopiering eller återställning av denna kärna pågår redan: ␠ |

Tecknet `␠` i tabellen representerar ett avslutande, verkligt blanksteg. Det ingår i själva förslaget men visas explicit här för granskning.

## Kontroller

- Källans avslutande blanksteg efter kolon är återställt; Crowdins ursprungliga QA-träff är därmed löst.
- `l10n-lint --language sv` passerade utan anmärkningar.
- Crowdins QA-validering returnerade inga träffar.
- Ingen annan text eller formatering ändrades.
