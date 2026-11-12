# RetroArch, svenska, Crowdin: batch 02

Datum: 2026-11-12
Projekt: RetroArch, Crowdin `380544`
Språk: `sv-SE`
Källa: Crowdins oöversatta-filter, sida 2, och aktuell API-källtext
Versionskälla: RetroArch `v1.22.2`, publicerad 2025-11-20; projektet är aktivt och versionen är yngre än 48 månader.

## Omfattning

50 strängar ur de aktuella kärnresurserna granskades och skickades som vanliga, ej automatiskt godkända Crowdin-förslag. De omfattar främst ljudalternativ för Odin-kärnan och MSX-alternativ.

`batch-02-source-20261112.json` är den orörda källsnapshoten. Egna ändringar finns enbart i `batch-02-delta-20261112.jsonl` och kandidatfilen.

## Terminologi och beslut

- `main board` → `huvudkort`
- `sound board` → `ljudkort`
- `woofer` → `bashögtalare`
- `sound mode` → `ljudläge`
- `machine` → `maskin`
- `core` → `kärna`

Produkt-, spel- och hårdvarunamn samt dB- och Hz-värden är medvetet oförändrade. `RetroArch`, `C-BIOS`, `MSX`, `ROM` och `VOLUME` har bevarats som tekniska namn eller kontrollnamn. Markeringen `<system>` är bevarad exakt.

## Kontroller

- Egen kontroll av täckning, markup och em dash: godkänd, 50 av 50.
- `l10n-lint`: 0 fel, 0 varningar. Informationsnotiserna gäller avsiktligt identiska dB- och Hz-värden.
- `svlang`: inga anglifieringar. Träffar från stavningsverktyg gäller namn, förkortningar och tekniska termer.
- `hunspell-sv`: endast förväntade egennamn, tekniska namn och kontrollnamn.
- `git diff --no-index --check`: godkänd.
- `gitleaks detect --no-git --source … --redact`: inga hemligheter hittades.
- `msgfmt`: inte tillämpligt; Crowdins API tar emot individuella JSON-förslag.

## Upstreamstatus

Alla 50 förslag skapades via Crowdin API med HTTP 201. `batch-02-verification-20261112.json` bekräftar att alla 50 därefter lästes tillbaka som samma text, skapad av `yeagersthlm`. Förslagen väntar på Crowdins granskning och är inte automatiskt godkända.
