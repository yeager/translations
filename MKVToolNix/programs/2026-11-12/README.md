# MKVToolNix, programs, svenska

Datum: 2026-11-12
Komponent: `programs`
Resurs: `o:moritz-bunkus:p:mkvtoolnix:r:programs`

## Resultat

Två tidigare oöversatta UI-strängar har granskats och skickats via Transifex API i en enda batch. HTTP-svaret var 200 och båda strängarna har lästs tillbaka med exakt samma svenska text. Resursen har därefter noll oöversatta svenska strängar.

| Källa | Svenska |
| --- | --- |
| `E&nable all items from same source file` | `A&ktivera alla objekt från samma källfil` |
| `D&isable all items from same source file` | `Ina&ktivera alla objekt från samma källfil` |

## Kontroller

- Strukturell kontroll av snabbtangenter, tomma mål, em dash och tre lika konsonanter: godkänd.
- `l10n-lint`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `svlang` och Hunspell rapporterade artefakter från JSON-metadatan och snabbtangensampersanden, inte språkfel i målen.
- `msgfmt`: inte tillämpligt; Transifex-resursen hanteras som JSON-API-strängar.

## Upstreamstatus

Uppladdad och verifierad i Transifex den 12 november 2026. Det finns ingen separat upstream-merge för denna åtgärd.
