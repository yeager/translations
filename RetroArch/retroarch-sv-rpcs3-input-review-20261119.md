# RetroArch RPCS3 – spak- och avtryckartrösklar, svensk granskningsbatch 2026-11-19

Åtta oöversatta svenska RPCS3-strängar i `rpcs3-libretro.json` har granskats via Crowdin API. Förslagen är inte sparade eller skickade till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 6234759 | Stick Deadzone | — | Spakens dödzon |
| 6234761 | How far a stick can be tilted before the game sees it move. Inside it the stick's output is scaled down to the Stick Anti-Deadzone rather than cut off, so a resting stick that drifts a little stays close to the centre. Applies to both sticks of every pad; RetroArch's own Analog Deadzone comes before it. | — | Så långt en spak måste lutas innan spelet uppfattar rörelse. Inom den skalas spakens utsignal ned till spakens antidödzon i stället för att klippas bort, så att en vilande spak med liten avdrift hålls nära mitten. Gäller båda spakarna på alla handkontroller; RetroArchs egen analoga dödzon tillämpas före den. |
| 6234769 | Stick Anti-Deadzone | — | Spakens antidödzon |
| 6234771 | Where the stick's output starts once it is tilted past the Stick Deadzone. Games for the DualShock 3 ignore a small tilt themselves, the deadzone of the pad they were made for; starting past it makes the slightest tilt count, for finer steering in racing games. 0% leaves the game's own deadzone in place. With a Stick Deadzone of 0% a stick that drifts makes the game move. | — | Där spakens utsignal börjar när den lutas förbi spakens dödzon. Spel för DualShock 3 ignorerar själva en liten lutning, dödzonen på handkontrollen de gjordes för; att starta efter den gör att minsta lutning räknas, för finare styrning i racingspel. 0 % lämnar spelets egen dödzon kvar. Med en spakdödzon på 0 % gör en spak med avdrift att spelet rör sig. |
| 6234773 | 13% | — | 13 % |
| 6234775 | Trigger Threshold | — | Tröskelvärde för avtryckare |
| 6234777 | How far L2 and R2 must be pressed before the game sees them; past it the press is scaled up from nothing to full. With a pad and frontend that report how far a trigger is pressed (analog triggers) the game gets that as the button's pressure, otherwise L2 and R2 stay all or nothing. 0% gives the whole travel of the trigger. | — | Så långt L2 och R2 måste tryckas in innan spelet registrerar dem; därefter skalas trycket från inget till fullt. Med en handkontroll och ett gränssnitt som rapporterar hur långt en avtryckare är intryckt (analoga avtryckare) får spelet detta som knappens tryckstyrka, annars förblir L2 och R2 helt av eller på. 0 % använder avtryckarens hela rörelseomfång. |
| 6234779 | 12% | — | 12 % |

## Kontroller

- Projektets Crowdin-TM kontrollerades via concordance i API:t. Något separat verktyg med namnet `swedish-tm` finns inte installerat; projektets TM användes som tillgänglig motsvarighet.
- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` och Crowdins QA markerar endast antidödzon, spakdödzon och DualShock. De är korrekta svenska sammansättningar respektive produktnamn.
- Inga platshållare eller formateringsmarkörer finns i batchen.
