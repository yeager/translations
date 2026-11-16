# Hosted Weblate – Weblate Application – svenska – granskningsbatch 004

Datum: 2026-11-16

## Omfattning

Tio strängar har granskats rad för rad i sitt UI- och källkodssammanhang och sparats direkt i Hosted Weblate. Sökningen `state:needs-editing` minskade från 29 till 19 poster efter uppdatering av resultaten.

| Engelska | Svenska |
| --- | --- |
| Automatic translation skipped strings that exceed the text length limit. | Den automatiska översättningen hoppade över strängar som överskrider textlängdsgränsen. |
| Could not validate repository URL: %s | Kunde inte verifiera förrådets URL: %s |
| Imported authors | Importerade författare |
| You do not have permission to edit this project. | Du har inte behörighet att redigera det här projektet. |
| The suggestion could not be accepted automatically: %s | Förslaget kunde inte godtas automatiskt: %s |
| The uploaded file contains a string that is too long: %s | Den uppladdade filen innehåller en sträng som är för lång: %s |
| %d string could not be propagated to all components. / %d strings could not be propagated to all components. | %d sträng kunde inte överföras till alla komponenter. / %d strängar kunde inte överföras till alla komponenter. |
| A translation upload is already in progress. | En översättningsuppladdning pågår redan. |
| The uploaded file has expired or was already processed. | Den uppladdade filen har upphört att gälla eller har redan behandlats. |
| The uploaded file has expired. | Den uppladdade filen har upphört att gälla. |

## Terminologi och kontroller

- `repository` följer projektets ordlista: **förråd**.
- Formatplatshållarna `%s` och `%d` har bevarats i respektive sträng och pluralformen har granskats i Weblates UI.
- Direkt sparat upstream i Hosted Weblate; detta är inte en separat upstream-granskning eller merge.
- Weblate-resultat verifierat efter uppdatering: 29 → 19 `state:needs-editing`.
- Diffkontroll: godkänd (ny arkivpost).
- Gitleaks: godkänd.
- `msgfmt`: ej tillämpligt; Hosted Weblate gav ingen lokal gettext-export för denna batch.
- `l10n-lint`, `svlang` och `hunspell-sv`: ej körda, eftersom ingen lokal översättningsfil exporterades från Hosted Weblate.
