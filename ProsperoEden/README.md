# ProsperoEden – svenska

ProsperoEden `v1.005.000` publicerades 2026-10-17 och har redan en svensk
gränssnittskatalog. Den aktuella källversionen lade till två texter utan svensk
översättning.

`prosperoeden-sv-SE-20261026.po` är den kompletta svenska katalogen med 555
texter. Patchen visar de två kompletteringarna och uppdaterade
källhänvisningar från projektets kataloggenerator.

Projektets egen katalogkontroll rapporterar noll fel för `sv-SE.po`.
`l10n-lint` rapporterar inga varningar och Gitleaks hittade inga hemligheter i
katalogen. Tre längdvarningar från projektets kontroll är kvar för befintliga
översättningar av säkerhetskopiering och synkning; de är inte nya och behöver
visuell kontroll i den faktiska PS5-layouten.

## Aktuell kontroll 2026-11-15

Huvudrepot finns nu på
[`mani-shankar-musani/ProsperoEden`](https://github.com/mani-shankar-musani/ProsperoEden).
Dess `main` pekar på `a26ba788222465ec7fb94dc813958fc749734e07` (v1.005.000,
2026-10-17). Den aktuella svenska katalogen hade 553 av 555 poster. Patchen
`prosperoeden-sv-frame-generation-20261115.patch` kompletterar de två
saknade texterna för MihawkGen-bildgenerering, utan andra katalogändringar.

Projektets kontroll rapporterar därefter 555 svenska texter, noll fel och
tre tidigare längdvarningar. `l10n-lint`, `svlang`, Hunspell-sv,
`git diff --check` och Gitleaks har också körts. Hunspell markerar
`MihawkGen-vikter` och `network.fgw` som projektnamn/filnamn, inte som
språkfel.

Ändringen är pushad till
[`yeager/ProsperoEden`](https://github.com/yeager/ProsperoEden), grenen
`l10n/sv-frame-generation`. Direkt push till huvudrepot saknas och GitHub
kan inte skapa en pull request från den äldre fork-kedjan till den återfunna
huvudrepon. Den är alltså arkiverad och offentlig, men ännu inte inskickad
till huvudrepot.
