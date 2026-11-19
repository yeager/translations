# RetroArch – modellstyrka och lokal struktur, svensk QA-rättning 2026-11-19

Två befintliga svenska översättningar i `msg_hash_us.json` har granskats via Crowdins QA-API. Förslagen är inte sparade eller skickade till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 6218627 | The model's overall strength, in percent. | Intensitet | Modellens övergripande styrka, i procent. |
| 6218631 | How strongly the model works fine detail and surface structure, in percent. | Lokal struktur | Hur starkt modellen arbetar med fina detaljer och ytstruktur, i procent. |

## Kontroller

- De befintliga måltexterna var förkortade etiketter som tappade källornas beskrivande innebörd och slutpunkt. Båda fullständiga betydelserna är återställda.
- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` passerade utan anmärkningar.
- Crowdins QA-validering returnerade inga träffar.
