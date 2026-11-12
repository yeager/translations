# Nextcloud Introvox – svenska batch 6, 2026-11-12

- Komponent: `o:nextcloud:p:nextcloud:r:introvox`.
- Omfattning: 25 strängar, index 125–149 i den aktuella API-exporten. Batchen innehåller bland annat Assistant- och Dashboard-checklistetexter.
- Terminologi: rundtur, Nextcloud-assistenten, tavla, kort, Dashboard, checklista och uppgift.
- Kontroller: svensk plural med `one` och `other` är bevarad; platshållarna `{language}`, `{number}`, `{example}`, `{task}` och `%n` är bevarade; HTML/markup, em dash och tredubbla konsonanter kontrollerade; l10n-lint, diffkontroll och Gitleaks körda. `msgfmt` är inte tillämpligt för JSON-resursen.
- Upstream: inte uppladdat på grund av `locked`-taggar. Transifex API returnerar HTTP 409 för översättningsuppdatering.
- Status: lokalt granskat och arkiverat som väntande delta.
