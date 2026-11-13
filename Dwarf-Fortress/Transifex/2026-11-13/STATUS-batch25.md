# Dwarf Fortress 50.* `text_set`: batch 25

Datum: 13 november 2026
Projekt: `dwarf-fortress-translation/dwarf-fortress-steam`
Komponent: `text_set`
Omfattning: 10 tidigare oöversatta titlar och dialogsträngar

## Granskning och kontroller

Alla dynamiska taggar har bevarats exakt. Familjerelationen använder formen
`[CONTEXT:FAMILY_RELATIONSHIP] till mig` för att undvika felaktigt antaget
svenskt genus i en variabel som kan bli exempelvis far, mor, son eller dotter.
JSON, l10n-lint, taggparitet, svlang, Hunspell-sv, `git diff --check` och
Gitleaks kördes. Hunspell-sv träffade endast förväntade taggvariabler.

## Upstream

Alla tio ändringar skickades i ett gemensamt Transifex API-anrop 13 november
2026 19:07:06 UTC. API-svaret bekräftade tio mottagna översättningar med
ursprung `API`; tio individuella återläsningar matchade exakt.

Status: inskickat och verifierat i Transifex; inte projektgranskat eller
publicerat i en utgåva.
