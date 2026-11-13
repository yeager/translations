# Nextcloud Talk, svenska

Datum: 13 november 2026  
Projekt: `nextcloud/nextcloud`  
Komponent: `spreed` (Nextcloud Talk)

## Granskad batch

Två nya UI-strängar granskades rad för rad mot deras källfiler i Talk:

- `Message in private conversation` → `Meddelande i privat konversation`
- `Error while opening file` → `Fel vid öppning av fil`

`privat konversation` följer etablerad svensk terminologi för privata
meddelandeflöden. Feltexten följer svensk fack- och UI-stil med
`fel vid öppning av`.

## Kontroller

- JSON syntaktiskt giltig.
- Inga platshållare, pluraler eller markup att bevara.
- Hunspell-sv gav inga träffar.
- l10n-lint: 0 problem.
- svlang: 10,0/10, inga rapporterade problem.
- `git diff --check` och Gitleaks passerade.
- `msgfmt` är inte tillämpligt på Transifex JSON-deltafilen.

## Upstream

Batchen skickades i ett gemensamt Transifex API-anrop 13 november 2026
18:08:32 UTC. API-svaret och två separata återläsningar bekräftar exakt
sparad måltext med `origin: API`. Resursstatistiken är därefter
2 523/2 523 översatta, 0 oöversatta. Texterna är ännu inte granskade av
projektets ordinarie granskningsflöde.
