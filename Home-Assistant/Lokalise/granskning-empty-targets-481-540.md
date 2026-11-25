# Home Assistant Core: tidigare tomma svenska mål 481–540

- Granskade och sparade: **60/60**. Samtliga fullständiga nycklar och engelska källor kontrollerades mot live Lokalise; måltext skrevs via API och lästes tillbaka direkt. HA Core-revision: `86a2eabe7e43f526db5821ef068087ce8404ae07`.
- Batchen innehåller 18 språk-/dialektetiketter, 33 Azure-regionnamn och 9 Modbus/myUplink-strängar. Inga referensnycklar. Alla tre platshållare i felfraserna bevarades exakt.
- Microsofts officiella Azure Speech-lista och regionregister användes: [Azure Speech language labels](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support) and [official Azure region names](https://learn.microsoft.com/en-us/azure/reliability/regions-list). Regionvalen behåller officiella Azure-namn, eftersom de fungerar som produktnamn och motsvarar region-ID:n. Dialekter och skriftsystem har översatts.
- Home Assistant-minnet visar redan `Modbus hub` → `Modbus-hubb`; ny text följer den etablerade termen. `svlang` från aktuell verktygskällkod gav inga radfel; skrivregler och platshållare passerade. Hunspell-svensk ordlista har uppdaterats med relevanta språk-/ortnamn och `Modbus`; 19 tester passerar.
- TMX uppdaterad och validerad: **17 667 poster**. Manifest: `2026-11-25-reviewed-empty-targets-481-540.json`; TM-underlag: `2026-11-25-reviewed-empty-targets-481-540-tm.json`.

## Radgranskning

### `component::microsoft::selector::language::options::tr-tr`
**Källa:** Turkish (Türkiye)
**Svenska:** Turkiska (Türkiye)
**Motivering:** Azure Speech-språketikett översatt till svenska; dialekt, region och förenklad/traditionell skrift har behållits.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::uk-ua`
**Källa:** Ukrainian (Ukraine)
**Svenska:** Ukrainska (Ukraina)
**Motivering:** Azure Speech-språketikett översatt till svenska; dialekt, region och förenklad/traditionell skrift har behållits.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::ur-in`
**Källa:** Urdu (India)
**Svenska:** Urdu (Indien)
**Motivering:** Azure Speech-språketikett översatt till svenska; dialekt, region och förenklad/traditionell skrift har behållits.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::ur-pk`
**Källa:** Urdu (Pakistan)
**Svenska:** Urdu (Pakistan)
**Motivering:** Azure Speech-språketikett översatt till svenska; dialekt, region och förenklad/traditionell skrift har behållits.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::uz-uz`
**Källa:** Uzbek (Latin, Uzbekistan)
**Svenska:** Uzbekiska (latinsk skrift, Uzbekistan)
**Motivering:** Azure Speech-språketikett översatt till svenska; dialekt, region och förenklad/traditionell skrift har behållits.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::vi-vn`
**Källa:** Vietnamese (Vietnam)
**Svenska:** Vietnamesiska (Vietnam)
**Motivering:** Azure Speech-språketikett översatt till svenska; dialekt, region och förenklad/traditionell skrift har behållits.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::wuu-cn`
**Källa:** Chinese (Wu, Simplified)
**Svenska:** Kinesiska (wu, förenklad)
**Motivering:** Azure Speech-språketikett översatt till svenska; dialekt, region och förenklad/traditionell skrift har behållits.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::yue-cn`
**Källa:** Chinese (Cantonese, Simplified)
**Svenska:** Kinesiska (kantonesiska, förenklad)
**Motivering:** Azure Speech-språketikett översatt till svenska; dialekt, region och förenklad/traditionell skrift har behållits.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::zh-cn`
**Källa:** Chinese (Mandarin, Simplified)
**Svenska:** Kinesiska (mandarin, förenklad)
**Motivering:** Azure Speech-språketikett översatt till svenska; dialekt, region och förenklad/traditionell skrift har behållits.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::zh-cn-guangxi`
**Källa:** Chinese (Guangxi Accent Mandarin, Simplified)
**Svenska:** Kinesiska (mandarin med Guangxi-accent, förenklad)
**Motivering:** Azure Speech-språketikett översatt till svenska; dialekt, region och förenklad/traditionell skrift har behållits.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::zh-cn-henan`
**Källa:** Chinese (Zhongyuan Mandarin Henan, Simplified)
**Svenska:** Kinesiska (Zhongyuan-mandarin, Henan, förenklad)
**Motivering:** Azure Speech-språketikett översatt till svenska; dialekt, region och förenklad/traditionell skrift har behållits.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::zh-cn-liaoning`
**Källa:** Chinese (Northeastern Mandarin, Simplified)
**Svenska:** Kinesiska (nordöstlig mandarin, förenklad)
**Motivering:** Azure Speech-språketikett översatt till svenska; dialekt, region och förenklad/traditionell skrift har behållits.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::zh-cn-shaanxi`
**Källa:** Chinese (Zhongyuan Mandarin Shaanxi, Simplified)
**Svenska:** Kinesiska (Zhongyuan-mandarin, Shaanxi, förenklad)
**Motivering:** Azure Speech-språketikett översatt till svenska; dialekt, region och förenklad/traditionell skrift har behållits.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::zh-cn-shandong`
**Källa:** Chinese (Jilu Mandarin, Simplified)
**Svenska:** Kinesiska (Jilu-mandarin, förenklad)
**Motivering:** Azure Speech-språketikett översatt till svenska; dialekt, region och förenklad/traditionell skrift har behållits.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::zh-cn-sichuan`
**Källa:** Chinese (Southwestern Mandarin, Simplified)
**Svenska:** Kinesiska (sydvästlig mandarin, förenklad)
**Motivering:** Azure Speech-språketikett översatt till svenska; dialekt, region och förenklad/traditionell skrift har behållits.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::zh-hk`
**Källa:** Chinese (Cantonese, Traditional)
**Svenska:** Kinesiska (kantonesiska, traditionell)
**Motivering:** Azure Speech-språketikett översatt till svenska; dialekt, region och förenklad/traditionell skrift har behållits.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::zh-tw`
**Källa:** Chinese (Taiwanese Mandarin, Traditional)
**Svenska:** Kinesiska (taiwanesisk mandarin, traditionell)
**Motivering:** Azure Speech-språketikett översatt till svenska; dialekt, region och förenklad/traditionell skrift har behållits.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::language::options::zu-za`
**Källa:** isiZulu (South Africa)
**Svenska:** Zulu (Sydafrika)
**Motivering:** Azure Speech-språketikett översatt till svenska; dialekt, region och förenklad/traditionell skrift har behållits.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::australiaeast`
**Källa:** Australia East
**Svenska:** Australia East
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::brazilsouth`
**Källa:** Brazil South
**Svenska:** Brazil South
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::canadacentral`
**Källa:** Canada Central
**Svenska:** Canada Central
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::canadaeast`
**Källa:** Canada East
**Svenska:** Canada East
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::centralindia`
**Källa:** Central India
**Svenska:** Central India
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::centralus`
**Källa:** Central US
**Svenska:** Central US
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::eastasia`
**Källa:** East Asia
**Svenska:** East Asia
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::eastus`
**Källa:** East US
**Svenska:** East US
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::eastus2`
**Källa:** East US 2
**Svenska:** East US 2
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::francecentral`
**Källa:** France Central
**Svenska:** France Central
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::germanywestcentral`
**Källa:** Germany West Central
**Svenska:** Germany West Central
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::italynorth`
**Källa:** Italy North
**Svenska:** Italy North
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::japaneast`
**Källa:** Japan East
**Svenska:** Japan East
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::japanwest`
**Källa:** Japan West
**Svenska:** Japan West
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::koreacentral`
**Källa:** Korea Central
**Svenska:** Korea Central
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::northcentralus`
**Källa:** North Central US
**Svenska:** North Central US
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::northeurope`
**Källa:** North Europe
**Svenska:** North Europe
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::norwayeast`
**Källa:** Norway East
**Svenska:** Norway East
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::qatarcentral`
**Källa:** Qatar Central
**Svenska:** Qatar Central
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::southafricanorth`
**Källa:** South Africa North
**Svenska:** South Africa North
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::southcentralus`
**Källa:** South Central US
**Svenska:** South Central US
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::southeastasia`
**Källa:** Southeast Asia
**Svenska:** Southeast Asia
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::swedencentral`
**Källa:** Sweden Central
**Svenska:** Sweden Central
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::switzerlandnorth`
**Källa:** Switzerland North
**Svenska:** Switzerland North
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::switzerlandwest`
**Källa:** Switzerland West
**Svenska:** Switzerland West
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::uaenorth`
**Källa:** UAE North
**Svenska:** UAE North
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::uksouth`
**Källa:** UK South
**Svenska:** UK South
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::ukwest`
**Källa:** UK West
**Svenska:** UK West
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::westcentralus`
**Källa:** West Central US
**Svenska:** West Central US
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::westeurope`
**Källa:** West Europe
**Svenska:** West Europe
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::westus`
**Källa:** West US
**Svenska:** West US
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::westus2`
**Källa:** West US 2
**Svenska:** West US 2
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::microsoft::selector::region::options::westus3`
**Källa:** West US 3
**Svenska:** West US 3
**Motivering:** Officiellt Azure-regionnamn; bevarat oförändrat så att det matchar Microsofts tjänstnamn och regionidentifierare.
**Status:** sparad och återläst i Lokalise.

### `component::modbus::exceptions::unknown_hub::message`
**Källa:** Modbus hub {hub} is not configured.
**Svenska:** Modbus-hubben {hub} är inte konfigurerad.
**Motivering:** Modbus-hubben är etablerad svensk HA-terminologi i befintligt minne; platshållaren {hub} bevarad.
**Status:** sparad och återläst i Lokalise.

### `component::myuplink::exceptions::get_datapoint_error::message`
**Källa:** Failed to get value for datapoint {point} on device {device}.
**Svenska:** Det gick inte att hämta värdet för datapunkten {point} på enheten {device}.
**Motivering:** myUplink-feltext; datapunktstermerna och platshållarna {point}/{device} bevarade.
**Status:** sparad och återläst i Lokalise.

### `component::myuplink::selector::datapoint::fields::datapoint_id::description`
**Källa:** The ID of the datapoint. Typically a five-digit number.
**Svenska:** Datapunktens ID. Vanligtvis ett femsiffrigt tal.
**Motivering:** myUplink-servicefält; datapunkt-ID och åtgärdsbeskrivningen återgivna på idiomatisk svenska.
**Status:** sparad och återläst i Lokalise.

### `component::myuplink::selector::datapoint::fields::datapoint_id::name`
**Källa:** Datapoint
**Svenska:** Datapunkt
**Motivering:** myUplink-servicefält; datapunkt-ID och åtgärdsbeskrivningen återgivna på idiomatisk svenska.
**Status:** sparad och återläst i Lokalise.

### `component::myuplink::services::get_datapoints::description`
**Källa:** Gets the values for a list of datapoint on a device.
**Svenska:** Hämtar värden för en lista med datapunkter på en enhet.
**Motivering:** myUplink-servicefält; datapunkt-ID och åtgärdsbeskrivningen återgivna på idiomatisk svenska.
**Status:** sparad och återläst i Lokalise.

### `component::myuplink::services::get_datapoints::fields::datapoints::description`
**Källa:** A list of datapoints to get, each containing a datapoint ID.
**Svenska:** En lista med datapunkter som ska hämtas, var och en med ett datapunkt-ID.
**Motivering:** myUplink-servicefält; datapunkt-ID och åtgärdsbeskrivningen återgivna på idiomatisk svenska.
**Status:** sparad och återläst i Lokalise.

### `component::myuplink::services::get_datapoints::fields::datapoints::name`
**Källa:** Datapoints
**Svenska:** Datapunkter
**Motivering:** myUplink-servicefält; datapunkt-ID och åtgärdsbeskrivningen återgivna på idiomatisk svenska.
**Status:** sparad och återläst i Lokalise.

### `component::myuplink::services::get_datapoints::fields::device_id::description`
**Källa:** The target device for this action.
**Svenska:** Målenheten för den här åtgärden.
**Motivering:** myUplink-servicefält; datapunkt-ID och åtgärdsbeskrivningen återgivna på idiomatisk svenska.
**Status:** sparad och återläst i Lokalise.

### `component::myuplink::services::get_datapoints::fields::device_id::name`
**Källa:** Device
**Svenska:** Enhet
**Motivering:** myUplink-servicefält; datapunkt-ID och åtgärdsbeskrivningen återgivna på idiomatisk svenska.
**Status:** sparad och återläst i Lokalise.
