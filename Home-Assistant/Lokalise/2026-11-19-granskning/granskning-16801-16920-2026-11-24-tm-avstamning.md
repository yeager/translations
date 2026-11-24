# Home Assistant Core – historisk avstämning 16801–16920

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 81 direkta källtexter matchar HA Core-källan; 28 referensanvändningar med 20 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 11 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 16801 | 869690082 | `component::aqvify::config::step::reauth_confirm::data_description::api_key` | Your Aqvify API key | Din Aqvify API-nyckel | Shared reference target checked |
| 16802 | 869690081 | `component::aqvify::config::step::reauth_confirm::data::api_key` | API key | API-nyckel | Shared reference target checked |
| 16803 | 869690080 | `component::aqvify::config::abort::unique_id_mismatch` | The entered API key corresponds to a different account. | Den angivna API-nyckeln motsvarar ett annat konto. | Core-literal match |
| 16804 | 869690079 | `component::aqvify::config::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | Source-path follow-up open |
| 16805 | 869676894 | `component::smtp::selector::encryption::options::tls` | SSL/TLS | SSL/TLS | Core-literal match |
| 16806 | 869676893 | `component::smtp::selector::encryption::options::starttls` | STARTTLS | STARTTLS | Core-literal match |
| 16807 | 869676892 | `component::smtp::selector::encryption::options::none` | None | Ingen | Core-literal match |
| 16808 | 869676891 | `component::smtp::issues::deprecated_yaml_import_issue_error::title` | Failed to import SMTP YAML configuration | Det gick inte att importera SMTP-konfigurationen i YAML-format | Core-literal match |
| 16809 | 869676890 | `component::smtp::issues::deprecated_yaml_import_issue_error::description` | YAML configuration for SMTP is being deprecated, but an error occurred while importing your existing configuration.<br><br>Verify that the YAML configuration is valid, then restart Home Assistant to try again. Alternatively remove the SMTP YAML configuration from your `configuration.yaml` file and continue to [set up the integration]({url}) manually.<br><br>**Configuration that could not be imported:**<br><br>```{config}``` | YAML-konfigurationen för SMTP fasas ut, men ett fel uppstod vid importen av din befintliga konfiguration.<br><br>Kontrollera att YAML-konfigurationen är giltig och starta sedan om Home Assistant för att försöka igen. Alternativt kan du ta bort SMTP-YAML-konfigurationen från din `configuration.yaml`-fil och fortsätta med att [konfigurera integrationen]({url}) manuellt.<br><br>**Konfiguration som inte kunde importeras:**<br><br>```{config}``` | Core-literal match |
| 16810 | 869676889 | `component::smtp::config_subentries::recipient::step::user::title` | Recipient | Mottagare | Core-literal match |
| 16811 | 869676888 | `component::smtp::config_subentries::recipient::step::user::description` | Set up a recipient for notifications. | Ange en mottagare för aviseringar. | Core-literal match |
| 16812 | 869676887 | `component::smtp::config_subentries::recipient::step::user::data_description::recipient` | Email address of the recipient. | Mottagarens e-postadress. | Core-literal match |
| 16813 | 869676886 | `component::smtp::config_subentries::recipient::step::user::data_description::name` | Name of the recipient | Mottagarens namn | Core-literal match |
| 16814 | 869676885 | `component::smtp::config_subentries::recipient::step::user::data::recipient` | Email | E-post | Shared reference target checked |
| 16815 | 869676884 | `component::smtp::config_subentries::recipient::step::user::data::name` | Name | Namn | Shared reference target checked |
| 16816 | 869676883 | `component::smtp::config_subentries::recipient::initiate_flow::user` | Add recipient | Lägg till mottagare | Core-literal match |
| 16817 | 869676882 | `component::smtp::config_subentries::recipient::entry_type` | Recipient | Mottagare | Core-literal match |
| 16818 | 869676881 | `component::smtp::config_subentries::recipient::abort::already_configured` | Recipient is already configured | Mottagaren är redan konfigurerad | Core-literal match |
| 16819 | 869676880 | `component::smtp::config::step::user::data_description::verify_ssl` | Enable certificate verification for secure SSL/TLS connections. | Aktivera certifikatverifiering för säkra SSL/TLS-anslutningar. | Core-literal match |
| 16820 | 869676879 | `component::smtp::config::step::user::data_description::username` | Username used to authenticate with the SMTP server. | Användarnamn som används för att autentisera sig hos SMTP-servern. | Core-literal match |
| 16821 | 869676878 | `component::smtp::config::step::user::data_description::server` | Hostname or IP address of the SMTP server. For example, `smtp.example.com`. | SMTP-serverns värdnamn eller IP-adress. Till exempel `smtp.example.com`. | Core-literal match |
| 16822 | 869676877 | `component::smtp::config::step::user::data_description::sender_name` | Display name shown as the email sender. | Det namn som visas som avsändare i e-postmeddelandet. | Core-literal match |
| 16823 | 869676876 | `component::smtp::config::step::user::data_description::sender` | Email address that will appear in the From field. | E-postadress som kommer att visas i fältet ”Från”. | Core-literal match |
| 16824 | 869676875 | `component::smtp::config::step::user::data_description::port` | Port number used by your SMTP server. Common values are `587` (STARTTLS) and `465` (TLS). | Portnummer som används av din SMTP-server. Vanliga värden är `587` (STARTTLS) och `465` (TLS). | Core-literal match |
| 16825 | 869676874 | `component::smtp::config::step::user::data_description::password` | Password or app-specific password for the SMTP account. | Lösenord eller appspecifikt lösenord för SMTP-kontot. | Core-literal match |
| 16826 | 869676873 | `component::smtp::config::step::user::data_description::encryption` | Encryption method used for the SMTP connection. **STARTTLS** upgrades a plain connection to encrypted (recommended). **SSL/TLS** uses encryption from the start. **None** sends without encryption. | Krypteringsmetod som används för SMTP-anslutningen. **STARTTLS** uppgraderar en okrypterad anslutning till en krypterad (rekommenderas). **SSL/TLS** använder kryptering från början. **Ingen** skickar utan kryptering. | Core-literal match |
| 16827 | 869676872 | `component::smtp::config::step::user::data::verify_ssl` | Verify SSL certificate | Verifiera SSL-certifikat | Shared reference target checked |
| 16828 | 869676871 | `component::smtp::config::step::user::data::username` | Username | Användarnamn | Shared reference target checked |
| 16829 | 869676870 | `component::smtp::config::step::user::data::server` | Host | Värd | Shared reference target checked |
| 16830 | 869676869 | `component::smtp::config::step::user::data::sender_name` | Sender name | Avsändarens namn | Core-literal match |
| 16831 | 869676868 | `component::smtp::config::step::user::data::sender` | Sender email | Avsändarens e-postadress | Core-literal match |
| 16832 | 869676867 | `component::smtp::config::step::user::data::port` | Port | Port | Shared reference target checked |
| 16833 | 869676866 | `component::smtp::config::step::user::data::password` | Password | Lösenord | Shared reference target checked |
| 16834 | 869676865 | `component::smtp::config::step::user::data::encryption` | Connection security | Anslutningssäkerhet | Core-literal match |
| 16835 | 869676864 | `component::smtp::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 16836 | 869676863 | `component::smtp::config::error::invalid_cert` | Invalid certificate | Ogiltigt certifikat | Source-path follow-up open |
| 16837 | 869676862 | `component::smtp::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 16838 | 869676861 | `component::smtp::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 16839 | 869676860 | `component::smtp::config::abort::already_configured` | Service is already configured | Tjänsten är redan konfigurerad | Shared reference target checked |
| 16840 | 869618586 | `component::yoto::exceptions::authentication_failed::message` | Yoto credentials are no longer valid. Please reauthenticate your account. | Dina Yoto-inloggningsuppgifter är inte längre giltiga. Vänligen logga in på ditt konto på nytt. | Core-literal match |
| 16841 | 869618585 | `component::yoto::config::step::reauth_confirm::title` | Authentication expired for {name} | Autentiseringen har upphört att gälla för {name} | Shared reference target checked |
| 16842 | 869618584 | `component::yoto::config::step::reauth_confirm::description` | The Yoto integration needs to re-authenticate your account. | Yoto-integrationen behöver autentisera ditt konto på nytt. | Core-literal match |
| 16843 | 869618583 | `component::yoto::config::abort::unique_id_mismatch` | The reauthorized account does not match the original Yoto account. Please log in with the same account. | Det omauktoriserade kontot matchar inte det ursprungliga Yoto-kontot. Vänligen logga in med samma konto. | Core-literal match |
| 16844 | 869618582 | `component::yoto::config::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | Source-path follow-up open |
| 16845 | 869121040 | `component::data_grand_lyon::config_subentries::stop::step::user::data_description::stop_id` | Search by stop name, address or city, or enter a stop ID directly. | Sök efter hållplatsnamn, adress eller ort, eller ange ett hållplats-ID direkt. | Core-literal match |
| 16846 | 869121039 | `component::data_grand_lyon::config_subentries::stop::step::pick_line::data::line` | Line | Linje | Core-literal match |
| 16847 | 869121038 | `component::data_grand_lyon::config_subentries::stop::error::invalid_stop_id` | Stop ID must be a number. | Hållplats-ID måste vara ett nummer. | Core-literal match |
| 16848 | 869121037 | `component::data_grand_lyon::config_subentries::stop::abort::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 16849 | 869121036 | `component::data_grand_lyon::config_subentries::stop::abort::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 16850 | 869121035 | `component::data_grand_lyon::config_subentries::stop::abort::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 16851 | 869056061 | `component::environment_canada::services::get_alerts::name` | Get alerts | Hämta varningar | Core-literal match |
| 16852 | 869056060 | `component::environment_canada::services::get_alerts::fields::config_entry_id::name` | Environment Canada service | Environment Canada-tjänst | Core-literal match |
| 16853 | 869056059 | `component::environment_canada::services::get_alerts::fields::config_entry_id::description` | The Environment Canada service to retrieve alerts from. | Den tjänst hos Environment Canada som varningar ska hämtas från. | Core-literal match |
| 16854 | 869056058 | `component::environment_canada::services::get_alerts::description` | Retrieves the alerts from the selected weather service. | Hämtar varningarna från den valda vädertjänsten. | Core-literal match |
| 16855 | 869056057 | `component::environment_canada::exceptions::not_connected::message` | Environment Canada is not connected | Environment Canada är inte anslutet | Core-literal match |
| 16856 | 869001313 | `component::aqvify::entity::sensor::water_level::name` | Water level | Vattennivå | Source-path follow-up open |
| 16857 | 869001312 | `component::aqvify::entity::sensor::meter_value::name` | Meter value | Mätarvärde | Source-path follow-up open |
| 16858 | 869001311 | `component::aqvify::config::step::user::description` | Navigate to your [Aqvify account]({aqvify_url}), copy your API key, and paste it below. | Gå till ditt [Aqvify-konto]({aqvify_url}), kopiera din API-nyckel och klistra in den nedan. | Core-literal match |
| 16859 | 869001310 | `component::aqvify::config::step::user::data_description::api_key` | Your Aqvify API key | Din Aqvify API-nyckel | Core-literal match |
| 16860 | 869001309 | `component::aqvify::config::step::user::data::api_key` | API key | API-nyckel | Shared reference target checked |
| 16861 | 869001308 | `component::aqvify::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 16862 | 869001307 | `component::aqvify::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 16863 | 869001306 | `component::aqvify::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 16864 | 869001305 | `component::aqvify::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 16865 | 869000761 | `component::kiosker::services::set_blackout::name` | Set blackout | Aktivera mörkläggningsläge | Core-literal match |
| 16866 | 869000760 | `component::kiosker::services::set_blackout::fields::visible::name` | Visible | Synlig | Core-literal match |
| 16867 | 869000759 | `component::kiosker::services::set_blackout::fields::visible::description` | Whether the blackout is visible | Anger om mörkläggningsläget är synligt | Core-literal match |
| 16868 | 869000758 | `component::kiosker::services::set_blackout::fields::text::name` | Text | Text | Core-literal match |
| 16869 | 869000757 | `component::kiosker::services::set_blackout::fields::text::description` | Text to display on blackout screen | Text som ska visas på mörkläggningsskärmen | Core-literal match |
| 16870 | 869000756 | `component::kiosker::services::set_blackout::fields::sound::name` | Sound | Ljud | Core-literal match |
| 16871 | 869000755 | `component::kiosker::services::set_blackout::fields::sound::description` | Sound to play when blackout is displayed (SystemSoundID, e.g., 1007) | Ljud som ska spelas upp när skärmen slocknar (SystemSoundID, t.ex. 1007) | Core-literal match |
| 16872 | 869000754 | `component::kiosker::services::set_blackout::fields::icon::name` | Icon | Ikon | Core-literal match |
| 16873 | 869000753 | `component::kiosker::services::set_blackout::fields::icon::description` | Icon to display (SF Symbols name) | Ikon som ska visas (namn enligt SF Symbols) | Core-literal match |
| 16874 | 869000752 | `component::kiosker::services::set_blackout::fields::foreground::name` | Foreground color | Förgrundsfärg | Core-literal match |
| 16875 | 869000751 | `component::kiosker::services::set_blackout::fields::foreground::description` | Text color in rgb format | Textfärg i rgb-format | Core-literal match |
| 16876 | 869000750 | `component::kiosker::services::set_blackout::fields::expire::name` | Expire time | Utgångstid | Core-literal match |
| 16877 | 869000749 | `component::kiosker::services::set_blackout::fields::expire::description` | Time in seconds before the blackout expires | Tid i sekunder innan mörkläggningsläget upphör | Core-literal match |
| 16878 | 869000748 | `component::kiosker::services::set_blackout::fields::dismissible::name` | Dismissible | Kan avfärdas | Core-literal match |
| 16879 | 869000747 | `component::kiosker::services::set_blackout::fields::dismissible::description` | Whether the blackout can be dismissed by user interaction | Om mörkläggningsläget kan avfärdas genom användarinteraktion | Core-literal match |
| 16880 | 869000746 | `component::kiosker::services::set_blackout::fields::device_id::name` | Device | Enhet | Core-literal match |
| 16881 | 869000745 | `component::kiosker::services::set_blackout::fields::device_id::description` | The Kiosker device to control | Kiosker-enheten som ska styras | Core-literal match |
| 16882 | 869000744 | `component::kiosker::services::set_blackout::fields::button_text::name` | Button text | Text för knapp | Core-literal match |
| 16883 | 869000743 | `component::kiosker::services::set_blackout::fields::button_text::description` | Text to display on the dismiss button | Text som ska visas på avfärdaknapp | Core-literal match |
| 16884 | 869000742 | `component::kiosker::services::set_blackout::fields::button_foreground::name` | Button foreground color | Förgrundsfärg för knapp | Core-literal match |
| 16885 | 869000741 | `component::kiosker::services::set_blackout::fields::button_foreground::description` | Text color of the dismiss button in rgb format | Textfärgen på avfärdaknapp i rgb-format | Core-literal match |
| 16886 | 869000740 | `component::kiosker::services::set_blackout::fields::button_background::name` | Button background color | Bakgrundsfärg för knapp | Core-literal match |
| 16887 | 869000739 | `component::kiosker::services::set_blackout::fields::button_background::description` | Background color of the dismiss button in rgb format | Bakgrundsfärg för avfärdaknapp i rgb-format | Core-literal match |
| 16888 | 869000738 | `component::kiosker::services::set_blackout::fields::background::name` | Background color | Bakgrundsfärg | Core-literal match |
| 16889 | 869000737 | `component::kiosker::services::set_blackout::fields::background::description` | Background color in rgb format | Bakgrundsfärg i rgb-format | Core-literal match |
| 16890 | 869000736 | `component::kiosker::services::set_blackout::description` | Set blackout screen with custom message | Visa mörkläggningsskärm med anpassat meddelande | Core-literal match |
| 16891 | 869000735 | `component::kiosker::services::navigate_url::name` | Navigate to URL | Navigera till URL | Core-literal match |
| 16892 | 869000734 | `component::kiosker::services::navigate_url::fields::url::name` | URL | URL | Core-literal match |
| 16893 | 869000733 | `component::kiosker::services::navigate_url::fields::url::description` | The URL to navigate to | URL att navigera till | Core-literal match |
| 16894 | 869000732 | `component::kiosker::services::navigate_url::fields::device_id::name` | Device | Enhet | Core-literal match |
| 16895 | 869000731 | `component::kiosker::services::navigate_url::fields::device_id::description` | The Kiosker device to control | Kiosker-enheten som ska styras | Core-literal match |
| 16896 | 869000730 | `component::kiosker::services::navigate_url::description` | Navigate to a specific URL | Navigera till en specifik URL | Core-literal match |
| 16897 | 868850492 | `component::ovhcloud_ai_endpoints::config_subentries::conversation::step::reconfigure::description` | Update the instructions and the tools for this conversation agent. Create a new conversation agent to use a different model. | Uppdatera prompten och Home Assistant LLM-API:erna för denna konversationsagent. Skapa en ny konversationsagent för att använda en annan modell. | Core-literal match |
| 16898 | 868850491 | `component::ovhcloud_ai_endpoints::config_subentries::conversation::step::reconfigure::data_description::prompt` | Instruct how the LLM should respond. This can be a template. | Instruera hur LLM:en ska svara. Detta kan vara en mall. | Shared reference target checked |
| 16899 | 868850490 | `component::ovhcloud_ai_endpoints::config_subentries::conversation::step::reconfigure::data_description::llm_hass_api` | **Device control** only accesses the entities you expose to voice assistants. **Home Assistant** accesses everything and only works for administrators, not voice assistant devices. | **Enhetsstyrning** har endast åtkomst till de entiteter som du exponerar för röstassistenter. **Home Assistant** har åtkomst till allt och fungerar endast för administratörer, inte för röstassistentenheter. | Shared reference target checked |
| 16900 | 868850489 | `component::ovhcloud_ai_endpoints::config_subentries::conversation::step::reconfigure::data::prompt` | Instructions | Instruktioner | Shared reference target checked |
| 16901 | 868850488 | `component::ovhcloud_ai_endpoints::config_subentries::conversation::step::reconfigure::data::llm_hass_api` | AI tools | AI-verktyg | Shared reference target checked |
| 16902 | 868850487 | `component::ovhcloud_ai_endpoints::config_subentries::conversation::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 16903 | 868850486 | `component::ovhcloud_ai_endpoints::config::step::reconfigure::description` | Update the API key used to authenticate with OVHcloud AI Endpoints. | Uppdatera API-nyckeln som används för autentisering med OVHcloud AI Endpoints. | Core-literal match |
| 16904 | 868850485 | `component::ovhcloud_ai_endpoints::config::step::reconfigure::data_description::api_key` | An OVHcloud AI Endpoints API key | En API-nyckel för OVHcloud AI Endpoints | Shared reference target checked |
| 16905 | 868850484 | `component::ovhcloud_ai_endpoints::config::step::reconfigure::data::api_key` | API key | API-nyckel | Shared reference target checked |
| 16906 | 868850483 | `component::ovhcloud_ai_endpoints::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 16907 | 868829774 | `component::hypontech::entity::sensor::total_power::name` | Total power | Total effekt | Core-literal match |
| 16908 | 868829773 | `component::hypontech::entity::sensor::pv_power::name` | PV power | Solceller effekt | Core-literal match |
| 16909 | 868829772 | `component::hypontech::entity::sensor::load_power::name` | Load power | Last effekt | Core-literal match |
| 16910 | 868829771 | `component::hypontech::entity::sensor::grid_power::name` | Grid power | Elnätets effekt | Core-literal match |
| 16911 | 868829770 | `component::hypontech::entity::sensor::battery_state_of_charge::name` | Battery state of charge | Batteriets laddningstillstånd | Core-literal match |
| 16912 | 868829769 | `component::hypontech::entity::sensor::battery_power::name` | Battery power | Batterieffekt | Core-literal match |
| 16913 | 868771002 | `component::v2c::issues::deprecated_sensor_scripts::title` | Deprecated sensor detected | Föråldrad sensor upptäckt | Source-path follow-up open |
| 16914 | 868771001 | `component::v2c::issues::deprecated_sensor_scripts::description` | The sensor {entity_name} (`{entity_id}`) is deprecated because it has been replaced with `{replacement_entity_id}`.<br><br>The sensor was used in the following automations or scripts:<br>{items}<br><br>Update the above automations or scripts to use the replacement entity, then disable the deprecated sensor to have it removed after the next restart. | Sensorn {entity_name} (`{entity_id}`) är utfasad eftersom den har ersatts med `{replacement_entity_id}`. <br><br>Sensorn användes i följande automatiseringar eller skript:<br>{items}<br><br>Uppdatera ovanstående automatiseringar eller skript så att de använder ersättningsenheten, inaktivera sedan den utfasade sensorn så att den tas bort efter nästa omstart. | Source-path follow-up open |
| 16915 | 868771000 | `component::v2c::issues::deprecated_sensor::title` | Deprecated sensor detected | Föråldrad sensor upptäckt | Source-path follow-up open |
| 16916 | 868770999 | `component::v2c::issues::deprecated_sensor::description` | The sensor {entity_name} (`{entity_id}`) is deprecated because it has been replaced with `{replacement_entity_id}`.<br><br>Update your dashboards, templates, automations and scripts to use the replacement entity, then disable the deprecated sensor to have it removed after the next restart. | Sensorn {entity_name} (`{entity_id}`) är utfasad eftersom den har ersatts med `{replacement_entity_id}`. <br><br>Uppdatera dina instrumentpaneler, mallar, automatiseringar och skript så att de använder den ersättande enheten och inaktivera sedan den utfasade sensorn så att den tas bort efter nästa omstart. | Source-path follow-up open |
| 16917 | 868770998 | `component::v2c::entity::number::voltage_installation::name` | Installation voltage | Installationsspänning | Core-literal match |
| 16918 | 868277648 | `component::kiosker::entity::button::blackout_clear::name` | Clear blackout | Avsluta mörkläggningsläge | Core-literal match |
| 16919 | 868201668 | `component::yoto::exceptions::unknown_group::message` | Unknown Yoto group: {group_id} | Okänd Yoto-grupp: {group_id} | Core-literal match |
| 16920 | 868110390 | `component::roborock::selector::region::options::custom` | Manual | Manuell | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 869690079 | `component::aqvify::config::abort::reauth_successful` | Re-authentication was successful |
| 869676863 | `component::smtp::config::error::invalid_cert` | Invalid certificate |
| 869618582 | `component::yoto::config::abort::reauth_successful` | Re-authentication was successful |
| 869001313 | `component::aqvify::entity::sensor::water_level::name` | Water level |
| 869001312 | `component::aqvify::entity::sensor::meter_value::name` | Meter value |
| 868850487 | `component::ovhcloud_ai_endpoints::config_subentries::conversation::abort::reconfigure_successful` | Reconfiguration was successful |
| 868850483 | `component::ovhcloud_ai_endpoints::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 868771002 | `component::v2c::issues::deprecated_sensor_scripts::title` | Deprecated sensor detected |
| 868771001 | `component::v2c::issues::deprecated_sensor_scripts::description` | The sensor {entity_name} (`{entity_id}`) is deprecated because it has been replaced with `{replacement_entity_id}`.

The sensor was used in the following automations or scripts:
{items}

Update the above automations or scripts to use the replacement entity, then disable the deprecated sensor to have it removed after the next restart. |
| 868771000 | `component::v2c::issues::deprecated_sensor::title` | Deprecated sensor detected |
| 868770999 | `component::v2c::issues::deprecated_sensor::description` | The sensor {entity_name} (`{entity_id}`) is deprecated because it has been replaced with `{replacement_entity_id}`.

Update your dashboards, templates, automations and scripts to use the replacement entity, then disable the deprecated sensor to have it removed after the next restart. |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
