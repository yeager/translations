# Hosted Weblate – Documentation – Swedish batch 010

Datum: 2026-11-16

Projekt: [Weblate](https://hosted.weblate.org/projects/weblate/)

Komponent: [Documentation / Svenska](https://hosted.weblate.org/projects/weblate/documentation/sv/)

## Omfattning

Fem tomma dokumentationssträngar har granskats rad för rad och sparats direkt i Hosted Weblate. Avsnittet fortsätter dokumentationen om identitetssäkra exporter och VCS-åtkomst.

1. ``translation.download`` tillsammans med en identitetssäker exporter.
2. Originalfiler och oklassificerade exporter.
3. Hämtningsbehörighet och åtkomst till bidragsgivaridentiteter.
4. Referens till export av Git-förråd.
5. Den separata behörigheten ``vcs.access`` och bevarad incheckningshistorik.

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

- repository: förråd
- contributor identity: bidragsgivaridentitet
- exporter: exporter
- download permission: behörighet att hämta
- commit history: incheckningshistorik

