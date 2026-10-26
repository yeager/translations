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
| network | nätverk | |
| tree | träd | För Cactis hierarkiska graf- eller enhetsträd. |
| data query | datafråga | |
| metric / measurand | mätstorhet | I Reportit avser båda en definierad mätstorhet; i andra komponenter kan metric syfta på ett mätvärde. |
| consolidation function | konsolideringsfunktion | Funktion som sammanfattar mätvärden. |
| step / stepping | steglängd | När värdet anger avståndet mellan numeriska val. |
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
