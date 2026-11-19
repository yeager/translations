# Rättad Google Weather-prognosbeskrivning

Sparad och återläst via Lokalise API i Home Assistant Core 2026-11-19. Översättningen förtydligar nederbördsenheten och snöns vattenmotsvarighet.

**Nyckel:** `component::google_weather::services::get_minute_forecast::description`

**Engelska:** Retrieves the precipitation forecast (nowcast) for up to 6 hours. Amounts are returned in the weather entity's precipitation unit; the snowfall amount is the liquid-water equivalent, not the snow depth. Unlike the cached forecasts, every call makes a live request to the Google Weather API and counts toward your quota.

**Tidigare svenska:** Hämtar nederbördsprognosen, en nu-prognos, för upp till 6 timmar. Mängderna returneras i väderenhetens nederbördsenhet. Snömängden avser flytande vattenekvivalent, inte snödjupet. Till skillnad från cachade prognoser gör varje anrop en direkt begäran till Google Weather API och räknas mot din kvot.

**Sparad svenska:** Hämtar nederbördsprognosen för upp till 6 timmar. Mängderna anges i väderentitetens nederbördsenhet. Snömängden avser motsvarande mängd flytande vatten, inte snödjupet. Till skillnad från cachade prognoser gör varje anrop en direkt förfrågan till Google Weather API och räknas mot din kvot.
