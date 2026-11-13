# Dwarf Fortress 50.* `text_set`: avslutad översättningsomgång

Datum: 13 november 2026
Projekt: `dwarf-fortress-translation/dwarf-fortress-steam`
Komponent: `text_set`
Språk: svenska

## Omfattning

Komponentens befintliga svenska översättningar granskades rad för rad, och
återstående oöversatta strängar översattes i verifierade API-batcher. De
projektunika kraven för Dwarf Fortress har följts: taggar i hakparenteser,
fältavgränsare, radbrytningar och relevanta mellanrum har bevarats exakt.

## Kontroller

JSON-validering, l10n-lint, taggparitet, Hunspell-sv, diffkontroll och
Gitleaks har körts för batcherna. `svlang` användes på hela svenska meningar;
fragment bedömdes i sin spelkontext. `msgfmt` är inte tillämpligt på
Transifex JSON-deltan.

## Upstream-status

Transifex API:s aktuella fråga med `filter[translated]=false` returnerade
`0` strängar och `next: null`. Samtliga här dokumenterade batcher har
skickats via API och återlästs individuellt med exakt resultat.

Status: lokalt granskat, arkiverat, inskickat och mottaget i Transifex.
Projektgranskning och publicering i en spelutgåva är inte verifierad här.
