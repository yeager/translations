# Ardour – import- och I/O-diagnostik

| Fält | Uppgift |
| --- | --- |
| Datum | 2026-11-04 |
| Kandidatcommit | `fdebe12` |
| Komponent | `libs/ardour/po/sv.po` |
| Ändrade strängar | 3 |
| Upstream | Inte inskickad: Ardour PR #1150 är öppen och en parallell PR skulle skapa konflikt. |

## Rättningar

- Tog bort de felaktiga lösryckta bokstäverna `e` och `d` ur två importdiagnoser.
- Rättade den engelska prepositionen `of` till **av** i diagnostiken för en okänd I/O-bunt.

## Verifiering

- `msgfmt --check --statistics`: godkänt, 854 översatta meddelanden.
- `l10n-lint`: 0 fel.
- `svlang`: träffarna i denna tekniska katalog är granskade som nominalfraser, loggformat eller identifierare; de berör inte denna batch.
- Hunspell: körd för berörda svenska former.
- `git diff --check`: godkänt.
- Gitleaks: inga hemligheter hittades.
