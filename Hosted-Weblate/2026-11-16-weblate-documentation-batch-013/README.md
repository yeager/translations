# Hosted Weblate – Documentation – Swedish batch 013

Datum: 2026-11-16

Projekt: [Weblate](https://hosted.weblate.org/projects/weblate/)

Komponent: [Documentation / Svenska](https://hosted.weblate.org/projects/weblate/documentation/sv/)

## Omfattning

Tre tomma dokumentationssträngar har granskats rad för rad och sparats direkt i Hosted Weblate:

1. Författarfilter i rapporter och ändringshämtningar.
2. Arbetsytebehörigheter och specifikare resursbegränsningar.
3. Originalarkiv, hjälpfiler och åtkomst till bidragsgivaridentiteter.

## Status

- Lokal granskning: klar för dessa tre strängar.
- Sparat upstream: ja, direkt i Hosted Weblate via webbgränssnittet.
- Upstream-granskning och merge: inte verifierat.

## Kontroller

- Diffkontroll: godkänd för arkivfilen.
- Gitleaks: godkänd för arkivkatalogen.
- `msgfmt`: godkänd mot den faktiska svenska dokumentations-PO-filen från `WeblateOrg/weblate` på `main`. Filen kan ligga efter de senaste sparningarna i Hosted Weblate.
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda eftersom någon lokal exporterad deltafil saknas.

