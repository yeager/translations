# Blender UI: QA-baslinje 7 november 2026

Katalogen `blender-ui-sv-weblate-complete-reviewed.po` analyserades lokalt med
`l10n-lint --language sv`. Resultatet var 0 fel, 218 varningar och 814
informationsposter.

## Tolkning

Kontrollen är ett urvalsstöd, inte ett automatiskt korrektur. Den stora mängden
informationsposter innehåller avsiktligt oförändrade produktnamn, kameramodeller,
färgrymdsprofiler, codec-namn, formatnamn, URI:er och API-identifierare, till
exempel ACES, Arri Alexa, Blackmagic, RED, DVCPRO och HDTV.

Prioritera i fortsatt radgranskning:

1. 14 typo-träffar och 4 träffar för dubblerade ord.
2. 1 false-friend-träff och 4 konsistensträffar.
3. Teckensättningsvarningar först när strängen är synlig för användaren eller
   är en sammanhängande hjälptext. Många av de 159 slutpunktsavvikelserna och
   169 interpunktionsavvikelserna kommer från API-fragment där källtextens
   avsiktliga form ska följas.
4. 114 träffar där käll- och måltext är lika. Kontrollera dem per kontext;
   flera är produkt- eller formatnamn och ska inte översättas.

Kontrollens 84 valutaträffar ska granskas i kontext: `USD` kan vara en
valutaförkortning men också Universal Scene Description, som ska behållas.

## Granskad varningsdisposition

Den här baslinjen bygger på baskatalogen och inte på en sammanslagen katalog
med de senare deltafilerna. Den ska därför inte användas som bevis för att en
träff fortfarande finns i den lokalt granskade versionen. Den 7 november
kontrollerades följande grupper mot den aktuella samlingsfilen för batch
626–667:

- Felstavnings- och false-friend-träffarna för bland annat *actual*,
  *fjärrresursbibliotek*, *klippplan*, *poppupppanel* och *Träfffärg* är
  antingen redan ersatta i senare deltabatcher eller avsiktliga tekniska
  sammansättningar i baskatalogen.
- De 14 versalvarningarna gäller huvudsakligen tidsformat (`AM`, `PM` och
  månadsförkortningar), standardiserade formatnamn (`glTF`) eller tekniska
  identifierare (`i18n`). De är inte svenska versalfel.
- De fyra träffarna för dubblerade ord är legitima: ett algoritmnamn följt av
  dess förklaring, negationen *inte, inte ens*, matematiska uttryck och en
  formatplatshållare.

Fortsatt arbete ska därför börja med en ny, effektiv katalog där aktuella
deltafiler har lagts ovanpå baskatalogen, eller med UI-kontroller som kan
verifieras direkt i Blender Translate.

## Effektiv lokal QA

En effektiv katalog skapades den 7 november genom att lägga de senaste
samlingsdeltana (`287–625` och `626–667`) samt de 20 tidigare importdelarna
ovanpå baskatalogen. `msgfmt --check --check-header` passerade. Den effektiva
katalogen gav 0 fel och 215 varningar i `l10n-lint`; den har 116 träffar med
identisk käll- och måltext, 4 dubbelordsträffar, 5 versalträffar och 187
slutpunktsavvikelser. Den har inga träffar för felstavning eller false friends.

Den effektiva katalogen är ett lokalt QA-underlag, inte en ny importfil: den
innehåller både redan importerade och ännu lokala ändringar. En sådan
sammanslagning får därför aldrig laddas upp som en deltafil.

Efter batch 673 byggdes underlaget om med den aktuella samlingsfilen
626–673. `msgfmt` passerade och `l10n-lint` gav 0 fel, 186 varningar, 114
källtextlika poster och inga träffar för felstavning eller false friends.
Den separata kontrollen för tre lika konsonanter ger sju träffar, men samtliga
är de avsiktliga årmaskerna `åååå` i datumformat och inte ordformer.

`svlang check` kan användas för enskilda svenska strängar, men inte som ett
automatiskt helkatalogmått för denna PO-fil. En körning på den effektiva
katalogen gav 0,0/10 och 3 701 påstådda V2-avvikelser, eftersom verktyget
tolkar PO-format, API-identifierare, platsmarkörer och korta UI-fragment som
löpande text. Exempel som *Blenders tilläggsförråd hittades inte* och
*Cachekatalogen för nedladdning av fjärranslutna resursbibliotek kan inte
ändras* är korrekt svenska trots att de flaggas. Kör därför `svlang` mot
avgränsade kandidatsträngar efter kontextgranskning, och låt inte den globala
naturlighetspoängen styra prioriteringen.

## Genomförd kontroll

- `msgfmt --check --check-header` används för varje deltafil.
- `l10n-lint`, `svlang`, Hunspell-kandidatsökning, diffkontroll och Gitleaks
  körs före arkivering av varje granskad batch.
- Tre lika konsonanter i följd kontrolleras med reguljärt uttryck för varje
  samlingsfil.

## Effektiv kontroll 8 november 2026

Ett nytt tillfälligt QA-underlag byggdes av den lokala Blender UI-exporten med
de senast arkiverade samlingsdeltana 811–956, 957–1 054 och 1 055–1 062
ovanpå baskatalogen. Underlaget innehåller 40 428 översatta poster och är
endast ett granskningsunderlag; det får inte laddas upp som en deltafil.

`msgfmt --check` gav endast de förväntade headernotiserna från sammanslagna
deltafiler. `l10n-lint` gav 0 fel och 27 varningar. De varningar som
kontrollerades manuellt i detta pass är inte ändringskandidater: intervall- och
datumformat är standardiserade formatvärden, `glTF` har sin projektspecifika
stavning, tekniska platshållare ska bevaras och den svenska formen `t.ex.`
behöver inte källtextens engelska kolon. Fortsätt därför prioritera konkreta
terminologiska och idiomatiska avvikelser framför dessa generella signaler.
