# Home Assistant Core: Zonneplan och Daikin, språklig rättning

Aktuell källa och svensk text kontrollerades och sparades därefter via Lokalises API 2026-11-19. Ändringarna följer den tidigare granskningsrapporten för Zonneplans elpris och Daikins molntjänst/Onecta-hänvisningar.

## `component::daikin::config::abort::unsupported_device`

**Engelska:** This Daikin adapter has no local control API. BRP069C4x/C8x require firmware 2.8.0 or later, while built-in adapters such as the Stylish FTXA20C2V1BW have no local API at all (2.6.3 is the latest firmware). Control the device through the Daikin cloud/Onecta app.

**Tidigare svenska:** Den här Daikin-adaptern har inget lokalt API för styrning. BRP069C4x/C8x kräver inbyggd programvara 2.8.0 eller senare, medan inbyggda adaptrar som Stylish FTXA20C2V1BW helt saknar lokalt API (2.6.3 är den senaste versionen av den inbyggda programvaran). Styr enheten via Daikin Cloud-/Onecta-appen.

**Sparad svenska:** Den här Daikin-adaptern har inget lokalt API för styrning. BRP069C4x/C8x kräver inbyggd programvara 2.8.0 eller senare, medan inbyggda adaptrar som Stylish FTXA20C2V1BW helt saknar lokalt API (2.6.3 är den senaste versionen av den inbyggda programvaran). Styr enheten via Daikins molntjänst eller appen Onecta.

## `component::daikin::exceptions::unsupported_device::message`

**Engelska:** This Daikin adapter has no local control API. Control the device through the Daikin cloud/Onecta app.

**Tidigare svenska:** Den här Daikin-adaptern har inget lokalt API för styrning. Styr enheten via Daikin Cloud-/Onecta-appen.

**Sparad svenska:** Den här Daikin-adaptern har inget lokalt API för styrning. Styr enheten via Daikins molntjänst eller appen Onecta.

## `component::zonneplan::services::get_electricity_prices::description`

**Engelska:** Returns the all-in electricity prices from Zonneplan.

**Tidigare svenska:** Returnerar elpriserna inklusive allt från Zonneplan.

**Sparad svenska:** Returnerar de totala elpriserna från Zonneplan.

