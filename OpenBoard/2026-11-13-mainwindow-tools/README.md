# OpenBoard, svenska huvudfönsterverktyg, 13 november 2026

Den här batchen omfattar 28 strängar i OpenBoards huvudfönster: rutnät, bakgrunder, ritverktyg, lägen, dokumentimport och favoriter.

Terminologi som normaliserats i batchen:

- grid → rutnät
- board mode → tavelläge
- document mode → dokumentläge
- web mode → webbläge
- capture web content → fånga webbinnehåll

Kontroller:

- Qt lrelease: 476 färdiga och 32 ofärdiga strängar
- Hunspell-sv för den svenska deltan: godkänd
- diffkontroll: godkänd
- Gitleaks för deltan: godkänd
- l10n-lint och svlang: katalogomfattande befintliga rapporter används som granskningsunderlag; inga nya relevanta fel hittades i denna avgränsade delta

Upstream: inskickat som [OpenBoard PR #1582](https://github.com/OpenBoard-org/OpenBoard/pull/1582) den 13 november 2026. PR:en är öppen och väntar på granskning.
