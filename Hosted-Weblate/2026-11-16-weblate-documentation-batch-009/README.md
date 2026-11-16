# Hosted Weblate – Documentation – Swedish batch 009

Datum: 2026-11-16

Projekt: [Weblate](https://hosted.weblate.org/projects/weblate/)

Komponent: [Documentation / Svenska](https://hosted.weblate.org/projects/weblate/documentation/sv/)

## Omfattning

Fem tomma dokumentationssträngar har granskats rad för rad och sparats direkt i Hosted Weblate. Avsnittet beskriver konfidentiellt samarbete, åtkomst till bidragsgivaridentiteter och exporter.

1. Referens till kombinerad konfiguration av roller och grupper.
2. Återskapade översättningsexporter, originalfiler och bidragsgivaridentiteter.
3. Översikt över oberoende sätt att lämna ut identiteter.
4. Behörigheten ``contribution.view_author`` på resurs- och språknivå.
5. Rubriken för återskapade innehållsexporter.

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

- contributor identity: bidragsgivaridentitet
- repository: förråd
- team: grupp
- permission: behörighet
- export: export

