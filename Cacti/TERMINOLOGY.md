# Gemensam svensk terminologi för Cacti

Datum: 2026-10-29

Den här ordlistan gäller Cacti Core, Core (v1.2.x) och insticksmodulerna.
Den bygger på granskade Cacti-deltan och används när samma engelska begrepp
återkommer i fler komponenter.

| Engelska | Svenskt val | Anmärkning |
| --- | --- | --- |
| Poller | datainsamlare | Cactis process/roll som hämtar mätvärden. Behåll `PollerID` när det är ett tekniskt fältnamn. |
| Data Collector | datainsamlare | Samma roll som `Poller` i Cacti 1.2+. Använd inte både *insamlare* och *datainsamlare* för samma UI-begrepp. |
| Collector | insamlare | Använd bara när det avser en separat mottagare, till exempel en FlowView-insamlare. |
| collect | samla in | Verbformen; *samlar in data*. |
| data source | datakälla | En namngiven Cacti-datakälla, inte *datakällan* utan bestämd form när sammanhanget kräver den. |
| graph | graf | Grundform i navigering och etiketter. |
| graph template | grafmall | Cactis mall för en graf. |
| aggregate graph | aggregerad graf | Ett enskilt diagram som är aggregerat. |
| aggregate template | mall för aggregerad graf | Sätt den beskrivande delen efter *mall för* för naturlig svenska. |
| graph aggregation | grafaggregation | Processen eller funktionen som sammanför grafer. Detta är tydligare än *aggregatgraf*. |
| aggregate (verb) | aggregera | Exempel: *aggregera grafer*. Skriv om till *sammanföra* om meningen blir mer lättläst. |
| aggregate (noun) | aggregat | Behåll bara när källtexten syftar på ett namngivet Cacti-objekt, exempelvis *äldre aggregat*. |
| threshold | tröskelvärde | Mätgräns som utlöser en åtgärd. För ett namngivet UI-fält kan kortformen *tröskel* användas. |
| alert | larm | Använd för en notifierad varning; *varning* är en lägre allvarlighetsnivå. |
| device | enhet | Cactis övervakade nätverksobjekt. Undvik *apparat*. |
| host | värd | Använd när källan avser värdnamn eller värdsystem; använd *enhet* när Cacti avser sitt Device-objekt. |
| hostname | värdnamn | Behåll engelska endast i oföränderliga fältnamn eller protokollvärden. |
| interface | gränssnitt | Nätverksgränssnitt i Cacti och MacTrack. |
| template | mall | Kort och konsekvent i alla komponenter. |
| cache | cache | Etablerad teknisk term; böj till *cachen* vid behov. |
| heartbeat | hjärtslag | I statusfrasen *hjärtslagsläge*. |

## Särskilda konsekvensregler

- Behåll produkt-, protokoll- och fältnamn som `Cacti`, `Spine`, `SNMP`,
  `PollerID`, `Graph Template` och `Data Collector` när de ingår i ett
  oföränderligt API-värde eller en teknisk identifierare.
- Översätt däremot användargränssnittets förklarande text runt sådana namn.
- Undvik `aggregatgraf`. Skriv *aggregerad graf* för objektet och
  *grafaggregation* för funktionen eller processen.
- Använd inte tre lika konsonanter i rad; välj vid behov en omskrivning eller
  ett bindestreck som följer svensk skrivregel.

## Belägg i arkivet

- `cacti-core-poller-overvakning-20261026.po` använder *datainsamlare* för
  `Poller`.
- `cacti-core12-datainsamlare-20261026.po` använder *datainsamlare* för
  `Data Collector`.
- `cacti-core-v12-aggregate-terminologi-20261026.po` använder *aggregerad
  graf* och *mall för aggregerad graf*.
- `cacti-core12-grafaggregation-20261026.po` dokumenterar *grafaggregation*.
