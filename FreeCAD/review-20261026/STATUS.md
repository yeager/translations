# FreeCAD: svensk granskning 26 oktober 2026

De två XLIFF-filerna innehåller endast granskade förslag vars källtext och tidigare översättning fortfarande överensstämde med aktuell Crowdin-export. FreeCAD-filen innehåller 867 strängar och FreeCAD-addons-filen 12. Ytterligare 587 respektive 2 680 förslag var redan samma som i exporterna. Inga källkonflikter eller saknade strängar upptäcktes i jämförelsen. Dokumentation ingår inte.

Tidigare granskning och kontrollresultat gäller de ursprungliga kandidatfilerna; dessa filer är ett urval av dem. Gitleaks hittade inga hemligheter i de två filerna. Uppladdningsförsöken och efterföljande verifiering beskrivs nedan.

2026-10-26: Båda filerna laddades därefter upp via Crowdin med alternativet att tillåta översättningar identiska med källan. Crowdin rapporterade för FreeCAD 1 importerad, 0 godkända och 866 överhoppade; för FreeCAD-addons 1 importerad, 0 godkända och 11 överhoppade. Orsaken till att de flesta hoppades över är inte fastställd. Granska dessa individuellt och kontrollera vilka förslag som finns och vilken översättning som väljs; uppladdningen innebär inte att samtliga ändringar har accepterats.

2026-10-26: Crowdins detaljerade servicelogg nekade åtkomst (403). Kontroll via Crowdins API visade att alla 12 måltexter i tilläggsfilen redan finns som översättningsförslag för respektive sträng. Ett stickprov om 10 av huvudfilens 867 måltexter visade också att samtliga finns som förslag; förslagen har olika upphovspersoner. Detta visar inte vilket förslag som valts, och stickprovet bevisar inte statusen för övriga 857 strängar. Fortsätt kontrollera förslag och röster innan arbetet anses helt infört.

2026-10-26: En efterföljande API-kontroll av alla 867 strängar i huvudfilen fann exakta måltexter bland förslagen för 863; inga API-fel inträffade. Fyra måltexter saknades: 194951, 176822, 177244 och 2593990. Kontrollresultatet per sträng och förslags-id finns i [crowdin-forslagskontroll-20261026.json](crowdin-forslagskontroll-20261026.json). Före inskick av dessa fyra behövs kontext- och terminologigranskning; kontrollen bevisar inte vilka av de 863 förslagen som valts genom röster eller godkännande.

2026-10-26: De fyra saknade strängarna har `translate="no"` i XLIFF-exporten och Crowdins API bekräftar `isHidden: true` för alla fyra. De är därmed dolda från översättning; en gäller dessutom den arkiverade Drawing-arbetsbänken. De lämnas orörda. De 863 synliga eller tidigare föreslagna måltexterna behöver fortfarande kontrolleras mot den valda översättningen och eventuell granskning.

2026-10-26: En ny Crowdin-XLIFF-export jämfördes per sträng-id och källtext med huvudfilens 867 förslag. Exporten innehåller 1 vald måltext som matchar förslaget, 861 som skiljer sig och 5 dolda strängar. Av de 861 avvikande är 542 märkta som godkända i exporten. Resultatet per id finns i [crowdin-vald-oversattning-20261026.json](crowdin-vald-oversattning-20261026.json). De 863 förekomsterna av förslag som hittades via API omfattar även förslag för dolda strängar; siffrorna mäter därför olika saker. Förslagen finns men är i huvudsak inte de valda översättningarna. Godkända översättningar kräver särskild granskning och kan inte antas ändras genom röster.

2026-10-26: Bland de 319 avvikande förslag som inte var godkända i exporten finns 33 med exakt måltext från kontot yeagersthlm. API:et visade inga befintliga röster för förslaget «Storhet» (sträng 6577608, översättning 16011255), men försöket att rösta upp det gav HTTP 403. Ingen röst registrerades. Orsaken till nekandet är inte fastställd; behörighet eller Crowdins regler för egna förslag behöver undersökas innan fler röstförsök görs.

2026-10-26: Förslaget ”Aktivera sida vid sida-bakgrund” för ”Enable tiled background” (sträng 6497133, översättning 16183291) är språkligt svagt och bör inte röstas upp. API-kontroll visar att det bättre förslaget ”Aktivera upprepad bakgrundsbild” redan finns på samma sträng (översättning 16011787, yeagersthlm). Ingen ny översättning eller röst har skickats. Det vid kontrollen högst poängsatta förslaget är ”Aktivera staplad bakgrund”; det är inte verifierat att detta valts i den aktuella exporten. Historiska XLIFF-filer behålls som dokumentation av det som laddades upp.

2026-10-26: Crowdins redigerare visade att ”Aktivera staplad bakgrund” var vald. Försök att spara det befintliga bättre förslaget stoppades av kontrollen för dubblett. Det missvisande förslaget har därefter röstats ned av yeagersthlm; API-kontroll bekräftar rösten och att både detta förslag och ”Aktivera upprepad bakgrundsbild” nu har poäng 0. Det är inte verifierat vilket förslag Crowdin väljer vid lika poäng. Under kontrollen gavs först en oavsiktlig uppåtröst till det tidigare valda förslaget; den togs bort innan nedåtrösten lades.

2026-10-27: Ett tredje läsande urval om 20 godkända avvikelser har granskats
och arkiverats i `approved-differences-sample-03-20261027.md`. En felkopplad
kandidat upptäcktes för sträng 6606469: måltexten beskriver en SVG-exportstil
fast källan gäller ett objekt utan giltig begränsningsruta. Kandidaten får inte
återanvändas; den föreslagna rättelsen ska först jämföras med den aktuellt
valda Crowdin-översättningen. Övriga nitton poster är rimliga i sin kontext.

2026-10-27: Ett fjärde läsande urval om 20 godkända avvikelser har granskats
och arkiverats i `approved-differences-sample-04-20261027.md`. Sträng 6683762
är felöversatt som ”Plats”: källkodskontexten visar att den är etikett i
autentiseringsdialogen för en nätverkswebbplats och därför ska vara
”Webbplats”. Övriga nitton poster är godtagbara eller avsiktligt oförändrade
kodnamn. Rättelsen ska först kontrolleras mot Crowdins valda måltext.

2026-10-27: Ett femte läsande urval om 20 godkända avvikelser har granskats
och arkiverats i `approved-differences-sample-05-20261027.md`. Alla poster är
godtagbara i sin kontext. Särskilt kontrollerades att ”verktygsrad” är den
etablerade termen i just dialogen för egna verktygsrader; ingen onödig
Crowdin-ändring ska göras.

2026-10-27: Ett sjätte läsande urval om 20 godkända avvikelser har granskats
och arkiverats i `approved-differences-sample-06-20261027.md`. Alla poster är
godtagbara i sin kontext. Källkoden och översättningsminnet bekräftar särskilt
”snurrplatta” och ”rotationsstil” för FreeCADs navigeringslägen; inga nya
Crowdin-förslag ska skapas från urvalet.

2026-10-27: Ett sjunde läsande urval om 20 godkända avvikelser har granskats
och arkiverats i `approved-differences-sample-07-20261027.md`. Alla poster är
godtagbara i sin kontext. Den granskade FreeCAD-terminologin bekräftar att
”beroende objekt” ska skrivas isär i dessa strängar; inga nya Crowdin-förslag
ska skapas från urvalet.

2026-10-27: Ett åttonde läsande urval om 20 godkända avvikelser har granskats
och arkiverats i `approved-differences-sample-08-20261027.md`. Två rättelser
kräver kontroll mot Crowdins valda måltexter: kandidaten ”Växlar till
perspektiviskt visningsläge” är bättre än den svagare lokala formuleringen
”perspektivt visningsläge”, och sträng 6687710 ska vara
”&Rektangelmarkering”, inte ”&Rutmarkering”, enligt FreeCAD-terminologin.
Övriga arton kandidater är godtagbara. Inga nya Crowdin-förslag har skapats.

2026-10-27: Ett nionde läsande urval om 20 godkända avvikelser har granskats
och arkiverats i `approved-differences-sample-09-20261027.md`. Fyra kandidater
använder den felaktiga termen ”rutmarkering” eller den ofullständiga
översättningen ”Kugghjul och kuggstång” för `RackPinion`. De rekommenderade
formerna är `rektangelmarkering`, `Rektangelmarkering av &element` och
`Kuggstång och pinjong`. De ska först jämföras med Crowdins valda måltexter.
Övriga 16 kandidater är godtagbara. Inga nya Crowdin-förslag har skapats.

2026-10-27: Ett tionde läsande urval om 20 godkända avvikelser har granskats
och arkiverats i `approved-differences-sample-10-20261027.md`. Fyra kandidater
ska rättas efter kontroll mot Crowdins valda måltexter: `Malformed joints` ska
vara ”Felaktigt definierade leder”, och `revolute joint` ska konsekvent vara
”rotationsled” i både kommandon och instruktioner. Övriga 16 kandidater är
godtagbara. Inga nya Crowdin-förslag har skapats.

2026-10-27: Ett elfte läsande urval om 20 godkända avvikelser har granskats
och arkiverats i `approved-differences-sample-11-20261027.md`. Fyra kandidater
ska rättas efter kontroll mot Crowdins valda måltexter: `Rack and Pinion Joint`
ska vara ”Kuggstångs- och pinjongled”, `revolute joints` ska vara
”rotationsleder” och den äldre Drawing-strängen ska använda
”Automatisk skala/position” utan blanksteg vid snedstrecket. Övriga 16
kandidater är godtagbara. Inga nya Crowdin-förslag har skapats.

2026-10-27: Ett tolfte läsande urval om 20 godkända avvikelser har granskats
och arkiverats i `approved-differences-sample-12-20261027.md`. En kandidat ska
rättas efter kontroll mot Crowdins valda måltext: `Plane Multi-Point Constraint`
ska vara ”Flerpunktsvillkor för plan”, inte ”Plant flerpunktsvillkor”. Övriga
19 kandidater är godtagbara. Inga nya Crowdin-förslag har skapats.

2026-10-27: Ett trettonde läsande urval om 20 godkända avvikelser har
granskats och arkiverats i `approved-differences-sample-13-20261027.md`. Alla
poster är godtagbara i sin FEM- och bildvisningskontext. Den felaktiga
ensamma avslutande parentesen finns redan i källsträngen och har bevarats för
att inte skapa en formatavvikelse. Inga nya Crowdin-förslag har skapats.

2026-10-27: Ett fjortonde läsande urval om 20 godkända avvikelser har
granskats och arkiverats i `approved-differences-sample-14-20261027.md`. En
kandidat ska rättas efter kontroll mot Crowdins valda måltext: `Section From
Plane` ska vara ”Snitt med plan”, inte ”Snitt från plan”. Övriga 19 kandidater
är godtagbara. Inga nya Crowdin-förslag har skapats.

2026-10-27: Ett femtonde läsande urval om 20 godkända avvikelser har
granskats och arkiverats i `approved-differences-sample-15-20261027.md`. En
kandidat ska rättas efter kontroll mot Crowdins valda måltext: `Meshing
Tolerance` ska vara ”Nätgenereringstolerans”, inte ”Nättolerans”. Övriga 19
kandidater är godtagbara. Inga nya Crowdin-förslag har skapats.

2026-10-27: Ett sextonde läsande urval om 20 godkända avvikelser har
granskats och arkiverats i `approved-differences-sample-16-20261027.md`. Alla
poster är godtagbara i sin Part-kontext. Inga nya Crowdin-förslag har skapats.

2026-10-27: Ett sjuttonde läsande urval om 20 godkända avvikelser har
granskats och arkiverats i `approved-differences-sample-17-20261027.md`. Tre
kandidater ska rättas efter kontroll mot Crowdins valda måltexter:
`Planar` är ”Planär” i byggdialogen, den booleska feltexten ska beskriva en
”yta som inte kan återställas”, och `Datums` är ”Referensgeometri” i
kommandogruppen. Övriga 17 kandidater är godtagbara. Inga nya Crowdin-förslag
har skapats.

2026-10-27: Ett artonde läsande urval om 20 godkända avvikelser har granskats
och arkiverats i `approved-differences-sample-18-20261027.md`. Fyra kandidater
ska rättas efter kontroll mot Crowdins valda måltexter: `plant` ska vara
”planärt”, och tre Part Design-poster ska använda ”referensgeometri” i stället
för ”referensobjekt”. Övriga 16 kandidater är godtagbara. Inga nya
Crowdin-förslag har skapats.

2026-10-27: Ett nittonde läsande urval om 20 godkända avvikelser har
granskats och arkiverats i `approved-differences-sample-19-20261027.md`. Tre
kandidater ska rättas efter kontroll mot Crowdins valda måltexter:
”Formelement för efterbearbetning” och två korta `Create Datum`-kommandon med
”Skapa referensgeometri”. Övriga 17 kandidater är godtagbara. Inga nya
Crowdin-förslag har skapats.

2026-10-27: Ett tjugonde läsande urval om 20 godkända avvikelser har
granskats och arkiverats i `approved-differences-sample-20-20261027.md`. Två
kandidater ska rättas efter kontroll mot Crowdins valda måltexter:
”Förflytta geometrier” och ”Visuella hjälpmedel”. Övriga 18 kandidater är
godtagbara. Inga nya Crowdin-förslag har skapats.

2026-10-27: Ett tjugoförsta läsande urval om 20 godkända avvikelser har
granskats och arkiverats i `approved-differences-sample-21-20261027.md`. Fem
kandidater ska rättas efter kontroll mot Crowdins valda måltexter:
förflyttningsvektorer, statusvärdet ”Inaktiv”, rotationssvep och ett explicit
framtida återställande av areavärden. Övriga 15 kandidater är godtagbara. Inga
nya Crowdin-förslag har skapats.

2026-10-27: Ett tjugoandra läsande urval om 20 godkända avvikelser har
granskats och arkiverats i `approved-differences-sample-22-20261027.md`. En
kandidat ska rättas efter kontroll mot Crowdins valda måltext: Arch-egenskaperna
`Width`, `Height` och `Align` ska behållas som modellidentifierare. Övriga 19
kandidater är godtagbara. Inga nya Crowdin-förslag har skapats.

2026-10-27: Ett tjugotredje läsande urval om 20 godkända avvikelser har
granskats och arkiverats i `approved-differences-sample-23-20261027.md`. Tre
kandidater ska rättas efter kontroll mot Crowdins valda måltexter:
”cellbindningar” samt totalmått uttryckta som ”i 2D” respektive ”i 3D”. Övriga
17 kandidater är godtagbara. Inga nya Crowdin-förslag har skapats.

2026-10-27: Ett tjugofjärde läsande urval om 20 godkända avvikelser har
granskats och arkiverats i `approved-differences-sample-24-20261027.md`. Tre
kandidater ska rättas efter kontroll mot Crowdins valda måltexter: `inom
parentes`, den fullständiga etiketten ”brittiska måttenheter” och ”bygg- och
anläggningsteknik”. Övriga 17 kandidater är godtagbara. Inga nya
Crowdin-förslag har skapats.

2026-10-27: Ett tjugofemte läsande urval om 20 godkända avvikelser har
granskats och arkiverats i `approved-differences-sample-25-20261027.md`. Fem
kandidater ska rättas efter kontroll mot Crowdins valda måltexter: stegvis
borrning, planfräsning av ämnets yta, markeringens kanter samt bestämda former
för rätblocksämnets längd och bredd. Övriga 15 kandidater är godtagbara. Inga
nya Crowdin-förslag har skapats.

2026-10-27: Ett tjugosjätte läsande urval om 20 godkända avvikelser har
granskats och arkiverats i `approved-differences-sample-26-20261027.md`. Tre
kandidater ska rättas efter kontroll mot Crowdins valda måltexter: bestämd form
för rätblocksämnets höjd, markeringens kanter och matrisupprepade
verktygsbanor. Övriga 17 kandidater är godtagbara. Inga nya Crowdin-förslag har
skapats.

2026-10-27: Ett tjugosjunde läsande urval om 20 godkända avvikelser har
granskats och arkiverats i `approved-differences-sample-27-20261027.md`.
Efter en senare kontroll återstår endast fyra CAM-rättelser för den
konsekventa termen ”matris”. Två tidigare föreslagna ändringar av `Toolbit`
har strukits: ”verktygsbit” är den etablerade FreeCAD-termen och Crowdins
aktuella värden ”Väljare för verktygsbit” och ”Formväljare för verktygsbit”
är korrekta. Alla fyra matriskorrigeringarna har kontrollerats direkt i
Crowdin, men är ännu inte sparade. Övriga 16 poster är godtagbara.

2026-10-27: De två återstående godkända avvikelserna har granskats och
arkiverats i `approved-differences-sample-28-20261027.md`. Crowdins aktuella,
godkända måltexter kontrollerades i den inloggade redigeraren och hade redan
”mätningsuppgiften” respektive ”en enstaka yta”. Därmed är samtliga 542
godkända avvikelser i underlaget granskade rad för rad. Inga nya
Crowdin-förslag har skapats.
