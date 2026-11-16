# Home Assistant: kontroll med korrekt språkfilter

Datum: 16 november 2026

En ny avläsning med Lokalises `filter_lang_id` och `filter_untranslated=1`
ersätter inte tidigare granskning, men visar att dess filter var för grovt
för att vara en fullständig slutkontroll.

| Komponent | Oöversatta svenska poster |
| --- | ---: |
| Core | 47 |
| Frontend | 11 |
| Android | 0 |
| iOS | 0 |

Core innehåller både tomma pluralvärden och tomma måltexter. Frontend har 11
tomma måltexter. Källtexterna och nycklarnas aktuella status måste hämtas och
bedömas innan någon svensk text sparas. Inga översättningar ändrades i denna
kontroll.

Detta är en statusavläsning från Lokalise API, inte en lokal programtestning,
upstream-granskning eller release.
