# dfint-installer: svensk komplettering

Datum: 13 november 2026
Projekt: `dwarf-fortress-translation/dfint-installer`
Komponent: `application.json`

## Omfattning

Samtliga 34 svenska UI-strängar granskades rad för rad mot installerarens
aktuella Rust-källkod. Arbetet omfattar 19 tidigare oöversatta strängar samt
tre korrigerade befintliga översättningar: `Report bug`, `Ok` och varningen om
äldre översättningsfiler. De omfattar installationens översättningsfiler,
Hook-komponenten, ordboken, versionskontroll och skrivbehörighet.

## Kontroller

- JSON- och l10n-lint-kontrollen passerade.
- Hunspell-sv träffade endast Dwarf Fortress och de dokumenterade
  projekttermerna `Hookdata` och `DF-version`.
- svlangs övriga träffar var falska positiva från sammanfogade fristående
  UI-etiketter och tekniska termer.
- `git diff --check` och Gitleaks passerade.
- `msgfmt` är inte tillämpligt: komponenten och deltat är JSON.

## Upstream

De 19 nya strängarna skickades i ett gemensamt Transifex API-anrop 13 november
2026 18:19:31 UTC. De tre korrigeringarna skickades därefter i ett andra,
samlat API-anrop. API-svaren och individuella återläsningar matchar exakt.
Resursen är 34/34 översatt, 0 oöversatt. Texterna är inskickade men inte
markerade som granskade av projektet.
