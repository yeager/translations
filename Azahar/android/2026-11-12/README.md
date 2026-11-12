# Azahar, Android, svenska

Datum: 2026-11-12
Komponent: `strings.xml`
Resurs: `o:azahar:p:azahar:r:android`
Version: Azahar 2126.2, publicerad 2026-10-08

## Resultat

29 tidigare oöversatta Android-strängar har granskats i funktionell UI-kontext och skickats i en enda Transifex API-batch. De omfattar behörigheter, anpassade GPU-drivrutiner, handkontrollbindningar, inställningar per program och ett snabbsparningsfel. HTTP-svaret var 200. Alla 29 mål har lästs tillbaka med exakt samma svenska text och komponenten har därefter noll oöversatta svenska strängar.

## Terminologiska beslut

- Android permission är `behörighet`.
- local network är `lokalt nätverk`.
- per-application settings är `inställningar per program`.
- frame är `bildruta`; input latency är `inmatningsfördröjning`.
- `GPU`, `3DS`, `Adreno`, `Vulkan`, `Anime4K`, `homebrew`, `CDATA`, `%1$s` och den bokstavliga `\n`-sekvensen är bevarade där de krävs.

## Kontroller

- Radvis granskning av samtliga 29 källsträngar.
- Kontroll av `%1$s`, CDATA, `<br/>`, bokstavlig `\n`, em dash och tre identiska konsonanter: godkänd.
- `l10n-lint`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `svlang` och Hunspell kördes på målen. Signalerna gäller produktnamn, markup och facktermer, inte identifierade språkfel.
- `msgfmt`: inte tillämpligt; resursen hanteras via Transifex JSON API.

## Upstreamstatus

Uppladdad och verifierad i Transifex den 12 november 2026. Ingen separat upstream-merge krävs för denna åtgärd.
