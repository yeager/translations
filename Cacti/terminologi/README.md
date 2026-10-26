# Gemensam svensk terminologi för Cacti

Arbetslista för alla Cacti-komponenter. Tillämpa orden efter sammanhang och ändra inte variabelnamn, protokollnamn eller etablerade produktnamn. En term kan behöva en annan böjning eller en förklarande formulering i en hel mening. Listan är påbörjad och hela komponentbeståndet är ännu inte kontrollerat mot den.

| Engelska | Svenska | Användning och avgränsning |
|---|---|---|
| device | enhet | Övervakad enhet. |
| host | värd | En dator eller annan värd; skilj från enhet om källtexten gör det. |
| data source | datakälla | |
| data collector | datainsamlare | En värd eller tjänst som samlar in data. |
| poller | datainsamlare, insamlingsprocess | Använd datainsamlare för en nod som tilldelas enheter, insamlingsprocess för den process som hämtar data. Cacti använder även remote poller om en fjärransluten datainsamlare. |
| polling | datainsamling, insamling | Välj efter sammanhang; insamlingsintervall för polling interval. |
| graph | graf | I Cactis övervakningsgränssnitt; diagram kan vara naturligare för andra visualiseringar. |
| aggregate graph | aggregerad graf | En graf som kombinerar flera grafer; grafaggregering beskriver processen. |
| graph template | grafmall | |
| aggregate template | aggregatmall | Mall för en aggregerad graf. |
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
