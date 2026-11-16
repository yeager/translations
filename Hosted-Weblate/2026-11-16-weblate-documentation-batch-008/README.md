# Hosted Weblate – Documentation – Swedish batch 008

Datum: 2026-11-16

Projekt: [Weblate](https://hosted.weblate.org/projects/weblate/)

Komponent: [Documentation / Svenska](https://hosted.weblate.org/projects/weblate/documentation/sv/)

## Omfattning

Fem tomma dokumentationssträngar har granskats rad för rad och sparats direkt i Hosted Weblate. Arbetet omfattar migrering av rollbehörigheter och synlighet för uppgifter om bidragsgivare.

1. Sammanfogning av inbyggda standardbehörigheter under databasmigrering.
2. Återställning av inbyggda roller till standardvärden.
3. Första uppgraderingen med redigerbara behörigheter för inbyggda roller.
4. Namnbyte av äldre anpassade roller före skapandet av nya inbyggda roller.
5. Behörigheten ``contribution.view_author`` och synlighet i historik, kommentarer, förslag och REST API.

## Status

- Lokal granskning: klar för dessa fem strängar.
- Sparat upstream: ja, direkt i Hosted Weblate via webbgränssnittet.
- Upstream-granskning och merge: inte verifierat; en sparning i Hosted Weblate är inte samma sak som att översättningen har införlivats i projektets Git-förråd.

## Kontroller

- Diffkontroll: godkänd för arkivfilen.
- Gitleaks: godkänd för arkivkatalogen.
- `msgfmt`: godkänd mot den aktuella svenska dokumentations-PO-filen från `WeblateOrg/weblate` på `main`. Filen kan ligga efter de senaste sparningarna i Hosted Weblate.
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda; någon lokal exporterad deltafil finns inte för denna direktsparade Weblate-batch.

## Terminologi

- built-in role: inbyggd roll
- custom role: anpassad roll
- permission: behörighet
- team: grupp
- contributor attribution: uppgifter om bidragsgivare

