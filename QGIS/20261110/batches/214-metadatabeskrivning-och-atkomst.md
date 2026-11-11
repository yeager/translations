# QGIS: metadatabeskrivning och åtkomst 214

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen rättar terminologi och grammatik i metadataredigeraren. Standarder,
akronymer, URI och språkkoder behålls oförändrade.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Not set` | `Inte satt` | `Inte angivet` |
| `This page describes the basic attribution of the %1. Please use the tooltips for more information.` | `Denna sida beskriver %1 grundläggande egenskaper. Använd verktygstips för mer information.` | `Den här sidan beskriver den grundläggande upphovsangivelsen för %1. Använd verktygstipsen för mer information.` |
| `Set from %1` | `Hämta från %1` | `Ange utifrån %1` |
| `undefined %1` | `odefinierad %1` | `oangiven %1` |
| `CRS: %1` | `Koordinatsystem: %1` | `Koordinatreferenssystem: %1` |
| `Same as layer properties but different than the provider.` | `Samma som lageregenskaper men olikt datakällan.` | `Samma som lageregenskaperna men skiljer sig från dataleverantören.` |
| `Same as the provider but different than the layer properties.` | `Samma som datakällan men olikt lageregenskaperna.` | `Samma som dataleverantören men skiljer sig från lageregenskaperna.` |
| `Does not match either layer properties or the provider.` | `Inte samma som varken lageregenskaper eller datakälla.` | `Matchar varken lageregenskaperna eller dataleverantören.` |
| `CRS: Not set.` | `Koordinatreferenssystem: Inte satt.` | `Koordinatreferenssystem: Inte angivet.` |
| `Ok, it seems valid according to the QGIS Schema.` | `Ok, det verkar riktigt enligt QGIS schema.` | `Okej, det verkar vara giltigt enligt QGIS-schemat.` |
| `A reference, URI, URL or some other mechanism to identify the parent resource that this resource is a part (child) of.` | `En referens, URI, URL eller annan mekanism för att identifiera den överordnade resursen som  denna resurs är en del (barn) av.` | `En referens, URI, URL eller annan mekanism för att identifiera den överordnade resurs som den här resursen ingår i.` |
| `Returns the human readable name of the resource, typically displayed in search results.` | `Namn som resursen är känd under.` | `Resursens namn i läsbar form, som vanligtvis visas i sökresultat.` |
| `While a formal vocabulary is not imposed, it is advised to use the ISO 19115 MD_ScopeCode values. E.g. 'dataset' or 'series'. If unsure about which type to select, use 'dataset'.` | `Även om en formell formulering inte är tvingande är det rekommenderat att använda ISO 19115 MD_ScopeCode värdena. T.ex. 'dataset' eller 'series'. Vid osäkerhet om vilken typ som ska väljas använd 'dataset'.` | `Även om någon formell vokabulär inte krävs rekommenderas värdena i ISO 19115 MD_ScopeCode, till exempel 'dataset' eller 'series'. Om du är osäker på vilken typ du ska välja, använd 'dataset'.` |
| `Creation date` | `Skapat datum` | `Skapandedatum` |
| `Usually the returned string will follow either the ISO 639.2 or ISO 3166 specifications, e.g. 'ENG' or 'SPA', however this is not a hard requirement and the caller must account for non compliant values.` | `Vanligtvis en textsträng som följer antingen ISO 639.2 eller ISO 3166 specifikationerna, t.ex. 'ENG' or 'SWE'. Detta är dock inte ett absolut krav och användaren måste räkna med värden som inte följer detta.` | `Den returnerade strängen följer vanligtvis ISO 639-2 eller ISO 3166, till exempel 'ENG' eller 'SPA'. Detta är dock inte ett absolut krav och anroparen måste hantera värden som inte följer standarden.` |
| `Categories chosen will be added as a new entry in the keywords tab.` | `Valda ämnesområden kommer att läggas som en ny rad i nyckelordsfliken.` | `De valda ämnesområdena läggs till som en ny post på fliken Nyckelord.` |
| `Add selected ISO categories to metadata` | `Lägg till valt ISO-ämnesområde till metadata` | `Lägg till valda ISO-ämnesområden i metadata` |
| `Removes a specified vocabulary.` | `Tar bort ett viss begrepp.` | `Tar bort en angiven vokabulär.` |
| `A set of descriptive keywords associated with the resource for a specified concept.` | `En uppsättning beskrivande nyckelord kopplade till resursen för ett specificerat begrepp.` | `En uppsättning beskrivande nyckelord som kopplas till resursen för en angiven vokabulär.` |
| `The fees, licences and rights for this dataset.` | `De avgifter, licenser och rättigheter som gäller för detta dataset.` | `Avgifter, licenser och rättigheter för denna datamängd.` |
| `List of attribution or copyright strings associated with the resource` | `Lista över referenser eller copyright knutna till resursen` | `Lista över upphovsangivelser eller upphovsrättsmeddelanden som hör till resursen` |
| `Rights (attribution or copyright)` | `Rättigheter (referens eller copyright)` | `Rättigheter (upphovsangivelse eller upphovsrätt)` |
| `Add Right` | `Lägg till rättigheter` | `Lägg till rättighet` |

Den felaktigt serialiserade HTML-hjälptexten för nyckelord lämnas medvetet
orörd tills en separat deltafil kan validera exakt XML-markup. Ingen extern
ändring har gjorts.
