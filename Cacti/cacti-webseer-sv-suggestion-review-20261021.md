# Cacti WebSeer: granskningslogg, 2026-10-21

Granskningen omfattade samtliga externa förslag i Weblate-sökningen `has:suggestion AND NOT suggestion_author:yeager74`.

| Källsträng | Beslut | Motivering |
|---|---|---|
| `%d Minute` | Avvisat | Förslaget ändrade PHP-platshållaren från `%d` till ogiltiga `% d`. |
| `Service Checks` | Avvisat | Befintliga `Tjänstekontroller` följer komponentens etablerade term `tjänst`. |
| `The Service Check history was purged for %s` | Egen ändring, förslag avvisat | Ändrat till `Tjänstekontrollens historik rensades för %s`; behåller platshållaren och konsekvent terminologi. |
| `Users Selected` | Avvisat | `Användare valda` har fel ordföljd i en etikett. |
| `Service Down` | Egen ändring, förslag avvisat | Ändrat till `Tjänsten är nere`; förslaget var språkligt fel. |
| `Purge Events` | Godtaget | `Rensa händelser` är en tydlig och naturlig åtgärdstext. |
| `Triggered` | Avvisat | `Utlöst` ska ha stor begynnelsebokstav i denna statusetikett. |

Efter granskningen gav samma Weblate-sökning inga träffar. Komponenten har 167 av 167 strängar översatta utan problem.

## Aktuell källkontroll 2026-10-27

Den tidigare komponentfilen `cacti-webseer-sv-granskning-20261026.po`
innehåller 22 rättelser. En radvis jämförelse med den aktuella katalogen på
`develop` (SHA-256
`4a8c0f060ee0a6225038134c3709ddddc1b544ed841d0636e81ab10966f54aed`)
visar att tre redan matchar uppströms: `Duplicate URL`, raderna om att ta bort
proxy samt `Delete Server`. Den komponentvisa filen
`cacti-webseer-sv-live-jamford-20261027.po` innehåller de 19 återstående
rättningarna.

Filen passerar `msgfmt`, `l10n-lint` (0 fel och 0 varningar), `svlang` och
Gitleaks. Hunspell träffar endast produktnamnet WebSeer. Den är inte
inskickad.
