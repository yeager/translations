# Baresip Store Metadata: Weblate-kontroll

Datum: 2026-10-29

## Aktuell export

Den svenska PO-exporten från Hosted Weblate för `baresip/store-metadata`
validerar med `msgfmt --check --check-format` (endast standardvarningar om
ofyllt revisionsdatum och översättarnamn).

Changelog-posten `changelogs/576.txt:1` fanns kvar i källan med tom svensk
måltext vid den första exportkontrollen.

## Förberedd rättning

Den granskade och arkiverade deltan
`store-metadata-sv-changelog-576-20261029.delta.po` innehåller den enda
kvarvarande översättningen:

```text
- Visa även inkommande DTMF-siffror i samtalets DTMF-fält
- Säkerhetskopiera nu om din senaste säkerhetskopiering gjordes före augusti 2026
```

Filen har redan kontrollerats med formatkontroll, l10n-lint, svlang och
avgränsad Gitleaks-kontroll. Den innehåller en sträng och ligger långt under
gränsen för uppdelad Weblate-import.

## Uppladdning och slutkontroll

Den förberedda måltexten sparades i Hosted Weblate 2026-10-29. En ny sökning
efter `state:<translated` är tom och komponentöversikten visar 428 av 428
svenska strängar (100 procent). De fem avfärdade kontrollerna fanns redan
före denna ändring; den sparade changelog-posten skapade ingen ny kontroll.
