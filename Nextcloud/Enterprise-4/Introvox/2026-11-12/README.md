# Nextcloud Enterprise Introvox – svenska, 2026-11-12

- Komponent: `o:nextcloud:p:enterprise-4:r:introvox`.
- Inventering: 367 oöversatta svenska strängar. Samtliga har Transifex-taggen `locked`.
- Återanvänd granskning: 325 strängar är källtextmässigt identiska med de redan rad för rad granskade strängarna i `o:nextcloud:p:nextcloud:r:introvox`; deras svenska måltexter har därför återanvänts utan ändring. De 42 Enterprise-specifika strängarna har därefter granskats rad för rad.
- Kontroller: samtliga 367 källor, pluralformer och platshållare matchar; em dash och tredubbla konsonanter kontrollerade; l10n-lint, diffkontroll och Gitleaks godkända. `msgfmt` är inte tillämpligt för JSON-resursen.
- Upstream: inte uppladdat. Transifex låser strängarna och avvisar översättningsuppdatering med HTTP 409.
- Status: 367 lokalt verifierade och arkiverade som ett väntande delta. Uppladdning väntar på att Transifex-låset tas bort.
