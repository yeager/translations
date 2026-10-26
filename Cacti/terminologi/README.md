# Gemensam svensk terminologi för Cacti

Arbetslista för alla Cacti-komponenter. Tillämpa orden efter sammanhang och ändra inte variabelnamn, protokollnamn eller etablerade produktnamn. En term kan behöva en annan böjning eller en förklarande formulering i en hel mening. Listan är påbörjad och hela komponentbeståndet är ännu inte kontrollerat mot den.

| Engelska | Svenska | Användning och avgränsning |
|---|---|---|
| device | enhet | Övervakad enhet. |
| host | värd | En dator eller annan värd; skilj från enhet om källtexten gör det. |
| data source | datakälla | |
| data retention | lagringstid | När inställningen anger hur länge data behålls; skilj från allmän datalagring. |
| collector / data collector | insamlare / datainsamlare | En komponent eller nod som samlar in data. Använd datainsamlare när sammanhanget behöver förtydligas. |
| poller | datainsamlare, insamlingsprocess | Använd datainsamlare för en nod som tilldelas enheter och insamlingsprocess när själva processen avses. En poller hämtar vanligtvis data genom återkommande förfrågningar. |
| remote poller | fjärransluten datainsamlare | En datainsamlare på en annan värd. |
| polling | datainsamling, insamling | Välj efter sammanhang; insamlingsintervall för polling interval. Använd avfrågning när det är själva förfrågan till en enhet som avses. |
| aggregate (verb) / aggregation | aggregera / aggregering | Att sammanställa värden eller grafer till en helhet; grafaggregering för processen. |
| graph | graf | I Cactis övervakningsgränssnitt; diagram kan vara naturligare för andra visualiseringar. |
| aggregate graph | aggregerad graf | En graf som kombinerar flera grafer; grafaggregering beskriver processen. |
| graph template | grafmall | |
| aggregate template | mall för aggregerad graf | Använd en kortare form om utrymmet kräver det och sammanhanget är tydligt. |
| alert | larm | En utlöst larmhändelse; alerts kan översättas med larm. |
| warning | varning | Skilj från larm när källtexten gör det. |
| criticality | kritikalitet | Enhetens prioritet eller betydelse för övervakningen. |
| availability | tillgänglighet | Avser om enheten är nåbar. |
| state | tillstånd | Använd för det aktuella tillståndet; status kan passa för en sammanfattande status. |
| poller run / poller cycle | insamlingskörning / insamlingscykel | Avser en körning eller cykel, inte insamlaren som nod. |
| threshold | tröskelvärde, tröskel | Välj tröskelvärde när ett gränsvärde avses; tröskel kan användas för funktionen. |
| prefix / prefixes | prefix | Obestämd singular och plural har samma form; behåll tekniska prefix oförändrade. |
| network | nätverk | |
| scan / scanning | skanna / skanning | I Mactrack för undersökning av enheter och adresser; kontrollera sammanhang i andra komponenter. |
| site / location | plats / placering | I Monitor skiljs den tilldelade platsen från enhetens fysiska placering. |
| tree | träd | För Cactis hierarkiska graf- eller enhetsträd. |
| data query | datafråga | |
| metric / measurand | mätstorhet | I Reportit avser båda en definierad mätstorhet; i andra komponenter kan metric syfta på ett mätvärde. |
| consolidation function | konsolideringsfunktion | Funktion som sammanfattar mätvärden. |
| step / stepping | steglängd | När värdet anger avståndet mellan numeriska val. |
| filename / file name | filnamn | Samma betydelse trots olika engelsk stavning. |
| log | logg | |
| uptime | drifttid | |
| heartbeat | hjärtslag, hjärtslagsintervall | I RRD-datakällor avser det ett tidsintervall; för en insamlingsprocess kan det avse själva livstecknet. En gemensam källsträng kan användas i flera sammanhang och ska inte ändras mekaniskt. |
| poller cache | datainsamlarens cache | Använd insamlingsprocessens cache om det tekniska sammanhanget kräver åtskillnad. |
| enabled / disabled | aktiverad / inaktiverad | |
| utilities | verktyg | För menyn med verktygsfunktioner. |
| delete | ta bort | För gränssnittets åtgärd. |

Underlag: Cactis [funktionsbeskrivning](https://docs.cacti.net/Principles-of-Operation.md) och [dokumentation om datainsamlare](https://docs.cacti.net/Data-Collectors.md), befintliga översättningar och källkod. En första inventering 2026-10-26 hittade lokala exporter för 18 komponenter. Bland fristående strängar förekommer både ”graf” och ”diagram” för graph samt ”insamlare” och ”poller” för poller. Dessa skillnader kräver kontroll mot aktuell Weblate-export och sammanhang innan de ändras. Övriga komponenter och alla sammansatta termer återstår att inventera.

### Kontext i servcheck och flowview

I servcheck är fältet *Poller* ett val av insamlare. En *poller run* eller *poller cycle* beskriver däremot en insamlingskörning respektive insamlingscykel. Flowviews *Graph* kan beteckna en visualisering av flera slag, bland annat stapel- och cirkeldiagram; där är **diagram** lämpligt. I Cactis vanliga tidsseriegränssnitt används **graf**. Översätt efter sammanhang, inte med en mekanisk ersättning.

I nätverks- och routningssammanhang översätts *peer* med **motpart** och *geolocation* med **geografisk plats**. Kontrollera den tekniska betydelsen för andra sammanhang.

2026-10-26: ”Poller in Heartbeat Mode” ändrades till ”Datainsamlare i hjärtslagsläge”. Weblate bekräftade uppladdning och visar samma översättning i core och core v1.2.x via fortplantning. msgfmt, l10n-lint och Hunspell passerade. Cacti release 1.2.31 publicerades 2026-06-15.

2026-10-26: Boost-varningen använder ”Boost-processen” enligt källkodens processkontext. Weblate bekräftade en uppdaterad sträng i core; den aktuella v1.2.x-vyn visar samma översättning genom fortplantning. msgfmt, l10n-lint och Hunspell passerade.

2026-10-26: Core-kontrollen för ”Click 'Continue' to Delete following Aggregate Graphs.” avfärdades efter jämförelse med Core 1.2:s motsvarande formulering. Båda betyder att följande aggregerade grafer tas bort. Kontrollen för konvertering till vanliga grafer kvarstår för jämförelse av källtexternas antal.

2026-10-26: Konverteringskontrollen avfärdades efter källkodsjämförelse. Core 1.2 itererar över de valda graferna och konverterar dem var för sig; den nyare versionen har separata texter för singular och plural. Samma pluralformulering är därför rimlig för flera valda grafer.

2026-10-26: Två återanvändningskontroller i Core avfärdades efter jämförelse med Core 1.2: koppling av valda grafer till en aggregerad graf och skapande av en aggregerad graf från valda grafer. Källtexternas skillnad är versalisering och Graph(s); plural används för flera val.

2026-10-26: Återanvändningskontrollen för ”Graph Template Item” och ”Graph Template Items” avfärdades: ”grafmallobjekt” har samma form i obestämd singular och plural. Båda Core-versionerna använder termen.

2026-10-26: Kontrollen för ”VDEF Item” och ”VDEF Items” avfärdades: ”VDEF-objekt” fungerar i obestämd singular och plural och VDEF behålls som teknisk beteckning.

2026-10-26: ”Report Delete” och ”Delete Report” granskades: den förra används som behörighetsbenämning för borttagning och den senare som åtgärd. ”Ta bort rapport” fungerar i båda fallen; återanvändningskontrollen avfärdades.

2026-10-26: Mactracks ”Maximum OID's Per Get Request” använder nu GET med versaler, som i Core. Weblate bekräftade en uppdaterad sträng. msgfmt och l10n-lint passerade; Hunspell flaggade den tekniska förkortningen OID:er.

2026-10-26: Core-kontrollen för högsta antal OID:er per GET-förfrågan avfärdades efter jämförelse med Mactrack. Källtexterna skiljer sig endast genom apostrof i engelsk plural och båda översätts nu likadant.

2026-10-26: ”Polling Interval” avser datakällans insamlingsfrekvens och ”Poller Interval” den globala insamlarens intervall enligt global_form.php respektive global_settings.php. ”Insamlingsintervall” fungerar i båda inställningarnas sammanhang; återanvändningskontrollen avfärdades.

2026-10-26: Återanvändningskontrollen för Core ”Prefix” och Reportit ”Prefixes” avfärdades i Weblate. Core använder prefix som fältbenämning och Reportit avser SI-prefix; svensk obestämd singular och plural har samma form.

2026-10-26: Routerconfigs ”Filename” och Cactis båda Core-versioners ”File Name” använder ”filnamn”. Återanvändningskontrollen avfärdades efter jämförelse i Weblate.

2026-10-26: ”Connection timeout” i Routerconfigs avser väntetiden vid nätverksanslutning till en enhet (includes/arrays.php). Core 1.2:s ”Connect Timeout” avser motsvarande tidsgräns för LDAP-anslutning (include/global_settings.php). ”Tidsgräns för anslutning” passar båda inställningarna; återanvändningskontrollen avfärdades i Weblate.

2026-10-26: Aktuella Weblate-exporter av Routerconfigs och Core jämfördes per källtext och kontext. Samtliga 54 gemensamma poster med singularöversättning överensstämde; jämförelsen omfattade inga pluralposter och bevisar inte att unika eller sammansatta termer är enhetliga.

2026-10-26: Ett försök att importera fem termändringar från Core 1.2 till Core gav 0 uppdaterade och 5 ej hittade strängar i Weblate. Förslaget sparas som cacti-core-termer-20261026-not-imported.po; strängarnas aktuella status måste utredas innan nytt importförsök. msgfmt, l10n-lint och Hunspell passerade.

2026-10-26: Weblates exakta källtextssökning i Core gav inga träffar för ”Delete All Checks”, trots att posten finns i den nedladdade PO-filen utan obsolete-markering. Importfelet kan alltså inte lösas genom att enbart läsa PO-postens status; övriga avvisade poster behöver också kontrolleras mot Weblates aktiva strängar.

2026-10-26: En samlad exakt källtextssökning efter de övriga fyra avvisade posterna gav inga träffar i Core på Weblate. Tillsammans med importkvittot stöder det att de fem inte är tillgängliga för import i aktuell komponent, även om de finns i PO-exporten. Underlaget för jämförelsen mellan Core-versionerna innehåller därmed potentiellt fler sådana poster och måste verifieras mot Weblate före ändring.

2026-10-26: Core ”Replacement Pattern” och Core 1.2 ”Replace Pattern” avser samma fält, replace_pattern, i inställningsformulär respektive regellista. ”Ersättningsmönster” är därför konsekvent; återanvändningskontrollen avfärdades i Weblate. Källkod: include/global_form.php och lib/api_automation.php.

2026-10-26: Syslogs ”Data Retention Settings” ändrades till ”Inställningar för lagringstid” efter kontroll av inställningens innehåll. Weblate bekräftade en uppdatering utan bortfall; msgfmt, l10n-lint och Hunspell passerade.

2026-10-26: Den tidigare inventeringens skillnad för ”Utilities” är inaktuell: Weblate visar nu ”Verktyg” i Audit, Gexport, Routerconfigs, WMI och båda Core-versionerna. Den gemensamma termen har lagts till i listan. Tholds meddelande om systemets availability använder ”systemtillgänglighet”; detta bekräftar termen i meddelandet men inte samtliga förekomster i komponenten.

2026-10-26: Weblate visar nu ”Tillgänglighet” för Availability i Thold, Monitor, Intropage och båda Core-versionerna, ”Larm” för Alerts i Intropage och Syslog samt ”Tröskelvärden” för Thresholds i Thold, Maint, Monitor och Intropage. Äldre inventeringsskillnader för dessa fristående strängar är inaktuella. Tholds ”No Thresholds” rättades från ”Tröskelvärden” till ”Inga tröskelvärden”; Weblate bekräftade en uppdaterad sträng. msgfmt, l10n-lint och Hunspell passerade. Den separata källsträngen ”No [Thold]” behöver kontextgranskas.

2026-10-26: Tholds källkod visar att ”No [Thold]”, ”No [Template]” och ”No [Template:Thold]” visas i kolumnen för aktivering. De översattes med ”Nej” och motsvarande orsak inom hakparentes. Samma fil rättar ”Edit Threshold Template” och bevarar förkortningen ”ALo:” oförändrad. Weblate bekräftade fem uppdaterade strängar; msgfmt, l10n-lint och Hunspell passerade. Källor: plugin_thold develop, thold.php och thold_graph.php.

2026-10-26: Tolv strängar i Tholds graf- och tröskelvy rättades, inklusive skilda varnings- och larmvärden, förkortningarnas versaler och text om borttaget tröskelvärde. Weblate bekräftade tolv uppdateringar. De tre återställda förkortningarna WHi, WLo och AHi ger kontroller för oförändrad översättning; de lämnas för granskning. msgfmt, l10n-lint och Hunspell passerade.

2026-10-26: WHi, WLo och AHi kontrollerades mot etiketter i thold.php och deras kontroller för oförändrad översättning avfärdades i Weblate. Tre malltexter rättades och uppladdningen bekräftade tre uppdateringar; msgfmt, l10n-lint och Hunspell passerade.

2026-10-26: Trettio texter i Tholds tröskelinställningar granskades och rättades, bland annat skillnaden mellan varning och larm, överträdelse och tidsintervall för rörligt medelvärde. Weblate bekräftade 30 uppdaterade strängar utan bortfall. msgfmt och l10n-lint passerade; Hunspell gav endast en tokeniseringsvarning för RRD-upplösningen.

2026-10-26: Fem hjälptexter i Thold kompletterades med saknade villkor för bekräftelse och varning. HRULE-texternas alternativnamn följer komponentens ”Ingen”, ”Exakt värde” och ”Procent”. Weblate bekräftade fem uppdateringar utan bortfall; msgfmt, l10n-lint och Hunspell passerade.

2026-10-26: Fjorton texter om aviseringar, RPN och skalkommandon rättades. Saknade ersättningstaggar och information om skriptmiljön återställdes, och taggarna jämfördes med källan. Weblate bekräftade 14 uppdateringar. msgfmt och l10n-lint passerade; Hunspell flaggade tekniska identifierare och sammansättningar.

2026-10-26: SNMP-hjälpen i Thold kompletterades med saknade enhets- och datafrågevariabler; samtliga variabelbindningar jämfördes med källan. Källkoden visar att ”Eternal ID” avser fältet external_id och etiketten External ID; översättningen är därför ”externt ID”. Weblate bekräftade tre uppdateringar. msgfmt och l10n-lint passerade; Hunspell flaggade den tekniska sammansättningen SNMP-aviseringar.

2026-10-26: Elva strängar om Tholds mallar och historik rättades; bekräftelserna för aktivering och inaktivering nämner nu både mallar och tröskelvärden, och överträdelser beskrivs utan att enbart anta överskridande. Weblate bekräftade 11 uppdateringar utan bortfall; msgfmt, l10n-lint och Hunspell passerade.

2026-10-26: Ordlistan förtydligar att collector kan vara insamlare, medan poller som nod är datainsamlare och som körande process kan vara insamlingsprocess. Aggregering betecknar sammanställningen och aggregerad graf resultatet. Termval ska kontrolleras mot varje strängs sammanhang; ingen fullständig komponentgranskning följer av denna ordlisteändring.

2026-10-26: Tre poster lades till i [Cactis gemensamma ordlista i Weblate](https://translate.cacti.net/browse/cacti/glossary/sv/) och kontrollerades efter omladdning: aggregate graph → aggregerad graf, collector → insamlare och poller → datainsamlare. Posterna innehåller även förklaringar om sammanhanget.

2026-10-26: Ytterligare tre poster verifierades i Weblates ordlista: threshold → tröskelvärde (gränsvärde som utlöser en varning eller ett larm; tröskel kan användas om funktionen), data source → datakälla (källa till mätvärden som Cacti samlar in och lagrar) samt graph template → grafmall (mall som styr hur en graf skapas och presenteras). Övriga termer i arbetslistan har ännu inte lagts in i Weblates ordlista.

2026-10-26: Weblates ordlista kompletterades med polling → datainsamling (avfrågning när själva förfrågan avses), availability → tillgänglighet (om en enhet eller tjänst är tillgänglig) och device → enhet (övervakad enhet). Samtliga tre kontrollerades i ordlistan efter inläsning.

2026-10-26: Sex hjälptexter för Tholds larm, varningar och återställning rättades. Dubbelkodade ersättningstaggar ersattes med källtextens exakta teckensekvenser. Weblate bekräftade sex uppdaterade strängar utan bortfall; msgfmt och l10n-lint passerade.

2026-10-26: Två återanvändningskontroller i Thold granskades och avfärdades i Weblate. ”Debug” är en loggnivå enligt includes/arrays.php och kan översättas med ”Felsökning”, liksom ”Debugging” och ”Troubleshooting” i deras sammanhang. De två källtexterna om hur länge ett tröskelvärde måste överträdas för att utlösa ett larm har samma innebörd och samma svenska översättning.

2026-10-26: Core 1.2 ”Viewing Graph” används som rubrik framför grafens namn i graph.php och rättades till ”Visar graf”. Åtgärden ”View Graph” behåller ”Visa graf”. Weblate bekräftade en uppdatering; msgfmt, l10n-lint och Hunspell passerade.

2026-10-26: Den omvända återanvändningskontrollen för de likvärdiga texterna om överträdelsens varaktighet avfärdades också. För ”DS Name” bekräftar thold_templates.php fältet data_source_name; ”Datakällans namn” motsvarar därför även ”Data Source Name”. Den kontrollen avfärdades. Weblate visar nu 896 översatta Thold-strängar och inga aktiva kontrollvarningar, med 19 strängar vars kontroller avfärdats. Detta är inte bevis för att alla strängar har granskats rad för rad. En exakt sökning efter ”Viewing Graph” gav inga träffar i nuvarande Core, så rättelsen i Core 1.2 kunde inte överföras dit som samma källsträng.

2026-10-26: I Core 1.2 granskades hjälptexten om datamallar och bekräftelsen för att ta bort aviseringsmottagare. Weblates punktkontroller avfärdades eftersom de svenska fullständiga meningarna har slutpunkt trots att källan saknar den. Pluralkontrollen för aviseringsmottagare avfärdades eftersom obestämd singular och plural har samma form. Övriga varningar och komponenter återstår att granska.

2026-10-26: Motsvarande bekräftelser för att aktivera och inaktivera aviseringsmottagare granskades i Core 1.2. De fyra kontrollerna för slutpunkt och identiska pluralformer avfärdades: de svenska meningarna är fullständiga och mottagare har samma obestämda form i singular och plural. Weblate visade båda kontrollerna som avfärdade för båda strängarna.

2026-10-26: Granskning av graftexterna i Core 1.2 gav ett utkast med tre språkliga rättelser i cacti-core-v1-2-x-grafutkast-20261026.po. Källtext och aktuell svensk text jämfördes i Weblate; den äldre exportens felaktiga ”Empty Graph” var redan rättat. Utkastet är inte uppladdat och behöver ingå i den fortsatta komponentgranskningen. msgfmt och l10n-lint passerade, liksom Hunspell för de svenska orden.

2026-10-26: Återanvändningskontrollen för Core 1.2 ”%s Hours” granskades mot ”%s Hrs”. Båda anger timmar och översättningen ”%s timmar” passar; kontrollen avfärdades i Weblate.

2026-10-26: Core 1.2-utkastet kompletterades med två granskade inställningstexter: ”språkhanterare” används konsekvent med den närliggande hjälptexten och spårningsalternativet beskrivs som avsett för utvecklare. Aktuella måltexter jämfördes i Weblate. Utkastet innehåller fem poster och är inte uppladdat. msgfmt, l10n-lint och Hunspell passerade.

2026-10-26: Källsträngen ”Lock Graph.” finns i Core 1.2 men en direkt kontroll av samma checksumma i Core gav ”Inga strängar hittades”. Överför därför inte just den posten till Core utan ny verifiering; detta säger inget om de övriga fyra utkastsposterna.

2026-10-26: Weblates ”Andra förekomster” visar att ”Preferred Language Processor” har samma källa och kontext i Core och Core 1.2 och är markerad för fortplantning. Båda visar ännu ”Föredragen språkprocessor”; den föreslagna termen ”Föredragen språkhanterare” finns endast i det ej uppladdade Core 1.2-utkastet. Kontrollera båda versionerna efter uppladdning.

2026-10-26: Weblate visar ”Data Sources [%s]” med samma kontext i båda Core-versionerna och en separat källvariant med blanksteg innanför hakparenteserna, också i båda versionerna. Den andra varianten lades till i Core 1.2-utkastet så båda får samma svenska format. De sex utkastsposterna är inte uppladdade. msgfmt och l10n-lint passerade.

2026-10-26: Två texter om Aggregate Template i Core 1.2 har anpassats i utkastet till arbetslistans ”mall för aggregerad graf”. De aktuella översättningarna kontrollerades i Weblate före ändringen. Utkastet innehåller åtta poster och är inte uppladdat. msgfmt och l10n-lint passerade; Hunspell flaggade ”grafmallen.”.

2026-10-26: Etiketten ”Aggregate Template” visar ”Aggregatmall” i båda Core-versionerna och är markerad för fortplantning. Utkastet kompletterades med ”Mall för aggregerad graf” enligt terminologilistan. Kontrollera fortplantningen när utkastet laddas upp. Utkastet innehåller nio poster; msgfmt, l10n-lint och Hunspell passerade.

2026-10-26: ”Aggregate Templates” finns med samma källa och kontext i båda Core-versionerna. Pluraletiketten ändrades i utkastet till ”Mallar för aggregerade grafer”, i linje med singularformen. Weblate anger fortplantning; kontrollera den efter uppladdning. Utkastet har tio poster, är inte uppladdat och har kontrollerats med msgfmt, l10n-lint och Hunspell.

2026-10-26: Core 1.2-utkastet cacti-core-v1-2-x-grafutkast-20261026.po laddades upp via Weblate. Bekräftelsen angav 16 uppdaterade strängar, inga överhoppade och inga saknade. Efter uppladdningen visade komponenten 44 strängar med aktiva kontrollvarningar; dessa återstår att granska. Kopian i arkivet innehåller samma 16 poster. msgfmt och l10n-lint passerade före uppladdningen.

2026-10-26: Två kontrollvarningar i Core 1.2 för ”Data Sources [%s]” och varianten med blanksteg avfärdades efter jämförelse: källorna betyder samma sak och den svenska etiketten är ”Datakällor [%s]”. Weblate visade båda kontrollerna som avfärdade. Andra förekomster visar att motsvarande strängar även finns i Core; formatet där behöver vid behov kontrolleras i redigeringsfältet eftersom tabellvyn normaliserar blanksteg.

2026-10-26: Aktuell Core 1.2-katalog hämtades från Weblate. Fjorton kvarvarande texter med ”aggregatmall” anpassades till ”mall för aggregerad graf”; formatvariabler bevarades. Weblate bekräftade 14 uppdaterade, inga överhoppade och inga saknade strängar. msgfmt och l10n-lint passerade; Hunspell flaggade den korrekta sammansättningen ”grafmallen”. Efter uppladdningen visades 42 strängar med aktiva kontrollvarningar.

2026-10-26: Den aktuella Core-katalogen hämtades och åtta komponentspecifika texter med ”aggregatmall” ändrades till ”mall för aggregerad graf”. Weblate bekräftade åtta uppdaterade strängar, inga överhoppade eller saknade. msgfmt och Hunspell passerade. l10n-lint rapporterade en slutpunktsvarning: den svenska översättningen är en fullständig mening och har därför slutpunkt. Efter uppladdningen visades 37 strängar med aktiva kontrollvarningar i Core.

2026-10-26: Datainsamlarens hjärtslagsvarning rättades och skickades till Core; Weblate bekräftade en uppdatering. Sex andra föreslagna poster fanns i PO-exporten men hittades inte vid uppladdningen; orsaken är inte fastställd. De ingår inte i den arkiverade filen med aktiva ändringar. msgfmt, l10n-lint och Hunspell passerade för filen före uppladdningen.

2026-10-26: Weblates sökning i Core efter ”1 hour guarded poller ratio” och bredare ”guarded” gav inga träffar, trots att den första källtexten finns som aktiv PO-post i den nedladdade filen. PO-exporten innehåller 5 705 poster, varav 177 är markerade föråldrade; Weblates komponentöversikt visar 5 198 strängar. Exportens poststatus räcker därför inte ensam för att avgöra vad som kan importeras. Kontrollera osäkra källsträngar i Weblate före uppladdning; den exakta orsaken till de sex omatchade posterna är inte fastställd.

2026-10-26: Fem pluralvarningar för att ta bort, aktivera och inaktivera datainsamlare i Core 1.2 granskades och avfärdades i Weblate. ”Datainsamlare” har samma obestämda form i singular och plural. Weblate visar därefter 38 strängar med aktiva kontrollvarningar, varav ingen gäller identiska pluralformer.

2026-10-26: Fyra punktkontroller i Core 1.2 granskades och avfärdades: översättningarna om XML-filer, avinstallation, borttagning av användargrupper och rrdcheck är fullständiga svenska meningar med slutpunkt. Weblate visar därefter 34 strängar med aktiva kontrollvarningar, samtliga av typen återanvänd översättning.

2026-10-26: Sju återanvändningskontroller i Core 1.2 avfärdades efter jämförelse: två likvärdiga meddelanden om slutförd automatisering, anslutningens tidsgräns, borttagningsmetod, ersättningsmönster, MB samt grafobjekt i singular och plural. Weblate visar därefter 27 strängar med aktiva kontrollvarningar.

2026-10-26: Nio återanvändningskontroller i Core 1.2 granskades och avfärdades för motsvarande texter om mallborttagning, lyckad åtgärd, grafträd, misslyckad autentisering, paket, skript, platsens delstat eller region samt filnamn. Weblate visar därefter 18 strängar med aktiva kontroller.

2026-10-26: RRD-filernas åtgärd ”Archive” rättades till ”Arkivera” i Core 1.2. Uppladdningen uppdaterade en sträng och ändringen fortplantades till Core; sammanhanget verifierades i rrdcleaner.php.

2026-10-26: Tretton återanvändningskontroller i Core 1.2 granskades och avfärdades: användare, alfabetisk sortering, ändringslogg, upplåsning, rensning, garantivillkor, skript och datainsamlare. Weblate visar därefter fyra strängar med aktiva kontroller; de kräver fortsatt undersökning.

2026-10-26: Båda domäntypkontrollerna i Core 1.2 avfärdades efter granskning av närliggande texter i user_domains.php: båda avser en domäns typ. Två kontroller återstår (Warnings och Objects).

2026-10-26: Tolv återanvändningskontroller i Core avfärdades efter jämförelse av källtexterna: grafmallar, paket, inläsning och uppgradering av insticksmoduler samt användaråtgärder i singular och plural. Weblate visar fyra strängar med aktiva kontroller i Core.

2026-10-26: Kontroller för ”Collector” och ”Delete Report” avfärdades i Core. ”Insamlare” följer Cactis ordlista för collector och poller; båda rapporttexterna gäller borttagning. Källkoden för rapportåtgärden och behörighetsrubriken kontrollerades. Två aktiva kontroller återstår i Core.

2026-10-26: Kontrollen för ”%s MB” i hmib avfärdades: den återanvända översättningen motsvarar även ”%s MBytes”. Mactrack har en inkonsekvensvarning för ”MAC Addresses”; de jämförda svenska formerna i komponenten är ”MAC-adresser”, men varningens fulla orsak är ännu inte klarlagd.

2026-10-26: Två texter i mactrack rättades från ”Mac-adresser” till ”MAC-adresser” och skickades till Weblate (2 uppdaterade). Filen kontrollerades med msgfmt och Hunspell; l10n-lint och svterm var inte tillgängliga i PATH vid denna kontroll.

2026-10-26: Efterkontroll av mactrack-filen med den lokala källkoden för l10n-lint gav inga anmärkningar. Svlang gav tre frekvensnoteringar för vanliga svenska ord, vilka granskades manuellt. Den lokala svenska termbanken använder också MAC-adress. Svterm har ännu inte körts på filen.

2026-10-26: Mactrack-texten om att ta bort platser rättades från ”sajter” till ”platser” enligt terminologin. Weblate bekräftade en uppdatering. msgfmt och Hunspell passerade; l10n-lints två varningar om källans frågetecken bedömdes manuellt eftersom den svenska uppmaningen avslutas med punkt. De två tidigare MAC-rättningarna verifierades i Weblate-editorn. Svterm hittades inte lokalt; GitHub-repot yeager/svterm kunde inte hittas.

2026-10-26: Mactracks fält ”Ticket Number” rättades från ”Biljettnummer” till ”Ärendenummer”, i enlighet med hjälptexten om ärendehanteringssystem och e-postmallen. Weblate bekräftade en uppdatering. msgfmt, l10n-lint och Hunspell passerade.

2026-10-26: Mactrack-texten ”No Non Interface Graphs in Cacti” förtydligades till ”Det finns inga grafer som inte gäller gränssnitt i Cacti”, i linje med motsvarande visningskommando. Weblate bekräftade en uppdatering. msgfmt och l10n-lint passerade; Hunspell flaggade produktnamnet Cacti.

2026-10-26: Tre mactrack-texter om standardplats och platsrapport rättades från ”webbplats” till ”plats”. Weblate bekräftade tre uppdateringar. msgfmt och l10n-lint passerade; Hunspell flaggade endast produktnamnen MacTrack och Cacti-loggen.

2026-10-26: Mactrack platsfilter och IP-intervall samordnades med övriga platstermer. Weblate bekräftade två uppdateringar; msgfmt och l10n-lint passerade, medan Hunspell flaggade sammansättningar med produktnamnet Mactrack. Den tidigare uppmaningen om borttagning av platser har två kvarvarande skiljeteckenkontroller eftersom den engelska källan slutar med frågetecken och den svenska uppmaningen med punkt.

2026-10-26: Mactracks kolumn ”Added/Modified” rättades från ”Inkom / Ändrad” till ”Tillagd/ändrad”. Weblate bekräftade en uppdatering; msgfmt, l10n-lint och Hunspell passerade.

2026-10-26: Mactracks ”Title of SNMP Option Set” ändrades till ”Titel för uppsättningen SNMP-alternativ”, i linje med intilliggande texter. Weblate bekräftade en uppdatering. msgfmt och l10n-lint passerade; Hunspell flaggade den tekniska sammansättningen SNMP-alternativ.

- Mactrack: `mactrack-tidsuppgifter-sv.po` laddades upp 2026-10-26; Weblate bekräftade fyra uppdaterade strängar. Granskningen fortsätter.

- Mactrack: `mactrack-8021x-sv.po` laddades upp 2026-10-26; fyra strängar uppdaterades. Granskningen är inte färdig.

- Mactrack: `mactrack-installningar-sv.po` laddades upp 2026-10-26; Weblate uppdaterade 11 strängar. Två lintvarningar gäller frågetecken i svenska frågor vars engelska källtext har punkt. Radgranskningen fortsätter.

- Mactrack: `mactrack-snmp-sv.po` laddades upp 2026-10-26; sju strängar uppdaterades. Granskning av komponenten pågår.

- 2026-10-26: Granskade mactracks kontrollvarningar och avfärdade sju varningar om skiljetecken och återanvändningen av ”Startdatum”, där översättningarna var korrekta. En varning om inkonsekvent översättning av ”MAC Addresses” återstår att undersöka över komponenterna.

- 2026-10-26: Projektets sökning och arkiverade PO-filer visade ”MAC-adresser” för de synliga förekomsterna av ”MAC Addresses”. Varningen i mactrack avfärdades; Weblate visade ingen avvikande översättning men angav inte den exakta orsaken till varningen.

- 2026-10-26: `mactrack-auktorisering-sv.po` skickades upp; tre strängar uppdaterades. Texterna anger att det är auktoriseringen som återkallas. msgfmt, l10n-lint och Hunspell passerade.

- 2026-10-26: Core 1.2: `core-12-graf-fargmall-sv.po` rättar båda pluralformerna till ”aggregerade grafer”. Weblate bekräftade en uppdaterad sträng; msgfmt, l10n-lint och Hunspell passerade. Äldre exportskillnader måste verifieras mot aktiva strängar eftersom fortplantning redan har rättat vissa.

- 2026-10-26: `core-koppla-graf-sv.po` laddades upp till core; Weblate bekräftade fyra uppdateringar. Texterna om att koppla grafer anger nu ”aggregerad graf”. msgfmt, l10n-lint och Hunspell passerade.

- 2026-10-26: `mactrack-skanning-sv.po` laddades upp; fyra strängar ändrades till skanning för enhetlighet inom komponenten. msgfmt och l10n-lint passerade; Hunspell flaggade den tekniska beteckningen 802.1X-skanning.

- 2026-10-26: `mactrack-skanning-beskrivning-sv.po` laddades upp; Weblate bekräftade tre uppdaterade strängar. msgfmt och l10n-lint passerade; Hunspell flaggade tekniska beteckningar och switchar.

- 2026-10-26: `mactrack-trafik-sv.po` skickades upp; två rubriker för inkommande och utgående trafik uppdaterades. Den befintliga svenska procentangivelsen bevarades. msgfmt, l10n-lint och Hunspell passerade.

- 2026-10-26: Kontrollerna för ”Start Date” och ”Objects” avfärdades efter jämförelse: ”Startdatum” passar även ”Date Started”, och ”objekt” har samma form i singular och plural. Weblate visade ingen aktiv varning för dessa i core 1.2 efteråt. Varningen för ”Warnings” behöver ytterligare underlag eftersom Weblate inte visade de andra källsträngarna.

- 2026-10-26: Thold: rättade skillnaden mellan varningar och larm samt återställde HTML-entiteter i en hjälptext. Weblate bekräftade två uppdaterade strängar; msgfmt, l10n-lint och Hunspell kontrollerade ändringarna.

- 2026-10-26: Intropage: filen cacti-intropage-varningar-larm-20261026.po laddades upp. Weblate uppdaterade fem av sex strängar; ”Host alerts (up/down/recovering) in last 30 minutes” hittades inte och är därmed inte uppladdad. msgfmt och l10n-lint passerade; Hunspell flaggade Intropage och Ping-svarstider. Granskningen fortsätter.

- 2026-10-26: Intropage: granskning av exportens inledande avsnitt gav 15 språk- och terminologirättningar i cacti-intropage-granskning-20261026.po. Weblate bekräftade 15 uppdateringar. msgfmt och l10n-lint passerade; Hunspell flaggade sammansättningen siduppdatering. Resten av komponenten återstår att granska.

- 2026-10-26: Intropage, fortsatt radgranskning av exportens poster 140–299: 23 korrigeringar skickades upp och Weblate bekräftade 23 uppdaterade. msgfmt passerade; l10n-lints två skiljeteckenvarningar gäller en rubrik med ellips i källan. Hunspell flaggade tekniska sammansättningar med NTP och SNMP. Resten återstår att granska.

- 2026-10-26: Intropage, genomgång av exportens återstående poster 300–546 gav 24 rättningar, bland annat Spine, misslyckade insamlingar och databegrepp. Weblate bekräftade 24 uppdaterade. msgfmt och l10n-lint passerade; Hunspell flaggade produktnamn och tekniska beteckningar. Övriga fynd och kontrollvarningar kräver fortsatt granskning.

- 2026-10-26: Intropage: ytterligare 14 ändringar laddades upp och bekräftades av Weblate. msgfmt och l10n-lint passerade; den numeriska noteringen för ”senaste dygnet” granskades, och Hunspell flaggade namn samt pingtid. Slutpunktskontrollen för rubriken om administratörspanelen avfärdades eftersom källan slutar med två punkter och den svenska rubriken med ”med mera”. Kontrollen för Warnings kvarstår.

- 2026-10-26: Intropage: ytterligare tolv rättningar av larmtexter, databasråd och övervakning laddades upp; Weblate bekräftade tolv uppdateringar. msgfmt och l10n-lint passerade; Hunspell flaggade tekniska namn och sammansättningar.

- 2026-10-26: Syslog: granskning av början av aktuell export gav 15 rättningar, inklusive kommandoflaggan --alert-name och HTML-taggar i uppgraderingsinformationen. Weblate bekräftade 15 uppdateringar. msgfmt och l10n-lint passerade; Hunspell flaggade tekniska namn och kommandoflaggor. Resterande rader återstår att granska.

- 2026-10-26: Syslog: 15 ytterligare ändringar i inställningar och instrumentpaneler laddades upp och bekräftades av Weblate. Larm, lagringstid, rapportregler och Syslog-facilitet följer nu terminologin i dessa poster. msgfmt och l10n-lint passerade; Hunspell flaggade tekniska sammansättningar. Radgranskningen fortsätter.

- 2026-10-26: Syslog: filen cacti-syslog-granskning-03-20261026.po innehöll 14 genomgångna poster; Weblate uppdaterade 12 och hoppade över två. msgfmt och l10n-lint passerade; Hunspell flaggade produktnamn och filnamn. Fortsatt radgranskning återstår.

- 2026-10-26: Syslog: 29 ändringar i larmregler, sökning och aviseringar skickades upp; Weblate bekräftade samtliga. msgfmt och l10n-lint passerade utan fel eller varningar (fyra informationsnoteringar om engelsk pluralparentes); Hunspell flaggade Syslog-sammansättningar. Återstående rader och tekniska mallar behöver fortsatt granskning.

- 2026-10-26: Syslog: 21 rättningar för borttagnings- och rapportregler samt två hjälptexter med HTML och ersättningsvariabler skickades upp; Weblate bekräftade samtliga. msgfmt och l10n-lint passerade; Hunspell flaggade tekniska termer och variabler. Hela exporten har nu gåtts igenom, men ytterligare fynd och kontroll av aktuellt resultat återstår.

- 2026-10-26: Syslog: fyra beskrivningar av fjärrdatainsamlare och larm rättades; Weblate bekräftade fyra uppdateringar. msgfmt och l10n-lint passerade, Hunspell flaggade tekniska namn. OBS: en ny PO-export visade äldre måltexter för tidigare uppladdningar, medan Weblates redigerings-/bläddringsvy visade de nya texterna. Utgå inte från exporten som bevis på aktuell Weblate-status utan jämför mot vyn.

- 2026-10-26: Syslog: sju texter om larm, aviseringslistor och import rättades; Weblate bekräftade sju uppdateringar. msgfmt passerade, l10n-lint gav en granskad kommavarning mellan två huvudsatser och Hunspell flaggade produktnamnet Thold.

- 2026-10-26: Efterkontroll: Weblates komponentinformation visar arkivrevision b8134bfd, och en läsning av dess svenska PO-fil saknar de senaste ändringarna trots att de syns i Weblates bläddringsvy. De enskilda inskickade ändringsfilerna finns i arkivet här; Weblates Git-arkivering och vidare överföring upstream är ännu inte verifierad. Någon orsak har inte fastställts.

- 2026-10-26: Syslog: tio rubriker och rapporttexter rättades; Weblate bekräftade tio uppdateringar. msgfmt passerade före uppladdning, l10n-lint gav endast informationsnoteringar om källans pluralparenteser och Hunspell flaggade Syslog-sammansättningar. Weblates Git-HEAD var fortfarande b8134bfd vid kontrollen; vidare upstream-överföring är inte verifierad.

- 2026-10-26: Flowview: åtta texter om frågor, DNS och rutter rättades; Weblate bekräftade åtta uppdaterade. msgfmt och l10n-lint passerade, Hunspell flaggade tekniska namn. Hela komponentens fortsatta radgranskning återstår.

2026-10-26: Flowview fick 12 korrigeringar för bland annat UDP-kö, aviseringslistor, in- och utgående gränssnitt och rapportfilter. Weblate bekräftade 12 uppdaterade och 0 saknade strängar. Delade strängar för graftyp och grafhöjd behölls. msgfmt, l10n-lint, svlangs skrivregler och Hunspell passerade. Weblates tidigare observerade fördröjning mellan redigeringsvyn och PO-exporten innebär att publicering till källförrådet behöver verifieras separat.

- 2026-10-26: Flowview: posterna 200–389 i den lokala exporten `cacti-flowview-sv (3).po` jämfördes med befintliga arkiverade rättningar. Äldre måltexter för bland annat UDP-kö, aviseringslista och gränssnitt är redan åtgärdade i inskickade deltafiler. Inga nya rättningar har skickats utifrån denna export; den är inte ett säkert underlag för aktuell Weblate-status. Källtexten ”Every %d Weeks, 2” behöver källkodskontext innan en ändring kan bedömas.

- 2026-10-26: Undersökte ”Every %d Weeks, 2” mot Flowviews uppdaterade develop-revision be20ab7. `flowview_schedules.php` skickar `__('Every %d Weeks, 2', 'flowview')`, medan timintervallen skickar talet som separat argument. Siffran 2 har alltså hamnat i källsträngen i stället för som formateringsargument. Dessutom anger intervallnycklarna för vecka, två veckor och månad 432000, 864000 respektive 1728000 sekunder; schemakoden använder värdena som sekunder, vilket motsvarar 5, 10 respektive 20 dygn. Detta är ett källkodsfel och kan inte rättas säkert med enbart översättning. Ingen ändring eller upstreamrapport har skickats; beakta befintliga sparade scheman vid en eventuell kodrättning.

- 2026-10-26: Flowview: meddelandet om borttagning av ett flödesfilter formulerades om och sparades i Weblate. En ny öppning av posten https://translate.cacti.net/translate/cacti/flowview/sv/?checksum=5321f71b0ae4b97d bekräftade texten. Deltafilen `cacti-flowview-delete-filter-20261026.po` passerade msgfmt och l10n-lint, och svensk text passerade svlang skrivregler och hunspell-sv. Överföring från Weblate till källförrådet är inte verifierad.

- 2026-10-26: Flowview: ”Legacy PHP Runner” ändrades till ”Äldre PHP-körare” för att stämma med den närliggande beskrivningen. Texten sparades och verifierades i Weblate: https://translate.cacti.net/translate/cacti/flowview/sv/?checksum=1dccb6b72745f8e6. msgfmt, l10n-lint, svlangs skrivregler och hunspell-sv passerade. Weblate anger ändringen som väntande; överföring till källförrådet är inte verifierad. Exportens poster från 715 och framåt är föråldrade och ingår inte i de 715 aktiva strängarna.

- 2026-10-26: Flowview: fyra granskningsförslag i `cacti-flowview-fyra-forslag-20261026.po`, inklusive kontakt-ID för ping enligt RFC 5943. Filen är lokalt kontrollerad med msgfmt, l10n-lint, svlang och hunspell-sv; Hunspell markerar fackordet ”ping”. Uppladdning är ännu inte bekräftad: filväljaren öppnades men inget importresultat har verifierats. Kontrollera aktuella värden och fortplantning innan import.

- Uppdatering 2026-10-26: `cacti-flowview-fyra-forslag-20261026.po` laddades upp till Flowview via Weblate. Importresultat: 4 bearbetade, 4 uppdaterade, 0 överhoppade och 0 saknade. Synkronisering till projektets källförråd har inte verifierats.

- 2026-10-26: Core 1.2: ”datasamlaren” ändrades till ”datainsamlaren” i beskrivningen av standardtrådar, enligt den gemensamma terminologin. Weblate bekräftade en uppdaterad sträng och noll saknade. msgfmt och l10n-lint passerade; svlang och hunspell-sv kontrollerade det ändrade ordet. Vidare synkronisering till källförrådet är inte verifierad.

- 2026-10-26: En uppföljande sökning i aktuell Weblate för Core efter ”datasamlare” gav inga träffar. Den tidigare skillnaden i `core-jamforelse-20261026.md` bygger på en äldre export och ska inte återinföras. Sökresultatet bevisar endast att den sökta formen saknas i Core, inte att hela komponentens terminologi är färdiggranskad.

- 2026-10-26: Core: den återstående aktiva återanvändningskontrollen för ”Warnings” → ”Varningar” granskades och avfärdades i Weblate. Översättningen är korrekt även för förekomsterna i Core 1.2 och Intropage. Weblate visade därefter alternativet ”Återställ”; detta är en kontrollåtgärd, inte en översättningsändring.

- 2026-10-26: Sökningen efter aktiva kontroller i Core 1.2 gav inga träffar vid kontrolltillfället. Flowviews återstående slutpunktsvarning för käll-AS-texten avfärdades: den svenska texten består av hela meningar med punkt, medan källtexten saknar avslutande punkt. Textens hänvisning till käll-AS har tidigare kontrollerats mot koden. Weblate visade ”Återställ” efter avfärdandet.

- 2026-10-26: GPS Maps: Weblate innehåller uppenbara språkfel, bland annat ”Starting Degree” → ”Startande examen”. GitHubs senaste publicerade release för Cacti/plugin_gpsmaps är dock v2.1 från 2019-03-01, äldre än den angivna gränsen på 48 månader. Ingen ny översättning har därför skickats in. Källa: https://github.com/Cacti/plugin_gpsmaps/releases/tag/v2.1. Projektöversiktens 100 % och noll kontroller innebär inte att texten är språkgranskad.

- 2026-10-26: Audit: tidigare export med ”poller-cykel” och ”Batchstorlek för poller” är inaktuell; Weblate visar ”insamlingscykel” och ”Batchstorlek för insamling” och anger ändringarna som väntande. Senaste GitHub-release för Cacti/plugin_audit är v1.2 från 2024-03-17, inom 48 månader. Vidare synkronisering är inte verifierad.

### Audit, 26 oktober 2026

Den aktuella exporten med 173 strängar genomgicks mot engelskan. Fyra formuleringar om behandling av begäran, Syslog-status, autentiseringskontroller och privat nyckel förtydligades. Weblate bekräftade fyra uppdaterade strängar utan överhoppade eller saknade strängar. Ändringsfil: `Cacti/cacti-audit-sv-sprakgranskning-20261026.po`. `msgfmt --check`, l10n-lint och svlang passerade; Hunspell-resultatet granskades med hänsyn till tekniska termer och PO-metadata.

### GPS Maps, 26 oktober 2026

Den aktuella katalogens 37 strängar jämfördes med Weblates vy och granskades. Tjugo ändringar skickades in; Weblate bekräftade 20 uppdaterade, inga överhoppade och inga saknade. Fil: `Cacti/cacti-gpsmaps-sv-granskning-20261026.po`. Kontroller med msgfmt, svlang och hunspell-sv passerade; l10n-lint påvisade endast skillnaden mellan källans punkt och frågetecknet i den svenska frågan. Weblates två motsvarande kontroller avfärdades. Senaste release är v2.1, 2019-03-01, alltså äldre än 48 månader. Tidigare beslut att avstå på grund av åldern var en för snäv tolkning av instruktionen att kontrollera releaseåldern. Weblate visade ändringarna som väntande i arkivet; överföring till källförrådet har inte verifierats.

### Gexport, 26 oktober 2026

Samtliga 208 aktiva poster i exporten jämfördes med källan och tidigare arkiverade rättningar. Rubriken för borttagning av grafexportdefinitioner ändrades så att den följer rubrikerna för aktivering och inaktivering. Weblate bekräftade en uppdaterad sträng och inga saknade. Ändringsfil: `Cacti/cacti-gexport-sv-granskning-20261026.po`. msgfmt och svlang passerade; l10n-lint gav endast en informationsnotering om källans pluralparentes och Hunspell flaggade sammansättningen grafexportdefinitioner. Senaste release: v2.1, 2023-07-27 (https://github.com/Cacti/plugin_gexport/releases/tag/v2.1), inom 48 månader. Synkronisering till källförrådet är inte verifierad.

### WMI, 26 oktober 2026

Samtliga 134 aktiva strängar i exporten granskades mot källtexten och Weblates bläddringsvy. Trettio ändringar skickades och bekräftades av Weblate; en av dem justerades därefter från ”Ta bort WMI-fråga” till ”Koppla bort WMI-fråga” och bekräftades separat. Källkoden i `setup.php` visar att åtgärden tar bort kopplingen till enhetsmallen, inte själva frågan. Även råa respektive formaterade prestandadata kontrollerades mot frågorna i `wmi_tools.php`. Ändringsfilen `Cacti/cacti-wmi-sv-granskning-20261026.po` innehåller de slutliga 30 värdena. msgfmt, l10n-lint och svlang passerade; hunspell-sv flaggade WMI-, WQL- och OD-sammansättningar. GitHub anger inga publicerade releaser för Cacti/plugin_wmi; åldersgränsen kan därför inte fastställas för en release. Weblate visade därefter 100 procent och inga aktiva kontroller. Den gemensamma strängen ”Queries” är fortfarande ”Databasfrågor” i WMI trots att den även omfattar WMI-frågor, och är kopplad till Core; kontrollera Core-kontexten innan den ändras. Upstreamsynkronisering är inte verifierad.

- 2026-10-26: Den delade strängen ”Queries” granskades mot WMI:s frågelista och Core `support.php` (databasprocesser). ”Frågor” fungerar som rubrik i båda sammanhangen, till skillnad från ”Databasfrågor” i WMI. Weblate bekräftade en uppdatering i WMI och Core-vyn bekräftade att ändringen fortplantats. Ändringsfil: `Cacti/cacti-wmi-sv-fragor-20261026.po`. msgfmt, l10n-lint, svlang och hunspell-sv passerade. Publicering till respektive källförråd är inte verifierad.

### Cycle, 26 oktober 2026

Alla 60 aktiva strängar jämfördes med källan och den aktuella Weblate-vyn. Tjugotvå korrigeringar förtydligar grafväxling och använder grafterminologi; även den felaktigt översatta instruktionen för reguljära uttryck rättades. Weblate bekräftade 22 uppdaterade, noll överhoppade och noll saknade. Ändringsfil: `Cacti/cacti-cycle-sv-granskning-20261026.po`. msgfmt, l10n-lint och svlang passerade; Hunspell flaggade sammansättningarna grafväxling och grafförklaring. Senaste GitHub-release är v4.1 från 2018-04-01 (https://github.com/Cacti/plugin_cycle/releases/tag/v4.1), äldre än 48 månader. Synkronisering till källförrådet har inte verifierats.

### Maint, 26 oktober 2026

De 120 aktiva posterna jämfördes med källtexten och Weblates vy. Femton rättningar av bland annat underhållsscheman, WebSeer och pluralparenteser skickades in; Weblate bekräftade 15 uppdateringar utan överhoppade eller saknade strängar. Ändringsfil: `Cacti/cacti-maint-sv-granskning-20261026.po`. msgfmt och svlang passerade; l10n-lint gav informationsnoteringar om källans pluralparenteser och hunspell-sv flaggade produktnamn och en förled. Två återanvändningskontroller för ”Device(s)” och ”Devices” kvarstår eftersom även ”View Devices” ingår i jämförelsen. Senaste release v1.3, 2026-01-28: https://github.com/Cacti/plugin_maint/releases/tag/v1.3. Överföring från Weblate till källförrådet är inte verifierad.

- 2026-10-26: Uppföljning av Maints återanvändningskontroller: Mactracks ”View Devices” används som knappens titel i `mactrack_view_sites.php` och ändrades från ”Enheter” till ”Visa enheter”, samma översättning som i HMIB. Weblate bekräftade en uppdatering; `Cacti/cacti-mactrack-sv-visa-enheter-20261026.po` passerade msgfmt, l10n-lint, svlang och hunspell-sv. Därefter avfärdades Maints två kontroller för ”Device(s)” och ”Devices”, vilka båda lämpligen översätts ”Enheter”. Senaste Mactrack-release v4.8 publicerades 2024-10-16: https://github.com/Cacti/plugin_mactrack/releases/tag/v4.8. Synkronisering till källförrådet är inte verifierad.

### Mikrotik, 26 oktober 2026

Katalogens 241 strängar granskades mot källtexten, Weblates vy och tidigare arkiv. Ändringsfilen `Cacti/cacti-mikrotik-sv-granskning-20261026.po` innehåller 66 poster; Weblate rapporterade 65 uppdaterade, en överhoppad och inga saknade. Orsaken till den överhoppade posten är inte verifierad. Terminologi för insamlare, nätverk och produktnamn rättades. msgfmt passerade; l10n-lint rapporterade en skiljeteckensskillnad och svlang flaggade förkortningen PPPoE. De två skiljeteckenskontrollerna avfärdades eftersom källans fråga slutar med punkt. Senaste release v3.1 publicerades 2023-01-29: https://github.com/Cacti/plugin_mikrotik/releases/tag/v3.1. Synkronisering till källförrådet är inte verifierad.

- Uppföljning: Weblates aktuella bläddringsvy på alla 13 sidor innehåller de granskade svenska formuleringarnas sökta textutdrag, inklusive de nio sist tillagda formuleringarna om behörigheter, minne och drifttid. Jämförelsen gjordes med textutdrag, inte en fullständig jämförelse av varje post och kontext; den identifierar inte den överhoppade importposten.

### Flowview, fortsatt granskning 26 oktober 2026

Weblates aktuella översikt visade 715 översatta strängar och inga aktiva kontrollvarningar. De första nio bläddringssidorna granskades mot källtexten: inställningar för DNS-cache, internetrutter och flödeslyssnare har redan rättats i den aktuella vyn, som skiljer sig från den äldre nedladdade PO-filen. Ingen äldre fil laddades därför upp på nytt. Fältetiketter för routningsregister behöver ytterligare kontextkontroll, bland annat ”MP Default” som visas som ”Standard” och ”Members By Fef” vars engelska källa kan innehålla ett skrivfel. Återstående sidor behöver granskas. Senaste publicerade release är v4.8 från 2024-08-19: https://github.com/Cacti/plugin_flowview/releases/tag/v4.8.

- Flowviews registerfält: källkoden `flowview_databases.php` kopplar ”Members By Fef” till `mbrs_by_ref`; översättningen ändrades till ”Medlemmar via referens”. ”MP Default” ändrades till ”MP-standard” så att MP-delen behålls. Weblate bekräftade två uppdaterade poster utan överhoppade eller saknade. Ändringsfil: `Cacti/cacti-flowview-sv-register-20261026.po`. msgfmt, svlang och hunspell-sv passerade. Överföring till källförrådet är inte verifierad; fortsatt granskning återstår.

- Flowview: de återstående bläddringssidorna 10–36 jämfördes med källtexterna. ”Graph Type” och ”Graph Height” ändrades till ”Diagramtyp” och ”Diagramhöjd” i enlighet med hjälptexterna för stapel-, cirkel- och träddiagram. Weblate bekräftade två uppdateringar utan överhoppade eller saknade poster. Fil: `Cacti/cacti-flowview-sv-diagram-20261026.po`. msgfmt, l10n-lint, svlang och hunspell-sv passerade. Källtexten ”Every %d Weeks, 2” har en misstänkt formateringsmiss i `flowview_schedules.php`; den behöver åtgärdas i källkoden. Weblates spridning av gemensamma strängar till andra komponenter och synkronisering till källförrådet är inte verifierade.

- Uppföljning av delade diagramsträngar: tidigare Core-exporter anger ”Grafhöjd” för `Graph Height` i grafmallar och rapporter samt ”Typ av diagram” för `Graph Type`. De exporterna är inte bevis för aktuellt Weblate-innehåll; kontroll av eventuell automatisk spridning återstår. I Flowviews aktuella källkod `flowview_schedules.php` har veckointervallet etiketten `Every %d Weeks, 2` utan separat numeriskt formateringsargument. Även värdena 432000, 864000 och 1728000 ligger intill etiketterna vecka, två veckor och månad; deras tidsenhet och beräkning behöver kontrolleras innan en kodändring föreslås.

- Rättelse av Flowviews diagrametiketter: Weblates vy ”Andra förekomster” visade att ändringarna automatiskt fortplantades till Core, Core 1.2 och för `Graph Height` även Cycle. Därför ändrades de gemensamma strängarna till ”Graftyp” och ”Grafhöjd”, som fungerar även i grafmallar och tidsserier. Weblate visade de nya värdena på samtliga angivna förekomster. Den tidigare filen med ”Diagramtyp” och ”Diagramhöjd” är historik och ska inte laddas upp igen. Slutlig korrigeringsfil: `Cacti/cacti-gemensam-grafetikett-korrigering-20261026.po`; ändringarna gjordes direkt i Weblate. msgfmt, l10n-lint och svlang passerade; hunspell-sv flaggade sammansättningen ”Graftyp”. Källkodens schemaläggning lägger `sendinterval` direkt till ett Unix-tidsvärde från `strtotime`, vilket bekräftar sekunder: de nuvarande valen för vecka, två veckor och månad motsvarar 5, 10 respektive 20 dygn. Ingen källkodsrättning eller migrering av befintliga scheman har gjorts.

- Intropage: Weblates aktuella översikt visade 542 översatta strängar och inga aktiva kontroller. Fyra ytterligare rättningar av delning, panelkopiering, panelbibliotek och automatisk avinstallation skickades i `Cacti/cacti-intropage-sv-uppfoljning-20261026.po`; Weblate bekräftade fyra uppdaterade, inga överhoppade eller saknade. msgfmt, l10n-lint och svlang passerade; hunspell-sv flaggade produktnamnets genitiv ”Intropages”. GitHubs senaste release är v4.0.4 från 2024-04-26: https://github.com/Cacti/plugin_intropage/releases/tag/v4.0.4. Synkronisering till källförrådet är inte verifierad.

- Intropage: åtta visningstexter för larmgränser fick svenska decimaltecken och mellanrum före s och ms; siffervärdena är oförändrade. Weblate bekräftade åtta uppdateringar, utan överhoppade eller saknade strängar. Fil: `Cacti/cacti-intropage-sv-varden-20261026.po`. msgfmt, l10n-lint, svlang och hunspell-sv för de svenska orden passerade. Synkronisering till källförrådet är inte verifierad.

- Intropage: sex rättningar av nätverks- och belastningstermer skickades i `Cacti/cacti-intropage-sv-natverk-20261026.po`, bland annat IP-adresser, MAC-adresser, processoranvändning och DNS-uppslagning. Weblate bekräftade sex uppdaterade, inga överhoppade eller saknade. msgfmt och svlang passerade; l10n-lint gav en informationsnotering om längre översättning av ”IPs”, och hunspell-sv flaggade tekniska namn. Automatisk spridning till andra komponenter och synkronisering till källförrådet är inte verifierade.

- Uppföljning av Intropage: Weblates jämförelse visade att `IPs` och `MACs` i MacTrack-panelen motsvarar flera annorlunda stavade källsträngar i Mactrack, samtliga med översättningarna ”IP-adresser” respektive ”MAC-adresser”. De två återanvändningskontroller som skapades av ändringen avfärdades efter kontextjämförelse; Weblates översikt visade därefter inga aktiva kontrollrader. Ändringarna i Intropage visas som väntande i Weblate, så synkronisering till källförrådet är fortfarande inte verifierad.

- Intropage: katalogens sista avsnitt granskades mot den aktuella Weblate-vyn. Sju ändringar förtydligar processoranvändning, pingtid och tröskelvärdeshändelser och rättar versaliseringen av dag. Weblate bekräftade sju uppdateringar utan överhoppade eller saknade; filen är `Cacti/cacti-intropage-sv-trosklar-20261026.po`. msgfmt och svlang passerade; l10n-lint noterade att ”Avg CPU” blev längre och hunspell-sv flaggade sammansättningen pingtid. Eventuell spridning av gemensamma strängar och synkronisering till källförrådet är inte verifierade.

- Uppföljning: `Threshold` visas som ”Tröskelvärde” i Intropage, Syslog, Thold och båda Core-versionerna, vilket passar sammanhangen. Weblates jämförelse för `%d Day` visade däremot att HMIB fortfarande hade ”%d Dag”; den ändrades direkt till ”%d dag” och Weblate visade den sparade formen. Övriga visade komponenter använde redan gemen form. Kopia: `Cacti/cacti-hmib-sv-dag-20261026.po`. msgfmt, l10n-lint, svlang och hunspell-sv passerade. Upstreamsynkronisering är inte verifierad.

- 2026-10-26: Syslog: aktuell bläddringsvy jämfördes med tidigare granskningar. Tio återstående språk- och terminologirättningar i `Cacti/cacti-syslog-sv-sprakgranskning-20261026.po` laddades upp; Weblate bekräftade tio uppdateringar utan saknade eller överhoppade poster. msgfmt och svlang passerade. l10n-lint noterade att en avslutande punkt saknas i källtexten; Hunspell flaggade produktnamn och exempeldomäner. Senaste release för plugin_syslog är v4.2 från 2024-03-17: https://github.com/Cacti/plugin_syslog/releases/tag/v4.2. Vidare synkronisering till källförrådet är inte verifierad.

### Mactrack, fortsatt radgranskning 26 oktober 2026

Weblates 38 bläddringssidor jämfördes med källtexterna och tidigare ändringar. Filen `Cacti/cacti-mactrack-sv-radgranskning-20261026.po` innehåller 18 rättningar av bland annat SNMP, enhetsspårning, kopplingar och portar. Weblate bekräftade 18 uppdaterade, inga överhoppade eller saknade. msgfmt, l10n-lint och svlang passerade; hunspell-sv flaggade tekniska namn och sammansättningen trunkportar. Senaste release v4.8 publicerades 2024-10-16: https://github.com/Cacti/plugin_mactrack/releases/tag/v4.8. Synkronisering från Weblate till källförrådet är inte verifierad. Ytterligare språkfel i äldre importhjälptexter och granskning av delade strängar återstår.

- Mactrack: tio äldre importhjälptexter för SNMP rättades i `Cacti/cacti-mactrack-sv-importhjalp-20261026.po`. Weblate bekräftade tio uppdaterade strängar, utan överhoppade eller saknade. msgfmt, l10n-lint och svlang passerade; hunspell-sv flaggade tekniska SNMP-termer. Kontrollen för oförändrat `ObjectID:` avfärdades som teknisk identifierare, och återanvändningskontrollen för `View Devices` mot `Show Units` avfärdades efter kontextjämförelse. Sökning efter aktiva kontroller gav därefter inga träffar. Synkronisering till källförrådet är inte verifierad.

### Routerconfigs, 26 oktober 2026

Weblates 304 strängar jämfördes med källtexten och tidigare arkiverat arbete. Filen `Cacti/cacti-routerconfigs-sv-granskning-20261026.po` innehåller 53 rättningar, varav 24 enhetliga klockslag; den felaktiga engelska etiketten `10:00 (12am)` återges som `10:00`. Övriga ändringar förtydligar bland annat inloggningsprompter, behörighet, säkerhetskopiering och tidsgränser. Weblate bekräftade 53 uppdaterade, inga saknade eller överhoppade. msgfmt, l10n-lint och svlang passerade; l10n-lints informationsnoteringar om klockslag och citattecken granskades, hunspell-sv flaggade SCP och TFTP-katalog. Två återanvändningskontroller för likvärdiga bekräftelseprompter avfärdades; därefter gav sökning efter aktiva kontroller inga träffar. Senaste release v1.7 publicerades 2026-02-03: https://github.com/Cacti/plugin_routerconfigs/releases/tag/v1.7. Överföring till källförrådet är inte verifierad.

### WebSeer, 26 oktober 2026

Weblates nio bläddringssidor granskades mot källorna och tidigare säkerhetskopior. Filen `Cacti/cacti-webseer-sv-granskning-20261026.po` innehåller 22 ändrade poster, inklusive pluralformer för duplicering och borttagning samt rättningar av aviseringar och tidsgränser. Weblate bekräftade 22 uppdaterade utan saknade eller överhoppade. msgfmt, l10n-lint och svlang passerade; hunspell-sv flaggade produktnamnet WebSeer. Två återanvändningskontroller för likvärdiga serveretiketter avfärdades; `Time Out` har en kvarvarande jämförelse med `Run Limit` som behöver kontext. `Master` är översatt med ”Säkerhetsansvarig” och behöver korrigeras efter kontroll av delade förekomster. Senaste release v3.2 publicerades 2023-02-05: https://github.com/Cacti/plugin_webseer/releases/tag/v3.2. Synkronisering från Weblate till källförrådet är inte verifierad.

- WebSeers `Master` avser en ja/nej-kolumn för serverns huvudroll enligt `webseer_servers.php`. Den tidigare felaktiga ”Säkerhetsansvarig” ersattes med ”Huvudserver”; även tre tillhörande etiketter och förklaringar rättades. Weblate bekräftade fyra uppdaterade, inga överhoppade eller saknade. `Cacti/cacti-webseer-sv-huvudserver-20261026.po` passerade msgfmt och svlang; l10n-lint noterade punkt som saknas i källans sista mening och hunspell-sv markerade egennamnets genitiv. Tre kontroller för återanvändning respektive punkt avfärdades efter jämförelse. Projektövergripande sökning visade även Git-grennamnet master, som är oförändrat. Weblates `Time Out`-kontroll mot `Run Limit` återstår att kontextgranska. Upstreamsynkronisering är inte verifierad.

- WebSeers återanvändningskontroll för `Time Out` avfärdades efter att Core-källans `automation_networks.php` visade att `Run Limit` avser en gräns i sekunder för upptäcktsprocessens körtid. Weblate-sökning visade inga återstående aktiva kontroller.

### Servcheck, 26 oktober 2026

Weblates 27 bläddringssidor jämfördes med källtexten och tidigare arkiverade rättningar. Fjorton poster med bland annat libcurl-fel, larm, certifikatkontroll och tekniska sökvägsexempel rättades i `Cacti/cacti-servcheck-sv-granskning-20261026.po`. Weblate bekräftade 14 uppdaterade, inga saknade eller överhoppade. msgfmt, l10n-lint och svlang passerade; hunspell-sv flaggade tekniska identifierare och sammansättningar. Senaste release v0.3 publicerades 2026-01-03: https://github.com/Cacti/plugin_servcheck/releases/tag/v0.3. Det återstår ytterligare språkliga förbättringar i katalogen och kontroll av delade strängar. Synkronisering till källförrådet är inte verifierad.

- Servcheck: ytterligare 15 rättningar i `Cacti/cacti-servcheck-sv-texter-20261026.po` gäller FTP-fel, formulärkodning, överföringsmetoder och felsträngar. Weblate bekräftade 15 uppdaterade utan överhoppade eller saknade. msgfmt och svlang passerade; l10n-lints enda varning gäller att produktnamnet libcurl börjar med gemen, och hunspell-sv flaggade tekniska termer. Delade strängars eventuella spridning och vidare synkronisering till källförrådet är inte fullständigt verifierade.

### NPC, 26 oktober 2026

Weblates 55 strängar granskades mot källtexterna och tidigare säkerhetskopior. Filen `Cacti/cacti-npc-sv-granskning-20261026.po` innehåller 13 rättningar av bland annat fördröjning, loggning och värdmappning. Weblate bekräftade 13 uppdaterade strängar, utan överhoppade eller saknade. msgfmt, l10n-lint och svlang passerade; hunspell-sv flaggade tekniska namn och sammansättningar. Projektets GitHub-förråd saknar publicerade releaser, så releaseåldern kunde inte fastställas. Synkronisering till källförrådet och eventuell spridning till andra komponenter är inte verifierade.

- Cycle: Vid ny genomgång av alla 60 aktiva strängar upptäcktes att fliknamnet `Cycle` fortfarande var översatt som ”Cykel”. Källkoden i `setup.php` visar att det är fliken för grafväxling. Det ändrades till ”Grafväxling” i `Cacti/cacti-cycle-sv-flik-20261026.po`; Weblate bekräftade en uppdatering, inga överhoppade eller saknade. msgfmt godkände filen med varningar om ofullständiga metadata i deltafilen, l10n-lint och svlang passerade och hunspell-sv flaggade sammansättningen grafväxling. Två kontroller för återanvänd översättning visas efter ändringen och behöver kontextgranskas. Senaste publicerade release v4.1 är från 2018-04-01, äldre än 48 månader. Synkronisering till källförrådet är inte verifierad.

- Uppföljning av Cycle: källkoden i `setup.php` visar att `Cycle` är fliknamnet och `Cycling` navigeringstiteln för samma vy. Båda återges därför som ”Grafväxling”. Weblates två kontroller om återanvänd översättning avfärdades efter jämförelsen, och en ny sökning efter aktiva kontroller gav inga träffar. Översättningen väntade fortfarande på arkivering i Weblates källförråd vid kontrollen.

- Aktuell uppföljning: Weblate-sökningen `has:check` i Maint gav inga träffar; de tidigare noterade kontrollerna visas alltså inte längre som aktiva. Projektövergripande målspråkssökningar efter `poller` respektive `polling` gav inga träffar vid kontrolltillfället. Detta verifierar sökresultaten, men inte att alla insamlingsrelaterade formuleringar i samtliga komponenter är konsekventa.

- Projektövergripande sökning efter källordet `collector`: nio resultatsidor jämfördes med terminologilistan. I Syslog ändrades `Remote Data Collector Rules Sync` från ”Synkronisering av regler för fjärrdatainsamling” till ”Synkronisering av regler för fjärrdatainsamlare”, i linje med närliggande inställningar. Weblate bekräftade en uppdaterad sträng utan bortfall; deltafil: `Cacti/cacti-syslog-sv-insamlarregler-20261026.po`. msgfmt godkände filen med varningar om saknade metadata, och l10n-lint, svlang och hunspell-sv passerade. Sökningen täcker träffar på collector, inte alla synonymer eller hela komponenterna. Syslogs senaste release v4.2 är från 2024-03-17; synkronisering till källförrådet är inte verifierad.

- Syslog: hjälptexten för pipelinelarm använder nu ”pipelinens status” i stället för ”hälsan” och ”insamlingsprocess” där `poller` avser en körning. Även aviseringslista följer etablerad terminologi. Weblate bekräftade en uppdatering utan saknade eller överhoppade poster. Fil: `Cacti/cacti-syslog-sv-pipelinestatus-20261026.po`. msgfmt, l10n-lint och svlang passerade; hunspell-sv markerade egennamnets genitiv ”Cactis”. Syslogs senaste release v4.2 publicerades 2024-03-17; synkronisering till källförrådet är inte verifierad. Den projektövergripande sökningen efter `poller` har påbörjats men inte granskats fullständigt.

- Thold: två kvarvarande engelska sammansättningar i aktuella Weblate-strängar rättades till ”insamlingscykler” och ”aviseringsprocessen”. Hjälptexten skiljer mellan direktavisering och avisering utanför den ordinarie processen. Weblate bekräftade två uppdaterade strängar, inga överhoppade eller saknade. Fil: `Cacti/cacti-thold-sv-insamling-20261026.po`. msgfmt, l10n-lint och svlang passerade; hunspell-sv markerade produktnamnet Thold. Senaste release v1.8.2 publicerades 2024-10-16. Synkronisering till källförrådet är inte verifierad. Den projektövergripande poller-granskningen återstår.

- Projektövergripande granskning av `source:poller`: samtliga tolv Weblate-resultatsidor jämfördes med översättningarna. Nod- och programreferenser använder i huvudsak insamlare eller datainsamlare; körningar och cykler använder insamlingskörning respektive insamlingscykel. De två felaktiga Thold-texterna på sidan 2 rättades enligt posten ovan. Samma källsträng visas ofta i båda Core-versionerna. Granskningen omfattar just denna sökning och innebär inte att alla närbesläktade termer eller hela Core har språkgranskats.

- Thold: `%d Polling Interval` och `%d Polling Intervals` översattes båda till `%d insamlingsintervall`, eftersom svenskans obestämda singular och plural har samma form. Weblate bekräftade två uppdateringar utan bortfall. Deltafil: `Cacti/cacti-thold-sv-intervall-20261026.po`. msgfmt, l10n-lint, svlang och hunspell-sv passerade. Senaste release v1.8.2 är från 2024-10-16. Överföring till källförrådet är inte verifierad. Sökningen efter `polling` är påbörjad men resterande resultatsidor återstår.

- Uppföljning av `source:polling`: Weblates fem resultatsidor jämfördes med terminologilistan och källtexterna. ”Insamling” och ”insamlingsintervall” används för den återkommande datainsamlingen; ”avfrågning” förekommer även där en värds eller databasens förfrågningar beskrivs. De två Thold-ändringarna ovan skapade varsin återanvändningskontroll för singular respektive plural. Båda avfärdades eftersom ”intervall” har samma form; en ny sökning gav inga aktiva Thold-kontroller. Kontrollen omfattar sökträffarna och innebär inte en fullständig språkgranskning av alla komponenter. Weblate visade intervalländringen som väntande i sitt arkiv.

- Core: projektets åtta Weblate-resultatsidor för `source:aggregate` jämfördes med terminologin. Tio etiketter där källkodens `aggregate_graphs.php` visar att åtgärderna gäller aggregerade grafer ändrades från ”aggregat” till ”aggregerad graf”, bland annat menyval för att skapa, koppla och namnge grafer. Weblate bekräftade 10 uppdaterade, inga överhoppade eller saknade. `Cacti/cacti-core-aggregate-terminology-20261026.po` passerade msgfmt, l10n-lint och Hunspell; svlang flaggade den sammanslagna listan med menyetiketter som en lång mening, vilket inte är en löptext. Gitleaks hittade inga hemligheter i deltafilen. Den delade strängen `Migrate Aggregate to use a Template` verifierades fortplantad till Core 1.2; övriga strängars fortplantning och synkronisering till källförrådet har inte verifierats. Andra kontextberoende förekomster av ”aggregat” återstår att bedöma.

- Uppföljning: aktuell Core 1.2-export innehöll nio av de tio föregående Core-ändringarna; den tionde källsträngen, `Aggregate Name`, saknades där. Core-källan visar att förhandsvisningen gäller en graf. Två texter om `Aggregate Preview` ändrades därför till ”förhandsvisning av den aggregerade grafen”. Weblate bekräftade två uppdateringar utan bortfall. `Cacti/cacti-core-aggregate-preview-20261026.po` passerade msgfmt, l10n-lint och Hunspell; Gitleaks hittade inga hemligheter. Fortplantning och synkronisering till källförråd återstår att verifiera.
- Viktigt vid jämförelser: Core-exporten via Weblates filmeny innehöll äldre översättningar för de tio senast uppladdade posterna trots att gränssnittet visade de nya. Använd aktuell enhetsvy eller databasexport för att verifiera väntande ändringar; anta inte att nedladdad PO innehåller dem innan arkivet har synkroniserats.

- Ytterligare sju Core-texter om migrering, kombination och färgmallar använder nu ”aggregerad graf” i stället för ”aggregat”, efter kontroll av åtgärderna i `aggregate_graphs.php` och `color_templates.php`. Weblate bekräftade sju uppdaterade och inga saknade eller överhoppade. `Cacti/cacti-core-aggregate-migration-20261026.po` passerade msgfmt och l10n-lint; Hunspell markerade sammansättningarna grafmallen och mallbaserad. Svlangs frekvens- och ordföljdsvarningar granskades som heuristiska träffar på tekniska termer och dessa meningar. Gitleaks hittade inga hemligheter. Fortplantning till Core 1.2 och synkronisering till källförråd är inte verifierad.

- Servcheck: en aktuell konverterad CSV-export från Weblates databas jämfördes med tidigare rättningar. Tjugo protokoll- och statusetiketter har förtydligats, bland annat ”krypterad/okrypterad HTTP”, ”SNMP-OID” och ”proxyautentisering”. Weblate bekräftade 20 uppdaterade, inga saknade eller överhoppade. `Cacti/cacti-servcheck-sv-protocol-review-20261026.po` passerade msgfmt och l10n-lint. Hunspell markerade protokollnamn och sammansättningar; svlang behandlade de fristående etiketterna som en enda lång mening. Gitleaks hittade inga hemligheter. Synkronisering till källförrådet och spridning till delade strängar är inte verifierad.

- Servcheck: resten av databaskatalogen granskades mot källtexterna. Rättningarna omfattar REST-API, protokoll, inställningar och hjälptexter. Den första uppladdningen uppdaterade 31 av 38 strängar; sju pluralposter hoppades över eftersom båda pluralformerna inte hade ändrats korrekt i filen. Dessa rättades och en andra uppladdning uppdaterade alla sju. `Cacti/cacti-servcheck-sv-complete-review-20261026.po` samlar de 38 ändringarna med korrekta pluralformer. msgfmt och l10n-lint kördes; l10n-lints två informationsmeddelanden gäller avsiktlig skillnad mellan singular och plural. Hunspell markerade tekniska namn; Gitleaks hittade inga hemligheter i den första filen. Upstreamsynkronisering är inte verifierad.

- 2026-10-26: Mactrack: tre ytterligare rättningar av undertyp, databasresultat och högsta användarportnummer skickades upp. Weblate bekräftade tre uppdateringar utan bortfall. Fil: `Cacti/cacti-mactrack-sv-portnummer-20261026.po`. msgfmt och l10n-lint passerade; hunspell-sv markerade den tekniska identifieraren lowPort. Synkronisering till källförrådet är inte verifierad.

- 2026-10-26: Mactrack: sju språk- och SNMP-rättningar skickades upp i `Cacti/cacti-mactrack-sv-snmp-sprak-20261026.po`. Weblate bekräftade sju uppdaterade, inga överhoppade eller saknade. Återanvändningskontrollen för Priv Proto avfärdades efter jämförelse med Priv Protocol i båda Core-versionerna: samma krypteringsprotokoll avses. msgfmt och l10n-lint passerade; svlang flaggade en falsk V2-varning mellan separata etiketter och hunspell-sv markerade SNMP-termer. Ändringarna visas som väntande i Weblate.

- 2026-10-26: Mactrack: fyra rättningar av portnamn, VLAN-ID, behörighet och databasresultat skickades upp i `Cacti/cacti-mactrack-sv-portnamn-20261026.po`. Weblate bekräftade fyra uppdateringar utan bortfall. Två återanvändningskontroller avfärdades eftersom Port Name och Portname avser samma begrepp. msgfmt och l10n-lint passerade; svlang markerade rubrikformulering och hunspell-sv den tekniska termen VLAN-ID. Synkronisering till källförrådet är inte verifierad.

- 2026-10-26: Mactracks DNS-intervall beskrivs nu som koppling mellan skannade IP- och MAC-adresser, efter kontroll av `poller_mactrack.php`. Även 802.1X-etikett och MacWatch-hjälptext rättades. Filen `Cacti/cacti-mactrack-sv-dns-dot1x-20261026.po` skickades upp; Weblate bekräftade tre uppdateringar utan bortfall. msgfmt och l10n-lint passerade; svlang markerade fråge- och huvudsats som V2-varningar och hunspell-sv markerade tekniska namn och platshållare. Synkronisering till källförrådet är inte verifierad.

- 2026-10-26: Aktuell databasexport från Core 1.2 bekräftar tre av sju nyligen uppladdade migrerings- och färgmallstexter med exakt samma källtext och översättning; fyra hade ingen exakt källtextsträff. En separat Core 1.2-variant om migrering rättades till ”mallbaserade aggregerade grafer” i `Cacti/cacti-core12-aggregate-migration-20261026.po`; Weblate bekräftade en uppdaterad sträng utan bortfall. msgfmt gav metadata-varningar men godkände filen, l10n-lint och Hunspell passerade; svlang gav heuristiska ordföljdsvarningar. Core-kontrollen för Priv Protocol avfärdades efter jämförelse med likvärdiga Priv Proto i Mactrack; Core 1.2 hade redan avfärdat samma kontroll. Synkronisering till källförrådet är inte verifierad.

- 2026-10-26: Fyra etiketter i Core 1.2 ändrades till ”aggregerad graf” efter kontroll av sammanhanget i aggregate_graphs.php, color_templates.php, data_sources.php och global_settings.php. Weblate bekräftade fyra uppdateringar utan bortfall. Fil: `Cacti/cacti-core12-aggregate-labels-20261026.po`. msgfmt godkände med metadatavarningar, l10n-lint och Hunspell passerade och svlang markerade tekniska ord som ovanliga. Spridning till Core och synkronisering till källförrådet är inte verifierade.

- Uppföljning 2026-10-26: Aktuell Core-databasexport bekräftar att tre av de fyra Core 1.2-etiketterna om aggregerade grafer har fortplantats med identisk källtext och översättning. `Aggregate Name:` saknas som exakt källtext i Core. Exporten visar inte att ändringarna har synkroniserats till källförrådet.

- 2026-10-26: Två texter om färgmallssynkronisering förtydligades efter granskning av `sync_color_templates` i color_templates.php: de hänvisar nu till aggregerade grafer och grafmallar. Weblate bekräftade två uppdateringar utan bortfall. Fil: `Cacti/cacti-core-color-sync-20261026.po`. msgfmt och l10n-lint passerade; Hunspell markerade grafmallar och svlang gav heuristiska ordföljdsvarningar. Gitleaks hittade inga hemligheter. Fortplantning till Core 1.2 och synkronisering till källförrådet är inte verifierade.

- 2026-10-26: Flowview: aktuell CSV-export med 715 strängar granskades mot källtext och arkiverade ändringar. Tretton rättningar skickades i `Cacti/cacti-flowview-sv-radgranskning-20261026.po`; Weblate bekräftade 13 uppdaterade utan bortfall. SQL-frågan för senaste uppdateringstid och källgränssnittet för AS-filtret kontrollerades i koden. Två återanvändningsvarningar för Treemap och Treemap Chart avfärdades efter sammanhangskontroll; översikten visar 715 översatta strängar och inga aktiva kontrollvarningar. msgfmt, svlang och Gitleaks passerade. l10n-lint noterade kolon i källan och att siffran 5 skrivits ut med bokstäver; hunspell-sv markerade CIDR och peeringuppsättning. GitHub listar v4.9 från 2025-03-23 som nyast daterade release, medan v4.8 har markeringen Latest. Synkronisering från Weblate till källförrådet har inte verifierats.

- 2026-10-26: Intropages aktuella export med 542 strängar jämfördes med källtexterna och tidigare inskickade ändringar. Tretton språk- och sakrättningar skickades i `Cacti/cacti-intropage-sv-slutgranskning-20261026.po`; Weblate bekräftade 13 uppdaterade, inga överhoppade eller saknade. Tre slutpunktsvarningar avfärdades eftersom de svenska fullständiga meningarna korrekt har punkt. Weblate visade därefter 542 översatta strängar utan aktiva kontrollvarningar. msgfmt, svlang och Gitleaks passerade; l10n-lint rapporterade samma tre slutpunktsavvikelser och Hunspell flaggade produktnamn och sammansättningar. Senaste GitHub-release v4.0.4 är från 2024-04-26; synkronisering från Weblate till källförrådet är inte verifierad.

- 2026-10-26: Syslogs aktuella CSV-export jämfördes med tidigare inskickade rättningar. Nio ändringar av bland annat uppdateringsintervall, underhållstider och delning skickades i `Cacti/cacti-syslog-sv-uppfoljning-20261026.po`. Weblate bekräftade nio uppdaterade utan bortfall. Den tidigare kontrollen för slutpunkt i domänlistans hjälptext avfärdades efter granskning; därefter visade Weblate 850 översatta strängar och inga aktiva varningar. msgfmt, l10n-lint, svlang och Gitleaks passerade; Hunspell markerade produktnamn, en sammansättning och en teknisk identifierare. Senaste release v4.2 publicerades 2024-03-17. Synkronisering till källförrådet är inte verifierad.

- 2026-10-26: Core: statusmeddelandet om att inställningar inte sparas på grund av heartbeat kontrollerades mot `lib/functions.php`. Där jämförs tiden sedan senaste status med två insamlingsintervall. Weblates aktuella översättning säger redan att datainsamlaren inte rapporterat sin status i tid; den äldre CSV-exportens formulering om ”hjärtslag” är inaktuell och ska inte återimporteras. Den aktiva återanvändningskontrollen för `Fail` jämfördes med `FAILED` och koden i `host.php`, där det är ett misslyckat resultat. ”Misslyckades” är korrekt; kontrollen avfärdades. Denna kontroll innebär inte att hela Core är radgranskat.

- 2026-10-26: Monitors aktuella CSV-export med 311 strängar granskades mot källtexterna. Tolv rättningar skickades i `Cacti/cacti-monitor-sv-granskning-20261026.po`; Weblate bekräftade 12 uppdaterade utan bortfall och visar inga aktiva kontrollvarningar. msgfmt, l10n-lint, svlang och Gitleaks passerade; Hunspell markerade HTML, produktnamn och tekniska sammansättningar. GitHub anger v2.9 från 2026-07-09 som senaste release. En text med ett dynamiskt infogat engelskt verb behöver en källkodsåtgärd. Synkronisering från Weblate till källförrådet har inte verifierats.

- 2026-10-26: Core och Core 1.2: två varningar om datainsamlarens uteblivna statusrapport förtydligades efter granskning av heartbeat-villkoret i båda versionernas `poller.php`. `Cacti/cacti-core12-statusrapport-20261026.po` skickades till Core 1.2; Weblate bekräftade två uppdateringar utan bortfall och visade båda ändringarna fortplantade till Core. Den tidigare ändrade texten om utebliven sparning var också redan fortplantad; en äldre CSV-export var inaktuell. msgfmt godkände filen med metadatavarningar; l10n-lint, svlang, hunspell-sv och Gitleaks passerade. GitHub anger Cacti v1.2.31 från 2026-06-15 som senaste release. Weblate visar ändringarna som väntande; synkronisering till källförrådet är inte verifierad. Core 1.2 visade två aktiva kontroller på andra strängar efter uppladdningen.

- 2026-10-26: Core 1.2:s återanvändningskontroller för `MaxValue` och `MinValue` jämfördes med `Maximum` och `Minimum` samt tabellkolumnerna i `lib/spikekill.php`. ”Maxvärde” respektive ”Minvärde” är lämpliga i dessa sammanhang; de två kontrollerna avfärdades. Weblate visade därefter 4 776 översatta strängar utan aktiva kontrollvarningar. Ingen översättning ändrades, och detta verifierar inte en fullständig radgranskning av Core.

- 2026-10-26: Core: två texter för tvåfaktorsautentisering rättades från QA-kod till QR-kod. Källans `tfa_qr_code` och beskrivningen om skanning bekräftar att QA är en felskrivning. Weblate bekräftade två uppdaterade strängar utan bortfall; fil: `Cacti/cacti-core-sv-qrkod-20261026.po`. msgfmt, l10n-lint, svlang och Gitleaks passerade; hunspell-sv markerade appnamn och förkortningar. Senaste Cacti-release v1.2.31 är från 2026-06-15. Spridning till Core 1.2 och synkronisering till källförrådet är inte verifierade. Genomgången av aktuell Core-export fortsätter; hela katalogen är inte färdiggranskad.

- 2026-10-26: Core: två pinghjälptexter förtydligades efter granskning av `automation_networks.php` och `include/global_form.php`: värdens SNMP-tidsgräns gäller för SNMP-ping och återförsök sker efter ett misslyckat första försök. Weblate bekräftade två uppdateringar utan bortfall. Fil: `Cacti/cacti-core-sv-ping-20261026.po`. msgfmt, l10n-lint, svlang och Gitleaks passerade; hunspell-sv markerade protokoll och tekniska sammansättningar. Core 1.2 och synkronisering till källförrådet är inte verifierade. Radgranskning av hela Core återstår.

- 2026-10-26: Core: hjälptexten för mönster för enhetsbeskrivningar förtydligades med bibehållna variabler, funktionsnamn och SQL-exempel. Weblate bekräftade en uppdatering utan bortfall. Fil: `Cacti/cacti-core-sv-enhetsbeskrivning-20261026.po`. msgfmt, l10n-lint, svlang och Gitleaks passerade; hunspell-sv markerade tekniska namn. Aktuell CSV-export från Core 1.2 bekräftar att båda pinghjälptexterna har fortplantats med identisk källtext och översättning. De två QR-kodstexterna och enhetsbeskrivningen saknar exakt källtext i Core 1.2-exporten. Synkronisering till källförrådet är inte verifierad; radgranskning av hela Core återstår.

- 2026-10-26: Core: det ofullständiga felsökningsmeddelandet `No Initial found!` förtydligades efter kontroll av grenen för lyckad första RRD-jämförelse i `data_debug.php`. Weblate bekräftade en uppdatering utan bortfall. Fil: `Cacti/cacti-core-sv-initialkontroll-20261026.po`. msgfmt, l10n-lint, svlang och Gitleaks passerade; hunspell-sv markerade RRD-filen. Fortplantning till Core 1.2 och synkronisering till källförrådet är inte verifierade. Radgranskning av hela Core återstår.

- 2026-10-26: Core: `Aggregates` ändrades till ”Aggregerade grafer” efter kontroll av länken till aggregate_graphs.php och menyn. En varning om förlorade anpassade data och avbruten datainsamling förtydligades. Weblate bekräftade två uppdateringar utan bortfall; fil: `Cacti/cacti-core-sv-datakallor-20261026.po`. msgfmt, l10n-lint, svlang, hunspell-sv och Gitleaks passerade. Fortplantning till Core 1.2 och synkronisering till källförrådet är inte verifierade; hela Core återstår att radgranska.

- 2026-10-26: Core: grafmallens kompatibilitetstext ändrades från ”100 %% kompatibel” till ”helt kompatibel”. `graphs.php` anropar `__()` utan formatargument, och `global_languages.php` returnerar då strängen direkt. Ett ensamt procenttecken underkändes av msgfmt på grund av källans php-formatflagga; den valda formuleringen passerar kontrollen och behåller betydelsen. Weblate bekräftade en uppdatering. Fil: `Cacti/cacti-core-sv-procent-20261026.po`. msgfmt, svlang, hunspell-sv och Gitleaks passerade; l10n-lint noterade att siffran 100 uttrycks med ord. Core 1.2 och upstreamsynkronisering är inte verifierade; hela Core återstår att radgranska.

- 2026-10-26: Core: nio språk- och terminologirättningar i enhetsvyn och datafrågor skickades i `Cacti/cacti-core-sv-enhetsvy-20261026.po`. Weblate bekräftade nio uppdaterade utan bortfall och inga aktiva kontrollvarningar. msgfmt, svlang och Gitleaks passerade; hunspell-sv markerade sammansättningen pingresultaten. l10n-lint noterade att källans kolon utelämnats vid omformulering. Fortplantning till Core 1.2 och synkronisering till källförrådet är inte verifierade; hela Core återstår att radgranska.

- 2026-10-26: Fortsatt preliminär jämförelse av Core-exporten `cacti-core-sv (6).csv`, rader med index 1650–2099 (nollbaserat), mot källtexten. Ingen översättning ändrades. Exporten kan vara inaktuell och genomgången behöver därför följas upp mot aktuell Weblate-status. Kontrollera särskilt konsekvent bruk av ”aggregationsnivå” och ”aggregeringsnivå” samt hjälptexten om hur länge data kan saknas innan värdet anges som okänt. Hela Core är inte färdiggranskad.

- 2026-10-26: Core: två hjälptexter om formatering av vänster och höger axel förtydligades efter jämförelse med aktuell Weblate-vy. Weblate bekräftade två uppdateringar och inga saknade strängar. Fil: `Cacti/cacti-core-sv-axelformat-20261026.po`. msgfmt och Gitleaks passerade. l10n-lint och svlang markerade kommatecken efter inskjutna bestämningar; hunspell-sv markerade formatnamn och kommandon. Upstreamsynkronisering är inte verifierad; hela Core återstår att granska.

- 2026-10-26: Core: tre hjälptexter för grafobjekt använder nu ”graf” enligt den gemensamma terminologin och en inställning för flera grafer per enhet uttrycker att de kan förekomma. Aktuella käll- och måltexter kontrollerades i Weblate före uppladdning; fyra uppdateringar och inga saknade rapporterades. Fil: `Cacti/cacti-core-sv-grafmallar-20261026.po`. msgfmt, l10n-lint, svlang, hunspell-sv och Gitleaks passerade. Upstreamsynkronisering är inte verifierad; fullständig radgranskning återstår.

- 2026-10-26: Core: hjälptexten om tiden innan data registreras som okända rättades efter jämförelse med aktuell Weblate-text. Weblate bekräftade en uppdatering utan bortfall. Fil: `Cacti/cacti-core-sv-okanda-data-20261026.po`. msgfmt, l10n-lint, svlang och Gitleaks passerade; hunspell-sv markerade HTML-entiteten quot. Upstreamsynkronisering och fullständig Core-granskning återstår.

- 2026-10-26: Core: ”Device Defaults” förtydligades till ”Standardinställningar för enheter” efter kontroll av aktuell Weblate-text. Weblate bekräftade en uppdatering utan bortfall. Fil: `Cacti/cacti-core-sv-enhetsstandard-20261026.po`. msgfmt, l10n-lint, svlang, hunspell-sv och Gitleaks passerade. Preliminär jämförelse av exportens poster 2230–2429 genomfördes; aktuell Weblate-status har inte kontrollerats för alla. Fullständig radgranskning och upstreamsynkronisering återstår.

- 2026-10-26: Core: inställningsbeskrivningarna för lokal sidhjälp och fjärrdatainsamlarnas TCP-port förbättrades efter kontroll av aktuella Weblate-texter. Weblate rapporterade två uppdateringar utan bortfall. Fil: `Cacti/cacti-core-sv-installningar-20261026.po`. msgfmt, l10n-lint, svlang och Gitleaks passerade; hunspell-sv markerade namn och sammansättningar med sidhjälp. Preliminär jämförelse av exportens poster 2430–2534 genomfördes; hela Core och upstreamsynkronisering återstår att verifiera.

- 2026-10-26: Core: två beskrivningar av SNMPv3:s autentiseringsprotokoll och autentiseringsanvändare rättades från auktorisering till autentisering, i enlighet med fältens etiketter. Weblate rapporterade två uppdateringar och inga saknade strängar. Fil: `Cacti/cacti-core-sv-snmp-autentisering-20261026.po`. msgfmt, l10n-lint, svlang och Gitleaks passerade; hunspell-sv markerade SNMPv3-sammansättningen. Preliminär genomgång av exportposter 2535–2659 genomfördes. Hela Core och upstreamsynkronisering är inte verifierade.

- 2026-10-26: Core: gästkontots hjälptext anger nu ”Ingen användare kopplad”, vilket matchar den aktuella etiketten för No User i Weblate. Uppladdningen gav en uppdatering utan bortfall. Fil: `Cacti/cacti-core-sv-gastkonto-20261026.po`. msgfmt, l10n-lint, svlang, hunspell-sv och Gitleaks passerade. Exportposter 2660–2759 jämfördes preliminärt; fullständig Core-granskning och upstreamsynkronisering återstår.

- 2026-10-26: Core: loggvarningen använder samma svenska nivånamn som den motsvarande varningen och proxytexten använder ”insticksmoduler”. De aktuella strängarna jämfördes i Weblate; uppladdningen gav två uppdateringar utan bortfall. Fil: `Cacti/cacti-core-sv-logg-proxy-20261026.po`. msgfmt, l10n-lint, svlang och Gitleaks passerade; hunspell-sv markerade Cactis. Exportposter 2760–2859 jämfördes preliminärt. Hela Core och upstreamsynkronisering är inte verifierade.

- 2026-10-26: Core: hjälptexten för säkerhetskopieringskatalogen förtydligades efter kontroll av inställningen och backupRRDFile i lib/spikekill.php. Formuleringen talar om angiven katalog, inte om katalogens innehåll. Weblate rapporterade en uppdatering utan bortfall. Fil: `Cacti/cacti-core-sv-rrd-sakerhetskopia-20261026.po`. msgfmt, l10n-lint, svlang och Gitleaks passerade; hunspell-sv markerade RRD-filerna. Exportposter 2860–2959 jämfördes preliminärt. Hela Core och upstreamsynkronisering återstår.

- 2026-10-26: Core: fjärrdatainsamlarens statusmeddelande använder svensk benämning på RRD-uppdatering på begäran och tydligare text om anslutningslägen. Aktuell text jämfördes i Weblate; uppladdningen gav en uppdatering utan bortfall. Fil: `Cacti/cacti-core-sv-fjarrstatus-20261026.po`. msgfmt och Gitleaks passerade. l10n-lint och svlang markerade kommatecken och källans kolon efter NOTE; hunspell-sv markerade tekniska namn. Exportposter 2960–3069 jämfördes preliminärt. Hela Core och upstreamsynkronisering återstår att verifiera.

- 2026-10-26: Core: uppladdningsfelet förtydligades till PHP-tilläggsmodul efter kontroll av felkod 8 i data_source_profiles.php och lib/api_automation.php. Weblate rapporterade en uppdatering utan bortfall. Fil: `Cacti/cacti-core-sv-uppladdningsfel-20261026.po`. msgfmt, l10n-lint, svlang, hunspell-sv och Gitleaks passerade. Exportposter 3070–3179 jämfördes preliminärt. Fullständig Core-granskning och upstreamsynkronisering återstår.

- 2026-10-26: Fortsatt preliminär jämförelse av Core-exportens poster 3180–3389 mot källtexterna. Inga ändringar gjordes. För ”Tested Bulk Walk Size ... response” bekräftar lib/data_query.php att värdet är förfluten tid (sluttid minus starttid), så ”svarstiden” behölls. Exporten kan vara inaktuell; genomgången innebär inte att samtliga aktuella Weblate-texter eller hela Core är färdiggranskade.

- 2026-10-26: De gamla Core-exportposterna 3390–3519 jämfördes med en ny PO-export från Weblate. Av 130 poster fanns 127 med samma källtext och kontext i den aktuella exporten; de övriga tre saknades. De 127 jämfördes med källtexten utan nya ändringar. Källkoden i `settings.php` och `lib/functions.php` kontrollerar hur lång tid som gått sedan datainsamlarens senaste status innan inställningar hoppas över, vilket stöder den befintliga översättningen av hjärtslagsmeddelandet. Detta är en avgränsad genomgång, inte en fullständig granskning av Core eller bevis för upstreamsynkronisering.

- 2026-10-26: Fortsatt jämförelse av gamla Core-poster 3520–3619 med aktuell Weblate-export. I Spike Kill avser ”Float Range” en åtgärd på värden i ett tidsintervall, inte datatypen flyttal: `lib/spikekill.php` visar att värden i intervallet ersätts. Tre förslag finns i [utkastet](../cacti-core-sv-samlat-utkast-20261026.po), där även simuleringsåtgärderna förtydligas. Utkastet är inte uppladdat; samla fortsatta ändringar i komponentfilen och kontrollera aktuell Weblate-text igen före uppladdning. msgfmt godkände filen med två varningar om ärvda metadata, l10n-lint och svlangs skrivregler rapporterade inga problem, Hunspell markerade sammansättningen ”luckfyllning” och Gitleaks fann inga hemligheter.

- 2026-10-26: Gamla Core-poster 3620–3889 jämfördes med aktuell export där posterna fortfarande finns. Elva bekräftelsetexter för rapportåtgärder använder nu samma svenska citattecken som övriga gränssnittet i det samlade utkastet. Utkastet har 14 ändringar och är inte uppladdat. msgfmt godkände filen med de två tidigare metadataförbehållen och l10n-lint rapporterade inga problem.

- 2026-10-26: Gamla Core-poster 3890–4039 jämfördes med den aktuella exporten där posterna finns. Sju installationstexter med ”fjärrinsamlare” har anpassats till ”fjärransluten datainsamlare” i det samlade utkastet, som nu innehåller 21 ändringar. HTML och variabler har bevarats. msgfmt godkände filen med två tidigare metadataförbehåll; svlangs skrivregler och Gitleaks fann inga problem. l10n-lint gav en skiljeteckenvarning för ett kolon i källan som inte behövs i den svenska meningen. Hunspell markerade tekniska namn, sökvägar och ”luckfyllning”. Utkastet är inte uppladdat.

- 2026-10-26: Gamla Core-poster 4040–4189 jämfördes med aktuell export där posterna finns. Ytterligare en text har anpassats till ”fjärransluten datainsamlare”. Ett löst avslutande citattecken togs bort i översättningen av ett automatiseringsmeddelande; det motsvarande källmeddelandet i `lib/installer.php` har samma lösa tecken. Formatvariablerna är oförändrade. Det samlade utkastet har 23 ändringar, är kontrollerat med msgfmt, l10n-lint, svlang, Hunspell och Gitleaks och är inte uppladdat. Kända metadata- och skiljeteckenvarningar kvarstår; l10n-lint noterar också den avsiktliga skillnaden mot källans sista citattecken.

- 2026-10-26: Gamla Core-poster 4190–4339 jämfördes med aktuell export där posterna finns. Tre meddelanden om hämtning av insticksmoduler översattes och ytterligare en hänvisning till fjärranslutna datainsamlare anpassades. Det samlade utkastet har 27 ändringar. msgfmt, l10n-lint, svlangs skrivregler, Hunspell och Gitleaks kördes; tidigare metadata- och skiljeteckenförbehåll kvarstår och Hunspell markerade tekniska namn, variabler och ”luckfyllning”. Utkastet är inte uppladdat.

- 2026-10-26: Gamla Core-poster 4340–4499 jämfördes med aktuell export där posterna finns. SNMP-aviseringarnas åtgärder använder nu konsekvent ”aviseringsmottagare” och ”aviseringsobjekt”; en knapptext för inaktivering av vidarebefordran har förtydligats efter kontroll av `managers.php`. En ytterligare text om fjärransluten datainsamlare har justerats. Utkastet innehåller 44 ändringar. msgfmt, l10n-lint, svlangs skrivregler, Hunspell och Gitleaks kördes med tidigare kända metadata- och skiljeteckenförbehåll; inga hemligheter hittades. Ingen uppladdning har gjorts.

- 2026-10-26: Gamla Core-poster 4500–4649 jämfördes med aktuell export där posterna finns. Fjorton texter för insticksmodulhantering har rättats, inklusive varningar om att avinstallation kan ta bort data och återställning kan skriva över en katalog. Begreppet ”insticksmodul” och knapptexten ”Ta bort” används konsekvent i de ändrade texterna. Utkastet innehåller 58 ändringar. msgfmt, l10n-lint, svlangs skrivregler, Hunspell och Gitleaks kördes; tidigare metadata- och skiljeteckenförbehåll kvarstår. Ingen uppladdning har gjorts.

- 2026-10-26: Gamla Core-poster 4650–4799 jämfördes med aktuell export där posterna finns. Nio texter för datainsamlare justerades med gemensamma termer för fjärranslutna datainsamlare och frånkopplad drift samt enhetliga citattecken. Det samlade utkastet innehåller 67 ändringar. msgfmt, l10n-lint, svlangs skrivregler, Hunspell och Gitleaks kördes; tidigare metadata- och skiljeteckenförbehåll kvarstår. Utkastet är inte uppladdat.

- 2026-10-26: Gamla Core-poster 4800–5049 jämfördes med aktuell export där posterna finns. Femton ändringar har lagts till i det samlade utkastet: adressfältet ”State” översätts till ”Delstat/region”, kartans zoomfält till ”Zoomnivå”, datainsamlartermer har anpassats och citattecken i bekräftelsetexter har gjorts enhetliga. Källplatserna i exporten kontrollerades för de korta etiketterna. Utkastet innehåller 82 ändringar och är inte uppladdat. msgfmt, l10n-lint, svlangs skrivregler, Hunspell och Gitleaks kördes; tidigare metadata- och skiljeteckenförbehåll kvarstår och Hunspell markerade bland annat tekniska namn och sammansättningar. Genomgången gäller denna del av exporten, inte hela komponenten.

- 2026-10-26: Gamla Core-poster 5050–5399 jämfördes med aktuell export där de finns. 25 texter för mallimport, träd, användare och grupper har fått enhetliga svenska citattecken i det samlade utkastet, som nu omfattar 107 ändringar. I LDAP-hjälptexten finns en ofullständig HTML-entitet även i källtexten; den har inte ändrats utan vidare kontroll. msgfmt, l10n-lint, svlangs skrivregler, Hunspell och Gitleaks kördes; tidigare metadata- och skiljeteckenförbehåll kvarstår. Utkastet är inte uppladdat och Core är inte färdiggranskat.

- 2026-10-26: Gamla Core-poster 5400–5704 jämfördes med den aktuella exporten där posterna finns. Texten om resurscachen har anpassats till datainsamlarterminologin och fyra VDEF-bekräftelser har fått enhetliga citattecken. Alla aktiva poster i den aktuella exporten har en motsvarande aktiv källtext och kontext i den äldre exporten. De tidigare posterna 0–3389 har dock bara granskats preliminärt och behöver färdiggranskas innan uppladdning. Utkastet omfattar 112 ändringar och är inte uppladdat. msgfmt, l10n-lint, svlangs skrivregler, Hunspell och Gitleaks kördes med tidigare kända metadata- och skiljeteckenförbehåll.

- 2026-10-26: Fördjupad granskning av gamla Core-poster 0–299 mot den aktuella exporten. Texten om automatiseringsgränssnittet för enheter har förtydligats och fjorton bekräftelsetexter har fått svenska citattecken. Utkastet innehåller 127 ändringar. msgfmt, l10n-lint, svlangs skrivregler, Hunspell och Gitleaks kördes; tidigare metadata- och skiljeteckenförbehåll kvarstår. Övriga tidigare preliminärt granskade poster och uppladdning återstår.

- 2026-10-26: Fördjupad granskning av gamla Core-poster 300–499 mot den aktuella exporten. Arton ändringar omfattar konsekventa citattecken, ”Ta bort nätverk” och en tydligare beskrivning av simulerad körning. Det samlade utkastet har 145 ändringar. msgfmt, l10n-lint, svlangs skrivregler, Hunspell och Gitleaks kördes; tidigare metadata- och skiljeteckenförbehåll kvarstår. Övriga preliminära poster och uppladdning återstår.

- 2026-10-26: Fördjupad granskning av gamla Core-poster 500–699 mot aktuell export. 28 ändringar gör bland annat bekräftelsernas citattecken enhetliga och anpassar termerna för kopplade grafregler och borttagning. Utkastet har 173 ändringar. msgfmt, l10n-lint, svlangs skrivregler, Hunspell och Gitleaks kördes; tidigare metadata- och skiljeteckenförbehåll kvarstår. Återstående preliminära poster och uppladdning återstår.

- 2026-10-26: Fördjupad granskning av gamla Core-poster 700–899 mot aktuell export. Femton ändringar gör citattecken och formatering enhetliga i färgmallar och datainmatning. Källkoden i data_debug.php granskades för det otydliga meddelandet ”No Initial found”; befintlig översättning behölls eftersom grenen anger att inga initiala RRD-matchningsproblem hittades. Utkastet har 188 ändringar. msgfmt, l10n-lint, svlangs skrivregler, Hunspell och Gitleaks kördes; tidigare metadata- och skiljeteckenförbehåll kvarstår. Återstående preliminära poster och uppladdning återstår.

- 2026-10-26: Fördjupad granskning av gamla Core-poster 900–1099 mot aktuell export. 23 ändringar förenhetligar bland annat kopplade mallar, borttagning och bekräftelser. Pluralformerna för borttagning av grafobjekt och grafer kontrollerades mot data_sources.php; valet styrs av antalet datakällor och de befintliga formerna behölls. Utkastet har 211 ändringar. msgfmt, l10n-lint, svlangs skrivregler, Hunspell och Gitleaks kördes; tidigare metadata- och skiljeteckenförbehåll kvarstår. Återstående preliminära poster och uppladdning återstår.

- 2026-10-26: Fördjupad granskning av gamla Core-poster 1100–1299 mot aktuell export. 22 ändringar omfattar enhetlig terminologi och citattecken samt tre pluralformer där antal grafer eller benämningen ”graf” tidigare avvek från källtexten. Utkastet har 233 ändringar. msgfmt, l10n-lint, svlangs skrivregler, Hunspell och Gitleaks kördes; tidigare metadata- och skiljeteckenförbehåll kvarstår. Återstående preliminära poster och uppladdning återstår.

- 2026-10-26: Fördjupad granskning av gamla Core-poster 1300–1499 mot aktuell export. Femton ändringar förenhetligar termer för kopplade grafmallar och citattecken i enhetsåtgärder. Utkastet har 248 ändringar. msgfmt, l10n-lint, svlangs skrivregler, Hunspell och Gitleaks kördes; tidigare metadata- och skiljeteckenförbehåll kvarstår. Återstående preliminära poster och uppladdning återstår.

- 2026-10-26: Fördjupad granskning av gamla Core-poster 1500–1699 mot aktuell export. Fem meddelanden om fjärranslutna datainsamlare och resurscache anpassades till gemensam terminologi. Utkastet har 253 ändringar. msgfmt, l10n-lint, svlangs skrivregler, Hunspell och Gitleaks kördes; tidigare metadata- och skiljeteckenförbehåll kvarstår. Återstående preliminära poster och uppladdning återstår.

- 2026-10-26: Fördjupad granskning av gamla Core-poster 1700–1899 mot aktuell export. ”Aggregate” har ändrats till ”Aggregerad graf” efter kontroll av båda användningarna i include/global_arrays.php, och Linux CPU-statistik har fått en tydligare formulering. Utkastet har 255 ändringar. msgfmt, l10n-lint, svlangs skrivregler, Hunspell och Gitleaks kördes; tidigare metadata- och skiljeteckenförbehåll kvarstår. Återstående preliminära poster och uppladdning återstår.

- 2026-10-26: Fördjupad granskning av gamla Core-poster 1900–2099 mot aktuell export. Två etiketter justerades för placeringsval och SNMP-aviseringsmottagare. Utkastet har 257 ändringar. msgfmt, l10n-lint, svlangs skrivregler, Hunspell och Gitleaks kördes; tidigare metadata- och skiljeteckenförbehåll kvarstår. Återstående preliminära poster och uppladdning återstår.

- 2026-10-26: Fördjupad granskning av gamla Core-poster 2100–2299 mot aktuell export. Tre texter om datakällans gränsvärde och grafens axel och gradient har förtydligats. Utkastet har 260 ändringar. msgfmt, l10n-lint, svlangs skrivregler, Hunspell och Gitleaks kördes; tidigare metadata- och skiljeteckenförbehåll kvarstår. Återstående preliminära poster och uppladdning återstår.

- 2026-10-26: Fördjupad granskning av gamla Core-poster 2300–2499 mot aktuell export. Tre etiketter och hjälptexter anpassades till termerna datainsamlare, kopplad graf och SNMP-aviseringsmottagare. Utkastet har 263 ändringar. msgfmt, l10n-lint, svlangs skrivregler, Hunspell och Gitleaks kördes; tidigare metadata- och skiljeteckenförbehåll kvarstår. Återstående preliminära poster och uppladdning återstår.

- 2026-10-26: Fördjupad granskning av gamla Core-poster 2500–2699 mot aktuell export. Fem texter skiljer nu mellan plats och placering och använder gemensamma termer för datainsamlare. Inställningens sammanhang kontrollerades i include/global_settings.php. Utkastet har 268 ändringar. msgfmt, l10n-lint, svlangs skrivregler, Hunspell och Gitleaks kördes; tidigare metadata- och skiljeteckenförbehåll kvarstår. Återstående preliminära poster och uppladdning återstår.

- 2026-10-26: Fördjupad granskning av gamla Core-poster 2700–2899 mot aktuell export. Fem texter anpassades för konsekvent terminologi om grafer, teckensnitt och fjärranslutna datainsamlare. Utkastet har 273 ändringar. msgfmt, l10n-lint, svlangs skrivregler, Hunspell och Gitleaks kördes; tidigare metadata- och skiljeteckenförbehåll kvarstår. Återstående preliminära poster och uppladdning återstår.

- 2026-10-26: Fördjupad granskning av gamla Core-poster 2900–3099 mot aktuell export. Texten om RRD-uppdatering på begäran anpassades till termen fjärranslutna datainsamlare. Utkastet har 274 ändringar. msgfmt, l10n-lint, svlangs skrivregler, Hunspell och Gitleaks kördes; tidigare metadata- och skiljeteckenförbehåll kvarstår. Återstående preliminära poster och uppladdning återstår.

- 2026-10-26: Fördjupad granskning av gamla Core-poster 3100–3389 mot aktuell export. Sex ändringar förtydligar fjärranslutna datainsamlare och samordnar terminologin. Det samlade utkastet innehåller 280 ändrade strängar. Samtliga jämfördes med den aktuella exporten utan konflikter. msgfmt, l10n-lint, svlangs skrivregler, Hunspell och Gitleaks kördes; kvarvarande lintervarningar gäller bland annat källans kolon och skiljetecken. Weblate bekräftade uppladdningen: 280 uppdaterade, inga överhoppade eller saknade. Därefter visades 80 varningar om återanvänd översättning som återstår att granska.

- 2026-10-26: Pluralformen för ”The following Data Source is in use by this Graph” rättades från ”denna graf” till ”dessa grafer” enligt den engelska pluralformen. Weblate bekräftade en uppdaterad sträng. De tre pluralposterna i den föregående uppladdningen kontrollerades mot respektive källform; 78 varningar om återanvänd översättning återstår.

- 2026-10-26: Varningen för ”Remove the following Discovered Devices” i Core jämfördes med Core 1.2:s ”Delete the following Discovered device(s)”. ”Ta bort följande upptäckta enheter” passar båda och kontrollen avfärdades. De fyra listningssidorna för återanvändning genomlästes; individuella jämförelser med andra förekomster återstår. I källkoden managers.php används vidarebefordran av aviseringsobjekt till samma mottagare i singular- och pluralgrenarna, vilket stöder den befintliga svenska formuleringen trots den ofullständiga engelska pluraltexten.

- 2026-10-26: Sju återanvändningskontroller i Core avfärdades efter individuell jämförelse: en för borttagning av grafregler samt sex för borttagning och inaktivering av nätverk i singular och plural. Svenska ”nätverk” har samma obestämda form i båda numerusen och formuleringarna motsvarar även Core 1.2. Weblate visar nu 70 strängar med aktiva återanvändningskontroller.

- 2026-10-26: Tolv återanvändningskontroller avfärdades efter jämförelse av källtexterna: aktivering, upptäckt, export och duplicering av nätverk samt borttagning och duplicering av SNMP-alternativ, i singular och plural. Både ”nätverk” och ”alternativ” har samma obestämda form i båda numerusen. Motsvarande Core 1.2- och MacTrack-texter kontrollerades där Weblate visade dem. Weblate visar 58 återanvändningskontroller kvar.

- 2026-10-26: Sex återanvändningskontroller i Core avfärdades efter jämförelse: två för export av SNMP-alternativ, två för borttagning av CDEF-objekt och två för datakällor som används av grafer. CDEF-texterna avser samma borttagningsåtgärd enligt `cdef.php`; datakällornas singular och plural stämmer med källorna. Weblates översikt visar 52 aktiva återanvändningskontroller. Core 1.2:s GPRINT-text med `Preset(s)` behöver ytterligare granskning eftersom den svenska texten bara använder plural.

- 2026-10-26: Core: kontrollen för `New Poller` jämfördes med `New Data Collector`. Båda anger namn på en datainsamlare enligt `install/functions.php` respektive `pollers.php`; ”Ny datainsamlare” följer ordlistan och kontrollen avfärdades. Weblate visar 51 aktiva återanvändningskontroller. I Core 1.2 visar `host.php` och `gprint_presets.php` att texterna med `(s)` används före listor som kan innehålla en eller flera poster; formuleringarna för borttagning, aktivering och inaktivering behöver därför fortsatt numerusgranskning. Ingen översättning ändrades.

- 2026-10-26: Core 1.2: fyra texter för borttagning av GPRINT-förinställningar samt aktivering, inaktivering och borttagning av enheter omformulerades så att samma text fungerar för en eller flera valda poster. Weblate bekräftade fyra uppdateringar utan bortfall. Filen `Cacti/cacti-core-1-2-sv-urval-20261026.po` passerade msgfmt, l10n-lint, svlang och Gitleaks; hunspell-sv markerade GPRINT-förinställningar som teknisk sammansättning. Weblate visade därefter 12 strängar med aktiva kontroller i Core 1.2. Synkronisering till källförrådet är inte verifierad.

- 2026-10-26: Core 1.2: sex återanvändningskontroller avfärdades efter jämförelse med Core och terminologilistan: fyra för aktivering, inaktivering, borttagning och upptäckt av nätverk, en för borttagning av SNMP-alternativ samt en för ”Ny datainsamlare”. Nätverk och alternativ har samma form i singular och plural. Weblate visar sex aktiva kontroller kvar i Core 1.2; övriga jämförelser omfattar bland annat rapporter och VDEF med `(s)` och behöver numerusgranskning.

- 2026-10-26: Core 1.2: fyra bekräftelser för upptäckta enheter och rapporter omformulerades för urval med en eller flera poster. Weblate bekräftade fyra uppdateringar utan bortfall; `Cacti/cacti-core-1-2-sv-rapporturval-20261026.po` passerade msgfmt, l10n-lint, svlang, hunspell-sv och Gitleaks. Två kontroller för grafregler och VDEF avfärdades efter jämförelse av källtexternas pluralformer. Därefter visade Weblate 4 776 översatta strängar och inga aktiva kontrollrader. Det innebär inte att hela komponenten är radgranskad; synkronisering till källförrådet är inte verifierad.

- 2026-10-26: Core: efter ändringarna i Core 1.2 visade Weblate 44 återanvändningskontroller. Sex kontroller avfärdades efter jämförelse: aktivering och inaktivering av enheter i Core och Mactrack samt singular- och pluralvarianter av borttagning av aviseringsmottagare. ”Mottagare” har samma form i singular och plural. Översikten visar därefter 38 återanvändningskontroller kvar.

- 2026-10-26: Core: åtta återanvändningskontroller för aktivering och inaktivering av aviseringsmottagare avfärdades efter jämförelse av singular- och pluraltexterna. Svenskans ”mottagare” har samma form i båda fallen. Weblate visar 30 återanvändningskontroller kvar.

- 2026-10-26: Core: åtta återanvändningskontroller avfärdades efter jämförelse: fyra för vidarebefordran av ett eller flera aviseringsobjekt till en mottagare, två för visning av insticksmodulens ändringslogg och två för borttagning av en eller flera datainsamlare. Källkoden i `managers.php` och `plugins.php` kontrollerades; ”objekt” och ”datainsamlare” har samma form i singular och plural. Weblate visar 22 återanvändningskontroller kvar.

- 2026-10-26: Core: nio återanvändningskontroller avfärdades efter jämförelse av singular- och pluraltexter: sex för aktivering, inaktivering och rensning av statistik för datainsamlare samt tre för borttagning och publicering av träd. ”Datainsamlare” och ”träd” har samma obestämda form i båda numerusen. Core-varningen som jämför platser med Mactracks `Site(s)` lämnades för fortsatt granskning av numerus. Weblate visar 13 återanvändningskontroller kvar.

- 2026-10-26: Core: tolv återanvändningskontroller avfärdades efter jämförelse: fem för publicering, avpublicering och upplåsning av träd, sex för borttagning, aktivering och inaktivering av användare samt en för borttagning av VDEF:er. Träd och användare har samma obestämda form i singular och plural; VDEF-texterna står båda i plural. Weblate visar en återanvändningskontroll kvar, för platser i Core och Mactrack.

- 2026-10-26: Mactracks bekräftelse för borttagning av platser omformulerades för ett urval med en eller flera platser efter kontroll av listan i `mactrack_sites.php`. Weblate bekräftade en uppdatering utan bortfall; filen `Cacti/cacti-mactrack-sv-platsurval-20261026.po` passerade msgfmt, svlang, hunspell-sv och Gitleaks. l10n-lint noterade att det engelska frågetecknet ersatts med punkt eftersom svenskan är en uppmaning. Core-översikten visade därefter 5 198 översatta strängar och inga aktiva kontrollrader. Detta verifierar inte fullständig radgranskning eller synkronisering till källförrådet.

- 2026-10-26: Fortsatt genomgång av den äldre Core-exportens poster 3390–3489: loggtexter för indexering, SNMP-frågor och felsökning jämfördes med källtexterna. Platshållarna och tekniska identifierare i de genomlästa posterna noterades; särskilt ”Transient Index Removal” (3390) behöver kontextkontroll eftersom den svenska texten kan beskriva ett tillfälligt index i stället för en tillfällig borttagning. Exporten är en äldre ögonblicksbild, så aktiva Weblate-värden måste kontrolleras innan någon ändring skickas. Ingen översättning ändrades i denna delgranskning.

- 2026-10-26: Uppföljning av `Transient Index Removal Detected`: `lib/data_query.php` testar `index_transient` innan meddelandet skrivs och lämnar den borttagna indexposten utan åtgärd. Den aktuella Weblate-texten ”Borttagning av ett tillfälligt index upptäckt” är därmed förenlig med sammanhanget; samma text finns i Core och Core 1.2. Ingen ändring behövs.

- 2026-10-26: Den äldre Core-exportens poster 3490–3589 granskades med särskild kontroll av graftexter. Weblate-sökningen `source:spikes` gav fem aktuella träffar, som alla använder ”toppar” eller ”ta bort toppar” på ett konsekvent sätt. Sökningen `source:outliers` gav ingen träff; den äldre exportens `Variance Outliers` kan därför inte behandlas som en aktuell översättning. Även `Time Graph View` förekommer i källkoden men dess aktuella Weblate-post är ännu inte säkert identifierad. Ingen översättning ändrades; hela komponenten återstår att granska rad för rad.

- 2026-10-26: Core: källkoden `include/global_settings.php` använder `%d Spikes` för både 1 och högre värden. Översättningen ändrades därför från ”%d toppar” till ”Antal toppar: %d”. Weblate bekräftade en uppdaterad sträng utan överhoppade eller saknade strängar. Filen `Cacti/cacti-core-antal-toppar-20261026.po` passerade msgfmt, svlang, hunspell-sv och Gitleaks; l10n-lint rapporterade endast en informationsnotis om ändrad början på strängen. Granskningen av den äldre exportens poster 3590–3689 är påbörjad; aktuell Weblate-text måste jämföras före fler ändringar. Synkronisering till källförrådet är inte verifierad.

- 2026-10-26: Den äldre exportens poster 3690–3789 genomlästes. Källkoden skiljer `%d Column` för värdet 1 från `%d Columns` för högre värden, så singularformen i den äldre exporten är rimlig. Sökningar i aktuell Core efter `source:injection` och `source:mailtime` gav inga träffar; äldre säkerhets- och rapporttexter ska därför inte skickas upp utan ny kontroll. `Float Range` och `Dry Run Float Range` är redan rättade i Weblate till ”Ersätt värden i intervall” respektive ”Simulera ersättning av värden i intervall”; källkoden anropar samma åtgärd med respektive utan simulering. Ingen översättning ändrades i denna genomgång.

- 2026-10-26: En ny fullständig Core-export hämtades från Weblate och sparades lokalt som `work/cacti-core-weblate-fresh-20261026.po`. Den innehåller 5 705 PO-poster, varav 177 är markerade föråldrade; Weblate visar 5 198 aktiva strängar. Exporten bekräftar ”Antal toppar: %d”. En jämförelse med den äldre exporten visar många ändrade måltexter, så fortsatt granskning ska utgå från den nya filen och kontrollera aktuella poster i Weblate före uppladdning. Poster 3789–3888 har lästs översiktligt; exempelvis `Graph Filters` behöver kontroll mot aktuellt användningssammanhang innan ändring. Ingen översättning ändrades i detta steg.

- 2026-10-26: `Graph Filters` följdes upp med Weblates exakta källsträngssökning. Den ger ingen träff i Core men en aktiv träff i Core 1.2, där översättningen redan är ”Graffilter”. Källkoden i Core 1.2 `lib/html_tree.php` placerar texten ovanför grafvyns filter; termen är därmed lämplig. Posten ”Grafiska filter” i Core-exporten är inte en aktiv Weblate-träff och ska inte skickas upp. Inga översättningar ändrades.

- 2026-10-26: Genomgång av den aktuella exportens poster 3989–4088 gav en aktiv terminologiavvikelse: `Configuration of Poller` ändrades från ”Konfiguration av insamlare” till ”Konfiguration av datainsamlare” enligt den gemensamma ordlistan. Weblate bekräftade en uppdaterad sträng, utan överhoppade eller saknade strängar. Ändringsfilen `Cacti/cacti-core-konfiguration-datainsamlare-20261026.po` passerade msgfmt, l10n-lint, svlang, hunspell-sv och Gitleaks. Några andra texter i exporten kan vara inaktiva och behöver kontrolleras mot Weblate innan de ändras; synkronisering till källförrådet är inte verifierad.

- 2026-10-26: I genomgången av exportens poster 4089–4199 kontrollerades `Repopulating poller cache` i Weblate och ändrades till ”Fyller datainsamlarens cache på nytt” enligt ordlistan. Weblate bekräftade en uppdatering utan bortfall. `Cacti/cacti-core-datainsamlare-cache-20261026.po` klarade msgfmt, l10n-lint, svlang, hunspell-sv och Gitleaks. Den språkligt felaktiga äldre posten `No tables where found or selected for conversion` gav ingen exakt träff i aktuell Core och skickades inte upp. Synkronisering till källförrådet är inte verifierad.

- 2026-10-26: I exportens poster 4200–4299 granskades meddelandet om en datafil som inte kan öppnas. Den aktiva översättningen ändrades till ”Kunde inte öppna datafilen. Datainsamlaren kanske inte har körts ännu” för att följa ordlistan. Weblate bekräftade en uppdaterad sträng utan bortfall. Ändringsfilen `Cacti/cacti-core-datafil-datainsamlare-20261026.po` klarade msgfmt, l10n-lint, svlang, hunspell-sv och Gitleaks. En misstänkt äldre sträng om utgåvor gav ingen exakt träff i aktuella Core och ändrades inte. Synkronisering till källförrådet är inte verifierad.

- 2026-10-26: Weblate-exporten `Cacti/cacti-core-sv-weblate-20261026-baslinje.po` arkiverades som granskningsunderlag, inte som färdig radgranskning. Gitleaks rapporterade inga fynd. `msgfmt --check` rapporterar två PHP-formatfel i exporten: InnoDB-beskrivningen med 25/80 procent och rådet om 80 procent MySQL/MariaDB-minne. Båda källtexterna har `php-format` trots att källkodens `__()` anropas utan formateringsargument; funktionen returnerar då översättningen direkt. Källornas procenttecken och formatflaggor behöver därför ses över innan en katalogkontroll kan passera utan att riskera felaktig visning. Ingen ändring laddades upp för dessa poster.

- 2026-10-26: I exportens poster 4410–4509 rättades två aktiva åtgärdstexter för aviseringsobjekt. `managers.php` visar att åtgärden aktiverar eller inaktiverar vidarebefordran, inte objekten själva. Weblate bekräftade två uppdateringar utan bortfall. Ändringsfilen `Cacti/cacti-core-vidarebefordran-20261026.po` klarade msgfmt, l10n-lint, svlang, hunspell-sv och Gitleaks. Svenska ”objekt” har samma form i singular och plural; Weblate kan därför rapportera återanvänd översättning. Synkronisering till källförrådet är inte verifierad.

- 2026-10-26: Efter de två rättelserna för vidarebefordran granskades fyra återanvändningsvarningar individuellt. Källorna är singular- och pluralvarianter av samma aktiverings- respektive inaktiveringsåtgärd och svenska ”objekt” har samma obestämda form i båda numerusen. Varningarna avfärdades; Core-översikten visar därefter inga aktiva kontrollrader. I exportens poster 4510–4609 upptäcktes också en felaktig äldre text för `Automatically Trust Signer`, men exakt sökning gav ingen aktiv träff i vare sig Core eller Core 1.2. Ingen översättning av den posten skickades upp.

2026-10-26: Fem varningar om datainsamlare i core granskades mot aktuell källkod och skickades upp till Weblate. Uppladdningen bekräftade fem uppdaterade strängar. Ändringarna finns i `cacti-core-datainsamlare-20261026.po`.

2026-10-26: Fyra aktiva texter i cores tekniksupport anpassades till termen datainsamlare. Weblate bekräftade fyra uppdateringar; ändringarna finns i `cacti-core-support-datainsamlare-20261026.po`.

2026-10-26: Rubriken ”Poller Information” i core ändrades till ”Information om datainsamlaren” efter kontroll av support.php. Weblate bekräftade uppdateringen; ändringen finns i `cacti-core-datainsamlare-information-20261026.po`.

2026-10-26: Sex cache- och ombyggnadstexter i core anpassades till termen datainsamlare. Weblate bekräftade sex uppdateringar; ändringarna finns i `cacti-core-cache-datainsamlare-20261026.po`.

2026-10-26: Fyra texter om cacheadministration och minnesanvändning i core anpassades till termen datainsamlare. Weblate bekräftade fyra uppdateringar; ändringarna finns i `cacti-core-cache-administration-20261026.po`.

2026-10-26: Åtta diagnostik- och cachetexter i core anpassades till termen datainsamlare. Weblate bekräftade åtta uppdateringar; ändringarna finns i `cacti-core-diagnostik-datainsamlare-20261026.po`.

2026-10-26: Sex inställnings- och statustexter i core anpassades till termen datainsamlare. Weblate bekräftade sex uppdateringar; ändringarna finns i `cacti-core-installningar-datainsamlare-20261026.po`.

2026-10-26: Sex inställnings- och cachetexter i core anpassades till termen datainsamlare. Två andra sökträffar var redan uppdaterade och lämnades oförändrade. Weblate bekräftade sex uppdateringar; ändringarna finns i `cacti-core-installningar-cache-20261026.po`.

2026-10-26: Fem hjälp- och feltexter i core anpassades till termen datainsamlare. Weblate bekräftade fem uppdateringar; ändringarna finns i `cacti-core-diagnostik-installningar-20261026.po`.

2026-10-26: Fem DNS-, resurscache- och Boost-texter i core anpassades till termen datainsamlare. Weblate bekräftade fem uppdateringar; ändringarna finns i `cacti-core-dns-resurscache-20261026.po`. L10n-lint markerade två befintliga skillnader i slutskiljetecken; svensk punkt respektive frågetecken behölls eftersom formuleringarna är hela meningar och den sista är en fråga.

2026-10-26: Fyra hjälptexter om säkerhet, minne och varningar i core anpassades till termen datainsamlare. Weblate bekräftade fyra uppdateringar; ändringarna finns i `cacti-core-sakerhet-minne-20261026.po`.

2026-10-26: Tre texter om Spine och Boost i core granskades och anpassades till termen datainsamlare respektive Boost-process. Weblate bekräftade tre uppdateringar; ändringarna finns i `cacti-core-spine-boost-20261026.po`. L10n-lint markerade en befintlig skillnad i slutskiljetecken: källtexten slutar med kommatecken, men översättningen är en fullständig mening och behåller punkt.

2026-10-26: Två varningar om RRD-filer och insamlingsintervall i core anpassades till termen datainsamlare och ett överflödigt kommatecken togs bort. Weblate bekräftade två uppdateringar; ändringarna finns i `cacti-core-rrd-intervall-20261026.po`. L10n-lint markerade att källans kolon efter NOTE saknas i översättningen, som använder svenskans ”OBS!”.

2026-10-26: Två hjälptexter om SNMP och synkronisering i core anpassades till termen datainsamlare. Weblate bekräftade två uppdateringar utan bortfall. Ändringsfilen `cacti-core-synk-snmp-20261026.po` klarade msgfmt, l10n-lint, svlang, hunspell-sv och Gitleaks.

2026-10-26: Den gemensamma rubriken ”Poller” i core ändrades till ”Datainsamlare” efter kontroll av användningsplatserna. Weblate bekräftade en uppdatering. Sju andra kandidater var redan uppdaterade. Ändringsfilen `cacti-core-poller-rubrik-20261026.po` klarade msgfmt, l10n-lint, svlang, hunspell-sv och Gitleaks.

2026-10-26: En ny Core-export jämfördes med den tidigare kandidaten på 732 poster efter ett uppladdningsförsök utan kvitto. 656 poster matchar kandidatens samtliga översättningsformer; 76 skiljer sig och inga saknas. Avvikelserna inkluderar senare terminologirättelser och får inte skrivas över utan ny bedömning. Detta visar aktuellt innehåll, men bevisar inte hur många poster som den tidigare uppladdningen ändrade. Underlag: `core-kontroll-20261026/core-aktuell.po` och `jamforelse.tsv`.
