# Audacity: tidsstyrningsspår och äldre effekter

Granskningen omfattar den enda oöversatta och de nio osäkra aktiva posterna i `au3/locale/sv.po` vid Audacity-huvudet `f6278e8`.

Tidsstyrningsspårets dialog använder nu konsekvent *hastighetsgräns* för den övre och nedre gränsen. Valideringsmeddelandet beskriver den faktiska relationen mellan dem. Två effektnamn och menyrubriken `Legacy` har återfått svenska namn. Klippnamnets numeriska platshållare är exakt samma `%d` som i källtexten.

Kontroller som passerade för patchen:

- `msgfmt --check --statistics` (4 443 aktiva översättningar)
- avgränsad Hunspell-sv-kontroll av samtliga nya svenska måltexter
- `git diff --check`
- Gitleaks

`l10n-lint` och `svlang` kördes på hela den befintliga katalogen. De rapporterar äldre problem utanför den här patchen, medan de nya posterna inte gav någon ny träff.

Upstream: [Audacity PR #12759](https://github.com/audacity/audacity/pull/12759) skapades 2026-11-13. Den är öppen och mergebar men inväntar obligatorisk granskning; inga CI-resultat, kommentarer eller upstream-merge fanns vid kontrollen.
