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

## Batch 018

Fjärde läspasset av `views-settings`: 100 ytterligare strängar.
Inga rättningar behövdes. Protokoll, produktnamn och tekniska termer i
kameraassistenten är korrekta och bevarar källans funktion.

## Batch 019

Femte läspasset av `views-settings`: 100 ytterligare strängar. Två rättningar
behövdes: rubriken beskriver nu *Kamerastatus och detaljer*, och *friendly
name* använder den redan etablerade termen *visningsnamn*.

## Batch 020

Sjätte läspasset av `views-settings`: 100 ytterligare strängar. Tre
granskningstermer rättades så att de konsekvent avser *granskning* och
*granskningsobjekt*.

## Batch 021

Sjunde läspasset av `views-settings`: 100 ytterligare strängar. Två
förekomster av *friendly name* normaliserades till *visningsnamn*.

## Batch 022

Åttonde läspasset av `views-settings`: 100 ytterligare strängar. Tre
rättningar behövdes: två åtgärder återställer lösenord, och poängtermen i
felsökningen är nu konsekvent.

## Batch 023

Nionde läspasset av `views-settings`: sträng 801–900 av 1 434. Åtta rättningar
behövdes: den lagrade systemrollen `viewer` bevaras exakt, formuleringarna för
rollens kameror och omstart är idiomatiska, och tekniska uttryck för säker
webbkontext, API-nyckel och inläsningsfel är korrigerade.

## Batch 024

Tionde läspasset av `views-settings`: sträng 901–1 000 av 1 434. Sex
rättningar behövdes: utlösarnas beskrivningar har korrekt handlingsriktning,
konsekvent imperativform och idiomatisk svenska. Mediesynkroniseringen
beskriver nu korrekt överblivna filer utan databasreferens.

## Batch 025

Elfte läspasset av `views-settings`: sträng 1 001–1 100 av 1 434. Elva
rättningar behövdes. Medietyper, integrationer, registreringsskyltar,
svensk typografi, strömordning och ärvda FFmpeg-inställningar är nu
terminologiskt och grammatiskt konsekventa.

## Batch 026

Tolfte läspasset av `views-settings`: sträng 1 101–1 200 av 1 434. Två
rättningar behövdes: snedstreckstypografin följer svensk UI-praxis och
GenAI-rollen använder den etablerade termen *inbäddning*.

## Batch 027

Trettonde läspasset av `views-settings`: sträng 1 201–1 300 av 1 434. Fjorton
rättningar behövdes. Profilnamn, återställning, synkroniseringsstatus och
återströmning är nu idiomatiska; interna konfigurationsvärden bevaras.

## Batch 028

Fjortonde och sista läspasset av `views-settings`: sträng 1 301–1 434 av
1 434. Sju rättningar behövdes. Bildruteannoteringar, modellresurser,
konfigurationsvärdet `recordings`, zoninställningar och
detekteringsmaskinvara återger nu korrekt funktion och terminologi.

## Batch 029

Hela `audio` har granskats rad för rad: 500 av 500 etiketter. Åtta rättningar
behövdes för faktiska sakfel i ljudklassernas svenska benämningar, bland annat
kattjämmer, valars läten, stråksektion, elhissar och summer.

## Batch 030

Första läspasset av `config/cameras`: sträng 1–80 av 522. Sju rättningar
behövdes. Produktnamnet *Birdseye* bevaras, och ljudtranskribering samt
ansiktsdetektering återger nu källans skilda funktioner.

## Batch 031

Andra läspasset av `config/cameras`: sträng 81–160 av 522. Elva rättningar
behövdes. Återströmning, omkodning, registreringsskyltigenkänning och
rörelsetrösklarnas faktiska beteende motsvarar nu aktuell källtext.

## Batch 032

Tredje läspasset av `config/cameras`: sträng 161–340 av 522. Nio rättningar
behövdes för interna MQTT- och lagringsvärden, visningsnamn, GenAI-instruktioner,
bildpublicering och TTL-lägen.

## Batch 033

Fjärde och sista läspasset av `config/cameras`: sträng 341–522 av 522. Nio
rättningar behövdes för ONVIF-protokoll, Frigate-namnet, zonfilter, uppehållstid
och interna statusfält.

## Batch 034

Första läspasset av `config/global`: sträng 1–100 av 775. Tre rättningar
behövdes för sessionsförnyelse, go2rtc-återströmning och TTL-lägen.

## Batch 035

Andra läspasset av `config/global`: sträng 101–300 av 775. Åtta rättningar
behövdes: Birdseye behåller sitt produktnamn, och globala liveinställningar
använder konsekvent *liveuppspelning* och *återströmning*.

## Batch 036

Tredje läspasset av `config/global`: sträng 301–400. Tretton rättningar
behövdes för omkodning, rörelselogik, interna MQTT-värden, ögonblicksbilder
och attributfilter.

## Batch 037

Fjärde läspasset av `config/global`: sträng 401–500. Nio rättningar behövdes
för attributfilter, avgränsningsrutor, konfidens och interna lagringsvärden.
