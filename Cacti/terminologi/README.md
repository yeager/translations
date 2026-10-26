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
