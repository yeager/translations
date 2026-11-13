# Dwarf Fortress 50.* `text_set`: batch 22

Datum: 13 november 2026
Projekt: `dwarf-fortress-translation/dwarf-fortress-steam`
Komponent: `text_set`
Omfattning: 10 tidigare oöversatta namngeneratorsträngar

## Granskning

Strängarna genererar titlar till verk och innehåller en oböjbar namnvariabel.
De svenska formuleringarna är därför betydelsebevarande men böjningsneutrala,
till exempel `Mer om [NO_ART_NAME]` och `Sanningen om [NO_ART_NAME]`.
Taggarna har bevarats exakt.

## Kontroller

- JSON och l10n-lint passerade utan fel.
- Anpassad taggkontroll bekräftade exakt paritet.
- svlang passerade för varje normaliserad sträng.
- Hunspell-sv rapporterade endast den förväntade taggvariabeln `NAME`.
- `git diff --check` och Gitleaks passerade.

## Upstream

Alla tio ändringar skickades i ett gemensamt Transifex API-anrop 13 november
2026 18:35:14 UTC. API-svaret bekräftade tio mottagna översättningar med
ursprung `API`; tio individuella återläsningar matchar deltat exakt.

Status: inskickat och verifierat i Transifex; inte projektgranskat eller
publicerat i en utgåva.
