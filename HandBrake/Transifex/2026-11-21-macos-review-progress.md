# HandBrake – macOS UI: pågående svensk radgranskning

Datum: 2026-11-21  
Plattform: Transifex API  
Resurs: `o:HandBrakeProject:p:mac-ui:r:enxliff`

## Aktuell inventering

Den aktuella svenska XLIFF-exporten innehåller 1 285 trans-units och inga tomma målsegment. Exporten hämtades via Transifex API före granskningen. Synliga tekniska filternamn jämfördes med den redan kontrollerade Linux-resursen och HandBrake-terminologilistan; filformat, kodeker och algoritmnamn lämnades oförändrade där de ska fungera som egennamn.

## Sparade och API-återlästa ändringar

| Fullständig Transifex-resurssträng | Engelska | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- | --- |
| `o:HandBrakeProject:p:mac-ui:r:enxliff:s:27727a36fae59b5260d01ed20d0abd73` | Chroma Smooth | Chroma Smooth | Kromautjämning | Synligt generiskt filternamn, redan etablerat i Linux UI. |
| `o:HandBrakeProject:p:mac-ui:r:enxliff:s:535f806857e989b59118dec6e43ddc35` | Comb Detect | Comb Detect | Comb-identifiering | Synligt generiskt filternamn, konsekvent med Linux UI. |
| `o:HandBrakeProject:p:mac-ui:r:enxliff:s:993aec0efffb6db77f0b96ea16f20175` | Deblock | Deblock | Blockborttagning | Synligt generiskt filternamn, konsekvent med Linux UI. |
| `o:HandBrakeProject:p:mac-ui:r:enxliff:s:725b7fcf22ffb8b8ff01c7ea3b2f4334` | Deinterlace | Deinterlace | Avflätning | Generiskt filternamn; svensk terminologi används i Linux UI. |
| `o:HandBrakeProject:p:mac-ui:r:enxliff:s:81416eb1f1248dbb22687f93b8547b74` | Denoise | Denoise | Brusreducering | Generiskt filternamn; svensk terminologi används i Linux UI. |

Varje ändring skickades via Transifex REST API och lästes tillbaka från sitt `resource_translation`-objekt.

## Verktyg

`l10n-lint --language sv` gav inga anmärkningar för ändringsmängden. Hunspell markerar `Kromautjämning` och `Comb-identifiering` som domänord, men inte som upptäckta stavfel; den manuella jämförelsen mot HandBrakes Linux UI har företräde. `svlang check` gav 10,0/10 och markerade samma två tekniska termer som ovanliga.

## Status

Inventering och de första säkra, synliga filterrättningarna är gjorda. Den semantiska radgranskningen av återstående macOS-strängar fortsätter. Rapporten innebär inte att macOS UI eller HandBrake som helhet är färdiggranskade.

## Fortsatt radgranskning – 2026-11-21

Färsk Transifex-hämtning omfattade 1 281 aktuella macOS-strängar. Nio ändringar sparades och återlästes via API:

| Engelska | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| Passthru Common Metadata | Genomström vanliga metadata | För över vanliga metadata | Begriplig svensk åtgärdsform. |
| Bottom/Top/Left/Right edge cropping amount in pixels (åtta punkt- och icke-punktvarianter) | Beskäring … | Beskärning … | Rätt svenskt ord; enhetlig formulering och bevarad interpunktion. |

l10n-lint med språk=sv gav 0 fel i den samlade aktuella katalogen. Hunspell-sv markerade inte de sparade texterna.


### Fortsatt semantisk kontroll

Sparade och API-återlästa: **Passthru Fallback:** → **Reservkodning vid genomströmning:**; två **Forced Only** → **Endast tvingade**; två längre hjälpposter för *Track Selection Behavior* med korrekta alternativnamn, utan dubbel negation och med bevarade radbrytningar; **Muxing…** → **Muxning…**.


### Fortsatt kontroll – ljudförstärkning

Sex synliga macOS-etiketter med engelska **Gain** sparades som **Förstärkning** och återlästes via Transifex API. Det följer etablerad svensk ljudterminologi och Linux UI:s *Ljudförstärkning* i beskrivande sammanhang.


### Fortsatt kontroll – filter

**Deband** → **Minska bandning** och **Unsharp** → **Oskarp mask** sparades och API-återlästes. Formuleringarna följer redan granskade Windows- och Linux-resurser.


### Fortsatt kontroll – val och förinställningar

Två spårvalsbeskrivningar och en förinställningshjälptext rättades och API-återlästes. **kodarinställningar** ersattes med **kodningsinställningar**, eftersom källan avser inställningar för hela kodningen och inte en specifik kodare.


### Referensmål för fortsatt kontroll

- Tre `Auto`-strängar är Cocoa-bindningsplatshållare (`ibShadowedIsNilPlaceholder`) och inte bekräftat synliga UI-etiketter; de lämnas därför oförändrade.
- Två `Pop Up`-strängar är NSMenuItem-titlar utan tillräcklig användningskontext. Nuvarande **Popupp** är inte ändrad spekulativt.


### Fortsatt kontroll – ljudterminologi

Åtta macOS-poster sparades och API-återlästes: tre hjälpposter med **Gain** → **Ljudförstärkning**, två **Mixdown** → **Nedmixning** och tre DRC-beskrivningar med **Dynamisk omfångskomprimering** samt svensk decimalmarkering `2,5`.


### Fortsatt kontroll – dubbletter i ljudpanelen

Fyra ytterligare macOS-poster sparades och API-återlästes: två **Mixdown** → **Nedmixning**, en Gain-hjälptext → **Ljudförstärkning** och en DRC-beskrivning → **Dynamisk omfångskomprimering** med decimalen `2,5`.


### Fortsatt kontroll – dimensioner

Fyra macOS-etiketter sparades och API-återlästes: två **Pad top** → **Fyll upptill**, **Pad bottom** → **Fyll nedtill** samt **Width (Pillarbox)** → **Bredd (pelarbox)**.


### Fortsatt kontroll – dimensioner och kö

Fyra macOS-poster sparades och API-återlästes: **Beskäring** i stället för felstavade *Beskäring*, **Fyll nedtill**, **Höjd (letterbox)** och **Flytta längst ner**.


### Fortsatt kontroll – menyer

Nio macOS-menyposter sparades och API-återlästes. Åtgärden **Open Source…** använder nu den etablerade termen **Öppna källfil…**, och **HandBrake Website** är **HandBrakes webbplats**. Menyernas ellipser har samtidigt återställts till källans Unicode-tecken (`…`) i stället för tre punkttecken, utan att kortkommandon eller annan formatering ändrades.


### Fortsatt kontroll – kö- och undertextinställningar

Tio poster sparades och API-återlästes. Åtta menyåtgärder återfick källans Unicode-ellipsis (`…`). De två undertextvalen ändrades från den betydelseförskjutande singularformen till **Endast tvingade undertexter**; den förklarande texten följer nu samma pluralform och bevarar citattecken samt källspårsreferens.


### Fortsatt kontroll – undertexter och videokodning

Sex macOS-poster sparades och API-återlästes: två **Valbeteende…** och **Lägg till titlar i kö…** använder källans ellipsis, **OK** följer standardstavningen, `Passthru` är **genomströmning** och **Kodning med flera pass** ersätter det oidiomatiska *flerpass*.


### Fortsatt kontroll – status och förhandsvisning

Sex poster sparades och API-återlästes: **Öppna källfil** följer etablerad källterminologi, **Körtid** ersätter det felaktiga *Speltid* för programkörningen, samt `OK` och två ellipsmenyer normaliserades. I förhandsvisningsmallen ändrades endast svensk versalisering; `%1$f`, `%2$f` och `%3$.0f%%` bevarades exakt.


### Fortsatt kontroll – köstatus och formatmallar

Blocket radgranskades. Enda säkra ändringen var **Starttid:** i stället för den ogrammatiska statusetiketten *Startades:*, och den sparades samt API-återlästes. Formatmallarna med `%@`, `%d`, `%lu`, `%s` och `%f` kontrollerades utan ändring; platshållarordning och antal är bevarade.


### Slutblock i lokal export – filterstatus

Tre poster sparades och API-återlästes: **Flera pass**, **Flera pass med turbo** och **Läser in titel %1$d av %2$d, förhandsvisning %3$d…**. Den lokala macOS-översikten omfattar nu samtliga 1 281 poster radvis, men slutstatus kräver fortfarande färsk API-export och format-/språkvalidering så att ändringar efter ögonblicksbilden upptäcks.
