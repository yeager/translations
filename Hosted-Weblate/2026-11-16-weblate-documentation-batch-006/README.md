# Hosted Weblate – Documentation – Swedish batch 006

Datum: 2026-11-16

Projekt: [Weblate](https://hosted.weblate.org/projects/weblate/)

Komponent: [Documentation / Svenska](https://hosted.weblate.org/projects/weblate/documentation/sv/)

## Omfattning

Fem tomma dokumentationssträngar har granskats rad för rad och sparats direkt i Hosted Weblate. Arbetet rör administration av konton, grupper, token och behörigheter. reStructuredText-markering och kodnamn har bevarats.

1. Uppgraderingskontroll för förväxlingsbara verifierade e-postadresser och återställning av konton.
2. Blockering som bevarar gruppmedlemskap och redan auktoriserat bakgrundsarbete.
3. Blockering av administratörer, grupptilldelningar och behörigheter för arbetsytor.
4. Återkallelse av projekttoken och bevarande av faktureringsåtkomst.
5. Anpassning av standardgruppers roller och behörigheter för skärmbilder.

## Status

- Lokal granskning: klar för dessa fem strängar.
- Sparat upstream: ja, direkt i Hosted Weblate via webbgränssnittet.
- Upstream-granskning och merge: inte verifierat; Hosted Weblate sparar översättningen men detta är inte samma sak som att den har införlivats i projektets Git-förråd.

## Kontroller

- Diffkontroll: godkänd för arkivfilen.
- Gitleaks: godkänd för arkivkatalogen.
- `msgfmt`: godkänd mot den aktuella svenska dokumentations-PO-filen från `WeblateOrg/weblate` på `main`. Filen kan ligga efter de senaste sparningarna i Hosted Weblate.
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda; någon lokal exporterad deltafil finns inte för denna direktsparade Weblate-batch.

## Terminologi

- team: grupp
- team administration: gruppadministration
- token: token
- workspace: arbetsyta
- finding: fynd

