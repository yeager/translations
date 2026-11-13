# Lokal granskningsrapport: innehåll, allmän FAQ

Datum: 2026-11-13  
Projekt: Warzone 2100-webbplatsen (`wz2100.net`)  
Källrevision: `387c5d29273584bd4526d87f6a9c633d63b70fdb`  
Omfattning: `content/en/faq/general/faq-01.md`–`faq-04.md`

## Kontext och omfattning

Sidorna visas som expanderbara FAQ-kort på startsidan och hjälper spelare att bedöma plattformsstöd och systemkrav samt att hitta sätt att bidra. Den lokala svenska kandidaten bevarar Hugo-kortkoder, länkmål, produktnamn och versionsnummer. Källtexten har fem filer, inklusive den huvudlösa indexfilen; kandidaten har motsvarande fem filer.

## Språkval

*Free* i samband med hämtning återges som *kostnadsfritt*. Teknisk terminologi som OpenGL, Vulkan, RAM, Windows, macOS, Linux, FreeBSD, Discord, IRC och GitHub lämnas kvar. *Integrated graphics* är *integrerad grafik*, vilket är vedertagen svensk teknisk term. Rubriker och brödtext är utformade för korta FAQ-svar snarare än direktöversatta marknadsfraser.

## Lokala kontroller

| Kontroll | Resultat |
| --- | --- |
| Käll- och målparitet | Godkänd: fem filer med motsvarande sökvägar |
| Hugo-kortkoder och länkmål | Godkänd: samtliga källvärden är oförändrade |
| Kontroll av tre lika konsonanter i följd | Godkänd: inga träffar |
| Diffkontroll | Godkänd: inga blankstegsproblem |
| Gitleaks | Godkänd: inga hemligheter hittades |
| Hunspell svenska | Endast avsiktliga tekniska namn och egennamn rapporterades |
| svlang | Kördes. V2-varningar och låg poäng härrör från korta listposter och sammanfogad Markdown utan sidkontext; ingen konkret svensk språkavvikelse kvarstod efter manuell granskning. |
| l10n-lint | Kan inte köras för Markdown; verktyget rapporterar filformatet som ej understött. |
| Hugo-byggning | Kan inte köras: `hugo` saknas i miljön. |
| msgfmt | Inte tillämpligt: resursen är Markdown, inte GNU gettext-PO. |

## Status

Batchen är lokalt färdiggranskad. Den är en kandidat tills svenska aktiveras i Crowdin. Ingen Crowdin-uppladdning, inget upstream-inskick och ingen upstream-merge har skett.
