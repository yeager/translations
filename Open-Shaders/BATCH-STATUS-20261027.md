# Open Shaders: lokal batchstatus 2026-10-27

Den aktuella engelska och svenska JSON-katalogen hämtades den 27 oktober
2026. Den svenska katalogen hade 5 140 strängar: 1 238 översatta och 3 902
tomma. Weblate-komponenten var låst och inga ändringar kunde skickas upp.

De 169 komponentvisa JSON-filerna med datumet 2026-10-27 omfattar 2 142 unika
källnycklar. Varje fil har kontrollerats mot den engelska katalogen före
arkivering. För filer med formatmarkörer har motsvarande markörer jämförts.
L10n-lint, svensk språkgranskning, Hunspell-genomgång, JSON-syntax och
Gitleaks har körts för respektive häfte.

Den 27 oktober jämfördes dessutom samtliga 367 aktuella nycklar i
`feature.effects11` med Open Shaders-arkivet. Alla 367 finns arkiverade utan
saknade eller extra nycklar. Denna kontroll säger endast att underlaget är
helt; varje delta ska fortfarande jämföras med en ny Weblate-export före
import efter upplåsningen.

Samma dag jämfördes även samtliga 96 aktuella nycklar i
`feature.exp_height_fog` med arkivet. Alla 96 finns arkiverade utan saknade
eller extra nycklar. Komponenten behöver på samma sätt en ny exportjämförelse
före import efter upplåsningen.

Kontrollen omfattar också två mindre komponenter: `feature.reverse_z` är
fullständig med 10 av 10 nycklar, och `feature.foliage_lighting` med 17 av
17. Inga nycklar saknas i respektive arkivjämförelse.

Menyn `menu.performance` är också fullständig med 24 av 24 nycklar i två
separata små häften. Inga nycklar saknas i arkivjämförelsen.

`feature.grass_optimizations` är fullständig med 45 av 45 nycklar.
`menu.home` är fullständig med 49 av 49 nycklar.
`menu.features` är fullständig med 54 av 54 nycklar.
`feature.vr` är fullständig med 58 av 58 nycklar.
`feature.skin` är fullständig med 61 av 61 nycklar.

`feature.sky_sync` är fullständig med 68 av 68 nycklar. De sex häftena har
sammanfogats lokalt och kontrollerats som en helhet: JSON, L10n-lint,
Gitleaks och formatmarkörer är godkända. Arkivjämförelsen visar 68 av 68
nycklar, utan saknade eller extra nycklar.

`feature.fur_shells` är fullständig med 73 av 73 nycklar. De sju häftena har
sammanfogats lokalt och kontrollerats som en helhet: JSON, L10n-lint,
Gitleaks och formatmarkörer är godkända. Arkivjämförelsen visar 73 av 73
nycklar, utan saknade eller extra nycklar.

Häftena 26–168 omfattar 1 725 av dessa nycklar. De är inte dubbletter av redan
arkiverade källnycklar, med undantag för Regndroppars ljusbrytning (häfte 29),
som är en dokumenterad språklig kvalitetshöjning av en äldre lokal version.

Samtliga 73 aktuella nycklar i `feature.snow_cover` är granskade och
arkiverade, utan saknade eller extra nycklar och utan avvikande formatmarkörer.

Samtliga 110 aktuella nycklar i `feature.weather_picker` är granskade och
arkiverade, utan saknade eller extra nycklar och utan avvikande formatmarkörer.

Samtliga 81 aktuella nycklar i `menu.issues` är granskade och arkiverade, utan
saknade eller extra nycklar och utan avvikande formatmarkörer.

Den enda aktuella nyckeln i `menu.features` är också granskad och arkiverad.

Samtliga 247 aktuella nycklar i `menu.settings` finns nu i arkivet, utan
saknade eller extra nycklar och utan avvikande formatmarkörer. De åtta nya
häftena omfattar de 119 nycklar som saknades vid denna genomgång.

Samtliga 144 aktuella nycklar i `feature.light_editor` är granskade och
arkiverade. De nio häftena har sammanfogats och jämförts med källkatalogen:
144 av 144 nycklar finns, utan saknade eller extra nycklar och utan avvikande
formatmarkörer eller radbrytningar. L10n-lint och Gitleaks är godkända för den
sammanslagna komponenten.

Samtliga 152 aktuella nycklar i `feature.perf_overlay` är granskade och
arkiverade. De tio häftena har sammanfogats och jämförts med källkatalogen:
152 av 152 nycklar finns, utan saknade eller extra nycklar och utan avvikande
formatmarkörer, bokstavliga procenttecken eller radbrytningar. L10n-lint och
Gitleaks är godkända för den sammanslagna komponenten.

För `menu.advanced` har de fem första häftena granskats: 80 av 157 nycklar. De
återstående 77 nycklarna behöver samma radvisa granskning.

Open Shaders uppfyller färskhetskravet genom den officiella utgåvan `v2.19.0`
från 18 oktober 2026. Nästa steg är att importera de komponentvisa filerna
när Weblate-komponenten har låsts upp.
