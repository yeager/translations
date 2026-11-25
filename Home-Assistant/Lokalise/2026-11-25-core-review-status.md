# Home Assistant Core – aktuell granskningsstatus

Senast uppdaterad: 2026-11-25

Aktuell Home Assistant Core-källrevision: 86a2eabe7e43f526db5821ef068087ce8404ae07

Lokalise-projekt: 130246255a974bd3b5e8a1.51616605

## Aktuellt läge

- Senast fullständigt behandlade Lokalise-position: **33 016**. Positionerna 29 611–30 616 var tidigare granskade och live-verifierades igen; intervallen 30 617–33 016 har nu granskats rad för rad. Nästa position att kontrollera mot tidigare fullnyckelrapporter: **33 017**.
- Kumulativa statusräkningar: **4 043** unika aktuella Core-nycklar och **599** källfrånvarande/historiska poster; 18 redan granskade aktiva nycklar i de fem senaste intervallen återverifierades. Tidigare rapporterade fullständiga nycklar spåras separat från nya positionsintervall.
- Av de 4 043 unika aktuella Core-nycklarna ändrades **1 069** mål inom de granskade intervallen och **2 974** verifierades oförändrade. Nio ytterligare aktiva mål synkades retroaktivt utanför intervallen. Totalt **1 078** aktiva ändringar har sparats och lästs tillbaka, inklusive de nio retroaktiva målen. En historisk, källfrånvarande sträng har också korrigerats och dokumenterats men räknas inte in i aktiv Core-täckning.
- Batchen 29 131–29 250: 120/120 nycklar aktiva och källmatchande; **17** ändringar sparade och återlästa, **103** texter oförändrade. Nästa batch 29 251–29 370: 85 aktuella Core-nycklar granskade utan ändring och 35 källfrånvarande poster uteslutna. Batchen 29 371–29 490: 54 aktiva Core-nycklar, 2 ändringar, 52 oförändrade; 66 källfrånvarande. Batchen 29 491–29 610: 95 aktiva Core-nycklar, ett OpenAI-referensalias synkat, 94 oförändrade; 25 källfrånvarande. Batchen 30 617–30 736: 104 aktiva Core-nycklar, 31 ändringar och 73 oförändrade; 16 källfrånvarande. Batchen 30 737–30 856: 110 aktuella nycklar, varav två överlappande återverifierades; 33 nya ändringar och 75 oförändrade bland de 108 nya aktiva posterna; 10 källfrånvarande. 31/31 aliasmål matchar live efter synkning. Batchen 30 857–30 976: 115 aktuella nycklar, varav två tidigare granskade återverifierades; 6 ändringar och 107 oförändrade bland 113 nya aktiva poster; 5 källfrånvarande. 24/24 aliasmål matchar. Platshållare 115/115; inga pluraler. Batchen 30 977–31 096: 96 aktuella nycklar, varav 12 tidigare granskade återverifierades; 11 ändringar och 73 oförändrade bland de 84 nya aktiva posterna; 24 källfrånvarande. 23/23 aliasmål matchar. Platshållare 96/96; inga pluraler. Batchen 31 097–31 216: 120/120 aktuella nycklar, sju fanns i tidigare dokumentation; 35 förbättringar sparades och lästes tillbaka, 85 poster verifierades oförändrade. Sex tidigare TM-värden för ZHA-energifaser rättades. Inga alias, pluraler eller platshållaravvikelser. Batchen 31 217–31 336: 110 aktuella nycklar och 10 källfrånvarande; 14 förbättringar sparades och 96 mål verifierades oförändrade. 68/68 alias matchar live; platshållare 110/110; inga pluraler. Batchen 31 337–31 456: 110 aktuella nycklar, varav 14 återverifierade från tidigare rapporter; 41 korrigeringar och 65 oförändrade bland 106 nya aktiva. Tio redan kända historiska nycklar uteslöts. Alla 13 alias matchar live. Två Synology-referensmål korrigerades retroaktivt. Batchen 31 457–31 576: 108 aktuella nycklar, varav sju återverifierades från tidigare rapporter; 14 ändringar och 87 oförändrade bland 101 nya aktiva. Tolv tidigare rapporterade historiska nycklar uteslöts. Alla 17 alias matchar live; platshållare 108/108; inga pluraler.
- Liveverifiering för batchen bekräftade nyckelidentitet, engelsk källtext, svensk måltext och Lokalise-ID för 120/120 poster. Rapporten innehåller fullständiga nycklar och raderna med befintlig/föreslagen text.

## TM och verktyg

- Home Assistant Core kanonisk TMX validerar nu med **21 984** enheter: 21 753 med Lokalise-ID och 231 historiska poster utan Lokalise-ID. Granskningen 31 937–32 056 tillför 530 enheter netto över de fem senaste batcherna; batcherna uppdaterade sammanlagt 14 befintliga ID-poster. Batcherna 30617–30736, 30737–30856, 30857–30976 och 30977–31096, 31097–31216, 31217–31336, 31337–31456, 31457–31576, 31577–31696, 31697–31816, 31817–31936, 31937–32056, 32057–32176, 32177–32296, 32297–32416, 32417–32536, 32537–32656, 32657–32776, 32777–32896, 32897–33016 samt retroaktiva PoolDose-, KNX- och Synology-nycklar har verifierade manifest; befintliga TM-värden skrevs över där de avvek från granskad och sparad svenska.
- Rapporter och manifest: `2026-11-25-reviewed-core-29131-29250.md` och `2026-11-25-reviewed-core-29251-29370.md`, med respektive JSON-underlag. Den äldre rapportens missade KNX-förslag för `component::knx::config_panel::dpt::options::14_004` följdes upp via fullständig nyckel och sparades som `Substansmängd`; TM-posten uppdaterades retroaktivt.
- KNX-terminologi jämfördes mot KNX Associations System Specifications. Hunspell-sv:s båda ordböcker fick stöd för `ASCII`, `Deltatid`, `Kompressibilitet`, `Magnetomotorisk`, `deltavolym`, `usb-dongel` och `Turboläge`. Philips svensk dokumentation belägger `deltavolym` och `Turboläge`; `usb-dongel` är användargodkänd. Regressionstesterna passerade **19/19**; ingen extra release gjordes.
- `svlang skrivregler` fann inga skrivregelavvikelser i någon av de två senaste batcherna. I 29251–29370 rapporterade svlang en falskt positiv V2-varning för bisatsen “när ... passerar”. Hunspell flaggade bara fragmenten `daily`, `hourly` och `link` inuti dokumentationsplatshållare; de är inte svensk måltext.
- Termbanken swedish-foss-terminology användes som stöd: dess befintliga svenska TM innehåller bland annat “deltatider” och “rörelsemängdsmoment”.

## Senaste batch: 31 697–31 816

120/120 strängar matchade Home Assistant Core-källrevisionen och ingen fullständig nyckel förekom i tidigare rapporter. 56 ändringar sparades och lästes tillbaka; 64 översättningar verifierades oförändrade. Alla 120 manifestposter liveverifierades mot Lokalise. Platshållare 120/120; inga pluraler eller referenser. TMX validerar med 20 991 enheter. Home Connects officiella programdokumentation verifierade bland annat ugnsjäsning, luftfuktighet och diskmaskinsprogram. 16 enheter fick korrekt gradtecken. svlang-test 16/16, Hunspell-sv 19/19. Se `2026-11-25-reviewed-core-31697-31816.md` och JSON-underlagen.

## Senaste batch: 31 817–31 936

94/120 poster har aktiv Core-källtext; 26 källfrånvarande poster återfanns i tidigare dokumentation. 37 mål korrigerades och lästes tillbaka; 57 verifierades oförändrade, och ett tidigare aktivt granskat mål återverifierades. Nio aliasreferenser matchar sina live-mål. Platshållare 94/94, inga pluraler. Alla 94 manifestposter verifieras via Lokalise API. TMX validerar med 21 084 enheter. svlang har noll träffar; Hunspell-sv:s 19 tester passerar. Home Connects API-dokumentation kontrollerade bland annat relativa start-/sluttider, kaffebryggning, vatten/kaffekontakttid och diskprogram. Se `2026-11-25-reviewed-core-31817-31936.md` och JSON-underlagen.

## Kvarstående hinder

- Lokalise API-tokenen saknar behörighet att sätta `is_reviewed` (tidigare HTTP 403). Textändringar kan sparas och verifieras. Ingen separat Reviewed-markering har därför kunnat sättas.
- Inventeringen 2026-11-25 fann **203 aktuella Core-källnycklar som saknas helt i Lokalise**. Skapande/import av nycklar avslogs tidigare med HTTP 403; se `2026-11-25-full-core-missing-audit.md`.
- Totalt **489** källfrånvarande poster i de nygranskade intervallen räknas inte som aktuell Core-täckning. Ett ytterligare överlapp 29 611–30 616 återverifierades separat: 742 aktiva mål matchar TM och 264 saknar aktiv Core-källväg.
- Granskningen är **inte klar**. Fortsätt från position 31 937; kontrollera nyttillkomna strängar, tidigare rapporter, referenser och hela källinventeringen.

## Senaste batch: 31 457–31 576

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

## TM och verktyg

- Home Assistant Core-kanonisk TMX är uppdaterad till position 29130, retroaktiva LG ThinQ-, OpenEVSE-, Open Router- och Fressnapf-referensmål. XML/proveniensvalideraren godkände **19 800** enheter; 19 569 har Lokalise-ID och 231 är historiska poster utan sådant ID. Varje batchpost anger nu också den exakta Core-källrevisionen i verifieringsproveniensen.
- swedish-foss-terminology innehåller åtta projektspecifika HA-termer för OpenEVSE, ViCare, USB-dongel, Tibbers hushållsnod, Matter-temperaturavvikelse, Yardians tryckslag, HDFurys hotplug-knapp och KNX-termen datapunkttyp. Exporterna CSV/TBX/JSONL validerades; termbankens 20 tester passerade. Tibber-tolkningen är markerad som källbaserad slutsats med uppföljning.
- Hunspell-sv innehåller HA-termerna och hårdvaruidentifierarna från granskningen, däribland Tibber, OpenAI, Proxmox, SMA, Namecheap, HDFury, `upptäckbar`, `inomhusluftkvalitet`, `skåptorrt`, `stryktorrt`, `XL-kaffe`, `nattdisk`, `försköljning`, `kaffemaskinprogram` och `spoltryck`. Ordboksräknarna och stavningskontrollen verifierades. Deklarerade poster kontrollerades. Hunspell-sv validerades och släpptes som `v2026.11.25`; PyPI-publiceringen lyckades. swedish-foss-terminology-exporter validerades och uppdaterades.
- svlang skrivregler fann inga skrivregelavvikelser i senaste batcherna; en regressionstestad regel flaggar felaktigt ordningstecken (º) i temperaturvärden. Platshållarkontrollen fann 0 avvikelser av 120 i senaste batchen.

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
