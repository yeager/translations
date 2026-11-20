# Foundation – slutförd svensk granskning: dlc_agriculture_buildings.json

Datum: 2026-11-20  
Omfattning: 132 av 132 aktuella strängar radgranskade via Crowdin API (offset 0–130; offset 140 verifierat tomt).

## Sparade ändringar

| Sträng-ID | Föreslagen svenska |
|---|---|
| 24042 | Ceremoniellt skördefyrfat |
| 24112 | Skördefestivalbod |
| 24198 | Lergrop för torp, inhägnad |
| 24200 | Lergrop för torp, öppen |
| 24206 | Torpstaketets grind |
| 24222 | Festligt fyrfat |
| 24246 | En plats där bybor kan konsumera {1} under skördefestivalen. Visas bara under evenemanget. |

Samtliga ändringar är sparade i Crowdin med API-svar 201 och arkiverade var för sig i delrapporterna 1–5.

## Validering

- `l10n-lint --language sv`: utan problem för varje förslagsbatch.
- `hunspell -d sv_SE`: inga stavningsanmärkningar för förslagen.
- Platshållaren `{1}` i den ändrade beskrivningen har bevarats.
