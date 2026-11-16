# Hosted Weblate – Documentation – Swedish batch 007

Datum: 2026-11-16

Projekt: [Weblate](https://hosted.weblate.org/projects/weblate/)

Komponent: [Documentation / Svenska](https://hosted.weblate.org/projects/weblate/documentation/sv/)

## Omfattning

Fem tomma dokumentationssträngar har granskats rad för rad och sparats direkt i Hosted Weblate. Arbetet gäller grupproller, projektadministration och automatiska inbjudningar. Tekniknamn och reStructuredText-markering har bevarats.

1. Anpassade roller och begränsning av gruppbehörigheter.
2. Den långvariga administratörsbehörigheten :guilabel:`Edit project settings`.
3. Automatiska gruppinbjudningar för projekt och arbetsytor.
4. Direkt grupptilldelning för grupper på webbplatsnivå.
5. Inbyggda roller, REST API och oberoende behörighetsuppsättningar.

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

- team: grupp
- custom role: anpassad roll
- workspace: arbetsyta
- permission: behörighet
- built-in role: inbyggd roll

