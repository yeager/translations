# Frigate NVR – radgranskning

Påbörjad 2026-11-15. Granskningen jämför Frigates engelska katalog på
utvecklingsgrenen med den aktuella svenska katalogen som hämtas från Hosted
Weblate. Filerna i Frigates gitgren används som källkontext men inte som
auktoritativ svensk målkatalog, eftersom Weblate ännu inte har synkats tillbaka
till grenen.

## Batch 001

Radgranskade komponenter: `components-icons` (2), `components-input` (2),
`views-recording` (6), `components-auth` (10), `views-configeditor` (10),
`config-groups` (25), `config-validation` (26) och `components-player` (37).

Tre materiella rättningar:

- `views-configeditor`: konsekvent substantivform *Konfigurationsredigerare*
  i dokumenttitel och gränssnittsnamn.
- `config-validation`: *Role header* avser ett HTTP-huvud i proxyns
  `header_map`, inte en vanlig rubrik.

Kontroller före uppladdning: JSON-validering, `l10n-lint`, `git diff --check`
och Gitleaks. `msgfmt` är inte tillämpligt för i18next-JSON.

## Batch 002

Radgranskade komponenter: `components-camera` (50), `views-replay` (46) och
`views-search` (49). Inga ändringar behövdes i kamera- eller reprisvyn.

Två funktionella rättningar i `views-search`: exemplen `cameras:`, `before:`
och `after:` är filterkommandon som användaren ska skriva och får därför inte
översättas. De bekräftades mot Frigates implementation av textfilter.

## Batch 003

Radgranskade komponenter: `views-motionsearch` (66) och `views-chat` (66).
Inga rättningar behövdes. Svenska målkatalogen hämtades från Hosted Weblate och
jämfördes rad för rad med den engelska källkatalogen på Frigates aktuella
utvecklingsgren.

## Batch 004

Radgranskad komponent: `views-events` (68). Två rättningar behövdes:

- `Events` är en fliketikett i plural och ska vara *Händelser*, inte
  *Händelse*.
- Sidtiteln `Review` betecknar funktionen, inte en uppmaning. Därför används
  substantivet *Granskning - Frigate*.

## Batch 005

Radgranskad komponent: `views-facelibrary` (64). Tre rättningar behövdes:

- Den korta fliketiketten `Recent` var felaktigt *Ny* och är nu *Senaste*.
- Åtgärden för det valda ansiktet får den idiomatiska formuleringen *Byt namn
  på ansiktet*.
- Framgångsmeddelandet uttrycker nu resultatet, *Ansiktet har fått namnet
  {{name}}*, i stället för den missvisande reflexiva formuleringen att
  ansiktet självt bytt namn.

## Batch 006

Radgranskad komponent: `components-filter` (74). Två rättningar behövdes:

- `Filter` används som flik, knappetikett och rubrik. Svenskan ska därför vara
  substantivet *Filter*, inte uppmaningen *Filtrera*.
- Filtergruppen för ögonblicksbild och videoklipp avser egenskaper och heter
  därför *Egenskaper*, inte det otydliga *Detaljer*.

## Batch 007

Radgranskad komponent: `components-dialog` (128). Tre rättningar behövdes:

- Platsmarkören för granskningsexport behåller bindestrecket från källtexten;
  em dash används inte när källtexten saknar det.
- *Restreaming* normaliseras till *återströmning* enligt Frigates ordlista.
- *Live view* normaliseras till *livevy* i kontexten för go2rtc-inställningar.

## Batch 008

Radgranskad komponent: `views-exports` (87). Två rättningar behövdes:

- Tomstatusen är nu den kompletta meningen *Inga exporter hittades*.
- Eftersom *ärende* är ett neutrum är datumetiketten *Skapat {{value}}*, inte
  *Skapad {{value}}*.

## Batch 009

Radgranskad komponent: `objects` (129). Inga ändringar behövdes. Etiketterna
följer vedertagna svenska namn för objektigenkänning; varumärken och
transportörnamn behålls oförändrade.

## Batch 010

Radgranskad komponent: `common` (273). Åtta rättningar behövdes: sex
dataenheter bevarar byte (`B`) i stället för den felaktiga bit-omvandlingen
(`bit`), och två texter använder nu de etablerade termerna
*granskningsobjekt* respektive *urklipp*.

## Batch 011

Radgranskad komponent: `views-live` (130). Tre rättningar behövdes:

- Kamerans dokumenttitel behåller källans bindestreck.
- *Live view* använder den fastställda termen *livevy*.
- Tomläget beskriver korrekt att inga kameror, inte en enda kamera, är
  konfigurerade.

## Batch 012

Radgranskad komponent: `views-classificationmodel` (148). Fem rättningar
behövdes: korrekta statusformer för pågående generering, *Senaste
klassificeringar* i stället för den felaktiga betydelsen ”nyligen tillagda”,
korrekt resultattext vid namnbyte och en omskriven informationstext som nu
återger källans betydelse.

## Batch 013

Radgranskad komponent: `views-explore` (147). Två rättningar behövdes:

- *Högsta poäng* ersätter den felaktiga sammansättningen med tre p.
- Raderingsvarningen bevarar den avsiktliga betoningen `INTE` i markupen.

## Batch 014

Radgranskad komponent: `views-system` (282). Tre rättningar behövdes:

- Två texter om nyckelrutors intervall har nu korrekt svensk satsstruktur.
- Diagrametiketten för bildrutor och detekteringar följer källans mellanrum
  kring snedstrecket.

## Batch 015

Första läspasset av `views-settings`: 100 av 1 434 strängar. Två rättningar
behövdes: *Objects* normaliseras till *Objekt* och produktnamnet *Birdseye*
behålls oförändrat.

## Batch 016

Andra läspasset av `views-settings`: 100 ytterligare strängar. Ett materiellt
fel rättades: `Motion tuner` betecknar inställningsverktyget
*Rörelsejustering*, inte en mottagare.

## Batch 017

Tredje läspasset av `views-settings`: 100 ytterligare strängar. Tre rättningar
behövdes: båda valfria fälten använder *Valfritt*, och RTSP-valideringen
bevarar både `rtsp://` och `rtsps://` från källtexten.
