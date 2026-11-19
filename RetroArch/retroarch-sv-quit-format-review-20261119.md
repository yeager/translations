# RetroArch – avsluta programmet, svensk QA-rättning 2026-11-19

En befintlig svensk översättning i `msg_hash_us.json` har granskats via Crowdins QA-API. Förslaget är inte sparat eller skickat till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 5118546 | Quit RetroArch. Killing the program in any hard way (SIGKILL, etc.) will terminate RetroArch without saving the configuration in any case. On Unix-likes, SIGINT/SIGTERM allows a clean deinitialization which includes configuration save if enabled. | Avsluta RetroArch. Om programmet avslutas med tvång, till exempel med SIGKILL eller liknande, avslutas RetroArch utan att konfigurationen sparas. På Unix-liknande system medför SIGINT/SIGTERM en ordnad avslutning och att konfigurationen sparas om det är aktiverat. | Avsluta RetroArch. Om programmet avslutas med tvång (SIGKILL osv.) avslutas RetroArch utan att konfigurationen sparas. På Unix-liknande system medför SIGINT/SIGTERM en ordnad avinitiering som även sparar konfigurationen om det är aktiverat. |

## Kontroller

- Källparenteserna kring `SIGKILL` är återställda; Crowdins ursprungliga parentes-QA-träff är därmed löst.
- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` markerar Unix-signaler och avinitiering; Crowdins slutliga QA markerar endast avinitiering som teknisk term.
- Inga platshållare eller annan formatering har ändrats.
