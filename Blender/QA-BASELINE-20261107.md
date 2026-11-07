# Blender UI: QA-baslinje 7 november 2026

Katalogen `blender-ui-sv-weblate-complete-reviewed.po` analyserades lokalt med
`l10n-lint --language sv`. Resultatet var 0 fel, 218 varningar och 814
informationsposter.

## Tolkning

Kontrollen är ett urvalsstöd, inte ett automatiskt korrektur. Den stora mängden
informationsposter innehåller avsiktligt oförändrade produktnamn, kameramodeller,
färgrymdsprofiler, codec-namn, formatnamn, URI:er och API-identifierare, till
exempel ACES, Arri Alexa, Blackmagic, RED, DVCPRO och HDTV.

Prioritera i fortsatt radgranskning:

1. 14 typo-träffar och 4 träffar för dubblerade ord.
2. 1 false-friend-träff och 4 konsistensträffar.
3. Teckensättningsvarningar först när strängen är synlig för användaren eller
   är en sammanhängande hjälptext. Många av de 159 slutpunktsavvikelserna och
   169 interpunktionsavvikelserna kommer från API-fragment där källtextens
   avsiktliga form ska följas.
4. 114 träffar där käll- och måltext är lika. Kontrollera dem per kontext;
   flera är produkt- eller formatnamn och ska inte översättas.

Kontrollens 84 valutaträffar ska granskas i kontext: `USD` kan vara en
valutaförkortning men också Universal Scene Description, som ska behållas.

## Genomförd kontroll

- `msgfmt --check --check-header` används för varje deltafil.
- `l10n-lint`, `svlang`, Hunspell-kandidatsökning, diffkontroll och Gitleaks
  körs före arkivering av varje granskad batch.
- Tre lika konsonanter i följd kontrolleras med reguljärt uttryck för varje
  samlingsfil.
