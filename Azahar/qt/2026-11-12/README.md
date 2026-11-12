# Azahar, QT, svenska

Datum: 2026-11-12
Komponent: `en.ts`
Resurs: `o:azahar:p:azahar:r:qt`
Version: Azahar 2126.2, publicerad 2026-10-08

## Resultat

22 tidigare oöversatta QT-strängar har granskats och skickats i en enda Transifex API-batch. Batchen omfattar grafikinställningar, skärmtangentbord, 3DS-paketfiler och felhantering för snabbsparningar. HTTP-svaret var 200. Alla 22 mål har lästs tillbaka med exakt samma svenska text och komponenten har därefter noll oöversatta svenska strängar.

Två skilda källsträngar, `Blank input is not allowed` och `Empty input is not allowed`, har samma korrekta svenska mål: `Tom inmatning tillåts inte`. Det är ett medvetet undantag, inte en dubblett att ändra.

## Kontroller

- Radvis granskning mot angivna QT-dialoger och källrader.
- Kontroll av HTML-markup, `<br/>`, `%1`, em dash och tre identiska konsonanter: godkänd.
- `l10n-lint`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `svlang` och Hunspell kördes på målen. Träffarna gäller HTML-markup, 3DS och den etablerade emulator-termen `snabbsparning`, inte språkfel.
- `msgfmt`: inte tillämpligt; resursen hanteras via Transifex JSON API.

## Upstreamstatus

Uppladdad och verifierad i Transifex den 12 november 2026. Ingen separat upstream-merge krävs för denna åtgärd.
