# Home Assistant Core – aktuell granskningsstatus

Senast uppdaterad: 2026-11-25

Aktuell Home Assistant Core-källrevision: 86a2eabe7e43f526db5821ef068087ce8404ae07

Lokalise-projekt: 130246255a974bd3b5e8a1.51616605

## Framsteg

- Senast fullständigt radgranskade Lokalise-position: **28 170**. Fortsätt från **28 171** och jämför varje batch mot aktuell källtext och tidigare rapporter.
- De sammanhängande intervallen 27 211–28 170 innehåller 960 positioner: 766 nycklar som finns i aktuell Core-källa och 194 historiska källfrånvarande poster.
- Bland de 766 aktuella nycklarna har **225 svenska texter ändrats och sparats/återlästs** i Lokalise; resterande **541 aktuella texter har granskats och återverifierats utan språkändring**.
- Den senaste batchen 27 691–27 810 innehöll 102 aktuella Core-nycklar: **31** språkändringar och **71** befintliga översättningar utan ändring. 18 äldre nycklar saknas i aktuell Core-källa och redovisas separat.
- 13 referenser i den senaste batchen jämfördes mot live-målen; 13/13 svenska värden matchar.
- En tidigare verifierad OpenEVSE-post utanför intervallet (component::openevse::entity::switch::current_shaper::name) korrigerades retroaktivt från Strömformare till Laststyrning; den tidigare TMX-enheten ersattes. Samma term används i de tre Shaper-sensorsammanhangen.

## Fortsatt radgranskning 2026-11-25 – position 27811–28020

Tre tidigare rapporter hade redan radgranskat intervallet och innehöll osparade förslag. Samtliga 210 positioner jämfördes mot aktuell Core-revision; 107 matchar aktuell källa och 103 är historiska källfrånvarande poster. Femton giltiga måltextförslag sparades och lästes tillbaka via Lokalise API; 92 befintliga aktuella mål verifierades utan språkändring. 29 referensalias jämfördes live med sina mål och samtliga matchar. Sex gamla `condition_behavior::options::any`-förslag saknar aktuell Core-nyckel och har hållits utanför TM. TMX-manifestets samtliga 107 nyckelidentiteter, engelska källor och svenska mål verifierades live med Lokalise API. Rapport och manifest: `2026-11-25-reviewed-core-27811-28020.md`, `2026-11-25-reviewed-core-27811-28020-changes.json`, `2026-11-25-reviewed-core-27811-28020-references.json` och `2026-11-25-reviewed-core-27811-28020-tm.json`.

## Fortsatt radgranskning 2026-11-25 – position 28021–28050

Den aktuella Lokalise-ordningen gav 30 nyckelposter efter position 28020. 29 matchar Core-källrevision `86a2eabe7e43f526db5821ef068087ce8404ae07`; 10 svenska mål ändrades och lästes tillbaka, 19 verifierades oförändrade. En äldre Ondilo-nyckel finns inte längre i Core-källan och uteslöts. Sexton referensalias matchar live-målen. Verktygsstödet kompletterades med `Inverter` → `växelriktare` i HA-terminologin samt `växelriktarström` och WaterFurnace-former i Hunspell-sv. TMX-manifestet för 29 aktuella poster verifierades live. Se `2026-11-25-reviewed-core-28021-28050.md` med JSON-underlag.

## TM och verktyg

- Home Assistant Core-kanonisk TMX är uppdaterad till position 28170 samt med den retroaktiva OpenEVSE-termposten. XML/proveniensvalideraren godkände **18 971** enheter; 18 740 har Lokalise-ID och 231 är historiska poster utan sådant ID. Varje batchpost anger nu också den exakta Core-källrevisionen i verifieringsproveniensen.
- swedish-foss-terminology innehåller fyra projektspecifika HA-termer för OpenEVSE, ViCare, USB-dongel och Tibbers hushållsnod. Exporterna CSV/TBX/JSONL validerades; Tibber-tolkningen är markerad som källbaserad slutsats med uppföljning.
- Hunspell-sv har ytterligare Tibber, OpenAI och Proxmox som godkända egennamn i båda ordböckerna och referenslistan. Deklarerade poster kontrollerades. Verktygsrelease har inte gjorts.
- svlang skrivregler fann inga skrivregelavvikelser i senaste batchen. Platshållarkontrollen fann 0 avvikelser av 90.

## Kvarstående hinder och uppföljning

- Lokalise API-tokenen får ändra översättningstexter men får HTTP 403 (No permission to update translation status) för att sätta is_reviewed. Ingen browser är tillgänglig i den här chatten. Därför har ändrade mål sparats, men Lokalises separata Reviewed-markering kunde inte sättas.
- Den fullständiga Core-inventeringen från 2026-11-25 fann **203 aktuella Core-källnycklar som saknas helt i Lokalise**. API-anropen för att skapa nycklar/importera fil avslogs med HTTP 403; den listan finns i 2026-11-25-full-core-missing-audit.md. Detta blockerar 100 % lokaliseringsomfattning oberoende av radgranskningen.
- Totalt 194 källfrånvarande positioner i de hittills granskade intervallen har inte räknats som aktuell Core-täckning. Tidigare rapporter identifierar äldre HDFury- och frontend-/historiknycklar som kräver eventuell separat korsmappning.
- Granskningen är **inte klar**. Nästa steg är fortsätta rad för rad från Lokalise-position 28 171, upptäcka nytillkomna strängar, matcha gamla rapporter via fullständig nyckel, spara ändringar direkt i Lokalise och synkronisera kanonisk TMX löpande.


## Fortsatt radgranskning 2026-11-25 – position 28051–28170

90/120 poster matchade Core-källrevisionen och granskades; 46 mål ändrades och lästes tillbaka, 44 behölls. 30 källfrånvarande poster hålls utanför TM. 20 referensalias verifierades, en avvikelse synkades. Platshållare 90/90; inga pluralformsposter. Se `2026-11-25-reviewed-core-28051-28170.md` och dess JSON-underlag. TM-manifestets 90 poster är liveverifierade; kanonisk TMX validerar med 18 971 enheter. Tibbers `load`-tolkning som hushållsnod är källbaserad men inväntar eventuell formell bekräftelse från Tibber.

## Fortsatta hinder

- Lokalise-API:t nekar fortfarande uppdatering av `is_reviewed` med HTTP 403; översättningstexterna kan sparas och återläsas.
- 203 Core-källnycklar saknas i Lokalise; key/import-skapande har tidigare nekats med HTTP 403.
- Granskningen är inte klar. Nästa liveposition är 28 171.
