# Begränsning av ljuskällor: häfte 11–14, granskning 2026-10-27

## Omfattning

Häfte 11–14 innehåller 64 strängar i `feature.light_limit_fix`. De täcker
visualiseringslägen, schemaläggning, radkontroller och partikelljus. Varje
sträng har jämförts rad för rad med den aktuella engelska källkatalogen.

## Språk- och termbeslut

- **punktljus**, **strålkastarljus** och **ljuskälla** används konsekvent för
  grafikkontextens `point light`, `spot light` och `light source`.
- *culling* återges som **gallring**, och termen undviker sammansättningar med
  tre lika konsonanter, till exempel **gallring av skuggor**.
- `frustum`, kodidentifierare, filvägar, formatsträngar och förkortningar som
  `LLF` och `TAA` är tekniska data och lämnas avsiktligt oförändrade.
- Svenska decimalkomman och tankstreck används i synliga intervall, medan
  platshållare och den struktur som motorn läser har bevarats exakt.

## Kontroller

JSON-tolkning, `l10n-lint`, svlang, Hunspell, Gitleaks, formatmarkörer,
bokstavliga procenttecken och radbrytningar har kontrollerats för varje fil.
Svlangs och Hunspells kvarvarande signaler gäller enbart tekniska termer,
namn, filändelser, grafiska API-begrepp eller förkortningar; inga svenska
stavnings- eller grammatikfel kvarstår efter manuell granskning.

Terminologibanken och översättningsminnet har använts som förslag och sedan
prövats mot den konkreta spel- och grafikfunktionen. Terminbankens förslag
`Spotlight` har inte använts, eftersom **strålkastarljus** är tydligare i det
här gränssnittet.

## Upstreamstatus

Filerna är sparade i arkivet men väntar på att Hosted Weblate-komponenten
låses upp. Före import måste varje komplett komponent jämföras med en ny export
från Weblate.
