# RetroArch – redigeringsläge för headsetskärmar, svensk QA-rättning 2026-11-19

En befintlig svensk översättning i `msg_hash_us.json` har förbättrats som utkast efter API-baserad QA-granskning. Förslaget är inte sparat eller skickat till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 6220935 | What the content does while Edit Screens moves the headset's screens: keeps running, or pauses until editing ends. Edit mode resumes only what it paused. | Vad innehållet gör medan Redigera skärmar flyttar VR-headsetets skärmar: fortsätter köra eller pausas tills redigeringen avslutas. Redigeringsläget återupptar bara det som det har pausat. | Vad innehållet gör medan Redigera skärmar flyttar VR-headsetets skärmar: fortsätter att köras eller pausas tills redigeringen avslutas. Redigeringsläget återupptar bara det som det själv pausade. |

## Kontroller

- `l10n-lint --language sv` passerade utan anmärkningar.
- Hunspell och Crowdins QA markerar endast `VR-headsetets`, en korrekt teknisk sammansättning.
- QA:s versalvarning beror på skillnaden mellan engelsk rubrikstil och svensk meningsstil.
- Inga platshållare eller annan teknisk formatering finns i strängen.
