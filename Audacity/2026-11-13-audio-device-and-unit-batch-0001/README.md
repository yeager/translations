# Audacity: ljudenheter och Audio Unit, batch 0001

Den här radvisa granskningsbatchen omfattar 40 aktiva poster i början av
`au3/locale/sv.po` vid Audacity-huvudet `41ef0f3`.

Den rättar felaktiga eller oidiomatiska diagnoser för ljudenheter,
samplingsfrekvenser och inspelningsfördröjning. Apples protokollnamn
`Audio Unit` behålls som produktnamn, medan kringtexten är svensk. Även
felmeddelanden för molnsynkronisering och förinställningar har fått korrekt
och konsekvent svensk terminologi.

Kontroller som passerade för patchen:

- `msgfmt --check --statistics` (4 443 aktiva översättningar)
- avgränsad Hunspell-sv-kontroll av de ändrade måltexterna; endast
  produktnamnen `Audio Unit` och `Cloud` behövde undantas
- `git diff --check`
- Gitleaks

`l10n-lint` och `svlang` kördes på hela den befintliga katalogen. De
rapporterar äldre katalogproblem utanför batchen; inga nya problem har
introducerats i patchen.

Upstream: [Audacity PR #12759](https://github.com/audacity/audacity/pull/12759)
uppdaterades 2026-11-13. PR:en är öppen och mergebar, men kräver fortfarande
upstreamgranskning. Inga CI-resultat eller upstream-merge fanns vid kontrollen.
