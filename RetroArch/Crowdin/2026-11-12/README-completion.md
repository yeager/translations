# RetroArch, svenska, Crowdin: komplettering 2026-11-12

Projekt: RetroArch, Crowdin `380544`
Språk: `sv-SE`
Versionskälla: RetroArch `v1.22.2`, publicerad 2025-11-20.

## Resultat

Totalt 309 tidigare oöversatta strängar granskades i Crowdins editor och skickades i sju batcher. Crowdins färska filter för oöversatta strängar visar `0 STRINGS`; projektets svenska översättningsgrad är 100 %.

Alla 309 förslag skapades som vanliga, ej automatiskt godkända Crowdin-förslag. Varje skickad sträng återlästes från API:t och matchades mot den arkiverade kandidattexten med kontot `yeagersthlm`.

## Innehåll

- Batch 01–02: linuxloader- och Odin-inställningar.
- Batch 03 och 05: openMSX-maskinvarubeteckningar, medvetet bevarade för exakt igenkänning i maskinväljaren.
- Batch 04: openMSX-tillägg.
- Batch 06: Odin-rendering, ljud, trådning och felsökningsnycklar.
- Batch 07: openMSX-maskiner, bildutmatning, kortplatser och tillägg.

## Kontroller

Varje batch kontrollerades för täckning, markup, platshållare och förbjuden em dash. `l10n-lint`, `svlang`, `hunspell-sv`, `git diff --check` och Gitleaks kördes. Informationsnotiser om identisk källa och mål gäller avsiktligt bevarade produktnamn, förkortningar och mått. `msgfmt` är inte tillämpligt eftersom Crowdins API tar emot individuella JSON-förslag.

## Status

Lokalt granskat: klart.
Arkiverat och pushat till `yeager/translations`: klart.
Inskickat till Crowdin och API-verifierat: klart.
Godkänt eller publicerat av RetroArch: väntar på projektets vanliga granskning.
