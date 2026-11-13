# Dwarf Fortress 50.* `text_set`: befintlig svenska, korrigering 01

Datum: 13 november 2026
Projekt: `dwarf-fortress-translation/dwarf-fortress-steam`
Komponent: `text_set`
Omfattning: 12 befintliga svenska strängar granskade rad för rad, 2 ändrade

## Ändringar

- `Jag kommer mosa dig till gröt!` blev `Jag ska mala ner dig till gröt!`.
- `Jag kommer äta dig hel!` blev `Jag ska sluka dig hel!`.

Övriga tio strängar i granskningsurvalet var korrekta och behölls.

## Kontroller och upstream

JSON, l10n-lint, svlang, Hunspell-sv, `git diff --check` och Gitleaks
passerade. De två ändringarna skickades i ett gemensamt Transifex API-anrop
13 november 2026 18:39:27 UTC. API-svaret bekräftade två uppdateringar med
ursprung `API`; båda individuella återläsningarna matchade exakt.

Status: inskickat och verifierat i Transifex; inte projektgranskat eller
publicerat i en utgåva.
