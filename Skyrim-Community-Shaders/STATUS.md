# Skyrim Community Shaders: svensk port

Den aktuella utvecklingsrevisionen `d3099b19f79f62d12bebbcaae4b3aa1ec1d3b28a`
har 4 237 engelska nycklar. Den tidigare arkiverade porten innehöll 2 132
svenska nycklar från en äldre katalog. Av dessa matchar 2 081 fortfarande
nyckel för nyckel i den aktuella katalogen. De 308 utgångna eller omdöpta
nycklarna är inte med i den nya språkfilen.

`skyrim-community-shaders-sv-current-port-20261028.json` är den rena,
nyckelordnade svenska porten. Den innehåller 3 667 översatta nycklar och
utelämnar 570 nya nycklar, vilka enligt projektets dokumenterade i18n-regel
faller tillbaka till engelska. Den är därför en säker partiell första
upstreaminsändning, inte en komplett svensk katalog.

Kontroller 2026-10-28:

- Projektets `extract-i18n.py --check` och `--orphans` passerar.
- Projektets `sort-i18n.py --check` passerar.
- De 89 nytillagda TM-posterna har entydig svensk måltext, exakt samma aktuella
  engelska källa och bevarade klammerplatshållare.
- `l10n-lint` rapporterar inga fel och en avgränsad Gitleaks-körning rapporterar
  inga fynd.
- svlangs enda skrivregelträff är den bevarade spelvariabeln
  `fGrassStartFadeDistance`; Hunspell-träffarna är spel-, shader-, fil- och
  API-termer som har granskats i kontext.

Efter den första porten jämfördes även de lokala Open Shaders-arkiven mot den
aktuella engelska källan. Endast 18 poster hade både oförändrad källa och en
entydig tidigare granskad svensk måltext; de lades till i PR:n. Hundra poster
med ändrad engelsk källa lämnades avsiktligt för manuell granskning.

Ytterligare 89 poster valdes ur `swedish-tm` efter exakt jämförelse med den
aktuella engelska källan och manuell kontextkontroll. Tvetydiga, felkodade och
oförändrade kandidater lämnades utanför. I samma genomgång återställdes `%s` i
ett äldre Nsight Perf-felmeddelande, eftersom programkoden skickar ett dynamiskt
byggtips till den strängen.

Sju ytterligare etiketter översattes därefter efter kontroll av deras exakta
användningsställen i koden: färggraderingsreglage, manuellt fokus,
uppskalningsförinställningen, ett inläsningsfilter och palettens Esc-hjälp.

CS-redigerarens grundetiketter har därefter granskats i en sats om 28 poster:
statusbrickor, filter, kopieringsåtgärder, baslager och grundinställningar.
Projektets termer `Editor ID`, `Form ID`, Effects 11 och Community Shaders
har behållits där de identifierar egna format eller komponenter.

En följande sats om 21 poster täcker navigering, kategorier, förinställningar,
sparade JSON-åsidosättningar och felmeddelanden i CS-redigeraren. Den befintliga
tekniktermen `Linsöverstrålning` har behållits konsekvent också i plural.

CS-redigerarens felsökningsvy har kompletterats med 38 korta statusfält för
celler, väder, scenposter, lager, platsdata och förinställningar. Tekniska
diagnostikbegrepp med oklarare funktionell innebörd har avsiktligt lämnats till
en senare kontextgranskning.

Ytterligare 42 generella diagnostikfält har översatts: tillstånd, tid, väder,
scendata, övergångar och resolverns status. Hunspell markerar endast de
projektspecifika sammansättningarna `Resolverns` och `Scentypposter`; de är
granskade i kod- och gränssnittskontext.

Sparning och förinställningar i CS-redigeraren har kompletterats med 19
strängar. Katalogen omfattar nu återställning, JSON-åsidosättningar,
felhantering och lokala sparåtgärder med samtliga platshållare bevarade.

Platsbläddraren i CS-redigeraren har kompletterats med 40 strängar för
platstyper, filter, redigering, borttagning och platsprioritet. `Form ID` och
`Editor ID` följer den befintliga svenska terminologin som formulär-ID och
redigerar-ID.

Scenkopieringsvyn har kompletterats med 36 korta kontroller, räknare och
hjälptexter för urval, mål, perioder och överskrivning. Alla
klammerplatshållare i satsen har jämförts med den engelska källan.

Exportdialogens 37 etiketter, räknare och korta resultatmeddelanden är
översatta. Produktförkortningen CS är medvetet bevarad i `CS-förinställning`.

Scenhanterarens grundetiketter och dess korta hjälptexter har kompletterats
med 17 poster. Interna ID:n efter `##` och tekniska namn som `Baseline` har
bevarats, medan gränssnittstexten använder den etablerade terminologin
`förinställning` och `åsidosättning`.

Exportpanelens första 23 poster har också granskats: spärrmeddelanden,
filstatus, räknare, kolumnrubriker och korta hjälptexter. Alla
klammerplatshållare och kortkommandot `Ctrl+Shift+S` har bevarats.

Scenhanterarens nästa 23 poster omfattar exportpaketens status,
funktionsåsidosättningar samt tids- och väderövergångar. Även här har interna ID:n,
klammerplatshållare och kortkommandon bevarats exakt.

Den avslutande scenhanterarsatsen med 15 poster täcker exportpanelen helt,
inklusive dess flerradiga arbetsflödeshjälp. Därmed har samtliga
`feature.scene_manager`-nycklar en svensk måltext i den aktuella katalogen.

Förinställningsmenyn har kompletterats med 21 poster för aktiva paket och
teman, Baseline-inställningar samt kompatibilitetsvarningar. De dynamiska
klammerplatshållarna för versioner, funktioner och insticksmoduler är
bevarade oförändrade.

Ytterligare 26 poster i förinställningsmenyn är översatta: scenlager,
aktivering, filter, valideringsmeddelanden samt öppningsåtgärder för paket,
teman och CS-redigeraren.

Förinställningsmenyns sista 16 poster täcker överlappningsdialogen, borttagning
av Baseline, omgenomsökning, källmarkeringar och teman. Därmed har samtliga
`menu.presets`-nycklar en svensk måltext i den aktuella katalogen.

Tangentbordsgenvägarnas samtliga 15 menyposter är översatta, inklusive ångra,
gör om, sparning och sidnavigering. Klammerplatshållaren `{name}` är bevarad.

Projektets senaste release, v1.9.1, publicerades 2026-09-24 och uppfyller
48-månaderskravet. Den partiella filen skickades som
[PR #3051](https://github.com/community-shaders/skyrim-community-shaders/pull/3051)
2026-10-28. PR:n är öppen och väntar på CI och uppströmsgranskning. Den
återstående katalogen behöver delas upp i granskningsbara satser.

PR:n riktades först felaktigt mot `main`, vilket gav en orelaterad
versionsgranskningsvarning. Den riktades om till projektets standardgren
`dev`; diffen omfattar nu endast `sv.json`. GitHub väntar på att en
underhållare godkänner arbetsflödeskörning för forken. Ingen lokalt eller
upstream påvisad översättningskontroll har felat.

2026-10-28: En ytterligare sats om 33 CS-redigerarsträngar omfattar
statusbrickor, felsökningsfält, lager, tidsperioder, FormID-fält samt
filter- och posträknare. Klammerplatshållarna `{count}`, `{shown}` och
`{total}` är bevarade. Projektets extraktions-, orphan- och sorteringskontroll
passerar. Den nya satsen har inga svlang-fynd; Hunspell-träffarna är
`Bas-FormID`, `EditorID`, `Referens-FormID` och platshållarnamnen.

2026-10-28: En sats om 31 strängar kompletterar scenlager, lagerprioritet,
förinställningskällor, redigerarens spärrmeddelanden, tidsperiodsvyn samt
gör-om-status. Platshållarna `{location}`, `{weather}`, `{period}`, `{layer}`,
`{context}`, `{count}`, `{}` och `%s` har kontrollerats mot källtexten.
Projektets extraktions-, orphan- och sorteringskontroll passerar. Satsen har
inga svlang-fynd, och Gitleaks gav inga fynd. Hunspell markerar endast
platshållarnamn och engelska interna kontextord.

2026-10-28: En sats om 16 redigerarsträngar täcker basinställningar,
förinställningsvärden, Effects 11-handover, startladdning, fri kamera och
inspektörens tomma läge. Den flerradiga startomstartshjälpen har bevarade
radbrytningar. Projektets egna kontroller och svlang passerar; Gitleaks gav
inga fynd. Hunspell-träffarna är `COC`, produktnamnet `Effects 11` och
projektspecifika sammansättningar.

2026-10-28: En sats om 23 strängar för scenåsidosättningar täcker moddar,
platslager, navigeringshjälp, prioritet, pausning och återställning. Den
dynamiska platshållaren `{place}` är bevarad. Projektets egna kontroller och
svlang passerar; Gitleaks gav inga fynd. Hunspell markerar endast
platshållarnamnet.

2026-10-28: En sats om 17 strängar täcker rensning, kopiering, export,
pausning och övergångar på en scenhanteringssida. Samtliga tre anonyma
platshållare i kopieringsresultatet och radbrytningar i dialogerna har
bevarats. Projektets kontroller och svlang passerar; Gitleaks gav inga fynd.
Hunspell markerar endast fackordet `blandningsbara`.

2026-10-28: En sats om 12 strängar kompletterar gråmarkerade inställningar,
övergångstider, väderval, sökning och redigerarens kortkommandon. Radbrytningen
i övergångshjälpen är bevarad. Projektets kontroller och svlang passerar;
Gitleaks gav inga fynd. Hunspell markerar endast sammansättningen
`CS-redigeraren` och böjningsformen `gråmarkerade`.

2026-10-28: En sats om 20 strängar kompletterar exportens omslagsbild,
kompatibilitet, funktionsurval, moddkällor, filersättning, taggar och
efterbearbetning. Anonyma platshållare, radbrytning och filformat har
bevarats. Projektets kontroller och svlang passerar; Gitleaks gav inga fynd.
Hunspell markerar endast filformat, produktnamn och avsiktliga tekniska
identiteter.

2026-10-28: Sex strängar för exporttyperna CS, Baseline och E11 har
kompletterats. Sökvägen `Presets/<Name>/effects11/`, ENB-identiteter och
versionsformatet är bevarade. Projektets kontroller och svlang passerar;
Gitleaks gav inga fynd. Hunspell-träffarna är endast tekniska identiteter.

2026-10-28: Fyra korta statussträngar har lagts till för scenfunktioner,
tomlista, Scenhanteraren och ImGui-felhantering. Platshållaren `%s` är bevarad.
Projektets kontroller och svlang passerar; Gitleaks gav inga fynd. Hunspell
markerar endast den tekniska sammansättningen `ImGui-avlyssningen`.

2026-10-28: En sats om 23 vädersträngar omfattar kategorier, vindriktningar,
väderkolumner, filter, redigeraråtgärder och felsökning. Projektets kontroller
och svlang passerar; Gitleaks gav inga fynd. Hunspell markerar endast
`CS-redigeraren` och vädertypen `norrskenssol`.

2026-10-28: En sats om 32 strängar kompletterar väderdiagnostikens vind-,
blixt-, nederbörds- och partikelfält. Samtliga formatplatshållare, enheter och
värdeintervall är bevarade. Projektets kontroller och svlang passerar;
Gitleaks gav inga fynd. Hunspell markerar endast format, `uint8` och den
tekniska termen `himmelsystemet`.

2026-10-28: En sats om 27 strängar kompletterar väderanalys, kategorier,
åskfrekvens, interna ID-fält och övergångsstatus. Platshållare, hexadecimal-
format och produktnamnet Creation Kit är bevarade. Projektets kontroller och
svlang passerar; Gitleaks gav inga fynd. Hunspell-träffarna är tekniska
identiteter, format och platshållare.

2026-10-28: En sammanhängande UI-sats om 49 strängar kompletterar
sidofältet, felsökning, tid, vädervyer, verktygsdialoger, interna ID:n och
återställning. Samtliga platshållare och radbrytningar är bevarade. Projektets
kontroller och svlang passerar; Gitleaks gav inga fynd. Hunspell-träffarna är
tekniska format, Light Placer och projektspecifika sammansättningar.

2026-10-28: En sats om 31 strängar kompletterar inställningsmenyns färg-,
typsnitts-, cache-, tangent- och utseendeinställningar. Platshållaren `{size}`
har bevarats. Projektets kontroller och svlang passerar; Gitleaks gav inga
fynd. Hunspell-träffarna är avsedda shader- och cachetermer.

2026-10-28: En sats om 49 strängar kompletterar språkval, palettgrupper,
återställning, shaderblockering, statusfält och ytornas kantinställningar.
Platshållarna `{key}` och `{percent}` samt sökvägen till typsnitt har
bevarats. Projektets kontroller och svlang passerar; Gitleaks gav inga fynd.
Hunspell-träffarna är filformat samt API- och grafiktermer.

2026-10-28: En sats om 48 strängar kompletterar menyns ytor, kort,
fyllningar, skuggor, hörnradier, animeringar och tvingade inställningar.
Projektets kontroller och svlang passerar; Gitleaks gav inga fynd. Hunspell
markerar endast tekniska sammansättningar och produktnamn.

2026-10-28: Funktionsmenyns 50 strängar är översatta: filter, favoriter,
Baseline-värden, förinställningar, profilering, scenindikatorer och
återställning. Projektets kontroller och svlang passerar; Gitleaks gav inga
fynd. Hunspell markerar endast projektspecifika Baseline- och
CS-sammansättningar.

2026-10-28: Startsidan och kommandopaletten har kompletterats med 52 strängar
för status, förinställningar, snabbåtkomst, kortkommandon, sökning och
navigering. Platshållarna `{count}`, `{time}` och `{path}` är bevarade.
Projektets kontroller och svlang passerar; Gitleaks gav inga fynd. Hunspell-
träffarna är produktnamn, kortkommandon, tekniktermer och platshållare.

2026-10-28: En sats om 31 strängar kompletterar avancerade menyns aktiva
shaders, kompilering, cache, loggnivåer, shadersteg och felsökning.
Hörnpunkt används konsekvent i användartexten för Vertex. Projektets kontroller
och svlang passerar; Gitleaks gav inga fynd. Hunspell-träffarna är filnamn,
produktnamn, grafiktermer och platshållare.

2026-10-28: Cachehjälptexten för ContentStore är översatt med bevarad
sökväg, tekniktermer och radbrytning. Projektets kontroller och svlang
passerar; Gitleaks gav inga fynd. Hunspell-träffarna är sökvägens tekniska
komponenter och shadertermen.

2026-10-28: Avancerade menyns testhjälptext är översatt. Spelkommandon,
argument och platsnamnet Whiterun har bevarats exakt, medan deras
användarförklaringar är svenska. Projektets kontroller och svlang passerar;
Gitleaks gav inga fynd.

2026-10-28: Uppskalningsfunktionen har kompletterats med 56 strängar för
DLSS, FSR, TAA, bildgenerering, Reflex och tekniska felsökningsinställningar.
Varumärken, filnamn och förkortningar är bevarade. Projektets extraktions-,
orphan- och sorteringskontroll samt svlang och l10n-lint passerar. Gitleaks
gav inga fynd. Hunspell-träffarna är tekniska produktnamn, förkortningar,
filnamn och domänspecifika sammansättningar som har granskats i kontext.

2026-10-28: Utvecklarverktygen har kompletterats med 38 strängar för
RenderDoc, Nsight Perf, devbench, MCP, REST och bildrutefångst. Varumärken,
protokoll och kortkommandot Print Screen är bevarade. Projektets extraktions-,
orphan- och sorteringskontroll samt svlang och l10n-lint passerar. Gitleaks
gav inga fynd. Hunspell-träffarna är avsedda produktnamn, förkortningar och
tekniska sammansättningar som har granskats i kontext.

2026-10-28: Linjär belysning har kompletterats med 30 inställningar för
gamma, reflektans, effektbelysning och färgrymd. Effects 11, ACEScg och PBR
är bevarade som produkt- och facktermer. Projektets extraktions-, orphan- och
sorteringskontroll samt svlang och l10n-lint passerar. Gitleaks gav inga fynd.
Hunspell-träffarna är enbart facktermer och tekniknamn, granskade i kontext.

2026-10-28: Ljusredigeraren har kompletterats med 21 strängar för listfilter,
kolumner, felmeddelanden, skuggljus och Light Placer. Platshållarna `{total}`
och `{shadow}` är bevarade. Projektets extraktions-, orphan- och
sorteringskontroll samt svlang och l10n-lint passerar. Gitleaks gav inga fynd.
Hunspell-träffarna är projektets egna modeller, format och tekniska identiteter.

2026-10-28: LUT-delen av efterbearbetningen har kompletterats med 21
strängar för 1D-/3D-format, texturer, filformat och scenomfång.
Platshållarna `{error}`, `{extension}`, `{dimension}` och `%s` är bevarade.
Projektets extraktions-, orphan- och sorteringskontroll samt svlang och
l10n-lint passerar. Gitleaks gav inga fynd. Hunspell-träffarna är filformat,
förkortningar och facktermen luma.

2026-10-28: Rörelseoskärpa och vinjettering har kompletterats med 19
strängar för kamerarörelse, samplingskvalitet, slutarskala och objektivets
optiska vinjettering. Procent- och gradformat är bevarade. Projektets
extraktions-, orphan- och sorteringskontroll samt svlang och l10n-lint
passerar. Gitleaks gav inga fynd. Hunspell-träffarna är formatmarkörer och
facktermerna anamorft och fjärdepotenslagen.

2026-10-28: Histogramstyrd automatisk exponering har kompletterats med 29
strängar för luminans, EV100, exponeringskompensation, anpassning och
Purkinjeeffekten. Samtliga tal- och formatplatshållare är bevarade. Projektets
extraktions-, orphan- och sorteringskontroll samt svlang och l10n-lint
passerar. Gitleaks gav inga fynd. Hunspell-träffarna är EV-format och
facktermerna Purkinjeeffekt och histogramstyrd.

2026-10-28: Lokal exponering har kompletterats med 28 strängar för
basblandning, luminansanalys, högdagrar, skuggor och mellangrått.
Projektets extraktions-, orphan- och sorteringskontroll samt svlang och
l10n-lint passerar. Gitleaks gav inga fynd. Hunspell-träffarna är den
bevarade tekniktermen Composite-passet och etablerade facktermer.

2026-10-28: COD Bloom och Horizon Fix har kompletterats med 24 strängar för
glödeffekt, mipnivåer, horisontband, vattenhorisont och HorizonFix.ini.
Tekniska inställningsnamn och INI-nycklar är bevarade. Projektets
extraktions-, orphan- och sorteringskontroll samt svlang och l10n-lint
passerar. Gitleaks gav inga fynd. Hunspell-träffarna är enbart produktnamn,
filnamn, parametrar och tekniska facktermer.

2026-10-28: Gräsbelysning har kompletterats med 13 strängar för
växttaksocklusion, tuvskuggning, PBR-gräs, SSS och LOD-ljusstyrka.
Projektets extraktions-, orphan- och sorteringskontroll samt svlang och
l10n-lint passerar. Gitleaks gav inga fynd. Hunspell-träffarna är tekniska
PBR-, SSS- och meshtermer som är granskade i kontext.

2026-10-28: Fjärrstyrningen har kompletterats med 12 strängar för devbench,
MCP, REST och Nsight Perf-fångster. Samtliga formatplatshållare och
verktygsidentiteter är bevarade. Projektets extraktions-, orphan- och
sorteringskontroll samt svlang och l10n-lint passerar. Gitleaks gav inga fynd.
Hunspell-träffarna är enbart protokoll, verktygsnamn, format och tekniktermer.

2026-10-28: Effects 11 har kompletterats med 14 strängar för kategorier,
ENBSeries-kompatibel efterbearbetning, förinställningar, scenöverlämning och
redigerarstatus. Sökvägar, filnamn och produktidentiteter är bevarade.
Projektets extraktions-, orphan- och sorteringskontroll samt svlang och
l10n-lint passerar. Gitleaks gav inga fynd. Hunspell-träffarna är enbart
tekniska produktnamn, filformat och projektspecifika identiteter.

2026-10-28: Light Limit Fix har kompletterats med 22 strängar för lokala
ljusskuggor, skuggcache, ljusgränsvisualisering och partikelstatistik.
Formatplatshållare och INI-nyckeln fPoissonRadiusScale är bevarade. Projektets
extraktions-, orphan- och sorteringskontroll samt svlang och l10n-lint
passerar. Gitleaks gav inga fynd. Hunspell-träffarna är den bevarade
INI-nyckeln och facktermen skuggmask.

2026-10-28: Experimentell höjddimma har kompletterats med fem strängar för
voxeljitter, froxeluppsampling, volymetrisk utsläckning och värdebrus.
Projektets extraktions-, orphan- och sorteringskontroll samt svlang och
l10n-lint passerar. Gitleaks gav inga fynd. Hunspell-träffarna är granskade
grafik- och dimfacktermer.

2026-10-28: Färggraderingens första 35 strängar har kompletterats med
grundparametrar för färgrymd, kurvförhandsvisning, HDR/SDR, tonmappning och
ASC CDL. Alla formatplatshållare och förkortningar är bevarade. Projektets
extraktions-, orphan- och sorteringskontroll samt svlang och l10n-lint
passerar. Gitleaks gav inga fynd. Hunspell-träffarna är avsedda
färgvetenskapliga termer och produktförkortningar.

2026-10-28: Färggraderingens andra sats omfattar 38 reglage för
färgomfång, HDR-utdata, nyans, logaritmtyper, OKLCH och visningsfärgrymd.
Alla formatplatshållare, standarder och förkortningar är bevarade. Projektets
extraktions-, orphan- och sorteringskontroll samt svlang och l10n-lint
passerar. Gitleaks gav inga fynd. Hunspell-träffarna är avsedda
färgvetenskapliga termer och standardidentiteter.

2026-10-28: Färggraderingens tredje sats omfattar 24 reglage för
tonkurvans tå och axel, LDR/HDR-växling, mättnad, färgton och LUT-utdata.
Projektets extraktions-, orphan- och sorteringskontroll samt svlang och
l10n-lint passerar. Gitleaks gav inga fynd. Hunspell-träffarna är bevarade
färgvetenskapliga förkortningar och etablerade facktermer.

2026-10-28: Färggraderingens sista 21 strängar omfattar tonmappningsmetoder
från ACES, AgX, Frostbite, Reinhard och fler. Namn, akademiska titlar och
produktidentiteter är bevarade. Projektets extraktions-, orphan- och
sorteringskontroll samt svlang och l10n-lint passerar. Gitleaks gav inga fynd.
Hunspell-träffarna är endast egennamn, titlar och färgvetenskapliga termer.
