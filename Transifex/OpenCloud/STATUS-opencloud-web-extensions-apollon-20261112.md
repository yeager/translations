# OpenCloud web-extensions-apollon – svenska översättningar

Datum: 2026-11-12  
Projekt och komponent: OpenCloud / `web-extensions-apollon`  
Källa: Transifex API, OpenClouds webbtilläggsprojekt och Apollons dokumentation  
Status: inskickat och verifierat i Transifex

## Omfattning

- 20 tidigare oöversatta UI-strängar för Apollons diagramtyper granskades och översattes.
- Omfattar UML-struktur och UML-beteende, Petrinät, BPMN, processlogik, simbanor och syntaxträd.
- Terminologin följer Apollons faktiska stöd för klass-, objekt-, aktivitets-, komponent-, Petri-, BPMN- och SFC-diagram.

## Kvalitetskontroller

- `l10n-lint --language sv --json-format entries`: godkänd.
- `svlang skrivregler --enable-interpunktion`: godkänd.
- Platshållar- och pluralformskontroll: godkänd.
- `hunspell -d sv_SE`: träffar endast för avsiktliga facktermer/platshållare: `UML-beteende`, `UML-struktur`, `hårdvarunoder` och `%{count}`.
- `git diff --no-index --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga läckor.
- `msgfmt`: ej tillämpligt för JSON-resursen; den validerades med l10n-lint, strukturkontroll och Transifex API.

## Upstream

En Transifex API-batch med 20 uppdateringar skickades 2026-11-12 och fick HTTP 200. Efterkontrollen med `translated=false` returnerade 0 oöversatta svenska strängar för komponenten.
