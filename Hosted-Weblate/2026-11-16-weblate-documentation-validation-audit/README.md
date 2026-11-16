# Hosted Weblate – Documentation – validation audit

Datum: 2026-11-16

Projekt: [Weblate](https://hosted.weblate.org/projects/weblate/)

Komponent: [Documentation / Svenska](https://hosted.weblate.org/projects/weblate/documentation/sv/)

## Korrigerad validering

Tidigare kontroller använde GitHubs innehållsändpunkt för en PO-fil som är större än gränsen för det svaret. Det gav tomt innehåll till `msgfmt`, vilket innebar att den kontrollen inte visade att själva PO-filen hade lästs.

Den faktiska filen hämtades därefter som rådata från `WeblateOrg/weblate`, `main`, och har validerats på nytt:

- Filstorlek: 3 183 883 byte.
- Antal `msgid`: 13 823.
- Oöversatta poster i Git-huvudgrenen: 3 086.
- `msgfmt -o /dev/null /tmp/weblate-docs-sv.po`: godkänd.

Denna kontroll gäller den aktuella filen i Git-huvudgrenen och kan ligga efter direktsparade ändringar i Hosted Weblate. Den ersätter inte kontroll av en exporterad deltafil för de senaste sparningarna.

## Status

- Lokal validering: korrekt genomförd mot faktisk upstream-PO.
- Hosted Weblate: tidigare direktsparade strängar är inte därmed verifierade som synkroniserade till Git.
- Upstream-granskning och merge: inte verifierat.

