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
| `o:HandBrakeProject:p:linux-ui:r:ghbpot:s:b0766b49dcb033bc1a70fc9538d64c52` | Available Options: {source-path} … {height} | Två blanksteg efter `{bit-depth}` | Ett blanksteg efter `{bit-depth}` | Samtliga platshållare bevarades och oavsiktligt dubbelt blanksteg togs bort. |
| `o:HandBrakeProject:p:linux-ui:r:ghbpot:s:25eda6ae48b35a7fad08b647148d5e0b` | Denoise filtering reduces … | Onödigt kommatecken före `kan` | Samma text utan kommatecknet | Svensk satsinterpunktion, radbrytningar bevarade. |
| `o:HandBrakeProject:p:linux-ui:r:ghbpot:s:54fb5927b3b5e5081b440cd284675f2c` | Denoise filtering reduces … | Onödigt kommatecken före `kan` | Samma text utan kommatecknet | Svensk satsinterpunktion, indrag och radbrytningar bevarade. |

Samtliga fem värden skickades genom Transifex REST API och hämtades igen från respektive `resource_translation`-objekt.

## Verktyg

- `l10n-lint --language sv`: inga anmärkningar för kandidaterna.
- `hunspell-sv`: endast produktnamnet HandBrake samt etablerade teknikord markeras; ingen svensk stavningsanmärkning.
- `svlang check`: produktnamn och teknikord är förväntade frekvensträffar, inte språkfel.

## Status

Inventering, täckningskontroll och terminologisökning är klara för Linux-resursen. Den semantiska radgranskningen fortsätter; denna rapport markerar inte Linux UI eller HandBrake som färdiggranskade.

## Fortsatt radgranskning – 2026-11-21

Färsk Transifex-hämtning av alla 801 Linux-strängar bekräftade att källsträngarna är oförändrade sedan föregående export. Följande sex korrigeringar sparades och återlästes individuellt via API:

| Engelska | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| Passthru Common Metadata | Genomström vanliga metadata | För över vanliga metadata | Begriplig svensk åtgärdsform. |
| Deblocking filter … blockiness … | Beskrev en annan filterverkan | Anger att filtret kan minska blockighet | Återger källans betydelse; båda radbrytningsvarianterna rättade. |
| Passthru Fallback: | Genomströmningsreserv: | Reservkodning vid genomströmning: | Avser den kodek som används när genomströmning inte kan användas. |
| Foreign Audio Subtitle Track | Främmande språks undertextspår | Undertextspår för främmande språk | Korrekt och idiomatisk svensk sammansättning. |
| SRT file does not exist … | reguljär fil; undantas | vanlig fil; ignoreras | Naturlig svensk feltext utan ändrade radbrytningar. |

l10n-lint med språk=sv gav 0 fel. Fyra kvarvarande varningar är kontrollerade falska positiva: sammansättningen *källljudspår*, tekniska I-/P-bildrutor och ett dubblerat engelskt *is* i källtexten. Hunspell-sv markerade inga av de sparade orden.


### Fortsatt semantisk kontroll

Sparade och API-återlästa: **Aspect Ratio:** → **Bildförhållande:**, **Resume Encoding** → **Återuppta kodningen** och **Stop Encoding** → **Stoppa kodningen**. Dessa ersätter felaktiga eller otydliga UI-former.


### Fortsatt kontroll – åtgärdsetiketter

Tre ytterligare Linux-ändringar sparades och återlästes via Transifex API: **S_top Encoding** → **S_toppa kodningen**, **_Resume Encoding** → **_Återuppta kodningen** samt **Your encode is complete.** → **Kodningen är slutförd.** Snabbkommandotecknen bevarades.
