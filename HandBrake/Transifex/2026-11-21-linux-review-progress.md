# HandBrake – Linux UI: pågående svensk radgranskning

Datum: 2026-11-21  
Plattform: Transifex API  
Resurs: `o:HandBrakeProject:p:linux-ui:r:ghbpot`

## Aktuell inventering

Den aktuella svenska PO-exporten innehåller 801 aktiva poster och sju pluralposter. Samtliga har en måltext. Exporten hämtades på nytt via Transifex API före kontrollen; tidigare lokala observationer användes därför inte som aktuell källa.

Terminologin har jämförts med `handbrake-sv-terminology-20261121.md`, `swedish-foss-terminology` och relevanta träffar i `swedish-tm`. Särskilt kontrollerades kodek, kodare, avkodare, bildfrekvens, bithastighet och genomströmning. De används konsekvent i de genomgångna posterna.

## Sparade och API-återlästa ändringar

| Fullständig Transifex-resurssträng | Engelska | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- | --- |
| `o:HandBrakeProject:p:linux-ui:r:ghbpot:s:ac76f4d9b546cda89b7b5ccee79d4c8f` | HandBrake For _Dummies | HandBrake For _Dummies | HandBrake för _nybörjare | Helt oöversatt synlig menypost. Snabbkommandotecknet bevarades. |
| `o:HandBrakeProject:p:linux-ui:r:ghbpot:s:0d668bd70867851f4882d042b8438342` | Start | Start | Starta | Åtgärdsknappen ska använda verbform på svenska. |

Båda värdena skickades genom Transifex REST API och hämtades igen från respektive `resource_translation`-objekt.

## Verktyg

- `l10n-lint --language sv`: inga anmärkningar för ändringsmängden.
- `hunspell-sv`: endast produktnamnet HandBrake markeras; ingen svensk stavningsanmärkning.
- `svlang check`: 10,0/10; produktnamnet är en förväntad frekvensträff, inte ett språkfel.

## Status

Inventering, täckningskontroll och terminologisökning är klara för Linux-resursen. Den semantiska radgranskningen fortsätter; denna rapport markerar inte Linux UI eller HandBrake som färdiggranskade. macOS-, Windows- och Windows Tooltips-resurserna är ännu inte genomgångna rad för rad.