# Dwarf Fortress 50.* `text_set`: batch 21

Datum: 13 november 2026
Projekt: `dwarf-fortress-translation/dwarf-fortress-steam`
Komponent: `text_set`
Omfattning: 10 tidigare oöversatta namngeneratorsträngar

## Granskning

Batchen består av bok- och artefaktnamn med dynamiska taggar. Formuleringarna
är medvetet böjningsneutrala så att de fungerar oavsett vilka namn, substantiv
och adjektiv som spelmotorn sätter in. Samtliga taggar har exakt samma struktur
som i källtexten.

Underlag: DFInts riktlinjer för Transifex och taggar samt Dwarf Fortress-wikins
beskrivning av namnspråkens begränsade morfologi.

## Kontroller

- JSON och l10n-lint passerade utan fel.
- Anpassad taggkontroll bekräftade exakt paritet för samtliga hakparentestaggar.
- svlang gav 10/10 för varje normaliserad svensk sträng.
- Hunspell-sv rapporterade endast taggvariabler såsom `NAME`, `NOUN` och `ADJ`.
- `git diff --check` och Gitleaks passerade.

## Upstream

Alla tio ändringar skickades i ett gemensamt Transifex API-anrop 13 november
2026 18:32:27 UTC. API-svaret bekräftade tio mottagna översättningar med
ursprung `API`. Tio individuella återläsningar matchar deltat exakt.

Status: inskickat och verifierat i Transifex; inte projektgranskat eller
publicerat i en utgåva.
