# MKVToolNix, man-pages, svenska

Datum: 2026-11-12
Komponent: `man-pages`
Resurs: `o:moritz-bunkus:p:mkvtoolnix:r:man-pages`

## Resultat

Två oöversatta metadatavärden har granskats och skickats via Transifex API i en batch. Båda ska avsiktligt vara identiska med källtexten: de är programmets versionsnummer respektive publiceringsdatum i manualsidorna. HTTP-svaret var 200, målen har lästs tillbaka och resursen har noll oöversatta svenska strängar.

| Källa | Svenska | Kontext |
| --- | --- | --- |
| `101.0` | `101.0` | Versionsentitet i fem manualsidor |
| `2026-08-24` | `2026-08-24` | Datumentitet i fem manualsidor |

## Kontroller

- Kontext- och strukturkontroll: godkänd.
- `l10n-lint`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `svlang` rapporterade JSON-metadatans hashvärden och engelska kommentarsfält, inte språkfel i målen.
- Hunspell gav inga relevanta träffar på versionen eller datumet.
- `msgfmt`: inte tillämpligt; resursen hanteras som JSON-API-strängar.

## Upstreamstatus

Uppladdad och verifierad i Transifex den 12 november 2026. Det finns ingen separat upstream-merge för denna åtgärd.
