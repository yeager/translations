# Foundation – Steam: kortbeskrivningar, svensk granskningsbatch 2026-11-19

Tre oöversatta strängar i `steam_page.json` har granskats via Crowdin API. Förslagen är utkast och har inte sparats i Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 26670 | Foundation is a grid-less, laidback medieval city-building game … | — | Foundation är ett avslappnat medeltida stadsbyggarspel utan rutnät, med fokus på organisk utveckling, monumentbyggen och resurshantering. |
| 26672 | The Guivre Garden is an hommage to the guivre … | — | Guivre-trädgården är en hyllning till Guivren, ett mytiskt odjur från medeltida Frankrike. Den här särskilda byggnaden består av 18 delar, med en huvudstaty och 3 sekundära statyer. |
| 26674 | Master the land by raising livestock … | — | Bemästra landet genom att föda upp boskap, plantera frodiga fruktträdgårdar och odla tåliga nya grödor. Utöka dina produktionskedjor för att skapa nya resurser och krön framgången genom att anordna den ståtligaste av skördefestivaler. |

## Kontroller

- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` passerade utan anmärkningar.
- Radbrytningen och talen 18 och 3 i sträng 26672 har bevarats.
