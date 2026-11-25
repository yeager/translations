# Home Assistant Core – aktuell granskningsstatus

Senast uppdaterad: 2026-11-25

Aktuell Home Assistant Core-källrevision: 86a2eabe7e43f526db5821ef068087ce8404ae07

Lokalise-projekt: 130246255a974bd3b5e8a1.51616605

## Framsteg

- Senast fullständigt radgranskade Lokalise-position: **28 890**. Fortsätt från **28 891** och jämför varje batch mot aktuell källtext och tidigare rapporter.
- De sammanhängande intervallen 27 211–28 890 innehåller 1 680 positioner: 1 382 nycklar som finns i aktuell Core-källa och 298 historiska källfrånvarande poster.
- Bland de 1 382 aktuella nycklarna har **430 svenska texter ändrats och sparats/återlästs** i Lokalise; resterande **952 aktuella texter har granskats och återverifierats utan språkändring**. Därutöver har fyra LG ThinQ-referensmål korrigerats retroaktivt och dokumenterats separat.
- Den senaste batchen 27 691–27 810 innehöll 102 aktuella Core-nycklar: **31** språkändringar och **71** befintliga översättningar utan ändring. 18 äldre nycklar saknas i aktuell Core-källa och redovisas separat.
- 13 referenser i den senaste batchen jämfördes mot live-målen; 13/13 svenska värden matchar.
- En tidigare verifierad OpenEVSE-post utanför intervallet (component::openevse::entity::switch::current_shaper::name) korrigerades retroaktivt från Strömformare till Laststyrning; den tidigare TMX-enheten ersattes. Samma term används i de tre Shaper-sensorsammanhangen.

## Fortsatt radgranskning 2026-11-25 – position 27811–28020

Tre tidigare rapporter hade redan radgranskat intervallet och innehöll osparade förslag. Samtliga 210 positioner jämfördes mot aktuell Core-revision; 107 matchar aktuell källa och 103 är historiska källfrånvarande poster. Femton giltiga måltextförslag sparades och lästes tillbaka via Lokalise API; 92 befintliga aktuella mål verifierades utan språkändring. 29 referensalias jämfördes live med sina mål och samtliga matchar. Sex gamla `condition_behavior::options::any`-förslag saknar aktuell Core-nyckel och har hållits utanför TM. TMX-manifestets samtliga 107 nyckelidentiteter, engelska källor och svenska mål verifierades live med Lokalise API. Rapport och manifest: `2026-11-25-reviewed-core-27811-28020.md`, `2026-11-25-reviewed-core-27811-28020-changes.json`, `2026-11-25-reviewed-core-27811-28020-references.json` och `2026-11-25-reviewed-core-27811-28020-tm.json`.

## Fortsatt radgranskning 2026-11-25 – position 28021–28050

Den aktuella Lokalise-ordningen gav 30 nyckelposter efter position 28020. 29 matchar Core-källrevision `86a2eabe7e43f526db5821ef068087ce8404ae07`; 10 svenska mål ändrades och lästes tillbaka, 19 verifierades oförändrade. En äldre Ondilo-nyckel finns inte längre i Core-källan och uteslöts. Sexton referensalias matchar live-målen. Verktygsstödet kompletterades med `Inverter` → `växelriktare` i HA-terminologin samt `växelriktarström` och WaterFurnace-former i Hunspell-sv. TMX-manifestet för 29 aktuella poster verifierades live. Se `2026-11-25-reviewed-core-28021-28050.md` med JSON-underlag.

## TM och verktyg

- Home Assistant Core-kanonisk TMX är uppdaterad till position 28890, retroaktiva LG ThinQ-, OpenEVSE-, Open Router- och Fressnapf-referensmål. XML/proveniensvalideraren godkände **19 571** enheter; 19 340 har Lokalise-ID och 231 är historiska poster utan sådant ID. Varje batchpost anger nu också den exakta Core-källrevisionen i verifieringsproveniensen.
- swedish-foss-terminology innehåller åtta projektspecifika HA-termer för OpenEVSE, ViCare, USB-dongel, Tibbers hushållsnod, Matter-temperaturavvikelse, Yardians tryckslag, HDFurys hotplug-knapp och KNX-termen datapunkttyp. Exporterna CSV/TBX/JSONL validerades; termbankens 20 tester passerade. Tibber-tolkningen är markerad som källbaserad slutsats med uppföljning.
- Hunspell-sv innehåller HA-termerna och hårdvaruidentifierarna från granskningen, däribland Tibber, OpenAI, Proxmox, SMA, Namecheap, HDFury, `upptäckbar` och `inomhusluftkvalitet`. Ordboksräknarna och stavningskontrollen verifierades. Deklarerade poster kontrollerades. Hunspell-sv validerades och släpptes som `v2026.11.25`; PyPI-publiceringen lyckades. swedish-foss-terminology-exporter validerades och uppdaterades.
- svlang skrivregler fann inga skrivregelavvikelser i senaste batchen. Platshållarkontrollen fann 0 avvikelser av 120 i senaste batchen.

## Kvarstående hinder och uppföljning

- Lokalise API-tokenen får ändra översättningstexter men får HTTP 403 (No permission to update translation status) för att sätta is_reviewed. Ingen browser är tillgänglig i den här chatten. Därför har ändrade mål sparats, men Lokalises separata Reviewed-markering kunde inte sättas.
- Den fullständiga Core-inventeringen från 2026-11-25 fann **203 aktuella Core-källnycklar som saknas helt i Lokalise**. API-anropen för att skapa nycklar/importera fil avslogs med HTTP 403; den listan finns i 2026-11-25-full-core-missing-audit.md. Detta blockerar 100 % lokaliseringsomfattning oberoende av radgranskningen.
- Totalt 298 källfrånvarande positioner i de hittills granskade intervallen har inte räknats som aktuell Core-täckning. Tidigare rapporter identifierar äldre HDFury- och frontend-/historiknycklar som kräver eventuell separat korsmappning.
- Granskningen är **inte klar**. Nästa steg är fortsätta rad för rad från Lokalise-position 28 891, upptäcka nytillkomna strängar, matcha gamla rapporter via fullständig nyckel, spara ändringar direkt i Lokalise och synkronisera kanonisk TMX löpande.


## Fortsatt radgranskning 2026-11-25 – position 28051–28170

90/120 poster matchade Core-källrevisionen och granskades; 46 mål ändrades och lästes tillbaka, 44 behölls. 30 källfrånvarande poster hålls utanför TM. 20 referensalias verifierades, en avvikelse synkades. Platshållare 90/90; inga pluralformsposter. Se `2026-11-25-reviewed-core-28051-28170.md` och dess JSON-underlag. TM-manifestets 90 poster är liveverifierade; kanonisk TMX validerar med 18 971 enheter. Tibbers `load`-tolkning som hushållsnod är källbaserad men inväntar eventuell formell bekräftelse från Tibber.

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
