# Home Assistant Core – nätverk och larm, svenska

Datum: 2026-11-15

Sex strängar har granskats i sin konkreta integrations- och entitetskontext,
sparats i Lokalise och återlästs i den svenska målspråkskolumnen.

| Källa | Svenska |
| --- | --- |
| Upload link rate | Uppladdningshastighet för länk |
| Max upload link rate | Högsta uppladdningshastighet för länk |
| Max download link rate | Högsta nedladdningshastighet för länk |
| Download link rate | Nedladdningshastighet för länk |
| Visual alarm | Visuellt larm |
| Acoustic alarm | Ljudlarm |

## Upstreamstatus

- Lokal granskning: klar.
- Sparad i Lokalise: klar, sex strängar.
- Återläst i Lokalise: klar, sex strängar.
- Projektgranskning och release: inte verifierade.

## Kontroller

- `l10n-lint`, `svlang` och `hunspell-sv`: körs mot den arkiverade
  kontrollfilen i denna batch.
- `msgfmt`: ej tillämpligt; Lokalise-källan är JSON-baserad och ingen PO-fil
  har exporterats.
- `git diff --check` och Gitleaks: körs före arkiveringens push.
