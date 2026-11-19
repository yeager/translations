# RetroArch – redigering av VR-headsetets skärmar, svensk granskningsbatch 2026-11-19

Två befintliga svenska översättningar i `msg_hash_us.json` har förbättrats som utkast efter API-baserad QA-granskning. Förslagen är inte sparade eller skickade till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 6220907 | Starts or stops moving the headset's screens and menu with its controllers. | Startar eller stoppar flytt av VR-headsetets skärmar och meny med dess handkontroller. | Startar eller stoppar förflyttning av VR-headsetets skärmar och meny med handkontrollerna. |
| 6220909 | Editing headset screens: grip grabs, the stick moves and resizes, the trigger tilts it with your hand, the other hand's stick turns and tilts it, the main button resets. | Redigerar VR-headsetets skärmar: greppknappen tar tag, styrspaken flyttar och ändrar storlek, avtryckaren vinklar skärmen med handen, den andra handens styrspak vrider och vinklar den, huvudknappen återställer. | Vid redigering av VR-headsetets skärmar: greppknappen tar tag, styrspaken flyttar och ändrar storlek, avtryckaren vinklar skärmen med handen, den andra handens styrspak vrider och vinklar den, huvudknappen återställer. |

## Kontroller

- `l10n-lint --language sv` passerade utan anmärkningar.
- Hunspell och Crowdins QA markerar endast `VR-headsetets`, en korrekt teknisk sammansättning.
- QA:s versalvarningar beror på skillnaden mellan engelsk rubrikstil och svensk meningsstil.
- Inga platshållare eller annan teknisk formatering finns i strängarna.
