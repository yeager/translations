# authselect — svensk granskning

Komponent: [master-application](https://translate.fedoraproject.org/projects/authselect/master-application/)

## Status

- Före arbetet: 276 översatta, 9 fuzzy, 2 oöversatta av 287 strängar (96,1 % översatta).
- Granskat: 11 poster (alla nio fuzzy och de två tomma posterna).
- Förslag: 11 översättningar, med platshållare och radbrytningar bevarade.
- Uppladdning: blockerad. Fedora Weblate svarade HTTP 403: “This translation is currently locked.” Ingen ändring skrevs till Weblate.
- Senast verifierat via API: komponenten är fortsatt låst; statistik är oförändrad på 276 översatta, 9 fuzzy och 287 totalt.

## Validering

- `msgfmt --check --check-format`: godkänd.
- `l10n-lint --language sv --skip-fuzzy --no-terminology`: 0 fel, 0 varningar.
- Hunspell (`sv_SE`): flaggade `strängarray`, `authselect-konfigurationen` och `växlingsbar`; dessa är granskade tekniska sammansättningar/produktterminologi.

## Ändrade strängar

Den kompletta filen före granskning, den granskade filen och unified diff finns i samma katalog. Ändringarna omfattar temporärfil, strängarray, konfigurationsstatus, profilmetadata (`Preset`, `Description`, `Source`, `Resolves to`, `Profile`, `Features`) och utskrift av `switchable-auth`-innehåll.

De granskade förslagen är lokalt klara. De kan skickas in när komponenten låses upp av Fedora Weblate.
