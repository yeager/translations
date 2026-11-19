# Foundation – regler II, svensk granskning 2026-11-19

Den andra delen av `rules.json` har granskats via Crowdin API. Förslagen är utkast och har inte skickats till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 6087 | Adds {1} to resources produced. | Lägger till {1} ​​till resurser som produceras. | Lägger till {1} till resurser som produceras. |
| 10432 | Happiness bonus of {1} for villagers with {2} status. | Lyckobonus om {1} för bybor med {2}-status. | Lyckobonus på {1} för bybor med {2}-status. |
| 10434 | Happiness bonus of {1} for villagers with {2} profile. | Lyckobonus om {1} för bybor med {2}-profil. | Lyckobonus på {1} för bybor med {2}-profil. |
| 10436 | Happiness bonus of {1} for villagers with {2} status or {3} profile. | Lyckobonus om {1} för bybor med {2}-status eller {3}-profil. | Lyckobonus på {1} för bybor med {2}-status eller {3}-profil. |
| 10442 | Because of Influence with {IMG1} | På grund av Inflytande med {IMG1} | På grund av inflytande med {IMG1} |
| 10458 | You can have {1} more concurring taxes without penalty. | Du kan ha ytterligare {1} skatter utan är bestraffas. | Du kan ha ytterligare {1} samtidiga skatter utan att bestraffas. |
| 22404 | Combatant training speed is increased by {IMG1}. | Stridandes utbildningshastighet ökas med {IMG1}. | Utbildningshastigheten för stridande ökar med {IMG1}. |

## Kontroller

- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` passerade utan anmärkningar.
- Samtliga bild- och textplatshållare är bevarade.
