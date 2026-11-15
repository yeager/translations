# Open Home Foundation, inventering av svenska l10n-mål 2026-11-15

## Metod

Aktuella GitHub-releaser kontrollerades och varje huvudgrens filträd söktes
efter vanliga kataloger och filer för användargränssnittslokalisering. Ett
projekt utan egen användargränssnittskatalog är inte ett rimligt mål för en
svensk översättning.

## Resultat

| Projekt | Senaste release | Bedömning |
| --- | --- | --- |
| ESPHome | 2026.10.2, 2026-11-02 | Ingen fristående UI-katalog. Konfigurationstexterna visas i Home Assistant, där de ska översättas. |
| Piper | v1.8.0, 2026-09-04 | Talsyntesmotor utan generell slutanvändar-UI. |
| microWakeWord | Ingen GitHub-release | Motor och träningskod utan generell slutanvändar-UI. |
| Z-Wave JS | v15.32.3, 2026-11-10 | Bibliotek utan generell slutanvändar-UI. |
| Zigpy | 2.4.1, 2026-10-28 | Bibliotek utan generell slutanvändar-UI. |
| Matter.js | v0.18.0, 2026-10-20 | Bibliotek utan generell slutanvändar-UI. |
| ESP Web Tools | 10.5.2, 2026-11-12 | Har en synlig installerar-UI. Svenskt stöd är inskickat i PR #774. |

## Avgränsning

HACS granskas inte som fristående mål. Projektet är på väg att ersättas av
Home Assistants inbyggda Marketplace. Arbetet ska därför ligga i Home
Assistant och Marketplace när deras etablerade översättningsflöde finns.

## Status

Inventeringen fann bara ett nytt aktivt och direkt översättningsbart UI-mål:
ESP Web Tools. Övriga projekt kräver inte en separat svensk UI-katalog.
