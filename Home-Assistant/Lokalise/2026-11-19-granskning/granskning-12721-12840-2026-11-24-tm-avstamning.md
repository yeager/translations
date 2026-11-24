# Home Assistant Core – historisk avstämning 12721–12840

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 98 direkta källtexter matchar HA Core-källan; 16 referensanvändningar med 14 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 6 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 12721 | 919306808 | `component::portainer::entity::event::docker_event::state_attributes::event_type::state::restart` | Restarted | Omstartad | Core-literal match |
| 12722 | 919306807 | `component::portainer::entity::event::docker_event::state_attributes::event_type::state::pause` | Paused | Pausad | Core-literal match |
| 12723 | 919306806 | `component::portainer::entity::event::docker_event::state_attributes::event_type::state::oom` | Out of memory | Slut på minne | Core-literal match |
| 12724 | 919306805 | `component::portainer::entity::event::docker_event::state_attributes::event_type::state::kill` | Killed | Tvångsavslutad | Core-literal match |
| 12725 | 919306804 | `component::portainer::entity::event::docker_event::state_attributes::event_type::state::health_status_unhealthy` | Health check failed | Hälsokontrollen misslyckades | Core-literal match |
| 12726 | 919306803 | `component::portainer::entity::event::docker_event::state_attributes::event_type::state::health_status_starting` | Health check starting | Hälsokontrollen påbörjas | Core-literal match |
| 12727 | 919306802 | `component::portainer::entity::event::docker_event::state_attributes::event_type::state::health_status_healthy` | Health check passed | Hälsokontrollen godkändes | Core-literal match |
| 12728 | 919306801 | `component::portainer::entity::event::docker_event::state_attributes::event_type::state::die` | Died | Avslutades | Core-literal match |
| 12729 | 919306800 | `component::portainer::entity::event::docker_event::name` | Docker event | Docker-händelse | Core-literal match |
| 12730 | 919303555 | `component::tessie::entity::climate::climate_state_cabin_overheat_protection::name` | Cabin overheat protection | Överhettningsskydd för kupén | Core-literal match |
| 12731 | 919288202 | `component::tessie::entity::button::enable_keep_accessory_power_mode::name` | Enable keep accessory power | Aktivera strömförsörjning till tillbehör | Core-literal match |
| 12732 | 919288201 | `component::tessie::entity::button::disable_keep_accessory_power_mode::name` | Disable keep accessory power | Inaktivera strömförsörjning till tillbehör | Core-literal match |
| 12733 | 919275586 | `component::midea::entity::binary_sensor::tank_full::name` | Tank full | Full tank | Core-literal match |
| 12734 | 919275585 | `component::midea::entity::binary_sensor::screen_status::name` | Screen | Skärm | Core-literal match |
| 12735 | 919275584 | `component::midea::entity::binary_sensor::salt::name` | Salt | Salt | Core-literal match |
| 12736 | 919275583 | `component::midea::entity::binary_sensor::rinse_aid::name` | Rinse aid | Sköljmedel | Core-literal match |
| 12737 | 919275582 | `component::midea::entity::binary_sensor::night_mode::name` | Night mode | Nattläge | Core-literal match |
| 12738 | 919275581 | `component::midea::entity::binary_sensor::led_status::name` | LED | LED | Core-literal match |
| 12739 | 919275580 | `component::midea::entity::binary_sensor::header_exist::name` | Header | Header | Core-literal match |
| 12740 | 919275579 | `component::midea::entity::binary_sensor::full_dust::name` | Full dust | Dammbehållare full | Core-literal match |
| 12741 | 919275578 | `component::midea::entity::binary_sensor::filter_cleaning_reminder::name` | Filter cleaning | Filterrengöring | Core-literal match |
| 12742 | 919275577 | `component::midea::entity::binary_sensor::fall_asleep_status::name` | Fall asleep | Somna | Core-literal match |
| 12743 | 919275576 | `component::midea::entity::binary_sensor::arofene_link::name` | Methanal | Metanal | Core-literal match |
| 12744 | 919274933 | `component::midea::entity::light::light::state_attributes::effect::state::reading` | Reading | Läsning | Core-literal match |
| 12745 | 919274932 | `component::midea::entity::light::light::state_attributes::effect::state::night` | Night | Natt | Core-literal match |
| 12746 | 919274931 | `component::midea::entity::light::light::state_attributes::effect::state::mildly` | Mildly | Mild | Core-literal match |
| 12747 | 919274930 | `component::midea::entity::light::light::state_attributes::effect::state::living` | Living | Levande | Core-literal match |
| 12748 | 919274929 | `component::midea::entity::light::light::state_attributes::effect::state::cinema` | Cinema | Bio | Core-literal match |
| 12749 | 919274901 | `component::demo::entity::cover::living_room_window::state_attributes::speed::state::slow` | Slow | Långsam | Shared reference target checked |
| 12750 | 919274900 | `component::demo::entity::cover::living_room_window::state_attributes::speed::state::default` | Default | Standard | Source-path follow-up open |
| 12751 | 919274899 | `component::cover::services::set_cover_position::fields::speed::name` | Speed | Hastighet | Shared reference target checked |
| 12752 | 919274898 | `component::cover::services::set_cover_position::fields::speed::description` | Speed at which to move the cover. | Den hastighet som skyddet ska förflyttas med. | Core-literal match |
| 12753 | 919274897 | `component::cover::services::open_cover::fields::speed::name` | Speed | Hastighet | Shared reference target checked |
| 12754 | 919274896 | `component::cover::services::open_cover::fields::speed::description` | Speed at which to open the cover. | Den hastighet som skyddet ska öppnas med. | Core-literal match |
| 12755 | 919274895 | `component::cover::services::close_cover::fields::speed::name` | Speed | Hastighet | Shared reference target checked |
| 12756 | 919274894 | `component::cover::services::close_cover::fields::speed::description` | Speed at which to close the cover. | Den hastighet som skyddet ska stängas med. | Core-literal match |
| 12757 | 919274893 | `component::cover::exceptions::not_valid_speed::message` | Speed {speed} is not valid. Valid speeds are: {supported_speeds}. | Hastighet {speed} är inte giltig. Giltiga hastigheter är: {supported_speeds}. | Source-path follow-up open |
| 12758 | 919274892 | `component::cover::common::field_speed_name` | Speed | Hastighet | Core-literal match |
| 12759 | 919274744 | `component::collection_image::title` | Collection image | Samlingsbild | Core-literal match |
| 12760 | 919274743 | `component::collection_image::exceptions::image_read_error::message` | Error reading image from {path}: {error} | Fel vid inläsning av bild från {path}: {error} | Source-path follow-up open |
| 12761 | 919274742 | `component::collection_image::config::step::user::submit` | Create | Skapa | Core-literal match |
| 12762 | 919274741 | `component::collection_image::config::step::user::description` | The Collection Image integration creates an image entity which renders an image from the selected media. | Integrationen ”Collection Image” skapar en bildentitet som visar en bild från det valda mediet. | Core-literal match |
| 12763 | 919274740 | `component::collection_image::config::step::user::data_description::media` | The media where images will be retrieved from. | Mediet varifrån bilderna kommer att hämtas. | Core-literal match |
| 12764 | 919274739 | `component::collection_image::config::step::user::data::media` | Media | Media | Core-literal match |
| 12765 | 919274738 | `component::collection_image::config::error::selected_media_no_images` | The selected media has no images. Please select a media directory with images. | Det valda mediet har inga bilder. Välj en mediekatalog med bilder. | Core-literal match |
| 12766 | 919274737 | `component::collection_image::config::error::failed_browse` | Failed to browse media: {error} | Det gick inte att bläddra bland mediefilerna: {error} | Core-literal match |
| 12767 | 919159612 | `component::midea::entity::switch::zone2_curve::name` | Zone 2 curve | Kurva för zon 2 | Core-literal match |
| 12768 | 919159611 | `component::midea::entity::switch::zone1_curve::name` | Zone 1 curve | Kurva för zon 1 | Core-literal match |
| 12769 | 919159610 | `component::midea::entity::switch::tbh::name` | TBH | TBH | Core-literal match |
| 12770 | 919159609 | `component::midea::entity::switch::sound::name` | Sound | Ljud | Core-literal match |
| 12771 | 919159608 | `component::midea::entity::switch::smart_eye::name` | Smart eye | Smart öga | Core-literal match |
| 12772 | 919159607 | `component::midea::entity::switch::self_clean::name` | Self clean | Självrengöring | Core-literal match |
| 12773 | 919159606 | `component::midea::entity::switch::screen_display::name` | Screen display | Skärmvisning | Core-literal match |
| 12774 | 919159605 | `component::midea::entity::switch::prompt_tone::name` | Prompt tone | Signalton | Core-literal match |
| 12775 | 919159604 | `component::midea::entity::switch::out_silent::name` | Outdoor silent mode | Tyst läge för utomhusenheten | Core-literal match |
| 12776 | 919159603 | `component::midea::entity::switch::night_light::name` | Night light | Nattlampa | Core-literal match |
| 12777 | 919159602 | `component::midea::entity::switch::disinfect::name` | Disinfect | Desinficera | Core-literal match |
| 12778 | 919159601 | `component::midea::entity::switch::aux_heating::name` | Auxiliary heating | Tillsatsvärme | Core-literal match |
| 12779 | 919159600 | `component::midea::entity::switch::anion::name` | Anion | Anion | Core-literal match |
| 12780 | 919138871 | `component::midea::entity::fan::fan::state_attributes::preset_mode::state::warm` | Warm | Varm | Core-literal match |
| 12781 | 919138870 | `component::midea::entity::fan::fan::state_attributes::preset_mode::state::strong` | Strong | Stark | Core-literal match |
| 12782 | 919138869 | `component::midea::entity::fan::fan::state_attributes::preset_mode::state::soft` | Soft | Mjuk | Core-literal match |
| 12783 | 919138868 | `component::midea::entity::fan::fan::state_attributes::preset_mode::state::smart` | Smart | Smart | Core-literal match |
| 12784 | 919138867 | `component::midea::entity::fan::fan::state_attributes::preset_mode::state::sleep` | Sleep | Sömn | Core-literal match |
| 12785 | 919138866 | `component::midea::entity::fan::fan::state_attributes::preset_mode::state::silent` | Silent | Tyst | Core-literal match |
| 12786 | 919138865 | `component::midea::entity::fan::fan::state_attributes::preset_mode::state::natural` | Natural | Naturlig | Core-literal match |
| 12787 | 919138864 | `component::midea::entity::fan::fan::state_attributes::preset_mode::state::induction` | Induction | Induktion | Core-literal match |
| 12788 | 919138863 | `component::midea::entity::fan::fan::state_attributes::preset_mode::state::eco` | Eco | Eko | Core-literal match |
| 12789 | 919138862 | `component::midea::entity::fan::fan::state_attributes::preset_mode::state::customize` | Customize | Anpassat | Core-literal match |
| 12790 | 919138861 | `component::midea::entity::fan::fan::state_attributes::preset_mode::state::comfort` | Comfort | Komfort | Core-literal match |
| 12791 | 919138860 | `component::midea::entity::fan::fan::state_attributes::preset_mode::state::circulation` | Circulation | Cirkulation | Core-literal match |
| 12792 | 919138859 | `component::midea::entity::fan::fan::state_attributes::preset_mode::state::baby` | Baby | Bebis | Core-literal match |
| 12793 | 919117034 | `component::home_connect::exceptions::fetch_image_error::message` | Error obtaining image from the API: {error} | Fel vid hämtning av bild från API: {error} | Source-path follow-up open |
| 12794 | 919117033 | `component::home_connect::entity::image::interior_right_camera::name` | Interior right camera | Höger innerkamera | Source-path follow-up open |
| 12795 | 919117032 | `component::home_connect::entity::image::door_right_camera::name` | Door right camera | Höger dörrkamera | Source-path follow-up open |
| 12796 | 919013737 | `component::netio::issues::deprecated_yaml::title` | The Netio YAML configuration is being removed | Netio-konfigurationen i YAML tas bort | Core-literal match |
| 12797 | 919013736 | `component::netio::issues::deprecated_yaml::description` | Configuring the Netio switch platform using YAML is being removed. The integration now connects to your device using the JSON API, which requires a new setup.<br><br>To set up your device:<br><br>1. Open the web interface of your Netio device and enable the **JSON API** protocol (**Settings** > **M2M API Protocols** > **JSON API**), creating an account with read-write access.<br>2. [Add the Netio integration]({url}) and enter the connection details, using the JSON API account credentials.<br>3. Remove the `netio` switch platform configuration from your `configuration.yaml` file and restart Home Assistant.<br><br>Afterwards, your device outputs are available as switch entities again. | Konfigurationen av Netio-switchplattformen med YAML tas bort. Integrationen ansluter nu till din enhet via JSON API, vilket kräver en ny konfiguration.<br><br>Så här konfigurerar du din enhet:<br><br>1. Öppna webbgränssnittet för din Netio-enhet och aktivera **JSON API**-protokollet (**Inställningar** > **M2M API-protokoll** > **JSON API**) och skapa ett konto med läs- och skrivbehörighet.<br>2. [Lägg till Netio-integrationen]({url}) och ange anslutningsuppgifterna med hjälp av inloggningsuppgifterna för JSON API-kontot.<br>3. Ta bort konfigurationen för `netio`-switchplattformen från din `configuration.yaml`-fil och starta om Home Assistant.<br><br>Därefter är utgångarna från din enhet återigen tillgängliga som switch-enheter. | Core-literal match |
| 12798 | 919013735 | `component::netio::config::step::user::data_description::verify_ssl` | Verify the SSL certificate of the device when using HTTPS. | Verifiera enhetens SSL-certifikat när du använder HTTPS. | Core-literal match |
| 12799 | 919013734 | `component::netio::config::step::user::data_description::username` | The username of a device account with read-write access to the JSON API. | Användarnamnet för ett enhetskonto med läs- och skrivåtkomst till JSON API:et. | Core-literal match |
| 12800 | 919013733 | `component::netio::config::step::user::data_description::ssl` | Connect to the device using HTTPS. | Anslut till enheten via HTTPS. | Core-literal match |
| 12801 | 919013732 | `component::netio::config::step::user::data_description::port` | The port of the JSON API web server on the device. | Porten för enhetens JSON API-webbserver. | Core-literal match |
| 12802 | 919013731 | `component::netio::config::step::user::data_description::password` | The password of the device account. | Lösenordet till enhetens konto. | Core-literal match |
| 12803 | 919013730 | `component::netio::config::step::user::data_description::host` | The hostname or IP address of your Netio device. | Värdnamnet eller IP-adressen för din Netio-enhet. | Core-literal match |
| 12804 | 919013729 | `component::netio::config::step::user::data::verify_ssl` | Verify SSL certificate | Verifiera SSL-certifikat | Shared reference target checked |
| 12805 | 919013728 | `component::netio::config::step::user::data::username` | Username | Användarnamn | Shared reference target checked |
| 12806 | 919013727 | `component::netio::config::step::user::data::ssl` | Uses an SSL certificate | Använder ett SSL-certifikat | Shared reference target checked |
| 12807 | 919013726 | `component::netio::config::step::user::data::port` | Port | Port | Shared reference target checked |
| 12808 | 919013725 | `component::netio::config::step::user::data::password` | Password | Lösenord | Shared reference target checked |
| 12809 | 919013724 | `component::netio::config::step::user::data::host` | Host | Värd | Shared reference target checked |
| 12810 | 919013723 | `component::netio::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 12811 | 919013722 | `component::netio::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Shared reference target checked |
| 12812 | 919013721 | `component::netio::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 12813 | 919013720 | `component::netio::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 12814 | 918996592 | `component::monzo::services::withdraw_from_pot::name` | Withdraw from pot | Ta ut från potten | Core-literal match |
| 12815 | 918996591 | `component::monzo::services::withdraw_from_pot::fields::pot::name` | From pot | Från pott | Core-literal match |
| 12816 | 918996590 | `component::monzo::services::withdraw_from_pot::fields::pot::description` | The pot to move money from. | Den pott som pengarna ska överföras från. | Core-literal match |
| 12817 | 918996589 | `component::monzo::services::withdraw_from_pot::fields::amount::name` | Amount | Belopp | Shared reference target checked |
| 12818 | 918996588 | `component::monzo::services::withdraw_from_pot::fields::amount::description` | The amount of money to move. | Det belopp som ska överföras. | Shared reference target checked |
| 12819 | 918996587 | `component::monzo::services::withdraw_from_pot::fields::account::name` | To account | Till konto | Core-literal match |
| 12820 | 918996586 | `component::monzo::services::withdraw_from_pot::fields::account::description` | The account to move money into. | Det konto som pengarna ska överföras till. | Core-literal match |
| 12821 | 918996585 | `component::monzo::services::withdraw_from_pot::description` | Moves money from a Monzo pot into an account. | Överför pengar från en Monzo-pott till ett konto. | Core-literal match |
| 12822 | 918996584 | `component::monzo::services::deposit_into_pot::name` | Deposit into pot | Sätt in i potten | Core-literal match |
| 12823 | 918996583 | `component::monzo::services::deposit_into_pot::fields::pot::name` | To pot | Till pott | Core-literal match |
| 12824 | 918996582 | `component::monzo::services::deposit_into_pot::fields::pot::description` | The pot to move money into. | Potten som pengarna ska överföras till. | Core-literal match |
| 12825 | 918996581 | `component::monzo::services::deposit_into_pot::fields::amount::name` | Amount | Belopp | Core-literal match |
| 12826 | 918996580 | `component::monzo::services::deposit_into_pot::fields::amount::description` | The amount of money to move. | Det belopp som ska överföras. | Core-literal match |
| 12827 | 918996579 | `component::monzo::services::deposit_into_pot::fields::account::name` | From account | Från konto | Core-literal match |
| 12828 | 918996578 | `component::monzo::services::deposit_into_pot::fields::account::description` | The account to move money from. | Det konto som pengarna ska överföras från. | Core-literal match |
| 12829 | 918996577 | `component::monzo::services::deposit_into_pot::description` | Moves money from a Monzo account into a pot. | Överför pengar från ett Monzo-konto till en pott. | Core-literal match |
| 12830 | 918996576 | `component::monzo::exceptions::transfer_status_unknown::message` | Home Assistant could not confirm whether the transfer completed. Check your Monzo balance before trying again. | Home Assistant kunde inte bekräfta om överföringen genomfördes. Kontrollera ditt saldo hos Monzo innan du försöker igen. | Core-literal match |
| 12831 | 918996575 | `component::monzo::exceptions::transfer_rejected::message` | Monzo rejected the transfer for {account_name} (account type: {account_type}): {reason}. If the reason does not explain why this account cannot be used for pot transfers, report an issue with the Monzo integration and include these details. | Monzo avvisade överföringen för {account_name} (kontotyp: {account_type}): {reason}. Om orsaken inte förklarar varför kontot inte kan användas för pottöverföringar, rapportera ett problem med Monzo-integrationen och ange dessa uppgifter. | Core-literal match |
| 12832 | 918996574 | `component::monzo::exceptions::transfer_failed::message` | The money could not be transferred. Try again later. | Pengarna kunde inte överföras. Försök igen senare. | Core-literal match |
| 12833 | 918996573 | `component::monzo::exceptions::pot_selected_as_account::message` | {device_name} is a pot, not an account. Choose a Monzo account in the Account field. | {device_name} är en pott, inte ett konto. Välj ett Monzo-konto i fältet ”Konto”. | Core-literal match |
| 12834 | 918996572 | `component::monzo::exceptions::pot_account_mismatch::message` | {pot_name} belongs to {pot_account_name}, not {account_name}. Choose its associated Monzo account, or choose a pot belonging to {account_name}. | {pot_name} tillhör {pot_account_name}, inte {account_name}. Välj det tillhörande Monzo-kontot eller en pott som tillhör {account_name}. | Core-literal match |
| 12835 | 918996571 | `component::monzo::exceptions::invalid_transfer_account::message` | {device_name} does not support pot transfers. Choose a different Monzo account. | {device_name} stöder inte pottöverföringar. Välj ett annat Monzo-konto. | Core-literal match |
| 12836 | 918996570 | `component::monzo::exceptions::invalid_pot::message` | The selected device ({device_name}) is not a pot belonging to this Monzo connection. | Den valda enheten ({device_name}) är inte en pott som hör till denna Monzo-anslutning. | Core-literal match |
| 12837 | 918996569 | `component::monzo::exceptions::invalid_device::message` | The selected Monzo device could not be found. | Den valda Monzo-enheten kunde inte hittas. | Core-literal match |
| 12838 | 918996568 | `component::monzo::exceptions::invalid_account::message` | The selected device ({device_name}) is not an account belonging to this Monzo connection. | Den valda enheten ({device_name}) är inte ett konto som hör till denna Monzo-anslutning. | Core-literal match |
| 12839 | 918996567 | `component::monzo::exceptions::different_entries::message` | The selected account and pot must belong to the same Monzo connection. | Det valda kontot och potten måste tillhöra samma Monzo-anslutning. | Core-literal match |
| 12840 | 918996566 | `component::monzo::exceptions::authentication_expired::message` | Authentication with Monzo has expired. Reauthentication has been started. | Autentiseringen hos Monzo har gått ut. En ny autentisering har påbörjats. | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 919274900 | `component::demo::entity::cover::living_room_window::state_attributes::speed::state::default` | Default |
| 919274893 | `component::cover::exceptions::not_valid_speed::message` | Speed {speed} is not valid. Valid speeds are: {supported_speeds}. |
| 919274743 | `component::collection_image::exceptions::image_read_error::message` | Error reading image from {path}: {error} |
| 919117034 | `component::home_connect::exceptions::fetch_image_error::message` | Error obtaining image from the API: {error} |
| 919117033 | `component::home_connect::entity::image::interior_right_camera::name` | Interior right camera |
| 919117032 | `component::home_connect::entity::image::door_right_camera::name` | Door right camera |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
