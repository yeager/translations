# Foundation – Steam: organisk utveckling, svensk granskningsbatch 2026-11-19

Fyra oöversatta strängar i `steam_page.json` har granskats via Crowdin API. Förslagen är utkast och har inte sparats i Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 26586 | [*]Organic development with our unique Painting tool: Guide your villagers by defining areas for building homes, decide where to pave roads and set patrols, designate forest extraction zones, and more! | — | [*]Organisk utveckling med vårt unika målningsverktyg: Vägled dina bybor genom att ange områden för att bygga bostäder, bestäm var vägar ska anläggas och patruller placeras, utse zoner för skogsavverkning och mycket mer! |
| 26588 | [*]Manage your village: Develop production chains, tax your villagers, trade with neighboring villages, or fight for the King. There are multiple ways to create a successful economy! | — | [*]Förvalta din by: Utveckla produktionskedjor, beskatta dina bybor, handla med grannbyar eller kämpa för kungen. Det finns flera sätt att skapa en framgångsrik ekonomi! |
| 26590 | [*]Progress with the three Estates of the Realm: Three distinct progress paths await you: [b]Labor[/b], [b]Clergy [/b]or [b]Kingdom[/b]. You can either specialize in one or combine all three. | — | [*]Gör framsteg med rikets tre stånd: Tre olika utvecklingsvägar väntar: [b]Arbetare[/b], [b]Prästerskap[/b] eller [b]Kungarike[/b]. Du kan specialisera dig på en av dem eller kombinera alla tre. |
| 26592 | [*]Tailor your gaming experience: Select an Aspiration, adjust the difficulty level or build without constraints by playing in Creative Mode. | — | [*]Anpassa din spelupplevelse: Välj en strävan, justera svårighetsgraden eller bygg utan begränsningar i kreativt läge. |

## Kontroller

- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` passerade utan anmärkningar.
- Listmarkörer och BBCode har bevarats. Källsträngens dubbla blanksteg före `homes` normaliseras i målspråket utan att innebörd eller formatering påverkas.
