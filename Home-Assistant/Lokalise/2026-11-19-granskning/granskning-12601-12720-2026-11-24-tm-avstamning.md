# Home Assistant Core – historisk avstämning 12601–12720

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 96 direkta källtexter matchar HA Core-källan; 22 referensanvändningar med 19 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 2 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 12601 | 920391733 | `component::mealie::services::update_mealplan::fields::note_title::name` | Meal note title | Titel på måltidsanteckning | Core-literal match |
| 12602 | 920391732 | `component::mealie::services::update_mealplan::fields::note_title::description` | Meal note title for when planning without recipe. | Titel på måltidsanteckning för planering utan recept. | Core-literal match |
| 12603 | 920391731 | `component::mealie::services::update_mealplan::fields::note_text::name` | Note text | Anteckning | Core-literal match |
| 12604 | 920391730 | `component::mealie::services::update_mealplan::fields::note_text::description` | Meal note text for when planning without recipe. | Måltidsanteckning när du planerar utan recept. | Core-literal match |
| 12605 | 920391729 | `component::mealie::services::update_mealplan::fields::mealplan_id::name` | Mealplan ID | Måltidsplan-ID | Core-literal match |
| 12606 | 920391728 | `component::mealie::services::update_mealplan::fields::mealplan_id::description` | The mealplan ID to update. | ID för den måltidsplan som ska uppdateras. | Core-literal match |
| 12607 | 920391727 | `component::mealie::services::update_mealplan::fields::entry_type::name` | Entry type | Typ av post | Shared reference target checked |
| 12608 | 920391726 | `component::mealie::services::update_mealplan::fields::entry_type::description` | The type of dish to update the recipe to. | Den typ av rätt som ska anges för receptet. | Core-literal match |
| 12609 | 920391725 | `component::mealie::services::update_mealplan::fields::date::name` | Date | Datum | Shared reference target checked |
| 12610 | 920391724 | `component::mealie::services::update_mealplan::fields::date::description` | The date to set the mealplan for. | Det datum som måltidsplanen ska ställas in för. | Shared reference target checked |
| 12611 | 920391723 | `component::mealie::services::update_mealplan::fields::config_entry_id::name` | Mealie instance | Mealie-instans | Shared reference target checked |
| 12612 | 920391722 | `component::mealie::services::update_mealplan::fields::config_entry_id::description` | The Mealie instance to use for this action. | Den Mealie-instans som ska användas för denna åtgärd. | Shared reference target checked |
| 12613 | 920391721 | `component::mealie::services::update_mealplan::description` | Updates a mealplan | Uppdaterar en måltidsplan | Core-literal match |
| 12614 | 920391720 | `component::mealie::services::delete_mealplan::name` | Delete a mealplan | Ta bort en måltidsplan | Core-literal match |
| 12615 | 920391719 | `component::mealie::services::delete_mealplan::fields::mealplan_id::name` | Mealplan ID | Måltidsplan-ID | Core-literal match |
| 12616 | 920391718 | `component::mealie::services::delete_mealplan::fields::mealplan_id::description` | The mealplan ID to delete. | ID för den måltidsplan som ska raderas. | Core-literal match |
| 12617 | 920391717 | `component::mealie::services::delete_mealplan::fields::config_entry_id::name` | Mealie instance | Mealie-instans | Shared reference target checked |
| 12618 | 920391716 | `component::mealie::services::delete_mealplan::fields::config_entry_id::description` | The Mealie instance to use for this action. | Den Mealie-instans som ska användas för denna åtgärd. | Shared reference target checked |
| 12619 | 920391715 | `component::mealie::services::delete_mealplan::description` | Deletes a mealplan | Tar bort en måltidsplan | Core-literal match |
| 12620 | 920391714 | `component::mealie::exceptions::mealplan_not_found::message` | Mealplan with ID `{mealplan_id}` not found. | Måltidsplan med ID ”{mealplan_id}” hittades inte. | Core-literal match |
| 12621 | 920334834 | `component::watergate::entity::switch::auto_shut_off::name` | Auto shut-off | Automatisk avstängning | Core-literal match |
| 12622 | 920323986 | `component::midea::exceptions::e1_device_off::message` | Turn on the dishwasher before starting a wash cycle. | Slå på diskmaskinen innan du startar ett diskprogram. | Core-literal match |
| 12623 | 920323985 | `component::midea::entity::button::start::name` | Start | Start | Core-literal match |
| 12624 | 920086806 | `component::homeassistant::exceptions::service_device_wrong_domain::message` | Device {device_name} does not belong to integration {domain}. | Enheten {device_name} ingår inte i integrationen {domain}. | Core-literal match |
| 12625 | 920086805 | `component::homeassistant::exceptions::service_device_not_found::message` | Device with ID {device_id} was not found. | Enhet med ID {device_id} hittades inte. | Core-literal match |
| 12626 | 919655096 | `component::madvr::exceptions::send_command_failed::message` | Failed to send the command {command} | Det gick inte att skicka kommandot {command} | Core-literal match |
| 12627 | 919655095 | `component::madvr::exceptions::power_on_failed::message` | Failed to turn on the device | Det gick inte att slå på enheten | Core-literal match |
| 12628 | 919655094 | `component::madvr::exceptions::power_off_failed::message` | Failed to turn off the device | Det gick inte att stänga av enheten | Core-literal match |
| 12629 | 919535530 | `component::vizio::config::step::pair_tv::data_description::pin` | The pairing code currently shown on your TV screen. | Parkopplingskoden som just nu visas på TV-skärmen. | Core-literal match |
| 12630 | 919534969 | `component::mailgun::exceptions::send_message_failed::message` | Failed to send the Mailgun notification. | Det gick inte att skicka Mailgun-meddelandet. | Core-literal match |
| 12631 | 919524435 | `component::hotspring::entity::binary_sensor::spa_connected::name` | Spa connected | Spa anslutet | Core-literal match |
| 12632 | 919524434 | `component::hotspring::entity::binary_sensor::heating::name` | Heating | Värmer | Core-literal match |
| 12633 | 919447072 | `component::knx::config_panel::expose::create::send_on_init::label` | Send on initialization | Skicka vid initialisering | Core-literal match |
| 12634 | 919447071 | `component::knx::config_panel::expose::create::send_on_init::description` | Send the value to the KNX bus when the expose is initialized. When disabled, a state change will trigger the first telegram. | Skicka värdet till KNX-bussen när Expose initialiseras. Om funktionen är inaktiverad kommer en tillståndsförändring att utlösa det första telegrammet. | Core-literal match |
| 12635 | 919312765 | `component::harbor::config::step::discovery_confirm::title` | Set up Harbor | Ställ in Harbor | Shared reference target checked |
| 12636 | 919312764 | `component::harbor::config::step::discovery_confirm::description` | Do you want to set up the Harbor camera with serial number {serial}? | Vill du konfigurera Harbor-kameran med serienumret {serial}? | Core-literal match |
| 12637 | 919312763 | `component::harbor::config::step::discovery_confirm::data_description::key_pem` | Paste the private key that matches the client certificate. | Klistra in den privata nyckeln som matchar klientcertifikatet. | Shared reference target checked |
| 12638 | 919312762 | `component::harbor::config::step::discovery_confirm::data_description::cert_pem` | Paste the client certificate from the Harbor app. | Klistra in klientcertifikatet från Harbor-appen. | Shared reference target checked |
| 12639 | 919312761 | `component::harbor::config::step::discovery_confirm::data::key_pem` | Private key | Privat nyckel | Shared reference target checked |
| 12640 | 919312760 | `component::harbor::config::step::discovery_confirm::data::cert_pem` | Client certificate | Klientcertifikat | Shared reference target checked |
| 12641 | 919312759 | `component::harbor::config::flow_title` | {name} | {name} | Core-literal match |
| 12642 | 919312758 | `component::harbor::config::abort::invalid_discovery_info` | The discovered device does not report a valid Harbor serial number | Den upptäckta enheten anger inte ett giltigt serienummer från Harbor | Core-literal match |
| 12643 | 919312757 | `component::harbor::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. | Detta konfigureras redan. Slutför den befintliga konfigurationen innan du börjar igen. | Source-path follow-up open |
| 12644 | 919309833 | `component::besen::exceptions::no_connectable_path::message` | No connectable Bluetooth path is available for this charger: {reason} | Det finns ingen anslutningsbar Bluetooth-sökväg för den här laddaren: {reason} | Core-literal match |
| 12645 | 919309832 | `component::besen::exceptions::command_failed::message` | The charger did not accept the command. | Laddaren accepterade inte kommandot. | Core-literal match |
| 12646 | 919309831 | `component::besen::exceptions::cannot_connect::message` | Cannot connect to the charger: {error} | Det går inte att ansluta till laddaren: {error} | Core-literal match |
| 12647 | 919309830 | `component::besen::entity::switch::charging::name` | Charge | Ladda | Core-literal match |
| 12648 | 919309829 | `component::besen::config::step::user::title` | Set up Besen | Ställ in Besen | Core-literal match |
| 12649 | 919309828 | `component::besen::config::step::user::description` | Select the discovered charger and enter its Bluetooth PIN. | Välj den upptäckta laddaren och ange dess Bluetooth-PIN-kod. | Core-literal match |
| 12650 | 919309827 | `component::besen::config::step::user::data_description::pin` | The 6-digit Bluetooth PIN configured on the charger. | Den 6-siffriga Bluetooth-PIN-koden som har ställts in på laddaren. | Core-literal match |
| 12651 | 919309826 | `component::besen::config::step::user::data_description::address` | The discovered Besen charger to set up. | Den upptäckta Besen-laddaren som ska konfigureras. | Core-literal match |
| 12652 | 919309825 | `component::besen::config::step::user::data::pin` | PIN code | PIN-kod | Shared reference target checked |
| 12653 | 919309824 | `component::besen::config::step::user::data::address` | Device | Enhet | Shared reference target checked |
| 12654 | 919309823 | `component::besen::config::step::bluetooth_confirm::title` | Set up Besen | Ställ in Besen | Core-literal match |
| 12655 | 919309822 | `component::besen::config::step::bluetooth_confirm::description` | Enter the 6-digit Bluetooth PIN for this charger. | Ange den 6-siffriga Bluetooth-PIN-koden för den här laddaren. | Core-literal match |
| 12656 | 919309821 | `component::besen::config::step::bluetooth_confirm::data_description::pin` | The 6-digit Bluetooth PIN configured on the charger. | Den 6-siffriga Bluetooth-PIN-koden som har ställts in på laddaren. | Core-literal match |
| 12657 | 919309820 | `component::besen::config::step::bluetooth_confirm::data::pin` | PIN code | PIN-kod | Shared reference target checked |
| 12658 | 919309819 | `component::besen::config::flow_title` | {name} | {name} | Core-literal match |
| 12659 | 919309818 | `component::besen::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 12660 | 919309817 | `component::besen::config::error::no_connectable_path` | No connectable Bluetooth path is available for this charger. | Det finns ingen anslutningsbar Bluetooth-sökväg för den här laddaren. | Core-literal match |
| 12661 | 919309816 | `component::besen::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 12662 | 919309815 | `component::besen::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 12663 | 919309814 | `component::besen::config::abort::not_supported` | This Bluetooth device is not a supported Besen charger. | Den här Bluetooth-enheten är inte en Besen-laddare som stöds. | Core-literal match |
| 12664 | 919309813 | `component::besen::config::abort::no_devices_found` | No devices found on the network | Inga enheter hittades i nätverket | Shared reference target checked |
| 12665 | 919309812 | `component::besen::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 12666 | 919309662 | `component::abode::exceptions::change_setting_failed::message` | Failed to change Abode setting: {error} | Det gick inte att ändra inställningen för Abode: {error} | Core-literal match |
| 12667 | 919309605 | `component::lastfm::options::error::hidden_recent_tracks` | User has hidden their recent listening information. Disable "Hide recent listening information" at {privacy_settings_url} | Användaren har dolt sin senaste lyssningshistorik. Inaktivera alternativet ”Dölj senaste lyssningshistorik” på {privacy_settings_url} | Shared reference target checked |
| 12668 | 919309604 | `component::lastfm::config::error::hidden_recent_tracks` | User has hidden their recent listening information. Disable "Hide recent listening information" at {privacy_settings_url} | Användaren har dolt sin senaste lyssningshistorik. Inaktivera alternativet ”Dölj senaste lyssningshistorik” på {privacy_settings_url} | Core-literal match |
| 12669 | 919308681 | `component::lyngdorf::entity::select::voicing::name` | Voicing | Voicing | Core-literal match |
| 12670 | 919308680 | `component::lyngdorf::entity::select::room_perfect_position::name` | RoomPerfect position | RoomPerfect-position | Core-literal match |
| 12671 | 919308382 | `component::lyngdorf::exceptions::unsupported_remote_key::message` | This device does not have that remote key. It supports: {keys} | Enheten har inte den fjärrkontrollknappen. Den stöder följande knappar: {keys} | Core-literal match |
| 12672 | 919308365 | `component::anglian_water::config::step::mfa::description` | Two-factor authentication is enabled on your account. Check your email for the security code. It will come from `no-reply@anglianwater.co.uk`. | Tvåfaktorsautentisering är aktiverad på ditt konto. Kontrollera din e-post för att hitta säkerhetskoden. Den skickas från `no-reply@anglianwater.co.uk`. | Core-literal match |
| 12673 | 919308364 | `component::anglian_water::config::step::mfa::data_description::code` | The security code sent to your email. | Säkerhetskoden som skickades till din e-postadress. | Core-literal match |
| 12674 | 919308363 | `component::anglian_water::config::step::mfa::data::code` | Security code | Säkerhetskod | Core-literal match |
| 12675 | 919308362 | `component::anglian_water::config::error::invalid_code` | The security code provided is invalid. Please check your email for the correct code. | Den angivna säkerhetskoden är ogiltig. Kontrollera din e-post för att få den rätta koden. | Core-literal match |
| 12676 | 919308237 | `component::teslemetry::entity::sensor::self_driving_miles_since_reset::name` | Self-driving miles since reset | Körsträcka med självkörning sedan återställning | Core-literal match |
| 12677 | 919308236 | `component::teslemetry::entity::sensor::miles_since_reset::name` | Miles since reset | Körsträcka sedan återställning | Core-literal match |
| 12678 | 919308235 | `component::teslemetry::entity::sensor::lifetime_energy_gained_regen::name` | Lifetime energy gained regen | Total återvunnen energi under livslängden | Core-literal match |
| 12679 | 919308217 | `component::remember_the_milk::config::step::reauth_confirm::title` | Authentication expired for {name} | Autentiseringen har upphört att gälla för {name} | Shared reference target checked |
| 12680 | 919308216 | `component::remember_the_milk::config::step::reauth_confirm::description` | The Remember The Milk integration needs to re-authenticate your account | Remember The Milk-integrationen behöver autentisera ditt konto på nytt. | Core-literal match |
| 12681 | 919308215 | `component::remember_the_milk::config::abort::unique_id_mismatch` | The login details correspond to a different account. Please re-authenticate to the previously configured account. | Inloggningsuppgifterna hör till ett annat konto. Autentisera det tidigare konfigurerade kontot på nytt. | Core-literal match |
| 12682 | 919308214 | `component::remember_the_milk::config::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | Source-path follow-up open |
| 12683 | 919307622 | `component::alexa_devices::entity::select::default_device::name` | Default device | Standardenhet | Core-literal match |
| 12684 | 919307330 | `component::smartthings::entity::select::dishwasher_washing_course::state::upper_express` | Upper express | Övre express | Core-literal match |
| 12685 | 919307329 | `component::smartthings::entity::select::dishwasher_washing_course::state::steam_soak` | Steam soak | Ångbad | Core-literal match |
| 12686 | 919307328 | `component::smartthings::entity::select::dishwasher_washing_course::state::self_clean` | Self clean | Självrengöring | Core-literal match |
| 12687 | 919307327 | `component::smartthings::entity::select::dishwasher_washing_course::state::rinse_only` | Rinse only | Endast sköljning | Core-literal match |
| 12688 | 919307326 | `component::smartthings::entity::select::dishwasher_washing_course::state::rinse_dry` | Rinse dry | Sköljning och torkning | Core-literal match |
| 12689 | 919307325 | `component::smartthings::entity::select::dishwasher_washing_course::state::quick` | Quick | Snabb | Core-literal match |
| 12690 | 919307324 | `component::smartthings::entity::select::dishwasher_washing_course::state::pre_wash` | Pre wash | Förtvätt | Core-literal match |
| 12691 | 919307323 | `component::smartthings::entity::select::dishwasher_washing_course::state::pre_blast` | Pre blast | Förtvätt | Core-literal match |
| 12692 | 919307322 | `component::smartthings::entity::select::dishwasher_washing_course::state::pots_and_pans` | Pots and pans | Kastruller och stekpannor | Core-literal match |
| 12693 | 919307321 | `component::smartthings::entity::select::dishwasher_washing_course::state::plastics` | Plastic | Plast | Core-literal match |
| 12694 | 919307320 | `component::smartthings::entity::select::dishwasher_washing_course::state::normal` | Normal | Normal | Core-literal match |
| 12695 | 919307319 | `component::smartthings::entity::select::dishwasher_washing_course::state::night_silence` | Night silence | Tyst nattprogram | Core-literal match |
| 12696 | 919307318 | `component::smartthings::entity::select::dishwasher_washing_course::state::night` | Night | Natt | Core-literal match |
| 12697 | 919307317 | `component::smartthings::entity::select::dishwasher_washing_course::state::machine_care` | Machine care | Maskinvård | Core-literal match |
| 12698 | 919307316 | `component::smartthings::entity::select::dishwasher_washing_course::state::intensive` | Intensive | Intensiv | Core-literal match |
| 12699 | 919307315 | `component::smartthings::entity::select::dishwasher_washing_course::state::heavy` | Heavy | Grov | Core-literal match |
| 12700 | 919307314 | `component::smartthings::entity::select::dishwasher_washing_course::state::glasses` | Delicate | Skonsamt | Core-literal match |
| 12701 | 919307313 | `component::smartthings::entity::select::dishwasher_washing_course::state::extra_silence` | Extra silence | Extra tyst | Core-literal match |
| 12702 | 919307312 | `component::smartthings::entity::select::dishwasher_washing_course::state::express` | Express | Express | Core-literal match |
| 12703 | 919307311 | `component::smartthings::entity::select::dishwasher_washing_course::state::eco` | Eco | Eco | Core-literal match |
| 12704 | 919307310 | `component::smartthings::entity::select::dishwasher_washing_course::state::dry_only` | Dry only | Endast torkning | Core-literal match |
| 12705 | 919307309 | `component::smartthings::entity::select::dishwasher_washing_course::state::drinkware` | Drinkware | Glas | Core-literal match |
| 12706 | 919307308 | `component::smartthings::entity::select::dishwasher_washing_course::state::delicate` | Delicate | Skonsamt | Core-literal match |
| 12707 | 919307307 | `component::smartthings::entity::select::dishwasher_washing_course::state::daily` | Daily | Dagligt | Core-literal match |
| 12708 | 919307306 | `component::smartthings::entity::select::dishwasher_washing_course::state::cold_rinse` | Cold rinse | Kall sköljning | Core-literal match |
| 12709 | 919307305 | `component::smartthings::entity::select::dishwasher_washing_course::state::chef` | Chef | Kock | Core-literal match |
| 12710 | 919307304 | `component::smartthings::entity::select::dishwasher_washing_course::state::babycare` | Baby care | Barnartiklar | Core-literal match |
| 12711 | 919307303 | `component::smartthings::entity::select::dishwasher_washing_course::state::baby_bottle` | Baby bottle | Nappflaska | Core-literal match |
| 12712 | 919307302 | `component::smartthings::entity::select::dishwasher_washing_course::state::auto` | Auto | Auto | Core-literal match |
| 12713 | 919307301 | `component::smartthings::entity::select::dishwasher_washing_course::state::ai` | AI Wash | AI-tvätt | Core-literal match |
| 12714 | 919307300 | `component::smartthings::entity::select::dishwasher_washing_course::name` | Cycle | Diskprogram | Core-literal match |
| 12715 | 919306817 | `component::vistapool::entity::time::filtration_interval_start::name` | Filtration interval {number} start | Start för filtreringsintervall {number} | Core-literal match |
| 12716 | 919306816 | `component::vistapool::entity::time::filtration_interval_end::name` | Filtration interval {number} end | Slut för filtreringsintervall {number} | Core-literal match |
| 12717 | 919306812 | `component::portainer::entity::event::docker_event::state_attributes::event_type::state::update` | Updated | Uppdaterad | Core-literal match |
| 12718 | 919306811 | `component::portainer::entity::event::docker_event::state_attributes::event_type::state::unpause` | Unpaused | Återupptagen | Core-literal match |
| 12719 | 919306810 | `component::portainer::entity::event::docker_event::state_attributes::event_type::state::stop` | Stopped | Stoppad | Core-literal match |
| 12720 | 919306809 | `component::portainer::entity::event::docker_event::state_attributes::event_type::state::start` | Started | Startad | Core-literal match |

## Sparade korrigeringar

| Lokalise-nyckel-ID | Nyckel | Sparad svenska |
|---:|---|---|
| 919308237 | `component::teslemetry::entity::sensor::self_driving_miles_since_reset::name` | Körsträcka med självkörning sedan återställning |
| 919308236 | `component::teslemetry::entity::sensor::miles_since_reset::name` | Körsträcka sedan återställning |
| 919307304 | `component::smartthings::entity::select::dishwasher_washing_course::state::babycare` | Barnartiklar |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 919312757 | `component::harbor::config::abort::already_in_progress` | This is already being configured. Finish the existing configuration before starting again. |
| 919308214 | `component::remember_the_milk::config::abort::reauth_successful` | Re-authentication was successful |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
