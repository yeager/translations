# Home Assistant Core: tidigare tomma svenska mål 601–641

- **41/41** mål granskade mot Core-revision `86a2eabe7e43f526db5821ef068087ce8404ae07`, kontrollerade i Lokalise och sparade/återlästa via API.
- **12 unika referensmål och 13 alias** kontrollerades live; alla alias matchar sitt svenska mål. Tomma delade mål för Volkszähler och Workday fylldes; vädernyckel och gemensam autentiseringstext verifierades.
- Platshållare och tekniska namn bevarades: `{site}`, `{index}`, `{policy_name}`, `{username}`, `{name}`, `middleware.php`, `.p8`, HEPA och VOC. En automatisk jämförelse av platshållare på samtliga 41 rader gav 0 avvikelser.
- `svlang skrivregler`: inga fel på 41/41. Naturlighetssignalen var 10/10 för alla; frekvensvarningarna granskades manuellt. Hunspell-flaggor gällde produkt-/protokollnamn, tekniska sammansättningar och platshållartext; ingen var ett stavfel i kontext. Hunspell-sv:s 19 regressionsprov passerar.

## Radgranskning

### `component::teslemetry::issues::energy_site_not_paired::title`
- Källa: Pair Teslemetry with the Powerwall system for {site}
- Svenska: Parkoppla Teslemetry med Powerwall-systemet för {site}
- Status: saved-and-read-back

### `component::threema::entity::image::gateway_qr_code::name`
- Källa: Gateway QR code
- Svenska: Gatewayens QR-kod
- Status: saved-and-read-back

### `component::unifi::device::outlet::name`
- Källa: Outlet {index}
- Svenska: Uttag {index}
- Status: saved-and-read-back

### `component::unifi::entity::select::firewall_policy_schedule_mode::name`
- Källa: {policy_name} schedule
- Svenska: Schema för {policy_name}
- Status: saved-and-read-back

### `component::unifi::entity::select::firewall_policy_schedule_mode::state::always`
- Källa: Always
- Svenska: Alltid
- Status: saved-and-read-back

### `component::unifi::entity::select::firewall_policy_schedule_mode::state::custom`
- Källa: Custom
- Svenska: Anpassat
- Status: saved-and-read-back

### `component::unifi::entity::select::firewall_policy_schedule_mode::state::every_day`
- Källa: Every day
- Svenska: Varje dag
- Status: saved-and-read-back

### `component::unifi::entity::select::firewall_policy_schedule_mode::state::every_week`
- Källa: Every week
- Svenska: Varje vecka
- Status: saved-and-read-back

### `component::unifi::entity::select::firewall_policy_schedule_mode::state::one_time`
- Källa: One time
- Svenska: En gång
- Status: saved-and-read-back

### `component::unifi::exceptions::schedule_mode_not_supported::message`
- Källa: This schedule mode can only be set in UniFi Network
- Svenska: Det här schemaläget kan bara ställas in i UniFi Network.
- Status: saved-and-read-back

### `component::upcloud::config::step::reauth_confirm::data::password`
- Källa: Password
- Svenska: Lösenord
- Status: saved-and-read-back
- Referens: svensk aliastext matchar det livekontrollerade målet exakt.

### `component::upcloud::config::step::reauth_confirm::data_description::password`
- Källa: The new password of the UpCloud API user.
- Svenska: Det nya lösenordet för UpCloud API-användaren.
- Status: saved-and-read-back

### `component::upcloud::config::step::reauth_confirm::description`
- Källa: The password for {username} is no longer valid.
- Svenska: Lösenordet för {username} är inte längre giltigt.
- Status: saved-and-read-back

### `component::upcloud::config::step::reauth_confirm::title`
- Källa: Authentication expired for {name}
- Svenska: Autentiseringen har upphört att gälla för {name}
- Status: saved-and-read-back
- Referens: svensk aliastext matchar det livekontrollerade målet exakt.

### `component::vesync::entity::sensor::hepa_filter_life::name`
- Källa: HEPA filter lifetime
- Svenska: HEPA-filtrets återstående livslängd
- Status: saved-and-read-back

### `component::vesync::entity::sensor::voc::name`
- Källa: Volatile organic compounds
- Svenska: Flyktiga organiska ämnen
- Status: saved-and-read-back

### `component::vicare::entity::binary_sensor::boiler_internal_pump::name`
- Källa: Internal pump
- Svenska: Intern pump
- Status: saved-and-read-back

### `component::vicare::entity::sensor::boiler_internal_pump_modulation::name`
- Källa: Internal pump modulation
- Svenska: Intern pumpmodulering
- Status: saved-and-read-back

### `component::vicare::entity::sensor::boiler_internal_pump_target_modulation::name`
- Källa: Internal pump target modulation
- Svenska: Pumpens målvärde för modulering
- Status: saved-and-read-back

### `component::volkszaehler::config::step::reconfigure::data::middleware`
- Källa: Use middleware.php
- Svenska: Använd middleware.php
- Status: saved-and-read-back
- Referens: svensk aliastext matchar det livekontrollerade målet exakt.
- Delat referensmål: tidigare tom svensk måltext fylld, sparad och återläst.

### `component::volkszaehler::config::step::reconfigure::data_description::middleware`
- Källa: Enable if your Volkszaehler instance uses 'middleware.php' in the URL (standard setup). Disable for Docker setups or custom endpoints without 'middleware.php'.
- Svenska: Aktivera om din Volkszähler-instans använder 'middleware.php' i URL:en (standardkonfiguration). Inaktivera för Docker-konfigurationer eller anpassade slutpunkter utan 'middleware.php'.
- Status: saved-and-read-back
- Referens: svensk aliastext matchar det livekontrollerade målet exakt.
- Delat referensmål: tidigare tom svensk måltext fylld, sparad och återläst.

### `component::volkszaehler::config::step::user::data::middleware`
- Källa: Use middleware.php
- Svenska: Använd middleware.php
- Status: saved-and-read-back
- Delat referensmål: tidigare tom svensk måltext fylld, sparad och återläst.

### `component::volkszaehler::config::step::user::data_description::middleware`
- Källa: Enable if your Volkszaehler instance uses 'middleware.php' in the URL (standard setup). Disable for Docker setups or custom endpoints without 'middleware.php'.
- Svenska: Aktivera om din Volkszähler-instans använder 'middleware.php' i URL:en (standardkonfiguration). Inaktivera för Docker-konfigurationer eller anpassade slutpunkter utan 'middleware.php'.
- Status: saved-and-read-back
- Delat referensmål: tidigare tom svensk måltext fylld, sparad och återläst.

### `component::weatherkit::config::step::reauth_confirm::data::key_id`
- Källa: Key ID
- Svenska: Nyckel-ID
- Status: saved-and-read-back
- Referens: svensk aliastext matchar det livekontrollerade målet exakt.

### `component::weatherkit::config::step::reauth_confirm::data::key_pem`
- Källa: Private key (.p8)
- Svenska: Privat nyckel (.p8)
- Status: saved-and-read-back
- Referens: svensk aliastext matchar det livekontrollerade målet exakt.

### `component::weatherkit::config::step::reauth_confirm::data_description::key_id`
- Källa: The ID of the new WeatherKit key.
- Svenska: ID:t för den nya WeatherKit-nyckeln.
- Status: saved-and-read-back

### `component::weatherkit::config::step::reauth_confirm::data_description::key_pem`
- Källa: The contents of the new private key file (.p8).
- Svenska: Innehållet i den nya privata nyckelfilen (.p8).
- Status: saved-and-read-back

### `component::weatherkit::config::step::reauth_confirm::description`
- Källa: Your WeatherKit key is no longer valid. Enter a new key ID and private key.
- Svenska: WeatherKit-nyckeln är inte längre giltig. Ange ett nytt nyckel-ID och en ny privat nyckel.
- Status: saved-and-read-back

### `component::weatherkit::config::step::reauth_confirm::title`
- Källa: Authentication expired for {name}
- Svenska: Autentiseringen har upphört att gälla för {name}
- Status: saved-and-read-back
- Referens: svensk aliastext matchar det livekontrollerade målet exakt.

### `component::workday::config::step::options::sections::country_settings::data::hindu_show_estimated`
- Källa: Mark estimated Hindu holidays
- Svenska: Markera hinduiska helgdagar med uppskattat datum
- Status: saved-and-read-back
- Delat referensmål: tidigare tom svensk måltext fylld, sparad och återläst.

### `component::workday::config::step::options::sections::country_settings::data::include_sundays`
- Källa: Include Sundays as holidays
- Svenska: Räkna söndagar som helgdagar
- Status: saved-and-read-back
- Delat referensmål: tidigare tom svensk måltext fylld, sparad och återläst.

### `component::workday::config::step::options::sections::country_settings::data::islamic_show_estimated`
- Källa: Mark estimated Islamic holidays
- Svenska: Markera islamiska helgdagar med uppskattat datum
- Status: saved-and-read-back
- Delat referensmål: tidigare tom svensk måltext fylld, sparad och återläst.

### `component::workday::config::step::options::sections::country_settings::data_description::hindu_show_estimated`
- Källa: Add "estimated" to the name of Hindu holidays with an estimated date
- Svenska: Lägg till ”uppskattat” i namnet på hinduiska helgdagar med uppskattat datum
- Status: saved-and-read-back
- Delat referensmål: tidigare tom svensk måltext fylld, sparad och återläst.

### `component::workday::config::step::options::sections::country_settings::data_description::include_sundays`
- Källa: Add all Sundays to the holidays of the country
- Svenska: Lägg till alla söndagar bland landets helgdagar
- Status: saved-and-read-back
- Delat referensmål: tidigare tom svensk måltext fylld, sparad och återläst.

### `component::workday::config::step::options::sections::country_settings::data_description::islamic_show_estimated`
- Källa: Add "estimated" to the name of Islamic holidays with an estimated date
- Svenska: Lägg till ”uppskattat” i namnet på islamiska helgdagar med uppskattat datum
- Status: saved-and-read-back
- Delat referensmål: tidigare tom svensk måltext fylld, sparad och återläst.

### `component::workday::options::step::init::sections::country_settings::data::hindu_show_estimated`
- Källa: Mark estimated Hindu holidays
- Svenska: Markera hinduiska helgdagar med uppskattat datum
- Status: saved-and-read-back
- Referens: svensk aliastext matchar det livekontrollerade målet exakt.

### `component::workday::options::step::init::sections::country_settings::data::include_sundays`
- Källa: Include Sundays as holidays
- Svenska: Räkna söndagar som helgdagar
- Status: saved-and-read-back
- Referens: svensk aliastext matchar det livekontrollerade målet exakt.

### `component::workday::options::step::init::sections::country_settings::data::islamic_show_estimated`
- Källa: Mark estimated Islamic holidays
- Svenska: Markera islamiska helgdagar med uppskattat datum
- Status: saved-and-read-back
- Referens: svensk aliastext matchar det livekontrollerade målet exakt.

### `component::workday::options::step::init::sections::country_settings::data_description::hindu_show_estimated`
- Källa: Add "estimated" to the name of Hindu holidays with an estimated date
- Svenska: Lägg till ”uppskattat” i namnet på hinduiska helgdagar med uppskattat datum
- Status: saved-and-read-back
- Referens: svensk aliastext matchar det livekontrollerade målet exakt.

### `component::workday::options::step::init::sections::country_settings::data_description::include_sundays`
- Källa: Add all Sundays to the holidays of the country
- Svenska: Lägg till alla söndagar bland landets helgdagar
- Status: saved-and-read-back
- Referens: svensk aliastext matchar det livekontrollerade målet exakt.

### `component::workday::options::step::init::sections::country_settings::data_description::islamic_show_estimated`
- Källa: Add "estimated" to the name of Islamic holidays with an estimated date
- Svenska: Lägg till ”uppskattat” i namnet på islamiska helgdagar med uppskattat datum
- Status: saved-and-read-back
- Referens: svensk aliastext matchar det livekontrollerade målet exakt.

## Minnes- och valideringsspår

- TM-manifest: `../Lokalise/2026-11-25-reviewed-empty-targets-601-641-tm.json`.
- API-evidens för referenser: `../Lokalise/2026-11-25-reference-targets-empty-601-641-live.json`.
- HA Core-TMX sammanfogat och validerat efter batchen: 17 768 poster.
