# 0 A.D. website – UI strings batch 03 (Swedish)

Datum: 2026-11-14
Projekt: `play0ad-website`
Resurs: `ui-strings`
Språk: svenska (`sv`)

## Omfattning och status

De sista 25 globala UI-strängarna granskades rad för rad: läsning, sök,
nedladdningar, torrentguide och språkreservtext. Hugo-platshållare och synliga
produktnamn bevarades exakt där det krävs.

- Lokal granskning: klar.
- Transifex API: 25 strängar sparade och lästa tillbaka; resursen har
  därefter 0 oöversatta av 108.
- Upstream-granskning: 0 granskade strängar enligt API vid arkivering.
- Upstream-merge/publicering: ej verifierad.

## Kontroller

- `l10n-lint --language sv`: godkänd.
- `svlang skrivregler`: godkänd.
- `hunspell -d sv_SE`: kontrollerad; träffar är platshållare, fil- och
  plattformstermer samt bevarade produktnamn.
- `msgfmt`: ej tillämpligt; resursen är `GITHUBMARKDOWN`, inte gettext/PO.
- API-läsning: samtliga 25 sparade måltexter matchar deltafilen.
- Diffkontroll och Gitleaks: körs på arkivets staged ändring före commit.

Den fullständiga, sparade deltafilen finns i `reviewed.json`.
