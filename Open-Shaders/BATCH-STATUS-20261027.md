# Open Shaders: lokal batchstatus 2026-10-27

Den aktuella engelska och svenska JSON-katalogen hämtades den 27 oktober
2026. Den svenska katalogen hade 5 140 strängar: 1 238 översatta och 3 902
tomma. Weblate-komponenten var låst och inga ändringar kunde skickas upp.

De 207 komponentvisa JSON-filerna med datumet 2026-10-27 omfattar 2 734 unika
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
fullständig med 10 av 10 nycklar och `feature.foliage_lighting` med 17 av
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

Häftena 26–206 omfattar 2 317 av dessa nycklar. De är inte dubbletter av redan
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

Samtliga 170 aktuella nycklar i `feature.scene_manager` är granskade och
arkiverade. De elva häftena har sammanfogats och jämförts med källkatalogen:
170 av 170 nycklar finns, utan saknade eller extra nycklar och utan avvikande
formatmarkörer, bokstavliga procenttecken eller radbrytningar. `l10n-lint` och
Gitleaks är godkända för den sammanslagna komponenten. Se även
[integrationsgranskningen](SCENE-MANAGER-INTEGRATION-REVIEW-20261027.md).

Samtliga 201 aktuella nycklar i `feature.wetness_effects` är granskade och
arkiverade i 13 häften. Den sammanslagna komponenten har jämförts med källan:
201 av 201 nycklar finns, utan saknade eller extra nycklar och utan avvikande
formatmarkörer, bokstavliga procenttecken eller radbrytningar. JSON-syntax,
`l10n-lint` och Gitleaks är godkända. Se även
[integrationsgranskningen](WETNESS-EFFECTS-INTEGRATION-REVIEW-20261027.md).

Samtliga 326 aktuella nycklar i `feature.light_limit_fix` är granskade och
arkiverade i 21 små häften samt i en sammanslagen komponentfil. De jämförda
nyckeluppsättningarna är identiska utan saknade eller extra nycklar och utan
avvikande formatmarkörer, bokstavliga procenttecken eller radbrytningar.
JSON-syntax, `l10n-lint` och Gitleaks är godkända för komponenten. Se
[integrationsgranskningen](LIGHT-LIMIT-FIX-INTEGRATION-REVIEW-20261027.md).

`feature.wind` är fullständig med 279 av 279 aktuella nycklar i 17 små
häften samt en sammanslagen komponentfil. Varje häfte har validerats med JSON-syntax,
`l10n-lint`, `svlang`, Hunspell-genomgång, Gitleaks och kontroll av
formatmarkörer, radbrytningar samt tre lika konsonanter i följd. `svlang` kan
markera tekniska sammansättningar och fullständiga svenska satser som möjliga
V2-avvikelser; dessa signaler har lästs och bedömts manuellt. Se även
[integrationsgranskningen](WIND-INTEGRATION-REVIEW-20261027.md).

Samtliga 157 aktuella nycklar i `menu.advanced` är granskade och arkiverade.
De tio häftena har sammanfogats och jämförts med källkatalogen: 157 av 157
nycklar finns, utan saknade eller extra nycklar och utan avvikande
formatmarkörer, bokstavliga procenttecken eller radbrytningar. L10n-lint och
Gitleaks är godkända för den sammanslagna komponenten.

Open Shaders uppfyller färskhetskravet genom den officiella utgåvan `v2.19.0`
från 18 oktober 2026. Nästa steg är att importera de komponentvisa filerna
när Weblate-komponenten har låsts upp.

Den 29 oktober tillkom första häftet för `feature.upscaling`, med 27
grundläggande nycklar för DLSS-förinställningar, skärpning och
bildgenerering. Det finns i
`open-shaders-upscaling-basics-01-sv-20261029.json` och är validerat mot den
lokala engelska katalogen. Det får importeras först efter en ny
exportjämförelse, eftersom Weblate-komponenten fortfarande är låst.

Samma dag tillkom andra uppskalningshäftet med 25 nycklar för foveerad
uppskalning i VR. Filen
`open-shaders-upscaling-foveated-02-sv-20261029.json` innehåller
kantövergångar, DLSS-lägen och områdesmasker och är validerad mot den lokala
engelska katalogen. Även detta häfte kräver en ny exportjämförelse före
import.

Det tredje uppskalningshäftet från samma datum innehåller 25 nycklar för
visning i periferin, områdesmasker och foveerad finjustering i VR. Filen
`open-shaders-upscaling-foveated-03-sv-20261029.json` är validerad mot den
lokala engelska katalogen och kräver också en ny exportjämförelse före import.

Det fjärde uppskalningshäftet från samma datum innehåller 25 nycklar för
bildgenerering, bildfrekvensgränser och FSR4-reservvägar. Filen
`open-shaders-upscaling-frame-generation-04-sv-20261029.json` är validerad
mot den lokala engelska katalogen och kräver en ny exportjämförelse före
import.

Det femte uppskalningshäftet från samma datum innehåller 25 nycklar för låg
latens, uppskalningsmotorer och grundläggande materialkategorier i Neural
Rendering. Filen `open-shaders-upscaling-neural-basics-05-sv-20261029.json`
är validerad mot den lokala engelska katalogen och kräver en ny
exportjämförelse före import.
