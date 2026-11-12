# VBA-M, wxvbam, svenska

Datum: 2026-11-12
Komponent: `wxvbam`
Resurs: `o:bgk:p:vba-m:r:wxvbam`
Version: VBA-M 2.2.3, publicerad 2025-10-25

## Resultat

79 tidigare oöversatta UI- och konfigurationssträngar har granskats rad för rad i källkodskontext och skickats i en enda Transifex API-batch. Batchen omfattar den nya DLSS-NR-funktionen, filåtkomst och länkningsserverfel. Transifex accepterade ändringarna och återläsning bekräftade 79 av 79 mål. Komponenten har därefter noll oöversatta svenska strängar.

## Terminologiska beslut

- `frame` är `bildruta` och `frame rate` är `bildfrekvens`.
- `display filter` är `skärmfilter`.
- `control mask` är `styrmask`.
- `scaled height` är `skalad höjd`.
- `DLSS-NR`, `DLSS NR`, `nr_frame`, kommandoflaggor och formatnamn är oförändrade.

## Kontroller

- Radvis kontextgranskning mot källkodens fil och rad.
- Kontroll av 79 av 79 snabbtangenter, `%s`-platshållare, `nr_frame` och dess flaggor: godkänd.
- Kontroll av em dash och tre identiska konsonanter: godkänd.
- Projektets svenska TM kontrollerades för bland annat `bildruta` och `bildfrekvens`.
- `l10n-lint`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `svlang` och Hunspell användes mot enbart måltexter. Deras signaler gäller produktnamn, kommandoflaggor, facktermer och snabbtangentsmarkeringar, inte identifierade språkfel.
- `msgfmt`: inte tillämpligt; resursen hanteras via Transifex JSON API.

## Upstreamstatus

Uppladdad och verifierad i Transifex den 12 november 2026. Ingen separat upstream-merge krävs för denna åtgärd.
