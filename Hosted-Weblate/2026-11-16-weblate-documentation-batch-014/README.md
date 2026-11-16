# Hosted Weblate – Documentation – Swedish batch 014

Datum: 2026-11-16

Projekt: [Weblate](https://hosted.weblate.org/projects/weblate/)

Komponent: [Documentation / Svenska](https://hosted.weblate.org/projects/weblate/documentation/sv/)

## Omfattning

Tre tomma dokumentationssträngar har granskats rad för rad och sparats direkt i Hosted Weblate:

1. Konfigurerade tillägg och deras administrativa sökomfång.
2. Aviseringar, betrodda integrationer och vidareförmedling av identitetsuppgifter.
3. Systemtillhandahållna uppgifter om bidragsgivare, anonymitet och Git-incheckningsidentitet.

## Status

- Lokal granskning: klar för dessa tre strängar.
- Sparat upstream: ja, direkt i Hosted Weblate via webbgränssnittet.
- Upstream-granskning och merge: inte verifierat.

## Kontroller

- Diffkontroll: godkänd för arkivfilen.
- Gitleaks: godkänd för arkivkatalogen.
- `msgfmt`: godkänd mot den faktiska svenska dokumentations-PO-filen från `WeblateOrg/weblate` på `main`. Filen kan ligga efter de senaste sparningarna i Hosted Weblate.
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda eftersom någon lokal exporterad deltafil saknas.

