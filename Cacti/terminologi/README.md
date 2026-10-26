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
| poller cache | insamlarens cache | Ändra vid behov till insamlingsprocessens cache om det tekniska sammanhanget kräver åtskillnad. |
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
