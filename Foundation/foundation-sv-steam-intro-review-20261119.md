# Foundation – Steam-introduktion, svensk granskningsbatch 2026-11-19

Två oöversatta svenska strängar i `steam_page.json` har granskats via Crowdin API. Förslagen är utkast och har inte sparats i Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 26566 | [b]Foundation is a gridless medieval city builder where you create modular buildings, shape organic cities and manage its villagers![/b] | — | [b]Foundation är ett medeltida stadsbyggarspel utan rutnät där du skapar modulära byggnader, formar organiska städer och förvaltar dess invånare![/b] |
| 26570 | Foundation combines free-building tools and procedural generation to create the ultimate organic city-building experience. | — | Foundation kombinerar verktyg för fritt byggande och procedurell generering för att skapa den ultimata upplevelsen av organiskt stadsbyggande. |

## Kontroller

- `l10n-lint --language sv` passerade utan anmärkningar.
- Hunspell markerar Foundation och procedurell; det är produktnamn respektive en korrekt teknisk term.
- Fetstilsmarkeringen `[b]…[/b]` är bevarad exakt.
