# Home Assistant Core – historisk avstämning 13681–13800

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 100 direkta källtexter matchar HA Core-källan; 17 referensanvändningar med 14 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 3 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 13681 | 906108238 | `component::bthome::entity::event::command_numbered::state_attributes::event_type::state::off` | Off | Av | Shared reference target checked |
| 13682 | 906108237 | `component::bthome::entity::event::command_numbered::name` | Command {number} | Kommando {number} | Core-literal match |
| 13683 | 906108236 | `component::bthome::entity::event::command::name` | Command | Kommando | Core-literal match |
| 13684 | 906108235 | `component::bthome::entity::event::button_numbered::state_attributes::event_type::state::triple_press` | Triple press | Trippeltryck | Shared reference target checked |
| 13685 | 906108234 | `component::bthome::entity::event::button_numbered::state_attributes::event_type::state::press` | Press | Tryck | Shared reference target checked |
| 13686 | 906108233 | `component::bthome::entity::event::button_numbered::state_attributes::event_type::state::long_triple_press` | Long triple press | Långt trippeltryck | Shared reference target checked |
| 13687 | 906108232 | `component::bthome::entity::event::button_numbered::state_attributes::event_type::state::long_press` | Long press | Lång tryckning | Shared reference target checked |
| 13688 | 906108231 | `component::bthome::entity::event::button_numbered::state_attributes::event_type::state::long_double_press` | Long double press | Långt dubbeltryck | Shared reference target checked |
| 13689 | 906108230 | `component::bthome::entity::event::button_numbered::state_attributes::event_type::state::hold_press` | Hold press | Håll nedtryckt | Shared reference target checked |
| 13690 | 906108229 | `component::bthome::entity::event::button_numbered::state_attributes::event_type::state::double_press` | Double press | Dubbeltryck | Shared reference target checked |
| 13691 | 906108228 | `component::bthome::entity::event::button_numbered::name` | Button {number} | Knapp {number} | Core-literal match |
| 13692 | 906108227 | `component::bthome::entity::event::button::name` | Button | Knapp | Source-path follow-up open |
| 13693 | 906051697 | `component::ai_task::title` | AI task | AI-uppgift | Core-literal match |
| 13694 | 905967706 | `component::hue::entity::binary_sensor::entertainment_area::name` | Entertainment area {area_name} | Underhållningsområde {area_name} | Core-literal match |
| 13695 | 905956408 | `component::actron_air::entity::binary_sensor::defrost_mode::name` | Defrost mode | Avfrostningsläge | Core-literal match |
| 13696 | 905956407 | `component::actron_air::entity::binary_sensor::clean_filter::name` | Clean filter | Rengör filter | Core-literal match |
| 13697 | 905944784 | `component::spotify::config::abort::already_configured` | Account is already configured | Kontot är redan konfigurerat | Shared reference target checked |
| 13698 | 905803362 | `component::mikrotik::entity::select::poe_out::state::off` | Off | Av | Shared reference target checked |
| 13699 | 905803361 | `component::mikrotik::entity::select::poe_out::state::forced_on` | On (forced) | På (tvingad) | Core-literal match |
| 13700 | 905803360 | `component::mikrotik::entity::select::poe_out::state::auto_on` | On (automatic) | På (automatisk) | Core-literal match |
| 13701 | 905803359 | `component::mikrotik::entity::select::poe_out::name` | PoE (out) | PoE (ut) | Core-literal match |
| 13702 | 905765975 | `component::actron_air::entity::sensor::outdoor_temperature::name` | Outdoor temperature | Utomhustemperatur | Core-literal match |
| 13703 | 905765974 | `component::actron_air::entity::sensor::fan_speed::name` | Fan speed | Fläkthastighet | Core-literal match |
| 13704 | 905765973 | `component::actron_air::entity::sensor::compressor_speed::name` | Compressor speed | Kompressorhastighet | Core-literal match |
| 13705 | 905765972 | `component::actron_air::entity::sensor::compressor_power::name` | Compressor power | Kompressoreffekt | Core-literal match |
| 13706 | 905765971 | `component::actron_air::entity::sensor::compressor_mode::state::off` | Off | Av | Shared reference target checked |
| 13707 | 905765970 | `component::actron_air::entity::sensor::compressor_mode::state::heat` | Heat | Värme | Core-literal match |
| 13708 | 905765969 | `component::actron_air::entity::sensor::compressor_mode::state::cool` | Cool | Kyla | Core-literal match |
| 13709 | 905765968 | `component::actron_air::entity::sensor::compressor_mode::name` | Compressor mode | Kompressorläge | Core-literal match |
| 13710 | 905765967 | `component::actron_air::entity::sensor::compressor_live_temperature::name` | Compressor live temperature | Kompressorns aktuella temperatur | Core-literal match |
| 13711 | 905765966 | `component::actron_air::entity::sensor::compressor_chasing_temperature::name` | Compressor chasing temperature | Kompressorns inställda temperatur | Core-literal match |
| 13712 | 905765965 | `component::actron_air::entity::sensor::compressor_capacity::name` | Compressor capacity | Kompressorkapacitet | Core-literal match |
| 13713 | 905742548 | `component::neopool::options::step::init::title` | NeoPool settings | NeoPool-inställningar | Core-literal match |
| 13714 | 905742547 | `component::neopool::options::step::init::description` | Changes take effect immediately and reload the integration. | Ändringarna träder i kraft omedelbart och integrationen laddas om. | Core-literal match |
| 13715 | 905742546 | `component::neopool::options::step::init::data_description::use_light` | Creates entities to control and monitor the pool light relay. | Skapar entiteter för att styra och övervaka reläet till poolbelysningen. | Core-literal match |
| 13716 | 905742545 | `component::neopool::options::step::init::data::use_light` | Enable pool light relay | Aktivera poolbelysningens relä | Core-literal match |
| 13717 | 905742544 | `component::neopool::exceptions::relay_in_auto_mode::message` | This relay is currently in automatic mode. Change the mode to manual first to control it directly. | Reläet är för närvarande inställt på automatiskt läge. Byt först till manuellt läge för att kunna styra det direkt. | Core-literal match |
| 13718 | 905742543 | `component::neopool::entity::light::light::name` | Pool light | Poolbelysning | Core-literal match |
| 13719 | 905590371 | `component::togrill::entity::button::silence::name` | Silence alarm | Tysta larm | Core-literal match |
| 13720 | 905336353 | `component::webostv::entity::switch::screen::name` | Screen | Skärm | Core-literal match |
| 13721 | 904893608 | `component::mikrotik::entity::switch::wlan::name` | WLAN | WLAN | Core-literal match |
| 13722 | 904893607 | `component::mikrotik::entity::switch::ether::name` | Ethernet | Ethernet | Core-literal match |
| 13723 | 904185454 | `component::coolmaster::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 13724 | 904128427 | `component::uptime_kuma::entity::sensor::type::state::pm2` | PM2 Process | PM2-process | Core-literal match |
| 13725 | 904128426 | `component::uptime_kuma::entity::sensor::type::state::ntp` | NTP | NTP | Core-literal match |
| 13726 | 904117127 | `component::music_assistant::services::get_library::fields::username::name` | Username | Användarnamn | Core-literal match |
| 13727 | 904117126 | `component::music_assistant::services::get_library::fields::username::description` | Music Assistant username used for this request. Providing the username will respect the user's configured provider filters. | Det Music Assistant-användarnamn som ska användas för denna begäran. Om användarnamnet anges kommer användarens konfigurerade leverantörsfilter att respekteras. | Core-literal match |
| 13728 | 904111441 | `component::reolink::entity::time::floodlight_schedule_start::name` | Floodlight schedule start | Starttid för strålkastarens schema | Core-literal match |
| 13729 | 904111440 | `component::reolink::entity::time::floodlight_schedule_end::name` | Floodlight schedule end | Sluttid för strålkastarens schema | Core-literal match |
| 13730 | 904111183 | `component::togrill::entity::number::timer::name` | Timer | Timer | Core-literal match |
| 13731 | 904042987 | `component::compit::entity::binary_sensor::mixer_pump_status::name` | Mixer pump | Blandarpump | Core-literal match |
| 13732 | 904042986 | `component::compit::entity::binary_sensor::ground_heat_exchanger_attached::name` | Ground heat exchanger attached | Markvärmeväxlare ansluten | Core-literal match |
| 13733 | 904006934 | `component::loqed::config::step::pick_lock::description` | Multiple locks found. Please select the lock you want to configure. | Flera lås hittades. Välj det lås du vill konfigurera. | Core-literal match |
| 13734 | 904006933 | `component::loqed::config::step::pick_lock::data::lock_id` | Select your lock | Välj ditt lås | Core-literal match |
| 13735 | 904006932 | `component::loqed::config::error::no_locks` | No locks found in your LOQED account. | Inga lås hittades i ditt LOQED-konto. | Core-literal match |
| 13736 | 904006931 | `component::google_generative_ai_conversation::selector::thinking_level::options::minimal` | Minimal | Lägsta | Core-literal match |
| 13737 | 904006930 | `component::google_generative_ai_conversation::selector::thinking_level::options::medium` | Medium | Medel | Core-literal match |
| 13738 | 904006929 | `component::google_generative_ai_conversation::selector::thinking_level::options::low` | Low | Låg | Core-literal match |
| 13739 | 904006928 | `component::google_generative_ai_conversation::selector::thinking_level::options::high` | High | Hög | Core-literal match |
| 13740 | 904006927 | `component::google_generative_ai_conversation::selector::thinking_level::options::auto` | Auto | Auto | Core-literal match |
| 13741 | 904006926 | `component::google_generative_ai_conversation::config_subentries::stt::step::set_options::data::thinking_level` | Thinking level | Tankenivå | Shared reference target checked |
| 13742 | 904006925 | `component::google_generative_ai_conversation::config_subentries::stt::step::set_options::data::thinking_budget` | Thinking budget | Resonemangsbudget | Shared reference target checked |
| 13743 | 904006924 | `component::google_generative_ai_conversation::config_subentries::conversation::step::set_options::data_description::thinking_level` | Thinking level for Gemini 3 and later text models, including the latest aliases. Unsupported levels use the model default; the saved choice is kept. Gemini 2.5 uses the thinking budget instead. "Minimal" does not guarantee that thinking is off. | Tankenivå för textmodeller från Gemini 3 och senare, inklusive alias för de senaste modellerna. Om nivån inte stöds används modellens standardnivå, men ditt val sparas. Gemini 2.5 använder tankebudgeten i stället. ”Lägsta” garanterar inte att tänkandet är avstängt. | Core-literal match |
| 13744 | 904006923 | `component::google_generative_ai_conversation::config_subentries::conversation::step::set_options::data_description::thinking_budget` | Token budget for model reasoning (Gemini 2.5 only). Use -1 for automatic or 0 to disable (not available for Gemini 2.5 Pro). | Tokenbudget för modellresonemang (endast Gemini 2.5). Använd -1 för automatiskt eller 0 för att inaktivera (ej tillgängligt för Gemini 2.5 Pro). | Core-literal match |
| 13745 | 904006922 | `component::google_generative_ai_conversation::config_subentries::conversation::step::set_options::data::thinking_level` | Thinking level | Tankenivå | Core-literal match |
| 13746 | 904006921 | `component::google_generative_ai_conversation::config_subentries::conversation::step::set_options::data::thinking_budget` | Thinking budget | Resonemangsbudget | Core-literal match |
| 13747 | 904006920 | `component::google_generative_ai_conversation::config_subentries::ai_task_data::step::set_options::data::thinking_level` | Thinking level | Tankenivå | Shared reference target checked |
| 13748 | 904006919 | `component::google_generative_ai_conversation::config_subentries::ai_task_data::step::set_options::data::thinking_budget` | Thinking budget | Resonemangsbudget | Shared reference target checked |
| 13749 | 903873938 | `component::green_planet_energy::services::get_prices::name` | Get energy prices | Hämta energipriser | Core-literal match |
| 13750 | 903873937 | `component::green_planet_energy::services::get_prices::fields::hours::name` | Hours | Timmar | Core-literal match |
| 13751 | 903873936 | `component::green_planet_energy::services::get_prices::fields::hours::description` | How many hours of price data to return, starting from the current 15-minute slot. Minimum 0.25, maximum 24. | Antal timmar med prisdata som ska returneras, med början i det aktuella 15-minutersintervallet. Minst 0,25 och högst 24. | Core-literal match |
| 13752 | 903873935 | `component::green_planet_energy::services::get_prices::fields::config_entry_id::name` | Config entry | Konfigurationspost | Core-literal match |
| 13753 | 903873934 | `component::green_planet_energy::services::get_prices::fields::config_entry_id::description` | The Green Planet Energy integration instance to use. | Den Green Planet Energy-integrationsinstans som ska användas. | Core-literal match |
| 13754 | 903873933 | `component::green_planet_energy::services::get_prices::description` | Returns raw 15-minute electricity price slots for the next N hours. Slots beyond the API horizon are omitted. | Returnerar obearbetade 15-minutersintervaller för elpriset för de kommande N timmarna. Intervaller som ligger utanför API:ets tidshorisont utelämnas. | Core-literal match |
| 13755 | 903495621 | `component::teslemetry::entity::binary_sensor::climate_state_is_rear_defroster_on::name` | Rear defroster | Bakrutevärme | Core-literal match |
| 13756 | 903354202 | `component::music_assistant::services::search::fields::username::name` | Username | Användarnamn | Core-literal match |
| 13757 | 903354201 | `component::music_assistant::services::search::fields::username::description` | Music Assistant username used for searching. Searches respect the user's configured provider filters. Defaults to the Music Assistant user linked to the Home Assistant user making the request. If there is no linked user, the request runs as the default account. | Music Assistant-användarnamnet som ska användas för sökningen. Sökningar följer användarens konfigurerade leverantörsfilter. Som standard används den Music Assistant-användare som är kopplad till Home Assistant-användaren som gör begäran. Om ingen användare är kopplad används standardkontot. | Core-literal match |
| 13758 | 903288607 | `component::ecovacs::config::step::reauth_confirm::description` | Enter the Ecovacs password for {username} to reconnect the integration. | Ange Ecovacs-lösenordet för {username} för att återansluta integrationen. | Core-literal match |
| 13759 | 903288606 | `component::ecovacs::config::step::reauth_confirm::data::password` | Password | Lösenord | Shared reference target checked |
| 13760 | 903288605 | `component::ecovacs::config::step::device_verification::description` | Enter the verification code Ecovacs sent to {username} to confirm Home Assistant as a trusted device. | Ange verifieringskoden som Ecovacs har skickat till {username} för att bekräfta Home Assistant som en betrodd enhet. | Core-literal match |
| 13761 | 903288604 | `component::ecovacs::config::step::device_verification::data::verification_code` | Verification code | Verifieringskod | Core-literal match |
| 13762 | 903288603 | `component::ecovacs::config::error::invalid_verification_code` | The verification code is invalid or has expired. | Verifieringskoden är ogiltig eller har gått ut. | Core-literal match |
| 13763 | 903288602 | `component::ecovacs::config::abort::reauth_successful` | Re-authentication was successful | Återautentisering lyckades | Source-path follow-up open |
| 13764 | 903135461 | `component::switchbot::entity::select::night_light::state::soft` | Soft | Mjuk | Core-literal match |
| 13765 | 903135460 | `component::switchbot::entity::select::night_light::state::bright` | Bright | Ljus | Core-literal match |
| 13766 | 903003257 | `component::casper_glow::config::abort::not_supported` | Device not supported | Enheten stöds inte | Core-literal match |
| 13767 | 902976494 | `component::webostv::exceptions::device_unavailable::message` | Device {device} is unavailable | Enheten {device} är inte tillgänglig | Source-path follow-up open |
| 13768 | 902566664 | `component::vizio::exceptions::update_failed::message` | Unable to connect to {host} | Det går inte att ansluta till {host} | Core-literal match |
| 13769 | 902446541 | `component::backup::entity::sensor::backup_manager_state::state::blocked` | Blocked | Blockerad | Core-literal match |
| 13770 | 902423604 | `component::fish_audio::config_subentries::tts::step::model::data_description::speed` | Speed of the generated speech. 1.0 is the normal speed; lower values speak slower and higher values speak faster. | Hastigheten på det genererade talet. 1,0 är normal hastighet. Lägre värden ger långsammare tal och högre värden ger snabbare tal. | Core-literal match |
| 13771 | 902423603 | `component::fish_audio::config_subentries::tts::step::model::data::speed` | Speech speed | Talhastighet | Core-literal match |
| 13772 | 902261193 | `component::unifiprotect::entity::event::sound_detection::state_attributes::event_type::state::speaking` | Speaking | Tal | Core-literal match |
| 13773 | 902261192 | `component::unifiprotect::entity::event::sound_detection::state_attributes::event_type::state::smoke` | Smoke alarm | Brandvarnare | Core-literal match |
| 13774 | 902261191 | `component::unifiprotect::entity::event::sound_detection::state_attributes::event_type::state::siren` | Siren | Siren | Core-literal match |
| 13775 | 902261190 | `component::unifiprotect::entity::event::sound_detection::state_attributes::event_type::state::glass_break` | Glass break | Glaskross | Core-literal match |
| 13776 | 902261189 | `component::unifiprotect::entity::event::sound_detection::state_attributes::event_type::state::co` | CO alarm | Kolmonoxidlarm | Core-literal match |
| 13777 | 902261188 | `component::unifiprotect::entity::event::sound_detection::state_attributes::event_type::state::car_horn` | Car horn | Biltuta | Core-literal match |
| 13778 | 902261187 | `component::unifiprotect::entity::event::sound_detection::state_attributes::event_type::state::car_alarm` | Car alarm | Billarm | Core-literal match |
| 13779 | 902261186 | `component::unifiprotect::entity::event::sound_detection::state_attributes::event_type::state::bark` | Barking | Skällande | Core-literal match |
| 13780 | 902261185 | `component::unifiprotect::entity::event::sound_detection::state_attributes::event_type::state::baby_cry` | Baby cry | Bebisgråt | Core-literal match |
| 13781 | 902261184 | `component::unifiprotect::entity::event::sound_detection::name` | Sound detection | Ljuddetektering | Core-literal match |
| 13782 | 902261183 | `component::unifiprotect::entity::event::smart_detection::state_attributes::event_type::state::vehicle` | Vehicle | Fordon | Core-literal match |
| 13783 | 902261182 | `component::unifiprotect::entity::event::smart_detection::state_attributes::event_type::state::pet` | Pet | Sällskapsdjur | Core-literal match |
| 13784 | 902261181 | `component::unifiprotect::entity::event::smart_detection::state_attributes::event_type::state::person` | Person | Person | Core-literal match |
| 13785 | 902261180 | `component::unifiprotect::entity::event::smart_detection::state_attributes::event_type::state::package` | Package | Paket | Core-literal match |
| 13786 | 902261179 | `component::unifiprotect::entity::event::smart_detection::state_attributes::event_type::state::license_plate` | License plate | Registreringsskylt | Core-literal match |
| 13787 | 902261178 | `component::unifiprotect::entity::event::smart_detection::state_attributes::event_type::state::face` | Face | Ansikte | Core-literal match |
| 13788 | 902261177 | `component::unifiprotect::entity::event::smart_detection::state_attributes::event_type::state::car` | Car | Bil | Core-literal match |
| 13789 | 902261176 | `component::unifiprotect::entity::event::smart_detection::state_attributes::event_type::state::animal` | Animal | Djur | Core-literal match |
| 13790 | 902261175 | `component::unifiprotect::entity::event::smart_detection::name` | Smart detection | Smart detektering | Core-literal match |
| 13791 | 902261174 | `component::unifiprotect::entity::event::motion_detection::state_attributes::event_type::state::motion` | Motion | Rörelse | Core-literal match |
| 13792 | 902261173 | `component::unifiprotect::entity::event::motion_detection::name` | Motion detection | Rörelsedetektering | Core-literal match |
| 13793 | 902248769 | `component::ecovacs::entity::sensor::lifespan_weed_rope::name` | Edge trimmer line lifespan | Kanttrimmerlinans livslängd | Core-literal match |
| 13794 | 902248768 | `component::ecovacs::entity::sensor::lifespan_trimmer_brush::name` | Edge trimmer brush lifespan | Kanttrimmerborstens livslängd | Core-literal match |
| 13795 | 902248767 | `component::ecovacs::entity::button::reset_lifespan_weed_rope::name` | Reset edge trimmer line lifespan | Återställ kanttrimmerlinans livslängd | Core-literal match |
| 13796 | 902248766 | `component::ecovacs::entity::button::reset_lifespan_trimmer_brush::name` | Reset edge trimmer brush lifespan | Återställ kanttrimmerborstens livslängd | Core-literal match |
| 13797 | 902235479 | `component::ecovacs::entity::sensor::lifespan_water_sink::name` | Water sink lifespan | Livslängd för vattenvask | Core-literal match |
| 13798 | 902235478 | `component::ecovacs::entity::sensor::lifespan_sewage_box::name` | Sewage box lifespan | Avloppsbehållarens livslängd | Core-literal match |
| 13799 | 902235477 | `component::ecovacs::entity::sensor::lifespan_cleaning_solution::name` | Cleaning solution lifespan | Rengöringslösningens livslängd | Core-literal match |
| 13800 | 902235476 | `component::ecovacs::entity::button::reset_lifespan_water_sink::name` | Reset water sink lifespan | Återställ vattenvaskens livslängd | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 906108227 | `component::bthome::entity::event::button::name` | Button |
| 903288602 | `component::ecovacs::config::abort::reauth_successful` | Re-authentication was successful |
| 902976494 | `component::webostv::exceptions::device_unavailable::message` | Device {device} is unavailable |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
