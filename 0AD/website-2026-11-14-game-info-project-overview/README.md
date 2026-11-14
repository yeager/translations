# 0 A.D. website – project overview (Swedish)

Datum: 2026-11-14
Projekt: `play0ad-website`
Resurs: `page-game-info-project-overview`
Språk: svenska (`sv`)

## Omfattning

18 av 18 strängar granskades rad för rad i kontexten av spelets
projektöversikt: bakgrund, historisk ambitionsnivå, licens, utveckling och
utgåva 28. Hugo-bildkort och Markdown-länkar har bevarats oförändrade.

## Status

- Lokal granskning: klar.
- Arkivering: klar i detta katalogunderlag.
- Transifex API: 18 strängar sparade och lästa tillbaka; 0 oöversatta.
- Upstream-granskning: 0 granskade strängar enligt API vid arkivering.
- Upstream-merge/publicering: ej verifierad.

## Kontroller

- `l10n-lint --language sv`: godkänd.
- `svlang skrivregler`: godkänd.
- `hunspell -d sv_SE`: kontrollerad; återstående träffar är egennamn,
  licenser, Hugo-kod, engelska produktnamn och sammansättningar.
- `msgfmt`: ej tillämpligt; resursen är `GITHUBMARKDOWN`, inte gettext/PO.
- API-läsning: samtliga 18 sparade måltexter matchar deltafilen.
- Diffkontroll och Gitleaks: körs på arkivets staged ändring före commit.

Se `reviewed.tsv` för den sparade svenska deltafilen.
