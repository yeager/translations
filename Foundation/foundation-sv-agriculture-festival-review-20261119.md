# Foundation – skördefestival och materialleverans, svensk granskningsbatch 2026-11-19

15 oöversatta svenska strängar i `dlc_agriculture_general.json` har granskats via Crowdin API. Förslagen är utkast och har inte sparats i Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 26406 | Cancel Material Resources Delivery | — | Avbryt leverans av materialresurser |
| 26408 | Are you sure you want to cancel the Material resources delivery? | — | Vill du verkligen avbryta leveransen av materialresurser? |
| 26676 | Festive Needs are temporary Needs filled by attending an ongoing Harvest Festival. | — | Festbehov är tillfälliga behov som uppfylls genom att delta i en pågående skördefestival. |
| 26678 | Undelivered Material resources will be cancelled… | — | Icke levererade materialresurser avbryts, men de tillhörande delarna av skördefestivalen visas fortfarande som förhandsvisningar. Alla delar av skördefestivalen för vilka materialresurser redan har levererats placeras ut under nästa skördefestival. |
| 26680 | Assign at least one {1}, {2}, or {3} to start the festival. | — | Tilldela minst en {1}, {2} eller {3} för att starta festivalen. |
| 26682–26700 | Festivalåtgärder och besökaraktiviteter | — | Validerade svenska förslag i batchens PO-underlag. |

## Kontroller

- `l10n-lint --language sv` passerade utan anmärkningar.
- Avgränsad `hunspell -d sv_SE` passerade utan anmärkningar.
- Platshållarna `{1}`, `{2}` och `{3}` samt den dubbla radbrytningen i 26676 är bevarade.
