# Home Assistant Core – historisk avstämning 15721–15840

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 72 direkta källtexter matchar HA Core-källan; 20 referensanvändningar med 18 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 28 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 15721 | 884491710 | `component::scrape::config_subentries::entity::step::reconfigure::sections::additional::data::attribute` | Attribute | Attribut | Shared reference target checked |
| 15722 | 884491709 | `component::scrape::config::step::user::sections::additional::name` | Additional settings | Ytterligare inställningar | Core-literal match |
| 15723 | 884491708 | `component::scrape::config::step::user::sections::additional::description` | Provide additional settings for the resource. | Ange ytterligare inställningar för resursen. | Core-literal match |
| 15724 | 884491707 | `component::scrape::config::step::user::sections::additional::data_description::verify_ssl` | Enables/disables verification of SSL/TLS certificate, for example if it is self-signed. | Aktiverar/inaktiverar verifiering av SSL/TLS-certifikat, t.ex. om det är självsignerat. | Core-literal match |
| 15725 | 884491706 | `component::scrape::config::step::user::sections::additional::data_description::timeout` | Timeout for connection to website. | Timeout för anslutning till webbplats. | Core-literal match |
| 15726 | 884491705 | `component::scrape::config::step::user::sections::additional::data_description::headers` | Headers to use for the web request. | Headers att använda för webbförfrågan. | Core-literal match |
| 15727 | 884491704 | `component::scrape::config::step::user::sections::additional::data_description::encoding` | Character encoding to use. Defaults to UTF-8. | Teckenkodning att använda. Standard är UTF-8 | Core-literal match |
| 15728 | 884491703 | `component::scrape::config::step::user::sections::additional::data::verify_ssl` | Verify SSL certificate | Verifiera SSL-certifikat | Shared reference target checked |
| 15729 | 884491702 | `component::scrape::config::step::user::sections::additional::data::timeout` | Timeout | Tidsgräns | Core-literal match |
| 15730 | 884491701 | `component::scrape::config::step::user::sections::additional::data::headers` | Headers | Headers | Core-literal match |
| 15731 | 884491700 | `component::scrape::config::step::user::sections::additional::data::encoding` | Character encoding | Teckenkodning | Core-literal match |
| 15732 | 884160402 | `component::openevse::config::step::reconfigure::description` | Update the configuration for your OpenEVSE charger. | Uppdatera konfigurationen för din OpenEVSE-laddare. | Core-literal match |
| 15733 | 884160401 | `component::openevse::config::step::reconfigure::data_description::username` | The username to access your OpenEVSE charger | Användarnamnet för att komma åt din OpenEVSE-laddare | Shared reference target checked |
| 15734 | 884160400 | `component::openevse::config::step::reconfigure::data_description::password` | The password to access your OpenEVSE charger | Lösenordet för att komma åt din OpenEVSE-laddare | Shared reference target checked |
| 15735 | 884160399 | `component::openevse::config::step::reconfigure::data_description::host` | Enter the IP address of your OpenEVSE. | Ange IP-adressen för din OpenEVSE. | Core-literal match |
| 15736 | 884160398 | `component::openevse::config::step::reconfigure::data::username` | Username | Användarnamn | Shared reference target checked |
| 15737 | 884160397 | `component::openevse::config::step::reconfigure::data::password` | Password | Lösenord | Shared reference target checked |
| 15738 | 884160396 | `component::openevse::config::step::reconfigure::data::host` | Host | Värd | Shared reference target checked |
| 15739 | 884160395 | `component::openevse::config::abort::unique_id_mismatch` | The charger identifier does not match the previous identifier | Laddarens identifierare stämmer inte överens med den tidigare identifieraren | Core-literal match |
| 15740 | 884160394 | `component::openevse::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 15741 | 883934040 | `component::mastodon::services::post::fields::quoted_status::name` | Quote | Citat | Core-literal match |
| 15742 | 883934039 | `component::mastodon::services::post::fields::quoted_status::description` | The ID of the status to quote in this post. | ID-numret för den status som ska citeras i det här inlägget. | Core-literal match |
| 15743 | 883934038 | `component::mastodon::services::post::fields::in_reply_to::name` | In reply to | Som svar på | Core-literal match |
| 15744 | 883934037 | `component::mastodon::services::post::fields::in_reply_to::description` | The ID of the status to reply to. Setting this makes the new post a reply, allowing you to create or continue a thread. | ID-numret för den status som du vill svara på. Om du anger detta blir det nya inlägget ett svar, vilket gör att du kan starta eller fortsätta en tråd. | Core-literal match |
| 15745 | 883830064 | `component::steam_online::exceptions::timeout_exception::message` | Failed to connect to Steam due to a request timeout | Anslutningen till Steam misslyckades på grund av en långsam förfrågan | Core-literal match |
| 15746 | 883830063 | `component::steam_online::exceptions::request_exception::message` | Failed to connect to Steam due to a request error | Anslutningen till Steam misslyckades på grund av ett problem med förfrågan | Core-literal match |
| 15747 | 883830062 | `component::steam_online::exceptions::auth_exception::message` | Failed to connect to Steam due to an authentication error | Anslutningen till Steam misslyckades på grund av ett autentiseringsfel | Core-literal match |
| 15748 | 883188726 | `component::switchbot::entity::select::night_light::state::off` | Off | Av | Shared reference target checked |
| 15749 | 883188725 | `component::switchbot::entity::select::night_light::state::level_2` | Level 2 | Nivå 2 | Source-path follow-up open |
| 15750 | 883188724 | `component::switchbot::entity::select::night_light::state::level_1` | Level 1 | Nivå 1 | Source-path follow-up open |
| 15751 | 883188723 | `component::switchbot::entity::select::night_light::name` | Night light | Nattlampa | Core-literal match |
| 15752 | 883188722 | `component::switchbot::entity::number::vertical_oscillation_angle::name` | Vertical oscillation angle | Vertikal oscilleringsvinkel | Core-literal match |
| 15753 | 883188721 | `component::switchbot::entity::number::horizontal_oscillation_angle::name` | Horizontal oscillation angle | Horisontell oscilleringsvinkel | Core-literal match |
| 15754 | 883136096 | `component::ccm15::config::step::user::data_description::port` | The TCP port of the CCM15 controller's HTTP interface. | TCP-porten för CCM15-styrenhetens HTTP-gränssnitt. | Core-literal match |
| 15755 | 883136095 | `component::ccm15::config::step::user::data_description::host` | The hostname or IP address of your CCM15 controller. | Värdnamnet eller IP-adressen för din CCM15-styrenhet. | Core-literal match |
| 15756 | 882895932 | `component::mqtt::config::step::broker::sections::other_settings::name` | Other settings | Övriga inställningar | Core-literal match |
| 15757 | 882895931 | `component::mqtt::config::step::broker::sections::other_settings::data_description::ws_path` | The WebSocket path to be used for the connection to your MQTT broker. | Den WebSocket-sökväg som ska användas för anslutningen till din MQTT-broker. | Core-literal match |
| 15758 | 882895930 | `component::mqtt::config::step::broker::sections::other_settings::data_description::ws_headers` | The WebSocket headers to pass through the WebSocket-based connection to your MQTT broker. | De WebSocket-headers som ska skickas genom den WebSocket-baserade anslutningen till din MQTT-broker. | Core-literal match |
| 15759 | 882895929 | `component::mqtt::config::step::broker::sections::other_settings::data_description::transport` | The transport to be used for the connection to your MQTT broker. | Den transport som ska användas för anslutningen till din MQTT-broker. | Core-literal match |
| 15760 | 882895928 | `component::mqtt::config::step::broker::sections::other_settings::data_description::tls_insecure` | Option to ignore validation of your MQTT broker's certificate. | Alternativ för att ignorera validering av din MQTT-brokers certifikat. | Core-literal match |
| 15761 | 882895927 | `component::mqtt::config::step::broker::sections::other_settings::data_description::set_client_cert` | When already selected, client certificate authentication is enabled. Upload a client certificate and key to enable. | Om alternativet redan är markerat är autentisering med klientcertifikat aktiverat. Ladda upp ett klientcertifikat och en nyckel för att aktivera funktionen. | Core-literal match |
| 15762 | 882895926 | `component::mqtt::config::step::broker::sections::other_settings::data_description::set_ca_cert` | When already set to **Custom**, a custom CA validation certificate is configured. Select **Auto** for automatic CA validation, or upload a custom CA certificate, to allow validating your MQTT broker's certificate. | När inställningen redan är **Anpassad** har ett anpassat CA-valideringscertifikat konfigurerats. Välj **Auto** för automatisk CA-validering, eller ladda upp ett anpassat CA-certifikat för att möjliggöra validering av din MQTT-brokers certifikat. | Core-literal match |
| 15763 | 882895925 | `component::mqtt::config::step::broker::sections::other_settings::data_description::keepalive` | A value less than 90 seconds is advised. Defaults to 60 seconds. | Ett värde på mindre än 90 sekunder rekommenderas. Standardvärdet är 60 sekunder. | Core-literal match |
| 15764 | 882895924 | `component::mqtt::config::step::broker::sections::other_settings::data_description::client_key_password` | The password for the private key file (if set). | Lösenordet för den privata nyckelfilen (om inställt). | Core-literal match |
| 15765 | 882895923 | `component::mqtt::config::step::broker::sections::other_settings::data_description::client_key` | The private key file that belongs to your client certificate. | Den privata nyckelfil som hör till ditt klientcertifikat. | Core-literal match |
| 15766 | 882895922 | `component::mqtt::config::step::broker::sections::other_settings::data_description::client_id` | The unique ID to identify the Home Assistant MQTT API as MQTT client. It is recommended to leave this option blank. | Det unika ID:t för att identifiera Home Assistant MQTT-API:et som MQTT-klient. Vi rekommenderar att du lämnar detta alternativ tomt. | Core-literal match |
| 15767 | 882895921 | `component::mqtt::config::step::broker::sections::other_settings::data_description::client_cert` | The client certificate to authenticate against your MQTT broker. | Klientcertifikatet för att autentisera mot din MQTT-broker. | Core-literal match |
| 15768 | 882895920 | `component::mqtt::config::step::broker::sections::other_settings::data_description::certificate` | The custom CA certificate file to validate your MQTT broker's certificate. | Den anpassade CA-certifikatfilen för att validera din MQTT-brokers certifikat. | Core-literal match |
| 15769 | 882895919 | `component::mqtt::config::step::broker::sections::other_settings::data::ws_path` | WebSocket path | WebSocket-sökväg | Core-literal match |
| 15770 | 882895918 | `component::mqtt::config::step::broker::sections::other_settings::data::ws_headers` | WebSocket headers in JSON format | WebSocket-headers i JSON-format | Core-literal match |
| 15771 | 882895917 | `component::mqtt::config::step::broker::sections::other_settings::data::transport` | MQTT transport | MQTT-transport | Core-literal match |
| 15772 | 882895916 | `component::mqtt::config::step::broker::sections::other_settings::data::tls_insecure` | Ignore broker certificate validation | Ignorera validering av broker-certifikat | Core-literal match |
| 15773 | 882895915 | `component::mqtt::config::step::broker::sections::other_settings::data::set_client_cert` | Use a client certificate | Använd ett klientcertifikat | Core-literal match |
| 15774 | 882895914 | `component::mqtt::config::step::broker::sections::other_settings::data::set_ca_cert` | Broker certificate validation | Validering av broker-certifikat | Core-literal match |
| 15775 | 882895913 | `component::mqtt::config::step::broker::sections::other_settings::data::keepalive` | The time between sending keep alive messages | Tiden mellan att skicka Keep Alive-meddelanden | Core-literal match |
| 15776 | 882895912 | `component::mqtt::config::step::broker::sections::other_settings::data::client_key_password` | Password | Lösenord | Shared reference target checked |
| 15777 | 882895911 | `component::mqtt::config::step::broker::sections::other_settings::data::client_key` | Upload private key file | Ladda upp privat nyckelfil | Core-literal match |
| 15778 | 882895910 | `component::mqtt::config::step::broker::sections::other_settings::data::client_id` | Client ID (leave empty for a randomly generated one) | Klient-ID (lämna tomt för ett slumpmässigt genererat) | Core-literal match |
| 15779 | 882895909 | `component::mqtt::config::step::broker::sections::other_settings::data::client_cert` | Upload client certificate file | Ladda upp klientcertifikatfil | Core-literal match |
| 15780 | 882895908 | `component::mqtt::config::step::broker::sections::other_settings::data::certificate` | Upload custom CA certificate file | Ladda upp anpassad CA-certifikatfil | Core-literal match |
| 15781 | 882632614 | `component::autoskope::config::step::user::sections::additional_settings::name` | Additional settings | Ytterligare inställningar | Core-literal match |
| 15782 | 882632613 | `component::autoskope::config::step::user::sections::additional_settings::data_description::host` | The URL of your Autoskope API endpoint. Only change this if you use a white-label portal. | Webbadressen till Autoskope-API:ts slutpunkt. Ändra bara detta om du använder en white-label-portal. | Core-literal match |
| 15783 | 882632612 | `component::autoskope::config::step::user::sections::additional_settings::data::host` | API endpoint | API-slutpunkt | Core-literal match |
| 15784 | 882622537 | `component::telegram_bot::config::step::user::sections::additional_settings::name` | Additional settings | Ytterligare alternativ | Core-literal match |
| 15785 | 882622536 | `component::telegram_bot::config::step::user::sections::additional_settings::data_description::proxy_url` | Proxy URL if working behind one, optionally including username and password.<br>({socks_url}) | Proxy-URL, om du arbetar bakom en. Eventuellt inklusive användarnamn och lösenord.<br>({socks_url}) | Core-literal match |
| 15786 | 882622535 | `component::telegram_bot::config::step::user::sections::additional_settings::data_description::api_endpoint` | Telegram bot API server endpoint.<br>The bot will be **locked out for 10 minutes** if you switch back to the default.<br>Default: `{default_api_endpoint}`. | Slutpunkt för Telegram-botens API-server.<br>Boten kommer att **spärras i 10 minuter** om du återgår till standardinställningen.<br>Standard: `{default_api_endpoint}`. | Core-literal match |
| 15787 | 882622534 | `component::telegram_bot::config::step::user::sections::additional_settings::data::proxy_url` | Proxy URL | Proxy-URL | Core-literal match |
| 15788 | 882622533 | `component::telegram_bot::config::step::user::sections::additional_settings::data::api_endpoint` | API endpoint | API-slutpunkt | Core-literal match |
| 15789 | 882622532 | `component::telegram_bot::config::step::reconfigure::sections::additional_settings::name` | Additional settings | Ytterligare alternativ | Shared reference target checked |
| 15790 | 882622531 | `component::telegram_bot::config::step::reconfigure::sections::additional_settings::data_description::proxy_url` | Proxy URL if working behind one, optionally including username and password.<br>({socks_url}) | Proxy-URL, om du arbetar bakom en. Eventuellt inklusive användarnamn och lösenord.<br>({socks_url}) | Shared reference target checked |
| 15791 | 882622530 | `component::telegram_bot::config::step::reconfigure::sections::additional_settings::data_description::api_endpoint` | Telegram bot API server endpoint.<br>The bot will be **locked out for 10 minutes** if you switch back to the default.<br>Default: `{default_api_endpoint}`. | Slutpunkt för Telegram-botens API-server.<br>Boten kommer att **spärras i 10 minuter** om du återgår till standardinställningen.<br>Standard: `{default_api_endpoint}`. | Shared reference target checked |
| 15792 | 882622529 | `component::telegram_bot::config::step::reconfigure::sections::additional_settings::data::proxy_url` | Proxy URL | Proxy-URL | Shared reference target checked |
| 15793 | 882622528 | `component::telegram_bot::config::step::reconfigure::sections::additional_settings::data::api_endpoint` | API endpoint | API-slutpunkt | Shared reference target checked |
| 15794 | 882619134 | `component::history_stats::options::step::init::sections::additional_settings::name` | Additional settings | Ytterligare inställningar | Shared reference target checked |
| 15795 | 882619133 | `component::history_stats::options::step::init::sections::additional_settings::data_description::min_state_duration` | The minimum state duration to account for the statistics. Default is 0 seconds. | Den minsta varaktigheten för ett tillstånd som ska beaktas i statistiken. Standardvärdet är 0 sekunder. | Shared reference target checked |
| 15796 | 882619132 | `component::history_stats::options::step::init::sections::additional_settings::data::min_state_duration` | Minimum state duration | Minsta varaktighet för tillståndet | Shared reference target checked |
| 15797 | 882619131 | `component::history_stats::config::step::options::sections::additional_settings::name` | Additional settings | Ytterligare inställningar | Core-literal match |
| 15798 | 882619130 | `component::history_stats::config::step::options::sections::additional_settings::data_description::min_state_duration` | The minimum state duration to account for the statistics. Default is 0 seconds. | Den minsta varaktigheten för ett tillstånd som ska beaktas i statistiken. Standardvärdet är 0 sekunder. | Core-literal match |
| 15799 | 882619129 | `component::history_stats::config::step::options::sections::additional_settings::data::min_state_duration` | Minimum state duration | Minsta varaktighet för tillståndet | Core-literal match |
| 15800 | 882550244 | `component::dnsip::config::step::user::sections::additional_options::name` | Additional options | Ytterligare alternativ | Core-literal match |
| 15801 | 882550243 | `component::dnsip::config::step::user::sections::additional_options::description` | Optionally change resolvers and ports. | Du kan vid behov ändra resolver och portar. | Core-literal match |
| 15802 | 882550242 | `component::dnsip::config::step::user::sections::additional_options::data_description::resolver_ipv6` | Resolver used for the IPv6 lookup. | Resolver som används för IPv6-uppslagning. | Core-literal match |
| 15803 | 882550241 | `component::dnsip::config::step::user::sections::additional_options::data_description::resolver` | Resolver used for the IPv4 lookup. | Resolver som används för IPv4-uppslagning. | Core-literal match |
| 15804 | 882550240 | `component::dnsip::config::step::user::sections::additional_options::data_description::port_ipv6` | Port used for the IPv6 lookup. | Port som används för IPv6-uppslagning. | Core-literal match |
| 15805 | 882550239 | `component::dnsip::config::step::user::sections::additional_options::data_description::port` | Port used for the IPv4 lookup. | Port som används för IPv4-uppslagning. | Core-literal match |
| 15806 | 882550238 | `component::dnsip::config::step::user::sections::additional_options::data::resolver_ipv6` | IPv6 resolver | IPv6-resolver | Core-literal match |
| 15807 | 882550237 | `component::dnsip::config::step::user::sections::additional_options::data::resolver` | IPv4 resolver | IPv4-resolver | Core-literal match |
| 15808 | 882550236 | `component::dnsip::config::step::user::sections::additional_options::data::port_ipv6` | IPv6 port | IPv6-port | Core-literal match |
| 15809 | 882550235 | `component::dnsip::config::step::user::sections::additional_options::data::port` | IPv4 port | IPv4-port | Core-literal match |
| 15810 | 882549782 | `component::openai_conversation::config_subentries::conversation::step::additional::title` | Additional settings | Ytterligare inställningar | Source-path follow-up open |
| 15811 | 882549781 | `component::openai_conversation::config_subentries::conversation::step::additional::data_description::store_responses` | If enabled, requests and responses are stored by OpenAI and visible in your OpenAI dashboard logs | Om aktiverat lagras förfrågningar och svar av OpenAI och syns i dina OpenAI-kontrollpanelloggar | Source-path follow-up open |
| 15812 | 882549780 | `component::openai_conversation::config_subentries::conversation::step::additional::data::top_p` | Top P | Top P | Source-path follow-up open |
| 15813 | 882549779 | `component::openai_conversation::config_subentries::conversation::step::additional::data::temperature` | Temperature | Temperatur | Source-path follow-up open |
| 15814 | 882549778 | `component::openai_conversation::config_subentries::conversation::step::additional::data::store_responses` | Store requests and responses in OpenAI | Lagra förfrågningar och svar i OpenAI | Source-path follow-up open |
| 15815 | 882549777 | `component::openai_conversation::config_subentries::conversation::step::additional::data::max_tokens` | Maximum tokens to return in response | Maximalt antal tokens att returnera i svar | Source-path follow-up open |
| 15816 | 882549776 | `component::openai_conversation::config_subentries::conversation::step::additional::data::chat_model` | Model | Modell | Source-path follow-up open |
| 15817 | 882549775 | `component::openai_conversation::config_subentries::ai_task_data::step::additional::title` | Additional settings | Ytterligare inställningar | Source-path follow-up open |
| 15818 | 882549774 | `component::openai_conversation::config_subentries::ai_task_data::step::additional::data_description::store_responses` | If enabled, requests and responses are stored by OpenAI and visible in your OpenAI dashboard logs | Om aktiverat lagras förfrågningar och svar av OpenAI och syns i dina OpenAI-kontrollpanelloggar | Source-path follow-up open |
| 15819 | 882549773 | `component::openai_conversation::config_subentries::ai_task_data::step::additional::data::top_p` | Top P | Top P | Source-path follow-up open |
| 15820 | 882549772 | `component::openai_conversation::config_subentries::ai_task_data::step::additional::data::temperature` | Temperature | Temperatur | Source-path follow-up open |
| 15821 | 882549771 | `component::openai_conversation::config_subentries::ai_task_data::step::additional::data::store_responses` | Store requests and responses in OpenAI | Lagra förfrågningar och svar i OpenAI | Source-path follow-up open |
| 15822 | 882549770 | `component::openai_conversation::config_subentries::ai_task_data::step::additional::data::max_tokens` | Maximum tokens to return in response | Maximalt antal tokens att returnera i svar | Source-path follow-up open |
| 15823 | 882549769 | `component::openai_conversation::config_subentries::ai_task_data::step::additional::data::chat_model` | Model | Modell | Source-path follow-up open |
| 15824 | 882549768 | `component::anthropic::config_subentries::conversation::step::additional::title` | Additional settings | Ytterligare inställningar | Source-path follow-up open |
| 15825 | 882549767 | `component::anthropic::config_subentries::conversation::step::additional::data_description::prompt_caching` | Optimize your API cost and response times based on your usage. | Optimera dina API-kostnader och svarstider baserat på din användning. | Source-path follow-up open |
| 15826 | 882549766 | `component::anthropic::config_subentries::conversation::step::additional::data_description::chat_model` | The model to serve the responses. | Modellen som ska hantera svaren | Source-path follow-up open |
| 15827 | 882549765 | `component::anthropic::config_subentries::conversation::step::additional::data::prompt_caching` | Caching strategy | Cachningsstrategi | Source-path follow-up open |
| 15828 | 882549764 | `component::anthropic::config_subentries::conversation::step::additional::data::chat_model` | Model | Modell | Source-path follow-up open |
| 15829 | 882549763 | `component::anthropic::config_subentries::ai_task_data::step::additional::title` | Additional settings | Ytterligare inställningar | Source-path follow-up open |
| 15830 | 882549762 | `component::anthropic::config_subentries::ai_task_data::step::additional::data_description::prompt_caching` | Optimize your API cost and response times based on your usage. | Optimera dina API-kostnader och svarstider baserat på din användning. | Source-path follow-up open |
| 15831 | 882549761 | `component::anthropic::config_subentries::ai_task_data::step::additional::data_description::chat_model` | The model to serve the responses. | Modellen som ska hantera svaren | Source-path follow-up open |
| 15832 | 882549760 | `component::anthropic::config_subentries::ai_task_data::step::additional::data::prompt_caching` | Caching strategy | Cachningsstrategi | Source-path follow-up open |
| 15833 | 882549759 | `component::anthropic::config_subentries::ai_task_data::step::additional::data::chat_model` | Model | Modell | Source-path follow-up open |
| 15834 | 882165858 | `component::smlight::config::step::reconfigure::title` | Reconfigure SMLIGHT device | Konfigurera om SMLIGHT-enhet | Core-literal match |
| 15835 | 882165857 | `component::smlight::config::step::reconfigure::description` | Please enter the new hostname or IP address of the SMLIGHT device. | Ange det nya värdnamnet eller IP-adressen för SMLIGHT-enheten. | Core-literal match |
| 15836 | 882165856 | `component::smlight::config::step::reconfigure::data_description::host` | The hostname or IP address of the SMLIGHT SLZB device | Värdnamnet eller IP-adressen för SMLIGHT SLZB-enheten | Shared reference target checked |
| 15837 | 882165855 | `component::smlight::config::step::reconfigure::data::host` | Host | Värd | Shared reference target checked |
| 15838 | 882165854 | `component::smlight::config::abort::unique_id_mismatch` | Please ensure you reconfigure against the same device. | Se till att du konfigurerar om mot samma enhet. | Core-literal match |
| 15839 | 882165853 | `component::smlight::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 15840 | 882128588 | `component::steam_online::config::error::timeout_connect` | Timeout while establishing a connection | Tidsgränsen överskreds när anslutningen upprättades. | Shared reference target checked |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 884160394 | `component::openevse::config::abort::reconfigure_successful` | Reconfiguration was successful |
| 883188725 | `component::switchbot::entity::select::night_light::state::level_2` | Level 2 |
| 883188724 | `component::switchbot::entity::select::night_light::state::level_1` | Level 1 |
| 882549782 | `component::openai_conversation::config_subentries::conversation::step::additional::title` | Additional settings |
| 882549781 | `component::openai_conversation::config_subentries::conversation::step::additional::data_description::store_responses` | If enabled, requests and responses are stored by OpenAI and visible in your OpenAI dashboard logs |
| 882549780 | `component::openai_conversation::config_subentries::conversation::step::additional::data::top_p` | Top P |
| 882549779 | `component::openai_conversation::config_subentries::conversation::step::additional::data::temperature` | Temperature |
| 882549778 | `component::openai_conversation::config_subentries::conversation::step::additional::data::store_responses` | Store requests and responses in OpenAI |
| 882549777 | `component::openai_conversation::config_subentries::conversation::step::additional::data::max_tokens` | Maximum tokens to return in response |
| 882549776 | `component::openai_conversation::config_subentries::conversation::step::additional::data::chat_model` | Model |
| 882549775 | `component::openai_conversation::config_subentries::ai_task_data::step::additional::title` | Additional settings |
| 882549774 | `component::openai_conversation::config_subentries::ai_task_data::step::additional::data_description::store_responses` | If enabled, requests and responses are stored by OpenAI and visible in your OpenAI dashboard logs |
| 882549773 | `component::openai_conversation::config_subentries::ai_task_data::step::additional::data::top_p` | Top P |
| 882549772 | `component::openai_conversation::config_subentries::ai_task_data::step::additional::data::temperature` | Temperature |
| 882549771 | `component::openai_conversation::config_subentries::ai_task_data::step::additional::data::store_responses` | Store requests and responses in OpenAI |
| 882549770 | `component::openai_conversation::config_subentries::ai_task_data::step::additional::data::max_tokens` | Maximum tokens to return in response |
| 882549769 | `component::openai_conversation::config_subentries::ai_task_data::step::additional::data::chat_model` | Model |
| 882549768 | `component::anthropic::config_subentries::conversation::step::additional::title` | Additional settings |
| 882549767 | `component::anthropic::config_subentries::conversation::step::additional::data_description::prompt_caching` | Optimize your API cost and response times based on your usage. |
| 882549766 | `component::anthropic::config_subentries::conversation::step::additional::data_description::chat_model` | The model to serve the responses. |
| 882549765 | `component::anthropic::config_subentries::conversation::step::additional::data::prompt_caching` | Caching strategy |
| 882549764 | `component::anthropic::config_subentries::conversation::step::additional::data::chat_model` | Model |
| 882549763 | `component::anthropic::config_subentries::ai_task_data::step::additional::title` | Additional settings |
| 882549762 | `component::anthropic::config_subentries::ai_task_data::step::additional::data_description::prompt_caching` | Optimize your API cost and response times based on your usage. |
| 882549761 | `component::anthropic::config_subentries::ai_task_data::step::additional::data_description::chat_model` | The model to serve the responses. |
| 882549760 | `component::anthropic::config_subentries::ai_task_data::step::additional::data::prompt_caching` | Caching strategy |
| 882549759 | `component::anthropic::config_subentries::ai_task_data::step::additional::data::chat_model` | Model |
| 882165853 | `component::smlight::config::abort::reconfigure_successful` | Reconfiguration was successful |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
