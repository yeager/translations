# 0 A.D. website – awards and acclaim (Swedish)

Datum: 2026-11-14
Projekt: `play0ad-website`
Resurs: `page-game-info-awards-and-acclaim`
Språk: svenska (`sv`)

## Omfattning och status

15 av 15 strängar granskades rad för rad: rubriker, sex presscitat och elva
länkade prisnamn. Publikations- och personnamn är bevarade; synlig svensk
länktext, URL:er, Markdown och blockcitat är kontrollerade.

- Lokal granskning: klar.
- Transifex API: 15 strängar sparade och lästa tillbaka; 0 oöversatta.
- Upstream-granskning: 0 granskade strängar enligt API vid arkivering.
- Upstream-merge/publicering: ej verifierad.

## Kontroller

- `l10n-lint --language sv`: godkänd.
- `svlang skrivregler`: godkänd.
- `hunspell -d sv_SE`: kontrollerad; träffar är egennamn, publikationsnamn,
  produktnamn och länkkod.
- `msgfmt`: ej tillämpligt; resursen är `GITHUBMARKDOWN`, inte gettext/PO.
- API-läsning: samtliga 15 sparade måltexter matchar deltafilen.
- Diffkontroll och Gitleaks: körs på arkivets staged ändring före commit.

Den fullständiga, sparade deltafilen finns i `reviewed.json`.
