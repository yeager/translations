# Baresip Store Metadata: Weblate-kontroll

Datum: 2026-10-29

## Aktuell export

Den svenska PO-exporten från Hosted Weblate för `baresip/store-metadata`
validerar med `msgfmt --check --check-format` (endast standardvarningar om
ofyllt revisionsdatum och översättarnamn).

Changelog-posten `changelogs/576.txt:1` finns kvar i källan och har tom svensk
måltext. Den är alltså inte redan inskickad eller synkroniserad.

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

## Nästa steg

Spara den förberedda måltexten i Hosted Weblate och kontrollera därefter med
en ny export att posten inte längre är tom.
