# Home Assistant Core – aktuell granskningsstatus

Senast uppdaterad: 2026-11-25

Aktuell Home Assistant Core-källrevision: 86a2eabe7e43f526db5821ef068087ce8404ae07

Lokalise-projekt: 130246255a974bd3b5e8a1.51616605

## Framsteg

- Senast fullständigt radgranskade Lokalise-position: **28 020**. Fortsätt från **28 021** och jämför varje batch mot aktuell källtext och tidigare rapporter.
- De sammanhängande intervallen 27 211–28 020 innehåller 810 positioner: 647 nycklar som finns i aktuell Core-källa och 163 historiska källfrånvarande poster.
- Bland de 647 aktuella nycklarna har **169 svenska texter ändrats och sparats/återlästs** i Lokalise; resterande **478 aktuella texter har granskats och återverifierats utan språkändring**.
- Den senaste batchen 27 691–27 810 innehöll 102 aktuella Core-nycklar: **31** språkändringar och **71** befintliga översättningar utan ändring. 18 äldre nycklar saknas i aktuell Core-källa och redovisas separat.
- 13 referenser i den senaste batchen jämfördes mot live-målen; 13/13 svenska värden matchar.
- En tidigare verifierad OpenEVSE-post utanför intervallet (component::openevse::entity::switch::current_shaper::name) korrigerades retroaktivt från Strömformare till Laststyrning; den tidigare TMX-enheten ersattes. Samma term används i de tre Shaper-sensorsammanhangen.

## Fortsatt radgranskning 2026-11-25 – position 27811–28020

Tre tidigare rapporter hade redan radgranskat intervallet och innehöll osparade förslag. Samtliga 210 positioner jämfördes mot aktuell Core-revision; 107 matchar aktuell källa och 103 är historiska källfrånvarande poster. Femton giltiga måltextförslag sparades och lästes tillbaka via Lokalise API; 92 befintliga aktuella mål verifierades utan språkändring. 29 referensalias jämfördes live med sina mål och samtliga matchar. Sex gamla `condition_behavior::options::any`-förslag saknar aktuell Core-nyckel och har hållits utanför TM. TMX-manifestets samtliga 107 nyckelidentiteter, engelska källor och svenska mål verifierades live med Lokalise API. Rapport och manifest: `2026-11-25-reviewed-core-27811-28020.md`, `2026-11-25-reviewed-core-27811-28020-changes.json`, `2026-11-25-reviewed-core-27811-28020-references.json` och `2026-11-25-reviewed-core-27811-28020-tm.json`.

## TM och verktyg

- Home Assistant Core-kanonisk TMX är uppdaterad med 102 poster från position 27691–27810, 107 poster från position 27811–28020 och den retroaktiva OpenEVSE-termposten. XML/proveniensvalideraren godkände **18 854** enheter; 18 623 har Lokalise-ID och 231 är historiska poster utan sådant ID. Varje batchpost anger nu också den exakta Core-källrevisionen i verifieringsproveniensen.
- swedish-foss-terminology fick ett projektspecifikt OpenEVSE-beslut: Current shaper → Laststyrning, med hänvisning till OpenEVSE-dokumentationen. Termbanken exporterades och rundresevaliderades.
- Hunspell-sv fick push-uppdateringar i huvud- och expanded-ordlistorna med regressionsterm; ordlistornas deklarerade antal matchar posterna. Ingen release har gjorts.
- svlang skrivregler fann inga skrivregelavvikelser bland batchens ändrade mål. Platshållarkontrollen fann 0 avvikelser.

## Kvarstående hinder och uppföljning

- Lokalise API-tokenen får ändra översättningstexter men får HTTP 403 (No permission to update translation status) för att sätta is_reviewed. Ingen browser är tillgänglig i den här chatten. Därför har ändrade mål sparats, men Lokalises separata Reviewed-markering kunde inte sättas.
- Den fullständiga Core-inventeringen från 2026-11-25 fann **203 aktuella Core-källnycklar som saknas helt i Lokalise**. API-anropen för att skapa nycklar/importera fil avslogs med HTTP 403; den listan finns i 2026-11-25-full-core-missing-audit.md. Detta blockerar 100 % lokaliseringsomfattning oberoende av radgranskningen.
- Totalt 163 källfrånvarande positioner i de hittills granskade intervallen har inte räknats som aktuell Core-täckning. Tidigare rapporter identifierar äldre HDFury- och frontend-/historiknycklar som kräver eventuell separat korsmappning.
- Granskningen är **inte klar**. Nästa steg är fortsätta rad för rad från Lokalise-position 28 021, upptäcka nytillkomna strängar, spara ändringar direkt i Lokalise och synkronisera kanonisk TMX löpande.
