# OpenCloud web-files – svenska översättningar

Datum: 2026-11-12
Projekt och komponent: OpenCloud / `web-files`
Källa: Transifex API och `opencloud-eu/web`
Status: inskickat och verifierat i Transifex

## Omfattning

- 20 tidigare oöversatta strängar granskades i Vue-/TypeScript-källkontext.
- Omfattar arbetsytans bildkontroll, delningsnamn för skärmläsare, versionsåterställning, papperskorg, sortering, uppladdningsfel och pluralformer.
- Projektets etablerade översättning `Space` → `arbetsyta` följdes konsekvent.
- `README` behölls medvetet som filnamn/etablerad teknisk term.

## Kvalitetskontroller

- `l10n-lint --language sv --json-format entries`: godkänd.
- `svlang skrivregler --enable-interpunktion`: godkänd.
- `hunspell -d sv_SE`: enda träffen var avsiktliga termen `README`.
- Egen kontroll av pluralformer och `%{…}`-platshållare: godkänd.
- `git diff --no-index --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga läckor.
- `msgfmt`: ej tillämpligt; denna komponent är en JSON-resurs och validerades med l10n-lint, struktur- och platshållarkontroll samt Transifex API.

## Versionskontroll

`opencloud-eu/web` är ett aktivt Vue.js-/TypeScript-projekt. Senaste stabila release som kontrollerades var `v8.2.2`, publicerad 2026-11-11.

## Upstream

En Transifex API-batch med 20 uppdateringar skickades den 2026-11-12 och fick HTTP 200. Efterkontrollen med `translated=false` returnerade 0 oöversatta svenska strängar för `web-files`.

## Återstående i OpenCloud

Vid komponentinventeringen återstod 99 oöversatta strängar i 14 andra komponenter. De behandlas separat för att bevara UI- och domänkontext.
