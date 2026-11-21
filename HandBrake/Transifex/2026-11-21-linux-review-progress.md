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


### Fortsatt kontroll – kodning

Sju Linux-poster med felaktigt **omkodning** som översättning av *encode/encoding* sparades och återlästes: målfilnamn, målmapp, enskilda loggar samt statusarna klar, avbruten, misslyckad och slutförd. De använder nu genomgående **kodning**; detta följer HandBrakes terminologilista och skiljer aktiv kodning från faktisk omkodning.


### Fortsatt kontroll – verb och direktsändning

Sju Linux-poster sparades och API-återlästes. *encode* återges konsekvent som **koda**, inte *koda om*, i intervall-, kapitel-, förhandsgransknings- och ljudspårsinställningar. Hjälptexten om minimerad fördröjning rättades också grammatiskt och förenklades till **direktsändningar**, utan ändrade platshållare eller radbrytningar.


### Fortsatt kontroll – svensk satsstil

Tio Linux-poster sparades och återlästes via API: kommatecken före bisats togs bort, **skall** moderniserades till **ska**, och hjälptexter om bildfrekvens, undertextval, ljudgenomströmning, kö och dubblettmål blev mer idiomatiska. Alla radbrytningar och platshållare behölls.


### Fortsatt kontroll – val och kompatibilitet

Fem Linux-poster sparades och API-återlästes: en Decomb/Avflätning-hjälptext återfick **filteralternativen** och korrekt mellanrum, undertextvalet använder nu korrekt **främmande ljud**, och tre kompatibilitetsdialoger har idiomatisk svenska med bevarade kodeknamn.


Korrigering: `Resume Encoding` sparades och API-återlästes som **Återuppta kodningen**. Det sista kvarvarande fallet av *omkodning* i Linux-resursen är därmed åtgärdat.


Korrigering: **Mixdown** uppdaterades från **Nermixning** till **Nedmixning** och API-återlästes. Detta är den etablerade svenska sammansättningen.


Korrigering: **Media Transcoder** uppdaterades från **Mediaomkodare** till **Medieomkodare** och API-återlästes. Omkodning behålls här eftersom *transcoder* specifikt avser omkodning mellan medieformat.


### Fortsatt kontroll – menyer och köpanel

Tio Linux-poster sparades och API-återlästes. Nio menyposter återfick korrekt acceleratorplacering och källans Unicode-ellipsis (`…`); särskilt den felaktiga `A_vsluta` blev **_Avsluta**. Köpanelens sammansättning rättades till **ködetaljpanelen**.


### Fortsatt kontroll – dimensioner och konstant kvalitet

Fem Linux-poster sparades och API-återlästes. **Dimensions** är nu **Dimensioner**, två korta beskrivningar fick svensk satsstil, och två avklippta hjälprutor för konstant kvalitet återställdes till kompletta svenska texter. Den ena behåller källans tvåteckensindrag på fortsättningsrader; den andra behåller ombrutningen utan indrag.


### Fortsatt kontroll – undertextval och ljud

Fem Linux-poster sparades och API-återlästes. **Valbeteende…** följer menyns formatering, beskrivningen gäller åter flera undertextspår, och två hjälptexter hänvisar korrekt till **Valda språk** respektive standardljudspåret. **Nedmixning** ersätter den felaktiga sammansättningen *Nermixning*.
