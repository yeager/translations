# Blender Manual: svensk granskningsbatch 55

Datum: 4 november 2026

Källa: `exports/2026-11-04/blender-manual-manual-sv.po` samt den officiella
Blender 5.3-manualen för applikationsmallar, kataloglayout, extensions och
Python-tillägg.

## Kontext och omfattning

Åtta poster för tre närliggande tekniska områden: applikationsmallar,
kommandoradshantering av tilläggsförråd och en Python-tutorial. `repo-info`,
JSON-exemplet och API-referensen är maskinläsbara eller formella värden och
bevaras exakt. I beskrivande svensk text används **förråd** för repository,
**användarinställningar** för user preferences och **applikationsmallar** i
linje med den befintliga Blender-manualen.

## Kontroller

- `msgfmt --check --statistics`: 8 översatta meddelanden och godkänd syntax.
- Radvis jämförelse av `(msgctxt, msgid)` mot råexporten: 8/8 träffar.
- `l10n-lint --language sv`, `svlang skrivregler --enable-interpunktion` och
  `svlang svengelska`: inga fel i måltexterna.
- Hunspell `sv_SE` noterar endast RST-rollen, JSON-exemplet, identifierare
  och exempeldata. De är formella värden och ska vara oförändrade.
- Identisk måltext för kommandot och JSON-exemplet är avsiktlig.
- `git diff --check` och Gitleaks: godkända, utan hemligheter.

Råexporten är orörd. Deltafilen är lokalt validerad men inte uppladdad till
Blender Translate.

## Terminologisk efterkontroll 5 november

Den officiella Blender-manualens kommandoradsdokumentation använder
*repository* för Blenders tilläggskällor. Den svenska katalogen har redan
*Förrådshantering*, *användarförråd* och *fjärrförråd* i samma avsnitt;
batchen följer därför **förråd** konsekvent. `repo-info` är däremot ett
underkommando och lämnas oförändrat. *Applikationsmallar* och
*användarinställningar* är också etablerade i den svenska manualen.

Formuleringen om första start justerades till *när programmet startas för
första gången* för idiomatisk svensk dokumentationsprosa. Den ändrar inte
Blenders funktionella innebörd.
