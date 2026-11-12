# iD Editor, imagery, svenska

Datum: 2026-11-12
Projekt: iD Editor 2.42.3, publicerad 2026-10-20
Komponent: `imagery`
Upstream: https://app.transifex.com/openstreetmap/id-editor/translate/#sv/imagery/

## Resultat

Två saknade källattributioner granskades mot iD:s `data/imagery.json` och
skickades i ett Transifex API-anrop. API:t återlämnade båda sparade målen och
efterkontrollen visar 0 oöversatta svenska strängar i komponenten.

* Dourados betecknas med det etablerade geografiska namnet; *aerial imagery*
  är `flygbilder` i denna kartkontext.
* Den bulgariska myndighetsattributionen är översatt som
  `Ministeriet för jordbruk och livsmedel`.

## Kontroller

* l10n-lint och svlang: godkända.
* hunspell-sv: endast ortnamnet `Dourados`, vilket är avsiktligt.
* Kontroll av em dash, platshållare och markup: godkänd.
* `git diff --check` och Gitleaks: godkända.
* `msgfmt`: inte tillämpligt, eftersom detta är en JSON-resurs.

## Status

Inskickad och mottagen i Transifex. Batchen är inte formellt granskad i
Transifex. Råexport, delta, API-kvitto och efterkontroll finns i denna katalog.
