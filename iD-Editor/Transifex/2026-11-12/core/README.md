# iD Editor, core, svenska

Datum: 2026-11-12
Projekt: iD Editor 2.42.3, publicerad 2026-10-20
Komponent: `core`
Upstream: https://app.transifex.com/openstreetmap/id-editor/translate/#sv/core/

## Resultat

Tre saknade svenska kärnsträngar granskades i iD:s aktuella källkod och
skickades i en Transifex API-batch. API-svaret innehåller alla tre måltexter.
Efter en kort cachefördröjning visar en ny API-läsning 0 oöversatta svenska
strängar i komponenten.

| Källa | Svenska | Källkontext |
| --- | --- | --- |
| Color picker | Färgväljare | Inspektörens fältkontroll |
| Converted an area to a line. | Konverterade en yta till en linje. | Åtgärdsnotis för felrättning |
| Converted a line to an area. | Konverterade en linje till en yta. | Åtgärdsnotis för felrättning |

## Terminologi

* `area` är `yta` och `line` är `linje` i iD:s geometriåtgärder.
* `Color picker` är den korta UI-termen `Färgväljare`.

## Kontroller

* Radvis källkontroll mot `data/core.yaml` och valideringskoden.
* l10n-lint: godkänd på explicit JSON-delta.
* svlang och hunspell-sv: inga träffar i målen.
* Kontroll av em dash, platshållare och markup: godkänd.
* `git diff --check`: godkänd.
* Gitleaks: inga hemligheter hittades.
* `msgfmt`: inte tillämpligt, eftersom Transifex-resursen och deltat är JSON.

## Status

Inskickad och mottagen i Transifex. Måltexterna är inte formellt granskade i
Transifex. Övriga iD-komponenter med oöversatta strängar behandlas separat.

`raw-missing-before.json` är den oförändrade råexporten. `sv-delta.json`
innehåller bara denna batch, och API-filerna dokumenterar mottagning samt
efterkontroll.
