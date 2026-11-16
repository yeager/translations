# Hosted Weblate – Documentation – Swedish batch 011

Datum: 2026-11-16

Projekt: [Weblate](https://hosted.weblate.org/projects/weblate/)

Komponent: [Documentation / Svenska](https://hosted.weblate.org/projects/weblate/documentation/sv/)

## Omfattning

Fyra tomma dokumentationssträngar har granskats rad för rad och sparats direkt i Hosted Weblate:

1. Fullständiga rapporter och ändringshämtningar.
2. De separata behörigheterna ``reports.view`` och ``change.download``.
3. Rapportskaparen, begränsad till sina egna bidrag.
4. Medlemskap, katalog- och profiluppgifter.

## Status

- Lokal granskning: klar för dessa fyra strängar.
- Sparat upstream: ja, direkt i Hosted Weblate via webbgränssnittet.
- Upstream-granskning och merge: inte verifierat.

## Kontroller

- Diffkontroll: godkänd för arkivfilen.
- Gitleaks: godkänd för arkivkatalogen.
- `msgfmt`: godkänd mot den aktuella svenska dokumentations-PO-filen från `WeblateOrg/weblate` på `main`; den kan ligga efter de senaste sparningarna i Hosted Weblate.
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda eftersom någon lokal exporterad deltafil saknas.

