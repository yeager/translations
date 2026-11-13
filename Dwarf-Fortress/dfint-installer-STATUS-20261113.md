# dfint-installer: svensk komplettering

Datum: 13 november 2026
Projekt: `dwarf-fortress-translation/dfint-installer`
Komponent: `application.json`

## Omfattning

Samtliga 19 tidigare oöversatta svenska UI-strängar granskades rad för rad
mot installerarens aktuella Rust-källkod. De omfattar installationens
översättningsfiler, Hook-komponenten, ordboken, versionskontroll och
skrivbehörighet.

## Kontroller

- JSON- och l10n-lint-kontrollen passerade.
- Hunspell-sv träffade endast Dwarf Fortress och de dokumenterade
  projekttermerna `Hookdata` och `DF-version`.
- svlangs övriga träffar var falska positiva från sammanfogade fristående
  UI-etiketter och tekniska termer.
- `git diff --check` och Gitleaks passerade.
- `msgfmt` är inte tillämpligt: komponenten och deltat är JSON.

## Upstream

Alla 19 strängar skickades i ett gemensamt Transifex API-anrop 13 november
2026 18:19:31 UTC. API-svaret och 19 individuella återläsningar matchar
exakt. Resursen är 34/34 översatt, 0 oöversatt. Texterna är inskickade men
inte markerade som granskade av projektet.
