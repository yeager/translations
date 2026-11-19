# RetroArch – handkontroller och OpenXR, svensk granskningsbatch 2026-11-19

Fem oöversatta svenska strängar i RetroArchs huvudfil `msg_hash_us.json` har granskats från aktuella Crowdin API-svar. Förslagen är inte sparade eller skickade till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 6237507 | Pressed | — | Nedtryckt |
| 6237509 | Press a button on a controller to find it. | — | Tryck på en knapp på handkontrollen för att hitta den. |
| 6237511 | Pick a connected controller to play as Player %u. It moves here from the player it plays now. | — | Välj en ansluten handkontroll som ska användas av spelare %u. Den flyttas hit från den spelare den används av nu. |
| 6237513 | Press to Find | — | Tryck för att hitta |
| 6237515 | How the headset's controllers appear. Combined makes both one gamepad. Separate makes each hand a gamepad of its own. Each plays as the player set for it in Controllers, player 1 unless set otherwise. | — | Hur headsetets handkontroller visas. Kombinerat gör båda till en handkontroll. Separat gör varje hand till en egen handkontroll. Var och en används av den spelare som har angetts för den i Handkontroller, spelare 1 om inget annat har angetts. |

## Kontroller

- `%u` i sträng 6237511 är bevarad.
- Inga markup-taggar eller URL:er förekommer i batchen.
- RetroArchs projekt-TM söktes via API:ets concordance-funktion. Den enda relevanta närliggande träffen stödde *nedtryckt*.
- `l10n-lint --language sv`, `hunspell -d sv_SE` och Crowdins förhandsvalidering passerade utan anmärkningar.

## Omfattning

Detta är en avgränsad batch från de 81 oöversatta strängarna i huvudfilen vid API-hämtningen. Den ersätter inte en fullständig svensk granskning av RetroArch.
