# Dwarf Fortress 50.* `text_set`: batch 32

Datum: 13 november 2026
Projekt: `dwarf-fortress-translation/dwarf-fortress-steam`
Komponent: `text_set`
Omfattning: 10 tidigare oöversatta berättelsefragment

## Granskning och kontroller

Berättelsefragmenten har översatts idiomatiskt och talarens kön har inte
antagits. Alla `[CONTEXT:…]`-taggar har bevarats exakt. Råformatets regler
för mellanrum, taggfält och radbrytningar följer DFInt:s rekommendationer.
JSON, l10n-lint, taggparitet, svlang på kompletta meningar, Hunspell-sv,
`git diff --check` och Gitleaks kördes. `svlang` flaggade den korrekta
V2-satsen ”Under tre år räddade jag vilsegångna barn” som en falsk positiv.

## Upstream

Alla tio ändringar skickades i ett gemensamt Transifex API-anrop 13 november
2026. API-svaret bekräftade tio mottagna översättningar med ursprung `API`;
tio individuella återläsningar matchade exakt.

Status: inskickat och verifierat i Transifex; inte projektgranskat eller
publicerat i en utgåva.
