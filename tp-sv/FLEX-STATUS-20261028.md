# Flex 2.6.5-rc1: status

Den aktuella svenska Translation Project-katalogen hämtades, granskades rad för
rad och kontrollerades 2026-10-28.

- Katalogstatus: 135 av 135 aktiva poster översatta; inga osäkra eller
  oöversatta poster återstår.
- Käll-POT: 2026-10-27.
- Senaste stabila GitHub-utgåva: `v2.6.4`, publicerad 2017-05-06.
- Kontroller: `msgfmt --check`, l10n-lint (0 fel), svlang, Hunspell och
  Gitleaks (inga hemligheter).

Den stabila utgåvan är äldre än 48 månader, men arbetet genomfördes efter
uttryckligt önskemål. Den färdiga filen är arkiverad som
`flex-2.6.5-rc1.sv.po`. Translation Projects robot accepterade och arkiverade
filen 2026-10-28 12:37.

## Inskickningsväg verifierad 2026-10-29

Translation Projects svenska teamsida visar att `flex` är oassignerat och
alltså fritt att översätta. TP-roboten tar emot filen som bilaga via
`robot@translationproject.org` med ämnesraden
`flex-2.6.5-rc1.sv.po`. Den kör själv `msgfmt` och återrapporterar resultatet.
Robotens bekräftelse anger att filen har accepterats och lagrats i arkivet.
Den lokala filen passerar `msgfmt --check --check-format`; l10n-lint har inga
fel och en enda korrekt svensk pluralvarning för `tillstånd`.
