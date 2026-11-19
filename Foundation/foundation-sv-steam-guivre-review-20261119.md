# Foundation – Steam: ljudspår och Guivre, svensk granskningsbatch 2026-11-19

Fem oöversatta strängar i `steam_page.json` har granskats via Crowdin API. Förslagen är utkast och har inte sparats i Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 26596 | [*]Foundation Original Soundtrack: Immerse yourself in over 100 minutes of atmospheric medieval music crafted by the award-winning composers at Audinity. | — | [*]Foundation Original Soundtrack: Fördjupa dig i över 100 minuter av stämningsfull medeltida musik skapad av de prisbelönta kompositörerna på Audinity. |
| 26600 | [i]This page has been translated with the help of the community![/i] | — | [i]Den här sidan har översatts med hjälp av communityn![/i] |
| 26602 | Long before our realm came to be … | — | Långt innan vårt rike kom till berättades historier om Guivren, ett majestätiskt, juvelprytt ormliknande odjur med så väldiga vingar och så vassa klor att den kunde rycka åt sig får rakt framför näsan på oförsiktiga herdar! Nu för tiden, av vördnad eller rädsla, bygger byborna dessa enastående landmärken för att hedra den mäktiga ormen. |
| 26604 | The Guivre Garden pays homage to the Guivre, a mythical beast from Medieval France. | — | Guivre-trädgården hyllar Guivren, ett mytiskt odjur från medeltida Frankrike. |
| 26606 | This special building contains [b]18 parts[/b], with a [b]main statue[/b] and [b]3 secondary statues.[/b] | — | Den här särskilda byggnaden består av [b]18 delar[/b], med en [b]huvudstaty[/b] och [b]3 sekundära statyer.[/b] |

## Kontroller

- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` passerade utan anmärkningar.
- HTML-entiteterna `&quot;`, kursivmarkeringar, fetmarkeringar samt siffrorna 18 och 3 har bevarats exakt.
