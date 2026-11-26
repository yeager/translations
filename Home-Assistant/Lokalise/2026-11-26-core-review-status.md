# Home Assistant Core – aktuell granskningsstatus

Senast uppdaterad: 2026-11-26

Aktuell Home Assistant Core-källrevision: c03d786a2335a70d01860cae56286798bb272871

Lokalise-projekt: 130246255a974bd3b5e8a1.51616605

## Aktuellt läge

- Senast behandlade Lokalise-position: **41 536** av 77 540 indexpositioner (cirka 53,5 %); 77 520 poster är aktiva. Nästa position: **41 537**; efter markören återstår 36 060 aktiva positioner. Källrevision: `c03d786a2335a70d01860cae56286798bb272871`.
- De äldre totalsiffrorna har inte omräknats efter nyare batcher och ska inte användas som aktuell kumulativ summering. Den kanoniska HA Core-TMX innehåller nu **29 637** enheter (29 406 poster med Lokalise-ID och 231 historiska poster).
- Fullständiga rader, ändringsförslag, källvägar, referenser och live-ID:n finns i respektive daterade batchrapport; senaste rapport: `2026-11-26-reviewed-core-41417-41536.md` och fullständiga JSON-underlag.
- Batchen 29 131–29 250: 120/120 nycklar aktiva och källmatchande; **17** ändringar sparade och återlästa, **103** texter oförändrade. Nästa batch 29 251–29 370: 85 aktuella Core-nycklar granskade utan ändring och 35 källfrånvarande poster uteslutna. Batchen 29 371–29 490: 54 aktiva Core-nycklar, 2 ändringar, 52 oförändrade; 66 källfrånvarande. Batchen 29 491–29 610: 95 aktiva Core-nycklar, ett OpenAI-referensalias synkat, 94 oförändrade; 25 källfrånvarande. Batchen 30 617–30 736: 104 aktiva Core-nycklar, 31 ändringar och 73 oförändrade; 16 källfrånvarande. Batchen 30 737–30 856: 110 aktuella nycklar, varav två överlappande återverifierades; 33 nya ändringar och 75 oförändrade bland de 108 nya aktiva posterna; 10 källfrånvarande. 31/31 aliasmål matchar live efter synkning. Batchen 30 857–30 976: 115 aktuella nycklar, varav två tidigare granskade återverifierades; 6 ändringar och 107 oförändrade bland 113 nya aktiva poster; 5 källfrånvarande. 24/24 aliasmål matchar. Platshållare 115/115; inga pluraler. Batchen 30 977–31 096: 96 aktuella nycklar, varav 12 tidigare granskade återverifierades; 11 ändringar och 73 oförändrade bland de 84 nya aktiva posterna; 24 källfrånvarande. 23/23 aliasmål matchar. Platshållare 96/96; inga pluraler. Batchen 31 097–31 216: 120/120 aktuella nycklar, sju fanns i tidigare dokumentation; 35 förbättringar sparades och lästes tillbaka, 85 poster verifierades oförändrade. Sex tidigare TM-värden för ZHA-energifaser rättades. Inga alias, pluraler eller platshållaravvikelser. Batchen 31 217–31 336: 110 aktuella nycklar och 10 källfrånvarande; 14 förbättringar sparades och 96 mål verifierades oförändrade. 68/68 alias matchar live; platshållare 110/110; inga pluraler. Batchen 31 337–31 456: 110 aktuella nycklar, varav 14 återverifierade från tidigare rapporter; 41 korrigeringar och 65 oförändrade bland 106 nya aktiva. Tio redan kända historiska nycklar uteslöts. Alla 13 alias matchar live. Två Synology-referensmål korrigerades retroaktivt. Batchen 31 457–31 576: 108 aktuella nycklar, varav sju återverifierades från tidigare rapporter; 14 ändringar och 87 oförändrade bland 101 nya aktiva. Tolv tidigare rapporterade historiska nycklar uteslöts. Alla 17 alias matchar live; platshållare 108/108; inga pluraler.
- Liveverifiering för batchen bekräftade nyckelidentitet, engelsk källtext, svensk måltext och Lokalise-ID för 120/120 poster. Rapporten innehåller fullständiga nycklar och raderna med befintlig/föreslagen text.


### Senaste batch: 33 977–34 096

93 aktiva Core-nycklar och 27 historiska/källfrånvarande poster granskades. 25 mål sparades och lästes tillbaka, samt två NUT-temperaturalias uppdaterades efter ändring av delade mål. 68 aktiva texter verifierades utan ändring. Alla 45 referenser kontrollerades; 37 matchar direkt och åtta Whirlpool-alias följer dokumenterade TM-uppdateringar till framtida källpositioner. Platshållare 93/93, inga pluraler. 25 historiska poster var tidigare dokumenterade. Två exakta källvägar har flyttats och följs upp vid sina nya köpositioner. Rapport: `2026-11-26-reviewed-core-33977-34096.md` med JSON-underlag. Nästa position: **34 097**.

### Senaste batch: 34 097–34 216

102 aktuella Core-nycklar, 18 historiska poster. 29 måltexter sparades och lästes tillbaka; 73 aktiva texter behölls. Alla 27 aliasreferenser matchar, platshållare 102/102 och inga pluraler. 30 tidigare granskade rader återfanns. Åtta Whirlpool-mål plus matchande alias synkades retroaktivt i Lokalise och TMX. `sv-home-assistant-core-lokalise-verified-canonical-2026-11-26.tmx` validerar med 23 010 enheter. Matter EVSE-termer och NUT `Floating` är noterade för protokollkontroll. Se `2026-11-26-reviewed-core-34097-34216.md` och JSON-underlaget. Nästa position: **34 217**.

### Senaste batch: 34 217–34 336

110 aktuella Core-nycklar och 10 källfrånvarande poster radgranskades. 16 ändringar i intervallet sparades och lästes tillbaka, plus ett NUT-referenstarget utanför intervallet; 94 aktiva mål i intervallet verifierades oförändrade. Alla 36 referenser matchar live-mål. Platshållare 110/110; inga pluraler. 14 nycklar återfanns i tidigare rapporter. TMX validerar med 23 118 enheter och varje aktiv manifestpost matchar. Hunspell-sv fick tillägget `ineffekt` i båda ordböckerna och regressionerna; 19/19 tester passerade. Se `2026-11-26-reviewed-core-34217-34336.md` med JSON-underlag. Nästa position: **34 337**.

### Senaste genomförda batcher: 35 297–36 016

Batch 51 (35 297–35 416): se dess daterade rapport och tidigare commit. Batch 52 (35 417–35 536) korrigerades efter att en felaktig key-path-jämförelse använde fel snapshotfält: 108 aktuella nycklar verifierades; 50 översättningar ändrades och sparades, 58 behölls; 12 äldre `advanced_settings`-poster återställdes till sina ursprungliga texter och uteslöts. De aktuella `other_settings`-nycklarna vid positionerna 58 572–58 586 granskades separat (12/12). Korrigeringsrapporten och TM manifesten skiljer nu äldre nycklar från aktiva aktuella nycklar.

Batch 53 (35 537–35 656): 119 aktuella Core-nycklar identifierades; 118 granskades och sparades/lästes tillbaka, varav 56 texter ändrades och 62 behölls. En historisk nyckel (35 652) saknar aktuell källväg. Platshållare 118/118, inga pluraler, 26 referenser matchade live-mål. `svlang skrivregler` utan fel. `is_reviewed` kunde inte ändras: Lokalise gav HTTP 403 även om texten sparades; readback visar flaggan `false`. Osäker Teslemetry BMS-etikett `Weld` (35 620) lämnades oförändrad och kräver källkontroll. Se `2026-11-26-reviewed-core-35537-35656.md` och JSON-underlaget.

Batch 54 (35 657–35 776): 117 aktiva nycklar, 3 äldre inaktuella nycklar. 116 aktiva mål granskades och sparades/lästes tillbaka; 61 korrigeringar och 55 oförändrade. 18/18 referenser matchar live-mål; platshållare 117/117, inga pluraler. Lämnades uppföljning för `Tonneau`-terminologi och hard TPMS-varningar. Se `2026-11-26-reviewed-core-35657-35776.md` med JSON-underlag.

Batch 55 (35 777–35 896): 104 aktuella nycklar och 16 historiska. Alla 104 aktiva sparade/lästes tillbaka; 28 korrigeringar och 76 oförändrade. Alla 41 referenser matchar live-mål efter synkning av två delade Z-Wave S2-mål. Platshållare 104/104; inga pluraler. Se `2026-11-26-reviewed-core-35777-35896.md` och JSON-underlaget.

Batch 56 (35 897–36 016): 87 aktiva nycklar och 33 historiska. Alla 87 aktiva sparade/lästes tillbaka; 35 korrigeringar och 52 oförändrade. Alla 15 referenser matchar; fem delade mål (binärsensor, SmartThings och AWS S3) rättades retroaktivt. Platshållare 87/87; inga pluraler. Mieles torksteg kontrollerades mot svensk Miele-dokumentation. Se `2026-11-26-reviewed-core-35897-36016.md` och JSON-underlaget.

Batch 57 (36 017–36 136): 89 aktiva och 31 historiska; 30 korrigeringar sparade/lästa tillbaka och 59 oförändrade. 10/10 referenser, platshållare 89/89, inga pluraler. Recorder-gruppen återkontrollerades mot rapporten från 19 november. Se `2026-11-26-reviewed-core-36017-36136.md` och JSON-underlaget.

Batch 58 (36 137–36 256): 105 aktiva nycklar och 15 historiska. 63 aktiva strängar matchade tidigare fullnyckelgranskningar, 42 granskades som nya/ej tidigare rapporterade. Sex förbättringar sparades/lästes tillbaka, 99 mål behölls. 25/25 referenser och platshållare 105/105; inga pluraler. Se `2026-11-26-reviewed-core-36137-36256.md` och JSON-underlaget.

Batch 59 (36 257–36 376): 114 aktiva och 6 historiska poster; alla aktiva hade tidigare fullnyckeldokumentation. En tidigare osparad rättelse om HTML-radbrytningar och versaler sparades/lästes tillbaka; övriga 113 mål behölls. 34/34 referenser och platshållare 114/114. Se `2026-11-26-reviewed-core-36257-36376.md` och JSON-underlaget.

Batch 60 (36 377–36 496): 107 aktiva nycklar, alla tidigare rapporterade, samt 13 källfrånvarande historiska. Nio tidigare MQTT-förslag saknades i Lokalise och sparades/lästes tillbaka; 98 mål behölls. Alla 17 referenser matchar, platshållare 107/107, HTML-radbrytningar bevarade. Se `2026-11-26-reviewed-core-36377-36496.md` och JSON-underlaget.

Batch 61 (36 497–36 616): 115 aktiva nycklar, alla tidigare dokumenterade, samt 5 historiska. Ett osparat Android TV Remote-förslag sparades/lästes tillbaka; övriga 114 mål behölls. Alla 31 referenser och 115/115 platshållare matchar. Se `2026-11-26-reviewed-core-36497-36616.md` och JSON-underlaget.

Batch 62 (36 617–36 736): 100 tidigare granskade aktiva mål återverifierades, utan nya textändringar. 20 historiska nycklar uteslöts. 1/1 referens och platshållare 100/100 matchar. Samtliga 100 aktuella poster synkades till kanonisk TMX. Se `2026-11-26-reviewed-core-36617-36736.md` och JSON-underlaget.

Batch 52-rättelsen samt batcher 53–65 är införda i kanonisk TMX. Validering efter batch 65: **25 572** poster, 25 341 med Lokalise-ID och 231 historiska. Backupen i `translations` är byte-identisk med TM-repot. Nästa Lokalise-position: **37 097**.

### Senaste batch: 36 737–36 856

113 aktiva Core-nycklar granskades mot aktuell källrevision; sju källfrånvarande historiska nycklar uteslöts. 106 källor matchade direkt och sju referensmål löstes och verifierades. 24 översättningar i batchen korrigerades och sparades/lästes tillbaka; 89 aktiva mål behölls efter granskning. Ytterligare 15 UniFi Protect-switch-alias synkades retroaktivt med ändrade mål (totalt 39 Lokalise-ändringar). Alla referenser verifierades; platshållare 113/113, inga pluraler. Fullständigt underlag och ändringsmotiv finns i `2026-11-26-reviewed-core-36737-36856.md` och JSON. TM-manifestet innehåller 128 poster inklusive retroaktiva alias och liveverifieras före TMX-synk. Nästa position: **36 857**.

### Senaste batch: 36 857–36 976

114 aktiva Core-nycklar radgranskades: 57 direkta källmatchningar och 57 referensnycklar mot 44 unika mål. Samtliga alias källtexter och svenska mål matchade live; 6 källfrånvarande poster uteslöts. 14 översättningar i intervallet ändrades och lästes tillbaka; 100 aktiva mål behölls. En tidigare rapporterad systemarkitekturtext i position 37 090 korrigerades också retroaktivt. Totalt 15 strängar sparades. Platshållare 114/114, inga pluraler. Alla 115 manifestposter verifierades live. Kanonisk TMX validerar med 25 467 poster (25 236 Lokalise-ID, 231 historiska). Se `2026-11-26-reviewed-core-36857-36976.md` och JSON. Tre UniFi Protect-termer står kvar som markerad uppföljning. Nästa position: **36 977**.

### Senaste batch: 36 977–37 096

110 aktiva Core-nycklar radgranskades: 52 direkta källmatchningar och 58 referensnycklar mot 11 unika mål. Alla 58 referenser matchar live-källtext och svenska mål; 10 historiska poster uteslöts. Elva översättningar i intervallet korrigerades och lästes tillbaka; 99 mål behölls. En Squeezebox-sträng från föregående block rättades retroaktivt; position 37 090 återverifierades. Totalt 12 sparade ändringar. Alla 111 manifestposter liveverifierades. Platshållare 110/110, inga pluraler. Kanonisk TMX validerar med 25 572 poster (25 341 Lokalise-ID, 231 historiska). Se `2026-11-26-reviewed-core-36977-37096.md` och JSON. Nästa position: **37 097**.


### Senaste batch: 40 217–40 336

120 positioner granskades rad för rad: 112 aktiva Core-nycklar och 8 poster utan aktuell källsträng. De åtta äldre posterna matchar exakt den arkiverade Lokalise-snapshoten från 2026-11-24 och ingår inte i aktuell TM. 18 korrigeringar sparades i Lokalise och lästes tillbaka; 94 aktiva översättningar behölls. Nio referensnycklar löstes mot åtta mål, alla med matchande engelsk källtext och svenskt mål. Alla 112 aktiva poster verifierades via API och skrevs till TM; TMX validerar med 28 629 enheter och translations-spegeln är byteidentisk. `svlang skrivregler`: inga fel. Hunspell regressioner 19/19; ordlistan kompletterad med fem KNX/IMEON-ord. Swedish-foss-terminology har två nya spårbara kontexttermer och 22 Home Assistant-termer. Markerad uppföljning: kontrollera visningen av `Scheduled every` och `Expire after last value update` i KNX-panelen. Se `2026-11-26-reviewed-core-40217-40336.md`. Nästa position: **40 337**.


### Senaste batch: 40 337–40 456

120 positioner granskades rad för rad: 84 aktiva Core-nycklar och 36 poster utan aktuell källtext. De 36 äldre posterna matchar exakt Lokalise-snapshoten från 2026-11-24 och uteslöts ur aktuell TM. 22 ändringar sparades i Lokalise och lästes tillbaka; 62 aktiva texter behölls. Samtliga 25 referenser löstes mot 21 mål och matchar live. 48 nycklar fanns i tidigare dokumentation och återkontrollerades mot aktuell källtext och Lokalise. Alla 84 aktiva TM-poster verifierades via API; TMX validerar med 28 713 enheter och translations-spegeln är byteidentisk. Hunspell och termbank uppdaterades med verifierade KNX-termer; testsviterna passerade 19/19 respektive 20/20. `svlang skrivregler`: inga fel. Nästa position: **40 457**. Rapport: `2026-11-26-reviewed-core-40337-40456.md`.


### Senaste batch: 40 457–40 576

120 positioner granskades rad för rad: 108 aktiva Core-nycklar och 12 poster utan aktuell källtext. De 12 äldre posterna matchar exakt 2026-11-24-snapshoten och uteslöts ur aktuell TM. 19 aktiva strängar ändrades och lästes tillbaka; 89 aktiva mål verifierades oförändrade. Alla 58 referenser matchade live. En separat retroaktiv rättelse ändrade den gemensamma `Release URL`-översättningen till `Versions-URL`, uppdaterade dess TM-post och synkade de två nuvarande aliasen. Totalt 109 TM-manifestposter verifierades via API. TMX validerar med 28 815 enheter; translations-spegeln är byteidentisk. `svlang`: inga skrivfel. Hunspell 19/19; termbank 20/20. Verktygen fick Bayesiansk/KNX-termer. Nästa position: **40 577**. Se `2026-11-26-reviewed-core-40457-40576.md` och `2026-11-26-release-url-term-correction.md`.

## TM och verktyg

- Home Assistant Core kanonisk TMX validerar nu med **28 815** enheter: 28 584 med Lokalise-ID och 231 historiska poster utan Lokalise-ID. Batch 65:s 110 aktiva Core-mål och en retroaktiv Squeezebox-rättelse finns i minnet; korrigerade poster skrevs över efter live-readback. Backupen i translations-repot är byte-identisk. Kanonisk TMX och identisk backup finns i `translations/Home-Assistant/Lokalise/sv-home-assistant-core-lokalise-verified-canonical-2026-11-26.tmx` och `tools/swedish-tm/Home-Assistant/sv-home-assistant-core-lokalise-verified-canonical-2026-11-26.tmx`.
- Rapporter och manifest: `2026-11-25-reviewed-core-29131-29250.md` och `2026-11-25-reviewed-core-29251-29370.md`, med respektive JSON-underlag. Den äldre rapportens missade KNX-förslag för `component::knx::config_panel::dpt::options::14_004` följdes upp via fullständig nyckel och sparades som `Substansmängd`; TM-posten uppdaterades retroaktivt.
- KNX-terminologi jämfördes mot KNX Associations System Specifications. Hunspell-sv:s båda ordböcker fick stöd för `ASCII`, `Deltatid`, `Kompressibilitet`, `Magnetomotorisk`, `deltavolym`, `usb-dongel` och `Turboläge`. Philips svensk dokumentation belägger `deltavolym` och `Turboläge`; `usb-dongel` är användargodkänd. Regressionstesterna passerade **19/19**; ingen extra release gjordes.
- `svlang skrivregler` fann inga skrivregelavvikelser i någon av de två senaste batcherna. I 29251–29370 rapporterade svlang en falskt positiv V2-varning för bisatsen “när ... passerar”. Hunspell flaggade bara fragmenten `daily`, `hourly` och `link` inuti dokumentationsplatshållare; de är inte svensk måltext.
- Termbanken swedish-foss-terminology användes som stöd: dess befintliga svenska TM innehåller bland annat “deltatider” och “rörelsemängdsmoment”.

## Senaste batch: 31 697–31 816

120/120 strängar matchade Home Assistant Core-källrevisionen och ingen fullständig nyckel förekom i tidigare rapporter. 56 ändringar sparades och lästes tillbaka; 64 översättningar verifierades oförändrade. Alla 120 manifestposter liveverifierades mot Lokalise. Platshållare 120/120; inga pluraler eller referenser. TMX validerar med 20 991 enheter. Home Connects officiella programdokumentation verifierade bland annat ugnsjäsning, luftfuktighet och diskmaskinsprogram. 16 enheter fick korrekt gradtecken. svlang-test 16/16, Hunspell-sv 19/19. Se `2026-11-25-reviewed-core-31697-31816.md` och JSON-underlagen.

## Senaste batch: 31 817–31 936

94/120 poster har aktiv Core-källtext; 26 källfrånvarande poster återfanns i tidigare dokumentation. 37 mål korrigerades och lästes tillbaka; 57 verifierades oförändrade, och ett tidigare aktivt granskat mål återverifierades. Nio aliasreferenser matchar sina live-mål. Platshållare 94/94, inga pluraler. Alla 94 manifestposter verifieras via Lokalise API. TMX validerar med 21 084 enheter. svlang har noll träffar; Hunspell-sv:s 19 tester passerar. Home Connects API-dokumentation kontrollerade bland annat relativa start-/sluttider, kaffebryggning, vatten/kaffekontakttid och diskprogram. Se `2026-11-25-reviewed-core-31817-31936.md` och JSON-underlagen.

### Senaste batch: 36 017–36 136

89 aktiva nycklar granskades, 30 korrigerades och lästes tillbaka från Lokalise, 59 behölls. 31 källfrånvarande historiska poster uteslöts från TM. Alla 10 aktiva referenser matchar sina live-mål; platshållare 89/89. svlang skrivregler passerade. Recorder-gruppen var tidigare granskad och återkontrollerades mot aktuell källa. Se `2026-11-26-reviewed-core-36017-36136.md` och JSON-underlaget. Nästa position: **36 737**.

- Källuppdatering: Core-checkouten flyttades till `c03d786a2335a70d01860cae56286798bb272871`. Aktiva källsträngar i positionerna 35 417–36 496 jämfördes igen; inga ändringar upptäcktes. Lokalise-kön uppdaterades från 77 528 till 77 540 nycklar. Tolv nytillagda nycklar (`geniushub` och två MQTT-klientcertifikatsträngar) ligger sist, vid positionerna 77 529–77 540, och återstår att granska när kön nås.

## Kvarstående hinder

- Lokalise API-tokenen saknar behörighet att sätta `is_reviewed` (tidigare HTTP 403). Textändringar kan sparas och verifieras. Ingen separat Reviewed-markering har därför kunnat sättas.
- Inventeringen 2026-11-25 fann **203 aktuella Core-källnycklar som saknas helt i Lokalise**. Skapande/import av nycklar avslogs tidigare med HTTP 403; se `2026-11-25-full-core-missing-audit.md`.
- Totalt **685** källfrånvarande/historiska nycklar är exkluderade från aktuell Core-täckning. Tio flyttade nycklar från det senaste blocket har aktuella mål senare i Lokalise-ordningen och är markerade för granskning vid respektive position.
- Granskningen är **inte klar**. Fortsätt från position **37 097**; kontrollera källvägar, nya strängar, tidigare rapporter, referenser och hela Core-inventeringen.

## Äldre batch: 31 457–31 576

108/108 aktuella poster matchar Core-källan. Bland 101 nya aktiva nycklar korrigerades 14 och 87 verifierades oförändrade; sju tidigare granskade aktiva nycklar återverifierades. Tolv tidigare rapporterade nycklar saknar aktiv källväg och uteslöts. Alla 17 alias matchar live. Kanonisk TMX validerar med 20 760 enheter. Se `2026-11-25-reviewed-core-31457-31576.md` och JSON-underlagen.

## Föregående batch: 30 977–31 096

104/120 nycklar matchar Core-källrevision `86a2eabe7e43f526db5821ef068087ce8404ae07`; 31 mål korrigerades, sparades och återlästes, 73 verifierades utan ändring. 16 källfrånvarande poster uteslöts ur Core-TM. 33 referensalias matchar live-målen efter synkning. Platshållare 104/104; inga pluralnycklar. Retroaktiv PoolDose-terminologi synkades på fem ytterligare nycklar. Kanonisk TMX validerar med 20 027 enheter. Se `2026-11-25-reviewed-core-30617-30736.md` och JSON-underlagen. Nästa position: **30 857**.

## Senaste batch: 30 737–30 856

110/120 poster matchade aktuell Core-källa; två hade redan granskats. Bland 108 nya aktiva strängar korrigerades 33 och 75 verifierades oförändrade; 10 källfrånvarande poster uteslöts. Alla 31 aliasreferenser matchar sina live-mål. Två KNX-referensmål synkades retroaktivt. Kanonisk TMX validerar med 20 132 enheter. Se `2026-11-25-reviewed-core-30737-30856.md` och JSON-underlagen.

## Senaste batch: 30 857–30 976

115/120 poster matchade aktuell Core-källa; två av de 115 hade redan granskats och återverifierades. Av 113 nya aktiva strängar korrigerades 6 och 107 verifierades oförändrade; 5 källfrånvarande poster uteslöts. Alla 24 aliasreferenser upplöstes mot aktuell Core-källa och liveöversättningar i Lokalise och matchade. Platshållare 115/115; inga pluralnycklar. Ohmes `Måltid` ändrades till `Önskad sluttid` efter kontroll av Ohmes eget uttryck ”ready by”. TM-manifestet lägger till 113 nya nycklar och återverifierar två befintliga; kanonisk TMX validerar med 20 245 enheter. `svlang skrivregler` fann inga fel. Nästa position: **30 977**. Se `2026-11-25-reviewed-core-30857-30976.md` och JSON-underlagen.

## Återverifierat överlapp: 29 611–30 616

Livekontroll av 1 006 tidigare dokumenterade fullständiga nycklar: 742 matchar aktuell Core-källrevision och deras aktuella Lokalise-texter stämmer med sparad TM; 264 är källfrånvarande. Ingen källdrift eller textskillnad hittades. Inget nytt översättningsarbete räknas. Se `2026-11-25-revalidated-overlap-core-29611-30616.md` och JSON-underlaget. Nästa nyckel utan tidigare fullnyckelrapport: **30 617**.

## Näst senaste batch: 29 251–29 370

85/120 poster matchar aktuell Core-källrevision `86a2eabe7e43f526db5821ef068087ce8404ae07`; samtliga 85 översättningar granskades, varav 31 alias jämfördes med 21 live-mål, 31/31 matchade. 35 Lokalise-poster saknar aktiv källa i den aktuella Core-checkouten och har inte räknats in i aktuell täckning eller TM. Live-manifest verifierat 85/85. Ingen översättning ändrades. Inga pluraler eller platshållaravvikelser. Fullständiga rader finns i `2026-11-25-reviewed-core-29251-29370.md` och JSON-underlag.

## Senaste batch: 29 131–29 250

120/120 aktuella Core-nycklar matchar revision `86a2eabe7e43f526db5821ef068087ce8404ae07`. 17 ändringar sparades och återlästes, 103 texter behölls. Referensalias: 0; pluralnycklar: 0; platshållaravvikelser: 0. Live-manifest verifierat 120/120. Kanonisk TMX validerar med 19 921 enheter. KNX-termerna inkluderar korrigeringar för deltatid, generiska signerade/osignerade heltal, värmeledningsförmåga, mekanisk spänning, rymdvinkel, rörelsemängd, massflöde, elektromotorisk spänning, elektrisk konduktivitet och rörelsemängdsmoment. Se `2026-11-25-reviewed-core-29131-29250.md` och dess JSON-underlag. Nästa position: **29 371**.

---

## Fortsatt radgranskning 2026-11-25 – position 27811–28020

Tre tidigare rapporter hade redan radgranskat intervallet och innehöll osparade förslag. Samtliga 210 positioner jämfördes mot aktuell Core-revision; 107 matchar aktuell källa och 103 är historiska källfrånvarande poster. Femton giltiga måltextförslag sparades och lästes tillbaka via Lokalise API; 92 befintliga aktuella mål verifierades utan språkändring. 29 referensalias jämfördes live med sina mål och samtliga matchar. Sex gamla `condition_behavior::options::any`-förslag saknar aktuell Core-nyckel och har hållits utanför TM. TMX-manifestets samtliga 107 nyckelidentiteter, engelska källor och svenska mål verifierades live med Lokalise API. Rapport och manifest: `2026-11-25-reviewed-core-27811-28020.md`, `2026-11-25-reviewed-core-27811-28020-changes.json`, `2026-11-25-reviewed-core-27811-28020-references.json` och `2026-11-25-reviewed-core-27811-28020-tm.json`.

## Fortsatt radgranskning 2026-11-25 – position 28021–28050

Den aktuella Lokalise-ordningen gav 30 nyckelposter efter position 28020. 29 matchar Core-källrevision `86a2eabe7e43f526db5821ef068087ce8404ae07`; 10 svenska mål ändrades och lästes tillbaka, 19 verifierades oförändrade. En äldre Ondilo-nyckel finns inte längre i Core-källan och uteslöts. Sexton referensalias matchar live-målen. Verktygsstödet kompletterades med `Inverter` → `växelriktare` i HA-terminologin samt `växelriktarström` och WaterFurnace-former i Hunspell-sv. TMX-manifestet för 29 aktuella poster verifierades live. Se `2026-11-25-reviewed-core-28021-28050.md` med JSON-underlag.


### Senaste batch: 33 977–34 096

93 aktiva Core-nycklar och 27 historiska/källfrånvarande poster granskades. 25 mål sparades och lästes tillbaka, samt två NUT-temperaturalias uppdaterades efter ändring av delade mål. 68 aktiva texter verifierades utan ändring. Alla 45 referenser kontrollerades; 37 matchar direkt och åtta Whirlpool-alias följer dokumenterade TM-uppdateringar till framtida källpositioner. Platshållare 93/93, inga pluraler. 25 historiska poster var tidigare dokumenterade. Två exakta källvägar har flyttats och följs upp vid sina nya köpositioner. Rapport: `2026-11-26-reviewed-core-33977-34096.md` med JSON-underlag. Nästa position: **34 097**.

### Senaste batch: 34 097–34 216

102 aktuella Core-nycklar, 18 historiska poster. 29 måltexter sparades och lästes tillbaka; 73 aktiva texter behölls. Alla 27 aliasreferenser matchar, platshållare 102/102 och inga pluraler. 30 tidigare granskade rader återfanns. Åtta Whirlpool-mål plus matchande alias synkades retroaktivt i Lokalise och TMX. `sv-home-assistant-core-lokalise-verified-canonical-2026-11-26.tmx` validerar med 23 010 enheter. Matter EVSE-termer och NUT `Floating` är noterade för protokollkontroll. Se `2026-11-26-reviewed-core-34097-34216.md` och JSON-underlaget. Nästa position: **34 217**.

### Senaste batch: 34 217–34 336

110 aktuella Core-nycklar och 10 källfrånvarande poster radgranskades. 16 ändringar i intervallet sparades och lästes tillbaka, plus ett NUT-referenstarget utanför intervallet; 94 aktiva mål i intervallet verifierades oförändrade. Alla 36 referenser matchar live-mål. Platshållare 110/110; inga pluraler. 14 nycklar återfanns i tidigare rapporter. TMX validerar med 23 118 enheter och varje aktiv manifestpost matchar. Hunspell-sv fick tillägget `ineffekt` i båda ordböckerna och regressionerna; 19/19 tester passerade. Se `2026-11-26-reviewed-core-34217-34336.md` med JSON-underlag. Nästa position: **34 337**.

## TM och verktyg

- Home Assistant Core-kanonisk TMX är uppdaterad till position 29130, retroaktiva LG ThinQ-, OpenEVSE-, Open Router- och Fressnapf-referensmål. XML/proveniensvalideraren godkände **19 800** enheter; 19 569 har Lokalise-ID och 231 är historiska poster utan sådant ID. Varje batchpost anger nu också den exakta Core-källrevisionen i verifieringsproveniensen.
- swedish-foss-terminology innehåller åtta projektspecifika HA-termer för OpenEVSE, ViCare, USB-dongel, Tibbers hushållsnod, Matter-temperaturavvikelse, Yardians tryckslag, HDFurys hotplug-knapp och KNX-termen datapunkttyp. Exporterna CSV/TBX/JSONL validerades; termbankens 20 tester passerade. Tibber-tolkningen är markerad som källbaserad slutsats med uppföljning.
- Hunspell-sv innehåller HA-termerna och hårdvaruidentifierarna från granskningen, däribland Tibber, OpenAI, Proxmox, SMA, Namecheap, HDFury, `upptäckbar`, `inomhusluftkvalitet`, `skåptorrt`, `stryktorrt`, `XL-kaffe`, `nattdisk`, `försköljning`, `kaffemaskinprogram` och `spoltryck`. Ordboksräknarna och stavningskontrollen verifierades. Deklarerade poster kontrollerades. Hunspell-sv validerades och släpptes som `v2026.11.25`; PyPI-publiceringen lyckades. swedish-foss-terminology-exporter validerades och uppdaterades.
- svlang skrivregler fann inga skrivregelavvikelser i senaste batcherna; en regressionstestad regel flaggar felaktigt ordningstecken (º) i temperaturvärden. Platshållarkontrollen fann 0 avvikelser av 120 i senaste batchen.

- Källuppdatering: Core-checkouten flyttades till `c03d786a2335a70d01860cae56286798bb272871`. Aktiva källsträngar i positionerna 35 417–36 496 jämfördes igen; inga ändringar upptäcktes. Lokalise-kön uppdaterades från 77 528 till 77 540 nycklar. Tolv nytillagda nycklar (`geniushub` och två MQTT-klientcertifikatsträngar) ligger sist, vid positionerna 77 529–77 540, och återstår att granska när kön nås.

## Kvarstående hinder och uppföljning

- Lokalise API-tokenen får ändra översättningstexter men får HTTP 403 (No permission to update translation status) för att sätta is_reviewed. Ingen browser är tillgänglig i den här chatten. Därför har ändrade mål sparats, men Lokalises separata Reviewed-markering kunde inte sättas.
- Den fullständiga Core-inventeringen från 2026-11-25 fann **203 aktuella Core-källnycklar som saknas helt i Lokalise**. API-anropen för att skapa nycklar/importera fil avslogs med HTTP 403; den listan finns i 2026-11-25-full-core-missing-audit.md. Detta blockerar 100 % lokaliseringsomfattning oberoende av radgranskningen.
- Totalt 298 källfrånvarande positioner i de hittills granskade intervallen har inte räknats som aktuell Core-täckning. Tidigare rapporter identifierar äldre HDFury- och frontend-/historiknycklar som kräver eventuell separat korsmappning.
- Granskningen är **inte klar**. Nästa steg är fortsätta rad för rad från Lokalise-position 31 097, upptäcka nytillkomna strängar, matcha gamla rapporter via fullständig nyckel, spara ändringar direkt i Lokalise och synkronisera kanonisk TMX löpande.


## Fortsatt radgranskning 2026-11-25 – position 28051–28170

90/120 poster matchade Core-källrevisionen och granskades; 46 mål ändrades och lästes tillbaka, 44 behölls. 30 källfrånvarande poster hålls utanför TM. 20 referensalias verifierades, en avvikelse synkades. Platshållare 90/90; inga pluralformsposter. Se `2026-11-25-reviewed-core-28051-28170.md` och dess JSON-underlag. TM-manifestets 90 poster är liveverifierade; kanonisk TMX validerar med 18 971 enheter. Tibbers `load`-tolkning som hushållsnod är källbaserad men inväntar eventuell formell bekräftelse från Tibber.

## Senaste batch: 31 577–31 696

111/120 poster har aktuell Core-källtext. 45 aktiva mål korrigerades och lästes tillbaka; 66 verifierades oförändrade. Nio historiska poster saknar aktiv källväg. En äldre Home Connect-sträng korrigerades separat men uteslöts ur aktuell TM. Båda aliasreferenserna matchar live-målen; platshållare 111/111 och inga pluralnycklar. Kanonisk TMX validerar med 20 871 enheter. 27 temperatursträngar rättades från º till °; svlang fick motsvarande skrivregel. Hunspell-sv uppdaterades med `skåptorrt` och `stryktorrt`; dess 19 tester passerar. Se `2026-11-25-reviewed-core-31577-31696.md` och JSON-underlagen. Osäkra robotprogramsetiketter redovisas där.

## Fortsatta hinder

- Lokalise-API:t nekar fortfarande uppdatering av `is_reviewed` med HTTP 403; översättningstexterna kan sparas och återläsas.
- 203 Core-källnycklar saknas i Lokalise; key/import-skapande har tidigare nekats med HTTP 403.
- Granskningen är inte klar. Nästa liveposition är 28 651.


## Fortsatt radgranskning 2026-11-25 – position 28171–28290

88 av 120 rader matchar aktuell Core-källa och granskades rad för rad. 19 ändringar sparades och lästes tillbaka, 69 mål behölls. 32 historiska poster saknar aktiv Core-källsträng och hålls utanför TM. Alla 25 referensalias matchade sina Lokalise-mål. Platshållare: 88/88. TMX-manifestets 88 nyckelidentiteter, engelska källor och svenska mål verifierades live med Lokalise API; TMX validerar med 19 054 enheter. Se `2026-11-25-reviewed-core-28171-28290.md` och tillhörande JSON-underlag.


## Fortsatt radgranskning 2026-11-25 – position 28291–28410

112 av 120 poster matchar aktuell Core-källa och granskades rad för rad; 29 ändringar sparades och återlästes, 83 mål behölls. Åtta historiska poster saknar aktiv källsträng. Alla 24 aliasreferenser verifierades live; fyra LG ThinQ-mål korrigerades retroaktivt och därefter matchade 24/24. Platshållare kontrolleras i manifestet. Manifestets 112 batchposter verifierades via Lokalise API. TMX innehåller 19 255 giltiga enheter. Se `2026-11-25-reviewed-core-28291-28410.md` och tillhörande JSON.


## Fortsatt radgranskning 2026-11-25 – position 28411–28530

86 av 120 poster matchade aktuell Core-källa och granskades rad för rad. 20 ändringar sparades och lästes tillbaka; 66 aktuella mål verifierades oförändrade. 34 historiska poster uteslöts ur aktuell Core-TM. Platshållare matchar 86/86; inga pluralnycklar. TM-manifestets samtliga 86 nycklar och mål verifierades live. Se `2026-11-25-reviewed-core-28411-28530.md` och tillhörande JSON. USB-dongel är bekräftad i termbanken och godkänns av båda Hunspell-ordlistorna.

Referensalias i batchen 28411–28530: 18 av 18 verifierade mot live-målen utan avvikelse.


## Fortsatt radgranskning 2026-11-25 – position 28531–28650

101 av 120 poster matchade aktuell Core-källa och granskades rad för rad. 54 måländringar sparades och återlästes; 47 oförändrade mål verifierades. Nitton källfrånvarande poster uteslöts ur aktuell Core-TM. Alla 16 aliasreferenser matchade live; platshållarna matchar 101/101 och inga pluralnycklar fanns. Alla 101 manifestposter verifierades live. TMX innehåller 19 353 enheter. Hunspell hittade en korrekt teknisk KNX-term, `datapunkttyper`, som nu stöds i ordlistan och termbanken enligt officiell svensk KNX-terminologi. Se `2026-11-25-reviewed-core-28531-28650.md` och JSON-underlagen.


## Fortsatt radgranskning 2026-11-25 – position 28651–28770

109 av 120 rader matchar aktuell Core-källa; 26 svenska texter ändrades, sparades och återlästes via Lokalise API. 83 befintliga mål granskades utan ändring. Elva poster saknar aktuell Core-källtext och uteslöts ur aktuell TM. 32 alias verifierades mot referensmål; tre mål (Open Router samt två Fressnapf-poster) korrigerades retroaktivt så att alias och mål överensstämmer. Platshållare 109/109; inga pluralnycklar. Alla 111 manifestposter är liveverifierade. Kanonisk TMX validerar med 19 459 enheter. Se `2026-11-25-reviewed-core-28651-28770.md` och JSON-underlagen. Nästa position: 28 771.


## Fortsatt radgranskning 2026-11-25 – position 28771–28890

120/120 rader matchar aktuell Core-källa. 57 texter sparades och lästes tillbaka; 63 befintliga mål granskades utan ändring. Inga historiska poster eller alias i batchen, inga pluralnycklar, platshållare 120/120. Tidigare förslag om Fluss, Velbus, Telegram Bot, klimat- och luftfuktarutlösare synkades efter kontroll av aktuell källtext. TMX-manifestet liveverifierades och kanonisk TMX validerar med 19 571 enheter. Hunspell avslöjade falska flaggningar för `börvärdet`-former, `hysteresband` och KLF200-sammansättningar; verktygets dictionaries och regressioner uppdaterades, 19/19 tester passerade. Ingen ny Hunspell-release gjordes efter samma dags release `v2026.11.25`. Nästa position: 28 891. Se `2026-11-25-reviewed-core-28771-28890.md` och JSON-underlagen.


## Fortsatt radgranskning 2026-11-25 – position 28891–29010

120/120 poster matchar aktuell Core-källa. 40 översättningar ändrades, sparades och återlästes via Lokalise API; 80 lämnades oförändrade efter granskning. Inga alias, källfrånvarande poster eller pluralnycklar. Platshållare 120/120; svlang utan skrivregelfel. Liveverifierat manifest och TMX validerar med 19 688 enheter (19 457 Lokalise-ID, 231 äldre ID). Tidigare dokumenterade förslag för ljus-, lås-, VELUX-, väder- och sirensträngar hanterades efter ny källkontroll. Verktygsgranskningen lade till VELUX i Hunspell-sv; 19/19 tester passerade, ingen andra release samma dag. Nästa position: 29 011. Se `2026-11-25-reviewed-core-28891-29010.md` och JSON-underlagen.


## Fortsatt radgranskning 2026-11-25 – position 29011–29130

120/120 poster matchar aktuell Core-källa. 23 översättningar sparades och lästes tillbaka; 97 befintliga mål granskades och behölls. Inga alias, historiska poster eller pluralnycklar. Platshållare 120/120, svlang utan skrivregelfel och Hunspell utan kvarvarande stavningsvarningar. TMX-manifestet liveverifierades; kanonisk TMX validerar med 19 800 enheter. Tidigare förslag för temperaturtrösklar och KNX generisk flyttalstyp följdes upp. Rättade `datapunktstyp` till `datapunkttyp`. Hunspell-sv fick stöd och regressioner för DPT, PM1/PM2/PM4/PM10 och VOC, plus ord från föregående batcher; 19/19 tester passerade, ingen andra release samma dag. Nästa position: 29 131. Se `2026-11-25-reviewed-core-29011-29130.md` och JSON-underlagen.


## Fortsatt radgranskning 2026-11-25 – position 31937–32056

114 av 120 poster matchar aktiv Core-källa; 36 översättningar korrigerades, sparades och återlästes via Lokalise API. 70 andra aktiva mål verifierades oförändrade och åtta tidigare granskade aktiva mål återverifierades. Sex historiska källsaknade poster dokumenterades och uteslöts ur aktiv Core-TM. Alla nio referensalias matchar live-målen. Platshållare 114/114; inga pluralnycklar. `svlang skrivregler` gav inga träffar. Hunspell-signaler gäller märken, namn och kodtermer; ingen ny ordlisteterm behövdes. TMX validerar med 21 188 enheter efter 104 nettotillägg och tio uppdateringar. Se `2026-11-25-reviewed-core-31937-32056.md` och JSON-underlagen. Nästa position: 32 057.


## Fortsatt radgranskning 2026-11-25 – position 32057–32176

120/120 poster matchar aktuell Core-källa. 17 översättningar korrigerades, sparades och återlästes via Lokalise API; 100 andra mål verifierades oförändrade, varav tre tidigare rapporterade återverifierades. Alla 75 aliasreferenser matchar sina källmål och svenska live-mål. Platshållare 120/120; inga pluralnycklar. `svlang skrivregler` gav inga träffar. Hunspell flaggar kvar produktnamn och identifierare utan behov av ordlisteändring. TMX validerar med 21 307 enheter. Nästa position: 32 177. Se `2026-11-25-reviewed-core-32057-32176.md` och JSON-underlagen.


## Fortsatt radgranskning 2026-11-25 – position 32177–32296

90 av 120 poster matchar aktuell Core-källa och granskades. 11 texter korrigerades, sparades och lästes tillbaka via Lokalise API; 79 aktiva mål verifierades oförändrade. De övriga 30 historiska nycklarna saknar aktuell källtext och är dokumenterade men exkluderade ur Core-TM. Alla 65 aktiva alias matchar sina engelska och svenska live-mål. Platshållare 90/90; inga pluralnycklar. `svlang skrivregler` gav inga träffar; Hunspell-flaggor är produktnamn, identifierare och platshållare. TMX validerar med 21 397 enheter. Nästa position: 32 297. Se `2026-11-25-reviewed-core-32177-32296.md` och JSON-underlagen.


## Fortsatt radgranskning 2026-11-25 – position 32297–32416

104 av 120 rader matchar aktiv Core-källa; 16 källsaknade historiska poster var redan dokumenterade och uteslöts ur aktiv Core-TM. 32 aktiva mål korrigerades, sparades och lästes tillbaka; 72 verifierades oförändrade, varav sex tidigare granskade mål återverifierades. 40 aliasreferenser matchar källmål och svenska live-mål. Tre delade Habitica-texter och deras alias synkades. Platshållare 104/104; inga pluraler. `svlang skrivregler` gav inga träffar; Hunspell-flaggor gäller främst produktnamn, identifierare och platshållare. TMX validerar med 21 498 enheter. Nästa position: 32 417. Se `2026-11-25-reviewed-core-32297-32416.md` och JSON-underlagen.


## Fortsatt radgranskning 2026-11-25 – position 32417–32536

116 av 120 rader matchar aktiv Core-källa; fyra historiska källsaknade poster var redan dokumenterade och lämnades utanför Core-TM. 33 aktiva måländringar sparades och lästes tillbaka; 83 verifierades oförändrade, varav en tidigare granskad. Alla 15 aliasreferenser matchar live. Platshållare 116/116; inga pluraler. `svlang skrivregler` gav inga träffar. Hunspell hade saknat korrekta ZHA-sammansättningar `eco-läge` och `hysteresläge`; båda ordböckerna och regressionstestet uppdaterades, 19/19 tester passerade. Ingen ny release gjordes samma dag. TMX validerar med 21 614 enheter. Två produktkontextfall (`Reverse` och Govee-effekten `Crossing`/scenetiketterna) är markerade för uppföljning i batchrapporten. Nästa position: 32 897. Se `2026-11-25-reviewed-core-32417-32536.md` och JSON-underlagen.


## Fortsatt radgranskning 2026-11-25 – position 32537–32656

86 av 120 poster matchar aktiv Core-källa; 34 historiska poster utan aktuell källtext dokumenterades och uteslöts ur aktuell Core-TM. 23 aktiva mål ändrades, sparades och återlästes; 63 verifierades oförändrade. Två tidigare granskade aktiva mål återverifierades. Alla 15 referensalias matchar live. Platshållare 86/86; inga pluralnycklar. Korrigeringarna omfattar SmartThings-programfaser, maskinstatus och gasmätarens fält. SmartThings-dokumentationen verifierade gasmätarens värmevärde, mättidpunkt och normalstatus för kolmonoxiddetektorn ([Capabilities Reference](https://developer.smartthings.com/docs/devices/capabilities/capabilities-reference)). TMX validerar med 21 881 enheter (21 650 Lokalise-ID och 231 historiska). Nästa position: 32 897. Se `2026-11-25-reviewed-core-32537-32656.md` och JSON-underlagen.


## Fortsatt radgranskning 2026-11-25 – position 32657–32776

113 av 120 poster matchar aktiv Core-källa; sju historiska poster saknar aktiv källtext och är uteslutna ur Core-TM. 39 tidigare rapporterade aktiva nycklar återverifierades; 17 mål ändrades, sparades och lästes tillbaka; 96 aktiva mål verifierades utan ändring. Av 31 referensalias matchar 28 delade live-mål. Tre kontextuella avvikelser granskades: rökdetektorns `clear` och `detected` behöver egna svenska uttryck trots delade CO-referenser, och lägesvärdet `stop` är substantivet ”Stopp” i stället för åtgärdsreferensens ”Stoppa”. Platshållare 113/113; inga pluralnycklar. `svlang skrivregler` utan träffar. Hunspell-flaggor gäller främst produkt-/modellnamn. TMX validerar med 21 881 enheter (21 650 Lokalise-ID, 231 historiska). Validerarens tillåtna TM-statusar utökades med `revalidated-prior-review` och regressionstest lades till; 4/4 tester passerade. Robottillståndet `after`, robotläget `reserve` och torktumlarens `internal_care` behöver produktkontext för finöversättning. Nästa position: 32 897. Se `2026-11-25-reviewed-core-32657-32776.md` och JSON-underlagen.


## Fortsatt radgranskning 2026-11-25 – position 32777–32896

109 av 120 poster matchar aktiv Core-källa; elva historiska poster saknar aktuell källtext och uteslöts ur Core-TM. Inga aktiva nycklar behövde granskas dubbelt. 32 översättningar ändrades, sparades och lästes tillbaka; 77 aktiva mål verifierades oförändrade. Alla 51 källreferenser matchar live efter att Habiticas frekvensfält och deras gemensamma mål uppdaterades synkroniserat. Platshållare 109/109; inga pluralnycklar. `svlang skrivregler` utan träffar. Hunspell-verktyget flaggade det korrekta svenska `uppgiftsalias` och dess former; båda ordlistorna och regressionerna uppdaterades, 19/19 tester passerade. Balboa-terminologi kontrollerades mot tillverkarens dokumentation för pumpfyllning vid start och felkoden `Hot fault`. TMX validerar med 21 881 enheter (21 650 Lokalise-ID, 231 historiska). Nästa position: 32 897. Se `2026-11-25-reviewed-core-32777-32896.md` och JSON-underlagen.


## Fortsatt radgranskning 2026-11-25 – position 32897–33016

118 av 120 poster matchar aktuell Core-källa; två historiska poster utan aktuell källväg uteslöts ur Core-TM. 15 aktiva nycklar återverifierades från äldre rapporter; 34 måländringar sparades och lästes tillbaka och 84 mål verifierades utan ändring. Två tidigare korrigerade IronOS-översättningar förbättrades ytterligare. Alla 54 källreferenser matchar live efter synkning av Habiticas checklist- och påminnelsemål med alias. Platshållare 118/118; inga pluralnycklar. `svlang skrivregler` utan träffar. Hunspell saknade de korrekta svenska sammansättningarna `checklistpunkt` och `lödspets`; båda ordlistorna och regressionerna uppdaterades, 19/19 tester passerade. TMX validerar med 21 984 enheter (21 753 Lokalise-ID, 231 historiska). Nästa position: 33 017. Se `2026-11-25-reviewed-core-32897-33016.md` och JSON-underlagen.


## Fortsatt radgranskning 2026-11-25 – position 33017–33136

109 av 120 poster matchar aktiv Core-källa; elva historiska poster saknar aktiv källtext och uteslöts ur Core-TM. Två tidigare aktiva nycklar återverifierades. 30 ändringar i intervallet sparades och lästes tillbaka; två AccuWeather-mål ändrades retroaktivt och synkades med sina alternativalias. 79 aktiva mål verifierades utan ändring. Alla 34 källreferenser matchar live. Platshållare 109/109; inga pluralnycklar. `svlang skrivregler` utan träffar. Hunspell fick stöd för `moppningsrutt`, `rumsnamn` och relevanta HA-produkt-/protokollnamn; regressionstesterna passerade 19/19. TMX validerar med 22 093 poster (21 862 Lokalise-ID, 231 historiska). Följdes av batcherna 33 137–33 256 och 33 257–33 376; nästa position: 33 377. Se `2026-11-25-reviewed-core-33017-33136.md` och JSON-underlagen.

## Fortsatt radgranskning 2026-11-25 – position 33137–33256

107 av 120 poster matchar aktiv Core-källa; 13 historiska poster var redan kända och uteslöts ur Core-TM. 18 måländringar sparades och lästes tillbaka; 89 aktiva mål verifierades oförändrade. Alla 77 referensalias matchar aktuella källmål och svenska live-mål. Sex delade Habitica-mål korrigerades retroaktivt och de sex aliasen i intervallet synkades. Ytterligare sex create_daily-alias på position 33 725–33 749 kontrollerades efter målsynken och matchade; de återkontrolleras i sin ordinarie omgång. Platshållare 107/107; inga pluralnycklar. `svlang skrivregler` fann inga fel. Hunspell-sv:s ordlistor fick `sviträknare` och vanliga böjningar; testerna passerade 19/19. Ingen ny release gjordes. Home Assistant-TM validerar med 22 212 poster. Se `2026-11-25-reviewed-core-33137-33256.md` och JSON-underlagen. Nästa position: **33 257**.

## Föregående radgranskning 2026-11-25 – position 33257–33376

117 av 120 poster matchar aktiv Core-källa; tre tidigare kända historiska poster utan aktiv källtext uteslöts ur Core-TM. Fyra aktiva poster fanns redan i äldre fullnyckelrapporter; två av deras översättningar förbättrades. Totalt 46 ändringar sparades och lästes tillbaka, 71 aktiva mål verifierades oförändrade. Av 35 referenser matchar 13 mål ordagrant; 22 Reolink-alias fick källtroget kontextuella händelsetexter i stället för gastillståndens generiska ”Klar” och ”Detekterad”. Platshållare 117/117; inga pluraler. `svlang skrivregler` utan träffar. Hunspell-sv uppdaterades med `nivålås` samt Ohme-, Reolink- och Snoo-former; regressionstesterna passerade 19/19. Ingen ny release gjordes. Home Assistant-TM validerar med 22 325 poster. Se `2026-11-25-reviewed-core-33257-33376.md` och JSON-underlagen. Nästa position: **33 377**.

## Fortsatt radgranskning 2026-11-26 – position 33377–33496

118 av 120 poster matchar aktiv Core-källa; två äldre nycklar saknar aktiv källtext och uteslöts. En tidigare rapporterad aktiv nyckel återgranskades. 64 texter ändrades, sparades och lästes tillbaka; 54 aktiva mål verifierades oförändrade. Alla 32 referensalias matchar live-mål efter synkning. Platshållare 118/118; inga pluralnycklar. `svlang skrivregler` fann inga avvikelser; dess naturlighetskontroll gav fem heuristiska V2-varningar som bedömdes manuellt. Hunspell-sv fick giltiga HA-produktnamn, tekniska förkortningar och orden `avlarmat`, `förbryggning` och `rpm`; testerna passerade 19/19. Home Assistant-TM validerar med 22 440 enheter (22 209 Lokalise-ID och 231 historiska). Se `2026-11-26-reviewed-core-33377-33496.md` och JSON-underlagen. Nästa position: **33 497**.


## Fortsatt radgranskning 2026-11-26 – position 33497–33616

113 av 120 nycklar matchar aktuell Core-källa, inklusive en nyckel med ändrad källväg; sju redan dokumenterade historiska nycklar uteslöts. 58 aktiva måltexter ändrades: 50 direkta Lokalise-ändringar sparades/lästes tillbaka och åtta Home Connect-alias följde det delade Present-målet. Ytterligare 39 sensoralias utanför ordinarie positioner uppdaterades retroaktivt via samma mål; Vodafone Stations delade värdmål korrigerades också. 55 aktiva mål verifierades oförändrade. Samtliga 40 referensalias i batchen matchar sina 19 live-mål efter ändringarna. Platshållare 113/113; inga pluralnycklar. `svlang skrivregler` fann inga fel; heuristiska träffar bedömdes manuellt. Hunspell-sv fick `skrynkelskydd` och HA-ord/varumärkesformer; tester 19/19. Ingen ny release gjordes; verktygsändringen pushades i `yeager/hunspell-sv` commit `5d9a0c5`. Home Assistant TMX validerar med 22 580 enheter. Se `2026-11-26-reviewed-core-33497-33616.md`, JSON-underlagen, `2026-11-26-home-connect-present-aliases.json`, `2026-11-26-reference-audit-33497-33616.json` och `2026-11-26-retroactive-reference-targets.json`. Nästa position: **33 737**.

## Fortsatt radgranskning 2026-11-26 – position 33617–33736

120/120 poster matchar aktuell Core-källa. 19 Home Connect-översättningar korrigerades, sparades via Lokalise API och lästes tillbaka; 70 aktiva texter verifierades oförändrade och 31 tidigare dokumenterade poster återverifierades. Alla 85 källreferenser matchar aktuell källa och svenska live-mål. Platshållare 120/120; inga pluralnycklar. Home Connect API-dokumentation bekräftar i-Dos låg nivå, instruktionen att ställa mjölkbehållaren svalt, fettfilterrengöring och robotdammsugarens åtgärd. `svlang skrivregler` gav inga fel; Hunspell flaggade enbart varumärkesdelarna i `Calc'N'Clean`, manuellt godkända. Termbankens generiska `Cleaning`-träffar var inte kontextuellt användbara. TMX validerar med 22 669 poster (22 438 Lokalise-ID, 231 historiska); 89 nya manifestposter lades till och 31 ersattes/återverifierades. Se `2026-11-26-reviewed-core-33617-33736.md` och JSON-underlagen. Nästa position: **33 737**.


## Fortsatt radgranskning 2026-11-26 – position 33737–33856

112 av 120 nycklar matchar aktuell Core-källa; åtta redan rapporterade historiska poster uteslöts. 31 direkta översättningar korrigerades och lästes tillbaka, och en Habitica-aliastext följde en korrigerad referens; dessutom uppdaterades Habiticas delade månadsbeskrivning och aliaset `update_daily` retroaktivt. Bland aktiva rader verifierades 75 utan ändring och fem tidigare granskade återverifierades. Alla 29 källreferenser och platshållare matchar; inga pluralnycklar. Home Assistant MQTT-, Reolink- och iometer-kontext kontrollerades mot officiell dokumentation/kod. `svlang skrivregler` utan fel; Hunspell-ordlistorna fick `linjekorsning`, `intrångsdetektering`, `uppspelningskö` med böjningar samt `Pterodactyl`, och regressionerna klarade båda diktionärerna. Ingen ny Hunspell-release gjordes denna dag. TMX validerar med 22 773 enheter (22 542 Lokalise-ID, 231 historiska). En ZHA-kalibreringstolkning är markerad för kontroll mot verklig enhet; inga referensmål återstår oklara. Se `2026-11-26-reviewed-core-33737-33856.md`, JSON-underlagen och `2026-11-26-retroactive-habitica-monthly-repeat.json`. Nästa position: **33 857**.

## Fortsatt radgranskning 2026-11-26 – position 33857–33976

46 aktiva nycklar och 74 källfrånvarande poster granskades. 15 ändringar sparades/lästes tillbaka, inklusive två tidigare rapporterade aktiva strängar; 31 nya aktiva mål lämnades oförändrade. Alla 15 referenser matchar live-målen. Se `2026-11-26-reviewed-core-33857-33976.md`. Nästa position: **33 977**.

## Fortsatt radgranskning 2026-11-26 – position 33977–34096

93 aktiva nycklar och 27 historiska poster granskades; 25 mål korrigerades och lästes tillbaka, 68 behölls. Alla 45 referenser granskades. Se `2026-11-26-reviewed-core-33977-34096.md`. Nästa position: **34 097**.

## Fortsatt radgranskning 2026-11-26 – position 34097–34216

102 aktiva nycklar och 18 historiska poster granskades; 29 mål ändrades och lästes tillbaka, 73 behölls. Alla 27 referenser matchar live-målen. Se `2026-11-26-reviewed-core-34097-34216.md`. Nästa position: **34 217**.

## Fortsatt radgranskning 2026-11-26 – position 34217–34336

110 aktiva nycklar och 10 historiska poster granskades; 22 aktiva mål ändrades. Ett delat NUT-mål och dess alias uppdaterades och lästes tillbaka. Alla 36 aliasreferenser matchar live-målen. Se `2026-11-26-reviewed-core-34217-34336.md`. Nästa position: **34 337**.

## Fortsatt radgranskning 2026-11-26 – position 34337–34456

96 aktiva nycklar och 24 historiska poster granskades; 19 slutliga ändringar sparades och lästes tillbaka, 77 nya aktiva mål verifierades oförändrade och en tidigare aktiv nyckel återgranskades. Alla 16 aliasreferenser matchar live-målen. Platshållare 96/96; inga pluraler. Miele-klassificeringarna Highlight-häll och vin/frys-kombination rättades med stöd i Mieles svenska produktterminologi. SyncThru-sensorernas kvarvarande procent kontrollerades i koden; befintliga nivånamn behölls. TMX validerar med 23 213 enheter. Se `2026-11-26-reviewed-core-34337-34456.md` och JSON-underlaget. Nästa position: **34 457**.

## Fortsatt radgranskning 2026-11-26 – position 34457–34576

98 aktiva nycklar och 22 historiska poster granskades; 41 slutliga ändringar sparades och lästes tillbaka. 57 aktiva texter verifierades oförändrade, varav fem tidigare aktiva rader återgranskades; en redan rapporterad sträng förbättrades. Alla 16 aliasreferenser kontrollerades: 14 följer live-målen och två Overkiz-väljare fick motiverade kontextuella overrides. Platshållare 98/98; inga pluralnycklar. `svlang` fann inga skrivregelfel. Hunspell-sv uppdaterades med `förinfusion` och böjningar; tester 19/19. Ingen ny release denna dag. TMX validerar med 23 307 enheter (23 076 Lokalise-ID, 231 äldre). Se `2026-11-26-reviewed-core-34457-34576.md` och JSON-underlaget. Nästa position: **34 577**.


## Fortsatt radgranskning 2026-11-26 – position 34577–34696

95 aktiva nycklar och 25 historiska poster granskades. 35 ändringar sparades i Lokalise och lästes tillbaka; 60 aktiva mål behölls efter radgranskning. 31 tidigare rapporterade nycklar återkontrollerades. Alla 38 aliasreferenser matchar live-målen. Platshållare 95/95; inga pluralnycklar. `svlang skrivregler` gav inga träffar; Hunspell flaggade `ntfy` och `pushaviseringar`, manuellt godkända i kontext. TMX valideras efter att samtliga 95 aktiva nycklar synkats med spårbara Lokalise-ID:n. Se `2026-11-26-reviewed-core-34577-34696.md` och JSON-underlagen. Nästa position: **34 697**.


## Fortsatt radgranskning 2026-11-26 – position 34697–34816

111 aktiva nycklar och 9 historiska poster granskades; 33 ändringar sparades och återlästes i Lokalise, 78 aktiva mål behölls. 12 rader hade tidigare rapporter. Alla åtta referensalias matchar; platshållare 111/111; inga pluralnycklar. `svlang skrivregler` utan fel. Tesla SentryMode `aware` är markerat som uppföljningsfall eftersom enumdokumentationen inte definierar den precisa etiketten. TMX validerar med 23508 enheter. Se batchrapporten och JSON-underlagen. Nästa position: **34 817**.


## Fortsatt radgranskning 2026-11-26 – position 34817–34936

119 aktiva nycklar och en historisk post granskades. 39 ändringar sparades och återlästes i Lokalise; 80 aktiva mål verifierades utan ändring, varav två hade tidigare rapporter. Alla platshållare stämmer; inga pluralnycklar. Miele-rättningar omfattar tydliga matnamns-/programfel, bland annat kålrabbi för German turnip, vitkål för green cabbage och hachee-köttgryta för Dutch hash. `svlang skrivregler` fann inga fel. TMX validerar med 23626 enheter. Se batchrapport och JSON-underlag. Nästa position: **34 937**.


## Fortsatt radgranskning 2026-11-26 – position 34937–35056

119 aktiva nycklar och en historisk källa-saknad post granskades; en aktiv sträng använder ett källalias. 27 ändringar sparades och återlästes; 92 aktiva mål verifierades utan ändring. Aliaset `normal` matchar sitt live-mål. Miele-etiketter för äggens storlek/kokgrad och några tidigare missvisande råvaru-/programnamn rättades. `svlang skrivregler` utan fel. TMX validerar med 23745 enheter. Se batchrapport/JSON. Nästa position: **35 057**.


## Retroaktiv korrigering 2026-11-26

Två tidigare Miele-nycklar med `Common sole` korrigerades från ”Rödtunga” till ”Sjötunga”. Båda ändringarna sparades/lästes tillbaka i Lokalise och uppdaterades i HA Core-TM, manifestet för 34817–34936 och dess rapport.


## Fortsatt radgranskning 2026-11-26 – position 35057–35176

Samtliga 120 rader matchar aktuell Core-källa. 44 ändringar sparades och återlästes; 76 mål behölls. Ingen tidigare rapporterad nyckel, ingen aliasreferens och inga pluralnycklar. Platshållare ej aktuellt i spannet. Potatisetiketter rättades från bokstavlig ”vaxartad” till fast sort, tillsammans med felaktiga fisknamn och böjningar. `svlang skrivregler` fann inga fel. TMX validerar med 23865 enheter. Se rapport och JSON-underlag. Nästa position: **35 177**.


## Fortsatt radgranskning 2026-11-26 – position 35177–35296

Alla 120 rader matchar aktiv Core-källa. 30 ändringar sparades och återlästes; 90 mål behölls. Rättningar omfattar nötköttets silverside/ytterlår, Mieles torknivå stryktorrt och robotdammsugarens målområde. `svlang skrivregler` utan fel. TMX validerar med 23985 enheter. Två specialprogram är markerade för kontroll mot exakt apparatpanel. Se rapport och JSON-underlag. Nästa position: **35 297**.


## Fortsatt radgranskning 2026-11-26 – position 35297–35416

110 aktiva Core-rader och 10 tidigare rapporterade historiska poster granskades. 18 ändringar sparades och återlästes i Lokalise; 92 aktiva mål behölls. Alla 21 referenser matchar live-målen; platshållare 110/110 och inga pluralformer. `svlang skrivregler` utan fel; Hunspell-flaggor och FOSS-termträffar bedömdes manuellt. TMX uppdaterades med alla 110 aktiva rader och valideras med 24095 segment. Se batchrapporten och JSON-underlaget. Nästa position: **35 417**.




## Fortsatt radgranskning 2026-11-26 – position 35417–35536

108 aktiva Core-nycklar granskades i spannet; 50 ändringar sparades/lästes tillbaka och 58 mål behölls. Tolv `advanced_settings`-poster är utgångna dubbletter; deras aktuella `other_settings`-motsvarigheter finns vid 58 572–58 586 och granskades separat (12 ändringar sparade/lästes tillbaka). De gamla posterna återställdes och togs bort ur aktiv TM. De två huvudspannsreferenserna och samtliga platshållare kontrollerades. TMX innehåller 24201 segment och backupen är identisk. Nästa position: **35 537**.

### Korrigering av tidigare rapport

Nyckelsnapshotten använder fältet `key`, inte `key_name`. Den tidigare statusen om saknade aktiva nycklar och blockerad nyckelnamnsändring var felaktig. De aktuella nycklarna finns och är nu granskade; endast de äldre, inaktuella Lokalise-posterna ligger kvar med sina ursprungliga värden.

## Fortsatt radgranskning 2026-11-26 – position 37097–37216

120 Lokalise-poster liveverifierades rad för rad; 19 textändringar sparades via API och lästes tillbaka, 90 aktiva nycklar behölls och 11 aktiva nycklar markerades med `source-path-follow-up`. Källkontrollen fann 73 direkta Core-källträffar och 28 aliasreferenser till 15 mål; samtliga engelska och svenska alias matchar sina live-mål. Elva poster saknar fortfarande motsvarande källnod i den valda Core-revisionens `strings.json` och är uttryckligen listade i rapporten för uppföljning. Platshållare matchar 120/120; inga pluralnycklar. `svlang skrivregler` utan fel. Hunspell-flaggor bedömdes manuellt; ingen ordboksändring. TMX-manifestet verifierades live mot 120 Lokalise-poster och TMX validerar med 25 690 enheter (25 459 Lokalise-ID, 231 legacy-source); backup byteidentisk. API:t avvisade endast ändring av granskningsflaggan (403); textändringarna sparades utan flagga. Se `2026-11-26-reviewed-core-37097-37216.md` och JSON-underlaget. Nästa position: **37 217**.

## Fortsatt radgranskning 2026-11-26 – position 37217–37336

120 poster granskades och liveverifierades; 8 rader i spannet rättades och 99 aktiva översättningar lämnades oförändrade. Ytterligare 10 aktuella OpenAI-strängar utanför spannet (5 målnycklar och 5 AI Task-alias) rättades retroaktivt; totalt 18 Lokalise-ändringar sparades/lästes tillbaka. Alla 71 referenser matchar sina mål efter att Alexa OTP-aliaset korrigerats. Platshållare 120/120 efter ändring; inga pluralnycklar. 13 nycklar saknar källa i aktuell Core-revision och finns listade som `source-path-follow-up`. Källkontrollen rättades för gemensamma strängar, flyttade OpenAI-nycklar och escapade radbrytningar i Lyric JSON. `svlang skrivregler` utan fel. TMX-manifestet verifierades live med 130 poster (120 i batchen samt 10 retroaktiva mål/alias); TMX validerar med 25 817 enheter (25 586 Lokalise-ID, 231 legacy-source), backup byteidentisk. Se `2026-11-26-reviewed-core-37217-37336.md`, batchens JSON och `2026-11-26-retroactive-openai-core-updates.json`. Nästa position: **37 337**.

## Fortsatt radgranskning 2026-11-26 – position 37337–37456

Alla 120 poster granskades och liveverifierades; 24 ändringar sparades/lästes tillbaka, 86 aktiva översättningar behölls och 10 aktiva rader markerades för källuppföljning. 75 direkta källtexter matchar och 32 källreferenser till 19 mål löstes; samtliga alias matchar efter ändring. Ytterligare två Assist Satellite-medie-ID-etiketter korrigerades retroaktivt; totalt 26 texter sparades. Platshållare 120/120; inga pluralnycklar. Hunspell-flaggor granskades manuellt; `svlang skrivregler` utan fel. TM-manifestet liveverifierades för 122 poster. TMX validerar med 25 926 enheter (25 695 Lokalise-ID, 231 legacy-source); backup byteidentisk. Se batchrapport, JSON och `2026-11-26-retroactive-assist-satellite-updates.json`. Nästa position: **37 457**.


## Batch 69: 37,457–37,576

120/120 granskade. 14 ändringar sparade och livekontrollerade. Källor: {'current-source-match': 72, 'source-absent': 23, 'reference-resolved': 25}; 25 referenser verifierade; platshållare 120/120; 23 äldre källsaknade nycklar att följa upp. Manifest/TMX tillagt.


## Batch 70: 37,577–37,696

120/120 granskade. 15 ändringar sparade och livekontrollerade. Källor: {'current-source-match': 76, 'reference-resolved': 23, 'source-absent': 21}; 23 referenser verifierade; platshållare 120/120; 21 äldre källsaknade nycklar att följa upp. Manifest/TMX tillagt.


## Batch 71: 37,697–37,816

120/120 granskade. 15 ändringar sparade och livekontrollerade. Källor: {'current-source-match': 77, 'reference-resolved': 30, 'source-absent': 13}; 30 referenser verifierade; platshållare 120/120; 13 äldre källsaknade nycklar att följa upp. Manifest/TMX tillagt.


## Batch 72: 37,817–37,936

120/120 granskade. 14 ändringar sparade och livekontrollerade. Källor: {'reference-resolved': 37, 'source-absent': 20, 'current-source-match': 63}; 37 referenser verifierade; platshållare 120/120; 20 äldre källsaknade nycklar att följa upp. Manifest/TMX tillagt.


## Batch 73: 37,937–38,056

120/120 granskade. 10 ändringar sparade och livekontrollerade. Källor: {'current-source-match': 67, 'source-absent': 16, 'reference-resolved': 37}; 37 referenser verifierade; platshållare 120/120; 16 äldre källsaknade nycklar att följa upp. Manifest/TMX tillagt.


## Batch 74: 38,057–38,176

120/120 granskade. 22 ändringar sparade och livekontrollerade. Källor: {'current-source-match': 80, 'source-absent': 9, 'reference-resolved': 31}; 31 referenser verifierade; platshållare 120/120; 9 äldre källsaknade nycklar att följa upp. Manifest/TMX tillagt.


## Batch 75: 38,177–38,296

120/120 rader granskade; 13 ändringar sparade och liveverifierade, 107 befintliga värden behållna. Källor: {'current-source-match': 72, 'source-absent': 15, 'reference-resolved': 33}; 33 referenser/29 mål verifierade; platshållare 120/120; 15 äldre/utgångna källnycklar markerade för uppföljning. TM-manifest sparat.


## Batch 76: 38,297–38,416

120/120 granskade; 27 rättade, sparade och återlästa; 93 värden behållna. Källstatus: {'current-source-match': 63, 'source-absent': 41, 'reference-resolved': 16}. Referenser: 16/16 alias till 14 mål. Platshållare 120/120. 41 källvägar behöver följas upp. TMX-manifest tillagt.


## Batch 77: 38,417–38,536

120/120 granskade; 26 ändringar sparade och liveåterlästa, 94 behållna. Källstatus: {'current-source-match': 65, 'source-absent': 15, 'reference-resolved': 40}. Referenser 40/40 till 32 mål verifierade efter synkronisering. Platshållare 120/120. 15 källvägar markeras för uppföljning. TMX-manifest tillagt.


## Batch 78: 38,537–38,656

120/120 granskade; 33 ändringar sparade/återlästa, 87 behållna. Källor: {'current-source-match': 89, 'reference-resolved': 22, 'source-absent': 9}; 22/22 alias till 16 mål matchar efter uppdatering. Platshållare 120/120. 9 utgångna källvägar att följa upp. TMX-manifest tillagt.


## Batch 79: 38,657–38,776

120/120 granskade; 74 rättade och sparade, 46 befintliga värden behållna. Källor: {'current-source-match': 18, 'reference-resolved': 25, 'source-absent': 77}. Referenser: 25/25 alias till 22 mål verifierade. Platshållare: 120/120. 77 källvägar följs upp, främst äldre Alexa-ljudnycklar som saknas i integrationens aktuella `strings.json`. TMX-manifest tillagt.


## Batch 80: 38,777–38,896

120/120 granskade; 93 ändringar sparade och återlästa, 27 verifierade och behållna. HA Core-snapshoten 2026-11-24 matchar alla 120 engelska texter och tidigare måltexter; aktuellt Core-träd saknar nycklarna. Referenser 0; platshållare 120/120; osäkra fall 6. Hunspell-ordlistorna och regressionstesterna uppdaterades för fem belagda ordformer; 19 tester och språkpolicykontroll passerade. TMX-manifest tillagt.

## Batch 81: 38,897–39,016

120/120 granskade; 71 ändringar sparade/återlästa, 49 verifierade och behållna. HA Core-snapshot 2026-11-24 matchar alla 120 engelska strängar; aktuell källrevision saknar nycklarna. Referenser 0; platshållare 120/120; osäkra fall 14. TMX-manifest tillagt.


## Batch 82: 39,017–39,136

120/120 granskade; 49 ändringar sparade och återlästa, 71 verifierade och behållna. Snapshot 2026-11-24 matchar alla 120 engelska källtexter och 120 tidigare svenska måltexter. Aktuell källrevision saknar posterna. Referenser 0; platshållare 120/120; osäkerhetsuppföljningar 14. Nästa indexposition: **39,137**.


## Batch 83: 39,137–39,256

120/120 granskade; 40 ändringar sparade och återlästa, 80 texter behållna. 63 engelska strängar matchar aktuell Core-källa, 49 äldre Alexa-ljudposter matchar snapshot 2026-11-24. Åtta referenser (sju unika mål) verifierade. Platshållare 120/120, inga pluraler. Osäkra ljudetiketter 14. Nästa indexposition: **39,257**.


## Batch 84: 39,257–39,376

120/120 granskade; 69 ändringar sparade och återlästa, 51 texter verifierade och behållna. 99 källmatchningar och 21/21 referenser verifierade. Fem gemensamma fan-preset-mål rättades retroaktivt för att synka klimat-alias. Platshållare 120/120, inga pluraler. Nästa indexposition: **39,377**.


## Batch 84: 39,257–39,376

120/120 granskade; 69 ändringar sparade och återlästa, 51 texter verifierade och behållna. 99 källmatchningar och 21/21 referenser verifierade. Fem gemensamma fan-preset-mål rättades retroaktivt för att synka klimat-alias. Platshållare 120/120, inga pluraler. Nästa indexposition: **39,377**.


## Batch 85: 39,377–39,496

120/120 granskade; 15 ändringar sparade och återlästa, 105 texter behållna. 48 aktuella källmatchningar och 12 arkivmatchningar. 60/60 referenser (35 unika mål) verifierade. Platshållare 120/120, inga pluraler. Nästa indexposition: **39,497**.


## Batch 86: 39,497–39,616

120/120 poster radgranskade; 17 ändringar sparade och återlästa, 103 texter verifierade och behållna. 65 direkta källmatchningar och 32 referensnycklar till 26 unika mål verifierades live. 23 äldre poster matchar exakt HA Core-snapshoten från 2026-11-24 och har uteslutits från aktuell TM. Platshållare 120/120; inga pluraler. TM-manifestet med 97 aktiva poster API-verifierades och TMX validerar med 27 924 enheter. Nästa position: **39 617**.


## Batch 87: 39,617–39,736

120/120 poster radgranskade; nio ändringar sparade slutligt och återlästa, 111 värden verifierade och behållna. 40 direkta källmatchningar och 52 referensnycklar till 50 unika mål kontrollerades; alla alias matchar. 28 äldre poster matchar exakt snapshoten 2026-11-24 och uteslöts från aktuell TM. Platshållare 120/120; inga pluraler. 92 aktiva TM-poster liveverifierade; TMX innehåller nu 28 009 enheter. Hunspell falsklarm för `Homee`/`homee-enheten` rättat; 19 tester passerade. Osäkert: Mieles etikett “Rinse salt” och emonCMS-källans “32 bits API key”. Nästa position: **39 737**.


## Batch 88: 39,737–39,856

120/120 rader radgranskade; 11 direkta texter och 19 Husqvarna-alias sparades och återlästes. Ytterligare 19 tidigare granskade Husqvarna-mål korrigerades retroaktivt och deras händelsealias synkades; totalt 49 Lokalise-ändringar. 90 värden verifierades och behölls. 55 direkta källmatchningar, 63/63 referenser till 59 mål verifierade. Två äldre poster snapshotmatchade och uteslöts från aktuell TM. Platshållare 120/120; inga pluraler. 118 aktuella manifestposter och 19 retroaktiva mål API-verifierade; TMX validerar med 28 146 enheter. `svlang` falsklarm för PPPoE rättat; alla 114 verktygstester passerade. Osäkra Husqvarna-förkortningar: `curr`, `dir`, `drive`. Nästa position: **39 857**.


### Senaste batch: 39 857–39 976

120/120 positioner radgranskades; 117 poster matchar aktuell Core-källa (23 direkta och 94 referenser), tre poster saknar aktuell källväg och matchar exakt 2026-11-24-snapshoten. 35 ändringar i intervallet sparades och lästes tillbaka; 82 aktiva texter verifierades oförändrade. Samtliga 94 referenser matchar live efter synkning. Dessutom rättades 27 delade Husqvarna-mål retroaktivt och lästes tillbaka. Lokalise verifierade 144 TM-manifestposter (117 aktuella + 27 retroaktiva). Kanonisk TMX validerar med 28 288 enheter. `svlang` fann inga skrivregelfel; Hunspell-sv fick verifierade Automower-termer och produktnamn, 19/19 tester passerade. Nästa position: **39 977**; 37 620 aktiva poster återstår efter markören. Rapport och komplett radräkning: `2026-11-26-reviewed-core-39857-39976.md`. Granskningen fortsätter.


### Terminologikorrigering: Husqvarna GeoFence

Efter kontroll av Husqvarnas svenska dokumentation korrigerades fyra tidigare sparade händelse-/sensortexter: två feltexter för GeoFence och två för området utanför GeoFence. Textändringarna återlästes från Lokalise och skrevs retroaktivt över i den kanoniska HA Core-TM. Se `2026-11-26-husqvarna-geofence-terminology-correction.md`. swedish-foss-terminology har nu två kontextbundna Husqvarna-termer, och Hunspell-sv känner igen egennamnet GeoFence. Ingen ny verktygsrelease gjordes.


### Senaste batch: 39 977–40 096

119 aktuella nycklar (67 direkta källmatchningar och 52 referenser) samt en äldre nyckel granskades rad för rad. 33 slutliga textändringar sparades och återlästes; 86 aktiva mål verifierades utan slutlig textändring. Två förkonditioneringsetiketter återställdes till den tydligare ursprungliga formuleringen efter termkontroll. Alla 52 referenser matchar sina 32 mål live. Den historiska raden matchar exakt exporten 2026-11-24 och uteslöts ur TM. Alla 119 manifestposter API-verifierades; TMX validerar med 28 404 enheter. svlang 0 skrivregelfel; Hunspell-sv 19/19 tester; swedish-foss-terminology 20/20 tester. Teslas svenska dokumentation bekräftar ”förkonditionering”; termen lades till projektordlistan. Nästa position: **40 097**; 37 501 aktiva poster återstår efter markören. Rapport: `2026-11-26-reviewed-core-39977-40096.md`.

Terminologiverifiering av Husqvarna GeoFence ledde till en separat retroaktiv korrigering av fyra tidigare texter; Lokalise, TMX och verktygsordlistorna har synkats. Se `2026-11-26-husqvarna-geofence-terminology-correction.md`.


### Senaste batch: 40 097–40 216

113 aktuella nycklar (81 direkta och 32 referenser) samt sju källfrånvarande äldre poster granskades rad för rad. De sju äldre raderna matchar exakt 2026-11-24-snapshoten och uteslöts ur aktuell TM. 34 slutliga ändringar i intervallet sparades och återlästes; 79 aktiva texter verifierades utan slutlig ändring. Alla 32 referenser matchar live efter synkning. Ett tidigare oansenligt 1-Wire-alias (`Sensed {id}`) rättades retroaktivt till `Ingångskanal {id}` efter kontroll av dess fullständiga nyckel och Home Assistants beskrivning av insignalskanalen. Totalt 114 TM-manifestposter (113 aktuella + 1 retroaktiv) verifierades mot Lokalise. Kanonisk TMX validerar med 28 517 enheter och spegelkopian är byteidentisk. `svlang`: inga skrivregelfel; Hunspell-sv 19/19 tester; swedish-foss-terminology 20/20 tester. Termbanken fick nio HA-termer, bland annat kontextbundna Fyta-gränsvärden, RMS-mätvärden och 1-Wire-kanaler. Nästa position: **40 217**; 37 388 aktiva poster återstår efter markören. Rapport: `2026-11-26-reviewed-core-40097-40216.md`.


## Batch 92: 40 217–40 336

120 positioner granskade: 112 aktiva nycklar och 8 äldre poster som matchar exakt 2026-11-24-snapshoten. 18 ändringar sparade/återlästa; 94 aktiva mål verifierade. Alla 9 referenser till 8 mål matchar. Aktuellt TM-manifest: 112 aktiva poster; TMX validerad med 28 629 enheter.

## Batch 93: 40 337–40 456

120 positioner granskade: 84 aktiva nycklar och 36 snapshotmatchade äldre poster. 22 ändringar sparade/återlästa; 62 aktiva mål verifierade. Alla 25 referenser till 21 mål matchar.

## Batch 94: 40 457–40 576

120 positioner granskade: 108 aktiva nycklar och 12 snapshotmatchade poster. 19 ändringar sparade/återlästa; 89 aktiva mål verifierade. Alla 58 referenser till 45 mål matchar. TMX validerad med 28 815 enheter före nästa batch.

## Batch 95: 40 577–40 696

120 positioner granskade: 107 aktiva (36 direkta källmatchningar, 71 referenser) och 13 poster som matchar exakt 2026-11-24-snapshoten. 50 aktiva ändringar sparade/återlästa; 57 aktiva mål verifierade oförändrade. Alla 71 referenser till 32 mål matchar live. 13 snapshotposter exkluderade från aktuell TM. Därtill 9 retroaktiva delade Bayesian-mål/alias rättade och API-verifierade; totalt 59 sparade ändringar. 107 aktuella och 9 retroaktiva manifestposter synkade till TM; kanonisk TMX har 28 897 enheter (28 666 Lokalise-ID:n + 231 historiska poster), spegeln är identisk. `svlang`: inga skrivregelfel; termbank 20/20 tester; TMX-validator 8/8 tester och 0 valideringsfel. Nästa position: **40 697**; **36 844 aktiva positioner återstår**. Granskningen fortsätter.


## Batch 96: 40 697–40 816

120 positioner radgranskade: 102 aktuella Core-poster (88 direkta källmatchningar, 14 referenser) och 18 äldre snapshotmatchade poster. 47 slutliga ändringar inom intervallet sparades och lästes tillbaka; 55 aktiva texter verifierades utan ändring. Två äldre Bayesian-alternativ uppdaterades retroaktivt. Ett PoolDose-referenstarget utanför intervallet korrigerades och lästes tillbaka. Alla 14 aliasreferenser till 12 mål matchar live. Platshållare 120/120; inga pluraler. 104 aktiva/uppföljande manifestposter synkades till TMX; validerad med 28 994 enheter, spegeln är byteidentisk. Nästa position: **40 817**; 36 724 aktiva positioner återstår. Rapport: `2026-11-26-reviewed-core-40697-40816.md` och JSON-underlagen.


## Batch 97: 40 817–40 936

120 rader granskade: 110 aktuella (88 direkta källmatchningar och 22 referenser) samt 10 äldre poster som matchar exakt 2026-11-24-exporten. 34 slutliga ändringar sparades och återlästes; 76 aktiva mål verifierades utan slutlig ändring. MQTT-larmkoder och payload-fält rättades till konsekvent svenska; även Habitica-, Aladdin Connect-, Husqvarna-, Alexa- och AI Task-strängar förbättrades. Alla 22 referenser till 19 mål matchar live. Platshållare 120/120; inga pluraler. 110 aktuella poster uppdaterade i TMX, som validerar med 29 098 enheter; backupkopian är byteidentisk. `svlang`: inga skrivregelfel. Hunspell-ordlistan fick 20 granskade HA-termer med regressionsexempel. Nästa position: **40 937**; 36 604 aktiva positioner återstår. Rapport: `2026-11-26-reviewed-core-40817-40936.md` och JSON-underlagen.


## Batch 98: 40 937–41 056

120 positioner granskade: 118 aktuella Core-poster (97 direkta källmatchningar, 21 referenser) och två äldre poster som matchar exakt 2026-11-24-exporten. 35 aktiva texter korrigerades och återlästes; 83 aktiva mål verifierades utan ändring. En snapshotmatchad äldre MQTT-titel uppdaterades retroaktivt. Alla 21 referenser till 15 mål matchar live. Platshållare 120/120; inga pluraler. 118 aktuella och en separat source-path-follow-up-post uppdaterades i TM. TMX validerar med 29 215 enheter; backupkopian är identisk. ToGrill-källan visade att Taste gäller stekgrad; ”Mark A/B/C” är dokumenterade som osäkra etiketter eftersom källan inte förklarar dem. Nästa position: **41 057**; 36 484 aktiva positioner återstår. Rapport: `2026-11-26-reviewed-core-40937-41056.md` och JSON-underlagen.


### Senaste batch: 41 057–41 176

120 köpositioner radgranskade: 116 aktuella Core-poster (38 direkta källmatchningar och 78 referensnycklar), samt fyra äldre OTBR-poster som matchar exakt den arkiverade exporten 2026-11-24. 89 ändringar i intervallet och 38 retroaktiva mål-/aliasändringar sparades i Lokalise och lästes tillbaka; totalt 127 ändringar bland 157 unika Lokalise-poster. 26 ytterligare förslag verifierades oförändrade. Alla 78 referenskanter kontrollerade; platshållare 120/120, inga pluraler. `svlang skrivregler` fann inga fel. Aktuell Core-TMX innehåller 153 poster från batchens manifest och validerar med 29 353 enheter; spegeln är byteidentisk. Nästa position: **41 177**; 36 368 aktiva positioner återstår. Se `2026-11-26-reviewed-core-41057-41176.md` med JSON-underlagen.


### Senaste batch: 41 177–41 296

120 köpositioner radgranskade: 103 aktuella Core-poster (73 direkta källmatchningar och 30 referensnycklar), samt 17 äldre poster som matchar exakt arkiverad export 2026-11-24. 36 textändringar sparades i Lokalise och lästes tillbaka; 75 poster/targets verifierades oförändrade. Alla 30 referenskanter till 28 mål matchar efter synkning. Platshållare 120/120; inga pluralnycklar. `svlang skrivregler` fann inga fel. `hunspell-sv` fick rekommenderad pluralform `emojier` och sammansättningen `emojikortkoder` med regressioner; 19/19 verktygstester passerade. Kanonisk TMX innehåller 29 449 enheter och spegeln är byteidentisk. Ingen ny verktygsrelease gjordes eftersom en redan publicerats samma dag. Nästa position: **41 297**; 36 265 aktiva positioner återstår. Se `2026-11-26-reviewed-core-41177-41296.md` med JSON-underlagen.


### Senaste batch: 41 297–41 416

120 positioner radgranskade: 104 aktiva Core-poster och 16 äldre poster som matchar arkiverad export. 44 ändringar sparades i Lokalise och lästes tillbaka; 60 aktiva mål verifierades oförändrade. Alla 39 referenskanter matchar efter alias-synkning. Platshållare 104/104; inga pluralnycklar. `svlang skrivregler` fann inga fel. TMX validerar med 29 544 enheter (29 313 Lokalise-ID, 231 historiska), spegeln är byteidentisk. Osäker uppföljning: kontrollera IMEON-källstatusen `Grid unsynchronized but used` mot protokoll/enhetsvisning. Nästa position: **41 417**; 36 161 aktiva positioner återstår. Se `2026-11-26-reviewed-core-41297-41416.md` och JSON-underlagen.


### Senaste batch: 41 417–41 536

120 positioner radgranskade: 101 aktiva Core-poster (71 direkta källmatchningar och 30 referensnycklar) samt 19 äldre poster som matchar exakt Lokalise-snapshoten 2026-11-24. 29 aktiva ändringar sparades och återlästes; 72 texter verifierades oförändrade. Alla 30 referenser matchar efter synkning av alias, inklusive ett alias vars mål ändrades i samma batch. Platshållare 101/101; inga pluralnycklar. `svlang skrivregler` utan fel; hunspellgranskning krävde ingen ordboksändring. TMX validerar med 29 637 enheter (29 406 Lokalise-ID, 231 historiska) och spegeln är byteidentisk. Nästa position: **41 537**; 36 060 aktiva positioner återstår. Se `2026-11-26-reviewed-core-41417-41536.md` och JSON-underlagen.
