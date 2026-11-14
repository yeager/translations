# 0 A.D. website – UI strings batch 01 (Swedish)

Datum: 2026-11-14
Projekt: `play0ad-website`
Resurs: `ui-strings`
Språk: svenska (`sv`)

## Omfattning och status

25 globala UI-strängar granskades rad för rad: navigering, sidmetadata,
sök, hämtning, utveckling och deltagande. Hugo-platshållare bevarades exakt.

- Lokal granskning: klar.
- Transifex API: 25 strängar sparade och lästa tillbaka; resursen har
  därefter 50 oöversatta av 108.
- Upstream-granskning: 0 granskade strängar enligt API vid arkivering.
- Upstream-merge/publicering: ej verifierad.

## Kontroller

- `l10n-lint --language sv`: godkänd.
- `svlang skrivregler`: godkänd.
- `hunspell -d sv_SE`: kontrollerad; träffar är platshållare, Gitea och
  produktnamnet 0 A.D.
- `msgfmt`: ej tillämpligt; resursen är `GITHUBMARKDOWN`, inte gettext/PO.
- API-läsning: samtliga 25 sparade måltexter matchar deltafilen.
- Diffkontroll och Gitleaks: körs på arkivets staged ändring före commit.

Den fullständiga, sparade deltafilen finns i `reviewed.json`.
