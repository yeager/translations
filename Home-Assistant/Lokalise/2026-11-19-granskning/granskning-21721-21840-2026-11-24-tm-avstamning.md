# Home Assistant Core – historisk avstämning 21721–21840

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 73 direkta källtexter matchar HA Core-källan; 31 referensanvändningar med 27 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 16 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 21721 | 828725807 | `component::victron_gx::entity::sensor::alternator_dc_voltage::name` | DC output voltage | DC-utgångsspänning | Shared reference target checked |
| 21722 | 828725806 | `component::victron_gx::entity::sensor::alternator_dc_power::name` | DC output power | DC-utgångseffekt | Shared reference target checked |
| 21723 | 828725805 | `component::victron_gx::entity::sensor::alternator_dc_current::name` | DC output current | DC-utgångsström | Shared reference target checked |
| 21724 | 828725804 | `component::victron_gx::entity::sensor::alternator_charge_current_limit::name` | Charge current limit | Gräns för laddström | Source-path follow-up open |
| 21725 | 828725803 | `component::victron_gx::entity::sensor::acsystem_mode::state::passthrough` | Passthrough | Genomgång | Source-path follow-up open |
| 21726 | 828725802 | `component::victron_gx::entity::sensor::acsystem_mode::state::on` | On | På | Source-path follow-up open |
| 21727 | 828725801 | `component::victron_gx::entity::sensor::acsystem_mode::state::off` | Off | Av | Source-path follow-up open |
| 21728 | 828725800 | `component::victron_gx::entity::sensor::acsystem_mode::state::inverter_only` | Inverter only | Endast växelriktare | Source-path follow-up open |
| 21729 | 828725799 | `component::victron_gx::entity::sensor::acsystem_mode::state::charger_only` | Charger only | Endast laddare | Source-path follow-up open |
| 21730 | 828725798 | `component::victron_gx::entity::sensor::acsystem_mode::name` | Mode | Läge | Source-path follow-up open |
| 21731 | 828725797 | `component::victron_gx::entity::sensor::acload_voltage_phase::name` | Voltage on {phase} | Spänning på {phase} | Shared reference target checked |
| 21732 | 828725796 | `component::victron_gx::entity::sensor::acload_voltage::name` | Voltage | Spänning | Shared reference target checked |
| 21733 | 828725795 | `component::victron_gx::entity::sensor::acload_power_phase::name` | Power on {phase} | Effekt på {phase} | Shared reference target checked |
| 21734 | 828725794 | `component::victron_gx::entity::sensor::acload_power::name` | Power | Effekt | Shared reference target checked |
| 21735 | 828725793 | `component::victron_gx::entity::sensor::acload_frequency::name` | Frequency | Frekvens | Shared reference target checked |
| 21736 | 828725792 | `component::victron_gx::entity::sensor::acload_energy_forward_phase::name` | Consumption on {phase} | Förbrukning på {phase} | Shared reference target checked |
| 21737 | 828725791 | `component::victron_gx::entity::sensor::acload_energy_forward::name` | Consumption | Förbrukning | Shared reference target checked |
| 21738 | 828725790 | `component::victron_gx::entity::sensor::acload_current_phase::name` | Current on {phase} | Ström på {phase} | Shared reference target checked |
| 21739 | 828725789 | `component::victron_gx::entity::sensor::acload_current::name` | Load current | Last ström | Core-literal match |
| 21740 | 828725788 | `component::victron_gx::config::step::user::data_description::username` | Username for the MQTT server, default is empty. Not needed by Victron devices. This is only needed if you route your MQTT messages through a non-Victron server and it does require a username. | Användarnamn för MQTT-servern, standardvärdet är tomt. Behövs inte för Victron-enheter. Detta behövs bara om du dirigerar dina MQTT-meddelanden via en server som inte är från Victron och som kräver ett användarnamn. | Core-literal match |
| 21741 | 828725787 | `component::victron_gx::config::step::user::data_description::ssl` | Indicates whether to use SSL to connect to the Victron device. Normally it is disabled. | Anger om SSL ska användas för att ansluta till Victron-enheten. Normalt är det inaktiverat. | Core-literal match |
| 21742 | 828725786 | `component::victron_gx::config::step::user::data_description::port` | The MQTT port on the host. Normally it is 1883. | MQTT-porten på värden. Normalt är den 1883. | Core-literal match |
| 21743 | 828725785 | `component::victron_gx::config::step::user::data_description::password` | Password for the Victron device, default is empty. This is not your VRM password. | Lösenord för Victron-enheten, standardinställningen är tom. Detta är inte ditt VRM-lösenord. | Core-literal match |
| 21744 | 828725784 | `component::victron_gx::config::step::user::data_description::host` | Hostname or IP address of Victron device, usually mDNS name like 'venus.local' | Värdnamn eller IP-adress för Victron-enhet, vanligtvis mDNS-namn likt 'venus.local' | Core-literal match |
| 21745 | 828725783 | `component::victron_gx::config::step::user::data::username` | Username | Användarnamn | Shared reference target checked |
| 21746 | 828725782 | `component::victron_gx::config::step::user::data::ssl` | Uses an SSL certificate | Använder ett SSL-certifikat | Shared reference target checked |
| 21747 | 828725781 | `component::victron_gx::config::step::user::data::port` | Port | Port | Shared reference target checked |
| 21748 | 828725780 | `component::victron_gx::config::step::user::data::password` | Password | Lösenord | Shared reference target checked |
| 21749 | 828725779 | `component::victron_gx::config::step::user::data::host` | Host | Värd | Shared reference target checked |
| 21750 | 828725778 | `component::victron_gx::config::step::ssdp_confirm::description` | Do you want to set up the Victron GX device {name}? | Vill du konfigurera Victron GX-enheten {name}? | Core-literal match |
| 21751 | 828725777 | `component::victron_gx::config::step::ssdp_auth::title` | Authenticate Victron GX | Autentisera Victron GX | Core-literal match |
| 21752 | 828725776 | `component::victron_gx::config::step::ssdp_auth::description` | Enter the GX password for the GX device at {host}. | Ange GX-lösenordet för GX-enheten på {host}. | Core-literal match |
| 21753 | 828725775 | `component::victron_gx::config::step::ssdp_auth::data_description::username` | Username for the MQTT server, default is empty. Not needed by Victron devices. This is only needed if you route your MQTT messages through a non-Victron server and it does require a username. | Användarnamn för MQTT-servern, standardvärdet är tomt. Behövs inte för Victron-enheter. Detta behövs bara om du dirigerar dina MQTT-meddelanden via en server som inte är från Victron och som kräver ett användarnamn. | Source-path follow-up open |
| 21754 | 828725774 | `component::victron_gx::config::step::ssdp_auth::data_description::ssl` | Indicates whether to use SSL to connect to the Victron device. Normally it is disabled. | Anger om SSL ska användas för att ansluta till Victron-enheten. Normalt är det inaktiverat. | Shared reference target checked |
| 21755 | 828725773 | `component::victron_gx::config::step::ssdp_auth::data_description::password` | Password for the Victron device, default is empty. This is not your VRM password. | Lösenord för Victron-enheten, standardinställningen är tom. Detta är inte ditt VRM-lösenord. | Shared reference target checked |
| 21756 | 828725772 | `component::victron_gx::config::step::ssdp_auth::data::username` | Username | Användarnamn | Source-path follow-up open |
| 21757 | 828725771 | `component::victron_gx::config::step::ssdp_auth::data::ssl` | Uses an SSL certificate | Använder ett SSL-certifikat | Shared reference target checked |
| 21758 | 828725770 | `component::victron_gx::config::step::ssdp_auth::data::password` | GX password | GX-lösenord | Core-literal match |
| 21759 | 828725769 | `component::victron_gx::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 21760 | 828725768 | `component::victron_gx::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 21761 | 828725767 | `component::victron_gx::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 21762 | 828725766 | `component::victron_gx::config::abort::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 21763 | 828725765 | `component::victron_gx::config::abort::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 21764 | 828725764 | `component::victron_gx::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 21765 | 828724388 | `component::schlage::services::add_code::fields::notify_on_use::name` | Notify when PIN is used | Avisera när PIN-koden används | Core-literal match |
| 21766 | 828724387 | `component::schlage::services::add_code::fields::notify_on_use::description` | Whether the native Schlage notification should be sent when this PIN is used. | Om den inbyggda Schlage-aviseringen ska skickas när denna PIN-kod används. | Core-literal match |
| 21767 | 828724386 | `component::anthropic::config_subentries::conversation::step::model::data_description::tool_search` | Enable dynamic tool discovery instead of preloading all tools into the context | Möjliggör dynamisk verktygsupptäckt i stället för att alla verktyg laddas in i kontexten | Core-literal match |
| 21768 | 828724385 | `component::anthropic::config_subentries::conversation::step::model::data::tool_search` | Enable tool search tool | Aktivera verktygssökning | Core-literal match |
| 21769 | 828724384 | `component::anthropic::config_subentries::ai_task_data::step::model::data_description::tool_search` | Enable dynamic tool discovery instead of preloading all tools into the context | Möjliggör dynamisk verktygsupptäckt i stället för att alla verktyg laddas in i kontexten | Shared reference target checked |
| 21770 | 828724383 | `component::anthropic::config_subentries::ai_task_data::step::model::data::tool_search` | Enable tool search tool | Aktivera verktygssökning | Shared reference target checked |
| 21771 | 828722086 | `component::backblaze_b2::exceptions::bad_request::message` | The Backblaze B2 API rejected the request: {error_message} | Backblaze B2 API avvisade begäran: {error_message} | Core-literal match |
| 21772 | 828722085 | `component::backblaze_b2::config::error::bad_request` | The Backblaze B2 API rejected the request: {error_message} | Backblaze B2 API avvisade begäran: {error_message} | Core-literal match |
| 21773 | 828712933 | `component::fritz::entity::switch::wi_fi_main_5ghz_high_6ghz::name` | Wi-Fi Main 5GHz High / 6GHz | Main 5 GHz High / 6 GHz | Core-literal match |
| 21774 | 828712932 | `component::fritz::entity::switch::wi_fi_main_5ghz::name` | Wi-Fi Main 5GHz | Main 5 GHz | Core-literal match |
| 21775 | 828712931 | `component::fritz::entity::switch::wi_fi_main_2_4ghz::name` | Wi-Fi Main 2.4GHz | Main 2.4 GHz | Core-literal match |
| 21776 | 828712930 | `component::fritz::entity::switch::wi_fi_guest::name` | Wi-Fi Guest | Gäst | Core-literal match |
| 21777 | 828643082 | `component::mastodon::services::update_profile::name` | Update profile | Uppdatera profil | Core-literal match |
| 21778 | 828643081 | `component::mastodon::services::update_profile::fields::note::name` | Bio | Bio | Core-literal match |
| 21779 | 828643080 | `component::mastodon::services::update_profile::fields::note::description` | The bio to set on your profile. You can @mention other people or #hashtags. | Den biografi du vill ange i din profil. Du kan @nämna andra personer eller använda #hashtags. | Core-literal match |
| 21780 | 828643079 | `component::mastodon::services::update_profile::fields::locked::name` | Lock profile | Lås profil | Core-literal match |
| 21781 | 828643078 | `component::mastodon::services::update_profile::fields::locked::description` | Whether to lock your profile. A locked profile requires you to approve followers and hides your posts from non-followers. | Om din profil ska låsas. En låst profil kräver att du godkänner följare och döljer dina inlägg från icke-följare. | Core-literal match |
| 21782 | 828643077 | `component::mastodon::services::update_profile::fields::header::name` | Header picture | Rubrikbild | Core-literal match |
| 21783 | 828643076 | `component::mastodon::services::update_profile::fields::header::description` | An image to set as your profile header. WEBP, PNG, or JPG. At most 8 MB. Will be downscaled to 1500x500px. | En bild att ange som profilrubrik. WEBP, PNG eller JPG. Högst 8 MB. Kommer att skalas ner till 1500x500px. | Core-literal match |
| 21784 | 828643075 | `component::mastodon::services::update_profile::fields::fields::name` | Extra fields | Extra fält | Core-literal match |
| 21785 | 828643074 | `component::mastodon::services::update_profile::fields::fields::description` | Additional profile fields as key-value pairs. Your homepage, pronouns, age, anything you want. Note that updating fields will replace all existing fields, not just the ones specified here. | Ytterligare profilfält som nyckel-värdepar. Din hemsida, pronomen, ålder, vad du vill. Observera att uppdatering av fält kommer att ersätta alla befintliga fält, inte bara de som anges här. | Core-literal match |
| 21786 | 828643073 | `component::mastodon::services::update_profile::fields::display_name::name` | Display name | Visningsnamn | Core-literal match |
| 21787 | 828643072 | `component::mastodon::services::update_profile::fields::display_name::description` | The display name to set on your profile. | Visningsnamnet som ska anges på din profil. | Core-literal match |
| 21788 | 828643071 | `component::mastodon::services::update_profile::fields::discoverable::name` | Discoverable | Upptäckbar | Core-literal match |
| 21789 | 828643070 | `component::mastodon::services::update_profile::fields::discoverable::description` | Whether your profile should be discoverable. Public posts and the profile may be featured or recommended across Mastodon. | Om din profil ska vara synlig för andra. Offentliga inlägg och profilen kan visas eller rekommenderas på Mastodon. | Core-literal match |
| 21790 | 828643069 | `component::mastodon::services::update_profile::fields::config_entry_id::name` | Mastodon account | Mastodon-konto | Shared reference target checked |
| 21791 | 828643068 | `component::mastodon::services::update_profile::fields::config_entry_id::description` | Select the Mastodon account to update the profile of. | Välj det Mastodon-konto som du vill uppdatera profilen för. | Core-literal match |
| 21792 | 828643067 | `component::mastodon::services::update_profile::fields::bot::name` | Automated account | Automatiserat konto | Core-literal match |
| 21793 | 828643066 | `component::mastodon::services::update_profile::fields::bot::description` | Signal to others that the account mainly performs automated actions. | Signalera till andra att kontot huvudsakligen utför automatiserade åtgärder. | Core-literal match |
| 21794 | 828643065 | `component::mastodon::services::update_profile::fields::avatar::name` | Profile picture | Profilbild | Core-literal match |
| 21795 | 828643064 | `component::mastodon::services::update_profile::fields::avatar::description` | An image to set as your profile picture. WEBP, PNG, or JPG. At most 8 MB. Will be downscaled to 400x400px. | En bild att ange som din profilbild. WEBP, PNG eller JPG. Högst 8 MB. Kommer att skalas ner till 400x400px. | Core-literal match |
| 21796 | 828643063 | `component::mastodon::services::update_profile::fields::attribution_domains::name` | Attribution domains | Attributionsdomäner | Core-literal match |
| 21797 | 828643062 | `component::mastodon::services::update_profile::fields::attribution_domains::description` | Websites allowed to credit you. Protects from false attributions. Note that setting attribution domains will replace all existing attribution domains, not just the ones specified here. | Webbplatser som får ange dig som källa. Skyddar mot felaktiga källangivelser. Observera att inställningen av källangivningsdomäner kommer att ersätta alla befintliga källangivningsdomäner, inte bara de som anges här. | Core-literal match |
| 21798 | 828643061 | `component::mastodon::services::update_profile::description` | Updates your Mastodon profile information and pictures. | Uppdaterar dina profiluppgifter och bilder på Mastodon. | Core-literal match |
| 21799 | 828643060 | `component::mastodon::selector::fields::fields::value::name` | Value | Värde | Core-literal match |
| 21800 | 828643059 | `component::mastodon::selector::fields::fields::value::description` | The value for this field. | Värdet för detta fält. | Core-literal match |
| 21801 | 828643058 | `component::mastodon::selector::fields::fields::name::name` | Label | Etikett | Core-literal match |
| 21802 | 828643057 | `component::mastodon::selector::fields::fields::name::description` | The label for this field. | Etiketten för det här fältet. | Core-literal match |
| 21803 | 828643056 | `component::mastodon::exceptions::unable_to_update_profile::message` | Unable to update profile. | Det gick inte att uppdatera profilen. | Core-literal match |
| 21804 | 828643055 | `component::mastodon::exceptions::media_source_not_supported::message` | Media source {media_content_id} is not supported. | Mediekälla {media_content_id} stöds inte. | Core-literal match |
| 21805 | 828453025 | `component::anthropic::selector::prompt_caching::options::prompt` | System prompt | Systemprompt | Core-literal match |
| 21806 | 828453024 | `component::anthropic::selector::prompt_caching::options::off` | Disabled | Inaktiverad | Core-literal match |
| 21807 | 828453023 | `component::anthropic::selector::prompt_caching::options::automatic` | Full | Fullständig | Core-literal match |
| 21808 | 828453022 | `component::anthropic::config_subentries::conversation::step::advanced::data_description::prompt_caching` | Optimize your API cost and response times based on your usage. | Optimera dina API-kostnader och svarstider baserat på din användning. | Source-path follow-up open |
| 21809 | 828453021 | `component::anthropic::config_subentries::conversation::step::advanced::data::prompt_caching` | Caching strategy | Cachningsstrategi | Source-path follow-up open |
| 21810 | 828453020 | `component::anthropic::config_subentries::ai_task_data::step::advanced::data_description::prompt_caching` | Optimize your API cost and response times based on your usage. | Optimera dina API-kostnader och svarstider baserat på din användning. | Source-path follow-up open |
| 21811 | 828453019 | `component::anthropic::config_subentries::ai_task_data::step::advanced::data::prompt_caching` | Caching strategy | Cachningsstrategi | Source-path follow-up open |
| 21812 | 828289178 | `component::gardena_bluetooth::entity::number::remaining_watering_time::name` | Remaining watering time | Återstående bevattningstid | Core-literal match |
| 21813 | 828287519 | `component::traccar_server::entity::sensor::power::name` | Supply voltage | Matningsspänning | Core-literal match |
| 21814 | 828287518 | `component::traccar_server::entity::sensor::battery::name` | Battery voltage | Batterispänning | Core-literal match |
| 21815 | 828287517 | `component::sunricher_dali::exceptions::cannot_discover_devices::message` | Unable to discover devices and scenes from the gateway. | Det går inte att upptäcka enheter och scener från gatewayen. | Core-literal match |
| 21816 | 828287516 | `component::sunricher_dali::exceptions::cannot_connect::message` | Could not connect to the gateway at {host}. Please check that the device is powered on and reachable | Det gick inte att ansluta till gateway på {host}. Kontrollera att enheten är påslagen och tillgänglig. | Core-literal match |
| 21817 | 828287008 | `component::lunatone::config::abort::unique_id_mismatch` | Please ensure you reconfigure against the same device. | Se till att du konfigurerar om mot samma enhet. | Core-literal match |
| 21818 | 828278208 | `component::rainforest_eagle::config::error::unsupported_device_type` | This type of Rainforest Eagle device is not supported. | Den här typen av Rainforest Eagle-enhet stöds inte. | Core-literal match |
| 21819 | 828278207 | `component::rainforest_eagle::config::error::unknown_device_type` | Unable to determine the type of Rainforest Eagle device. Please ensure your device is supported. | Det går inte att identifiera vilken typ av Rainforest Eagle-enhet det rör sig om. Kontrollera att din enhet stöds. | Core-literal match |
| 21820 | 828278206 | `component::rainforest_eagle::config::error::no_meters_connected` | No meters are currently connected. Ensure your meter is connected and try again. | Det finns för närvarande inga mätare anslutna. Se till att din mätare är ansluten och försök igen. | Core-literal match |
| 21821 | 828274973 | `component::portainer::entity::button::kill_container::name` | Kill container | Döda container | Core-literal match |
| 21822 | 828257749 | `component::fritz::issues::deprecated_cleanup_button::title` | 'Cleanup' button is deprecated | Knappen "Cleanup" är föråldrad | Source-path follow-up open |
| 21823 | 828257748 | `component::fritz::issues::deprecated_cleanup_button::description` | The 'Cleanup' button is deprecated and will be removed in Home Assistant Core {removal_version}. Please update your automations and dashboards to remove any usage of this button. The action is now performed automatically at each data refresh. | Knappen ”Cleanup” är föråldrad och kommer att tas bort i Home Assistant Core {removal_version}. Uppdatera dina automatiseringar och kontrollpaneler så att denna knapp inte längre används. Åtgärden utförs nu istället automatiskt vid varje datauppdatering. | Source-path follow-up open |
| 21824 | 828244183 | `component::opendisplay::exceptions::authentication_error::message` | Authentication failed. Please update the encryption key. | Autentiseringen misslyckades. Uppdatera krypteringsnyckeln. | Core-literal match |
| 21825 | 828244182 | `component::opendisplay::config::step::reauth_confirm::title` | Re-authentication required | Återautentisering krävs | Core-literal match |
| 21826 | 828244181 | `component::opendisplay::config::step::reauth_confirm::description` | Authentication failed for {name}. Enter the correct encryption key, or leave blank if encryption has been disabled on the device. | Autentiseringen misslyckades för {name}. Ange rätt krypteringsnyckel, eller lämna fältet tomt om krypteringen har inaktiverats på enheten. | Core-literal match |
| 21827 | 828244180 | `component::opendisplay::config::step::reauth_confirm::data_description::encryption_key` | Enter the 32-character hexadecimal AES-128 encryption key for this device. | Ange den 32 tecken långa hexadecimala AES-128-krypteringsnyckeln för den här enheten. | Shared reference target checked |
| 21828 | 828244179 | `component::opendisplay::config::step::reauth_confirm::data::encryption_key` | Encryption key | Krypteringsnyckel | Shared reference target checked |
| 21829 | 828244178 | `component::opendisplay::config::step::encryption_key::title` | Encryption required | Kryptering krävs | Core-literal match |
| 21830 | 828244177 | `component::opendisplay::config::step::encryption_key::description` | {name} requires an encryption key to connect. | {name} kräver en krypteringsnyckel för att ansluta. | Core-literal match |
| 21831 | 828244176 | `component::opendisplay::config::step::encryption_key::data_description::encryption_key` | Enter the 32-character hexadecimal AES-128 encryption key for this device. | Ange den 32 tecken långa hexadecimala AES-128-krypteringsnyckeln för den här enheten. | Core-literal match |
| 21832 | 828244175 | `component::opendisplay::config::step::encryption_key::data::encryption_key` | Encryption key | Krypteringsnyckel | Core-literal match |
| 21833 | 828244174 | `component::opendisplay::config::error::invalid_key_format` | The encryption key must be exactly 32 hexadecimal characters (0-9, a-f). | Krypteringsnyckeln måste vara exakt 32 hexadecimala tecken lång (0-9, a-f). | Core-literal match |
| 21834 | 828244173 | `component::opendisplay::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 21835 | 828244172 | `component::opendisplay::config::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | Source-path follow-up open |
| 21836 | 828243537 | `component::portainer::entity::button::volumes_prune::name` | Prune unused volumes | Rensa oanvända volymer | Core-literal match |
| 21837 | 828242211 | `component::matter::entity::number::detection_threshold::name` | Detection threshold | Detekteringströskelvärde | Core-literal match |
| 21838 | 828242210 | `component::matter::entity::number::detection_delay::name` | Detection delay | Detekteringsfördröjning | Core-literal match |
| 21839 | 827880647 | `component::smhi::entity::sensor::precipitation_category::state::wet_snow` | Wet snow | Blötsnö | Core-literal match |
| 21840 | 827880646 | `component::smhi::entity::sensor::precipitation_category::state::thunderstorm` | Thunderstorm | Åskväder | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 828725804 | `component::victron_gx::entity::sensor::alternator_charge_current_limit::name` | Charge current limit |
| 828725803 | `component::victron_gx::entity::sensor::acsystem_mode::state::passthrough` | Passthrough |
| 828725802 | `component::victron_gx::entity::sensor::acsystem_mode::state::on` | On |
| 828725801 | `component::victron_gx::entity::sensor::acsystem_mode::state::off` | Off |
| 828725800 | `component::victron_gx::entity::sensor::acsystem_mode::state::inverter_only` | Inverter only |
| 828725799 | `component::victron_gx::entity::sensor::acsystem_mode::state::charger_only` | Charger only |
| 828725798 | `component::victron_gx::entity::sensor::acsystem_mode::name` | Mode |
| 828725775 | `component::victron_gx::config::step::ssdp_auth::data_description::username` | Username for the MQTT server, default is empty. Not needed by Victron devices. This is only needed if you route your MQTT messages through a non-Victron server and it does require a username. |
| 828725772 | `component::victron_gx::config::step::ssdp_auth::data::username` | Username |
| 828453022 | `component::anthropic::config_subentries::conversation::step::advanced::data_description::prompt_caching` | Optimize your API cost and response times based on your usage. |
| 828453021 | `component::anthropic::config_subentries::conversation::step::advanced::data::prompt_caching` | Caching strategy |
| 828453020 | `component::anthropic::config_subentries::ai_task_data::step::advanced::data_description::prompt_caching` | Optimize your API cost and response times based on your usage. |
| 828453019 | `component::anthropic::config_subentries::ai_task_data::step::advanced::data::prompt_caching` | Caching strategy |
| 828257749 | `component::fritz::issues::deprecated_cleanup_button::title` | 'Cleanup' button is deprecated |
| 828257748 | `component::fritz::issues::deprecated_cleanup_button::description` | The 'Cleanup' button is deprecated and will be removed in Home Assistant Core {removal_version}. Please update your automations and dashboards to remove any usage of this button. The action is now performed automatically at each data refresh. |
| 828244172 | `component::opendisplay::config::abort::reauth_successful` | Re-authentication was successful |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
