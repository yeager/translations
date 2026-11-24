# Home Assistant Core – historisk avstämning 12841–12960

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 111 direkta källtexter matchar HA Core-källan; 8 referensanvändningar med 5 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 1 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 12841 | 918996565 | `component::monzo::exceptions::account_selected_as_pot::message` | {device_name} is an account, not a pot. Choose a Monzo pot in the Pot field. | {device_name} är ett konto, inte en pott. Välj en Monzo-pott i fältet Pott. | Core-literal match |
| 12842 | 918969510 | `component::unifiprotect::exceptions::light_not_available::message` | Light {light_name} is no longer available | Lampan {light_name} är inte längre tillgänglig | Core-literal match |
| 12843 | 918955678 | `component::samsung_exlink::exceptions::command_rejected::message` | The TV rejected the command: {error} | TV:n avvisade kommandot: {error} | Core-literal match |
| 12844 | 918955677 | `component::samsung_exlink::exceptions::command_failed::message` | Failed to send the command to the TV: {error} | Det gick inte att skicka kommandot till TV:n: {error} | Core-literal match |
| 12845 | 918955676 | `component::samsung_exlink::exceptions::cannot_connect::message` | Error connecting to the Samsung TV: {error} | Fel vid anslutning till Samsung-TV:n: {error} | Core-literal match |
| 12846 | 918955675 | `component::samsung_exlink::entity::media_player::tv::state_attributes::source::state::tv` | TV | TV | Core-literal match |
| 12847 | 918955674 | `component::samsung_exlink::entity::media_player::tv::state_attributes::source::state::s_video3` | S-Video 3 | S-Video 3 | Core-literal match |
| 12848 | 918955673 | `component::samsung_exlink::entity::media_player::tv::state_attributes::source::state::s_video2` | S-Video 2 | S-Video 2 | Core-literal match |
| 12849 | 918955672 | `component::samsung_exlink::entity::media_player::tv::state_attributes::source::state::s_video1` | S-Video 1 | S-Video 1 | Core-literal match |
| 12850 | 918955671 | `component::samsung_exlink::entity::media_player::tv::state_attributes::source::state::rvu` | RVU | RVU | Core-literal match |
| 12851 | 918955670 | `component::samsung_exlink::entity::media_player::tv::state_attributes::source::state::pc3` | PC 3 | PC 3 | Core-literal match |
| 12852 | 918955669 | `component::samsung_exlink::entity::media_player::tv::state_attributes::source::state::pc2` | PC 2 | PC 2 | Core-literal match |
| 12853 | 918955668 | `component::samsung_exlink::entity::media_player::tv::state_attributes::source::state::pc1` | PC 1 | PC 1 | Core-literal match |
| 12854 | 918955667 | `component::samsung_exlink::entity::media_player::tv::state_attributes::source::state::hdmi4` | HDMI 4 | HDMI 4 | Core-literal match |
| 12855 | 918955666 | `component::samsung_exlink::entity::media_player::tv::state_attributes::source::state::hdmi3` | HDMI 3 | HDMI 3 | Core-literal match |
| 12856 | 918955665 | `component::samsung_exlink::entity::media_player::tv::state_attributes::source::state::hdmi2` | HDMI 2 | HDMI 2 | Core-literal match |
| 12857 | 918955664 | `component::samsung_exlink::entity::media_player::tv::state_attributes::source::state::hdmi1` | HDMI 1 | HDMI 1 | Core-literal match |
| 12858 | 918955663 | `component::samsung_exlink::entity::media_player::tv::state_attributes::source::state::dvi3` | DVI 3 | DVI 3 | Core-literal match |
| 12859 | 918955662 | `component::samsung_exlink::entity::media_player::tv::state_attributes::source::state::dvi2` | DVI 2 | DVI 2 | Core-literal match |
| 12860 | 918955661 | `component::samsung_exlink::entity::media_player::tv::state_attributes::source::state::dvi1` | DVI 1 | DVI 1 | Core-literal match |
| 12861 | 918955660 | `component::samsung_exlink::entity::media_player::tv::state_attributes::source::state::component3` | Component 3 | Komponent 3 | Core-literal match |
| 12862 | 918955659 | `component::samsung_exlink::entity::media_player::tv::state_attributes::source::state::component2` | Component 2 | Komponent 2 | Core-literal match |
| 12863 | 918955658 | `component::samsung_exlink::entity::media_player::tv::state_attributes::source::state::component1` | Component 1 | Komponent 1 | Core-literal match |
| 12864 | 918955657 | `component::samsung_exlink::entity::media_player::tv::state_attributes::source::state::av3` | AV 3 | AV 3 | Core-literal match |
| 12865 | 918955656 | `component::samsung_exlink::entity::media_player::tv::state_attributes::source::state::av2` | AV 2 | AV 2 | Core-literal match |
| 12866 | 918955655 | `component::samsung_exlink::entity::media_player::tv::state_attributes::source::state::av1` | AV 1 | AV 1 | Core-literal match |
| 12867 | 918955654 | `component::samsung_exlink::config::step::user::description` | Make sure the TV is powered on before continuing. Home Assistant queries the TV during setup to confirm the connection, and a TV in standby will not respond. | Se till att TV:n är påslagen innan du fortsätter. Home Assistant skickar en förfrågan till TV:n under installationen för att bekräfta anslutningen, och en TV i standby-läge svarar inte. | Core-literal match |
| 12868 | 918955653 | `component::samsung_exlink::config::step::user::data_description::model` | Select your TV's generation to translate the active input back into a named source. Leave empty if your model is not listed; you can still switch sources. | Välj din TV:s generation för att omvandla den aktiva ingången till en namngiven källa. Lämna fältet tomt om din modell inte finns med i listan; du kan fortfarande växla mellan källor. | Core-literal match |
| 12869 | 918955652 | `component::samsung_exlink::config::step::user::data_description::device` | Serial port path to connect to. | Sökvägen till serieporten som ska användas. | Core-literal match |
| 12870 | 918955651 | `component::samsung_exlink::config::step::user::data::model` | TV generation | TV-generation | Core-literal match |
| 12871 | 918955650 | `component::samsung_exlink::config::step::user::data::device` | Port | Port | Shared reference target checked |
| 12872 | 918955649 | `component::samsung_exlink::config::step::troubleshoot::title` | Connection failed | Anslutningen misslyckades | Core-literal match |
| 12873 | 918955648 | `component::samsung_exlink::config::step::troubleshoot::description` | Home Assistant could not communicate with the Samsung TV over the serial port.<br><br>The most common cause is that ExLink control is not enabled. On TVs that use the USB-to-ExLink dongle, **EXT Link Support** and **USB Serial** must be enabled in the hidden service menu (on the remote, press **Mute → 1 → 8 → 2 → Power**); the exact path varies by model, so check your TV's documentation.<br><br>Also make sure that:<br>- The TV is powered on. A TV in standby does not answer status queries.<br>- The cable is connected to the TV's 3.5 mm ExLink jack (or the Samsung USB-to-ExLink dongle) and is fully seated.<br>- The correct serial port was selected.<br><br>Select **Submit** to try again. | Home Assistant kunde inte kommunicera med Samsung-TV:n via den seriella porten.<br><br>Den vanligaste orsaken är att ExLink-styrningen inte är aktiverad. På TV-apparater som använder USB-till-ExLink-dongeln måste **EXT Link Support** och **USB Serial** vara aktiverade i den dolda servicemenyn (tryck på fjärrkontrollen på **Mute → 1 → 8 → 2 → Power**); den exakta vägen varierar beroende på modell, så kontrollera din TV:s dokumentation.<br><br>Se också till att:<br>- TV:n är påslagen. En TV i standby-läge svarar inte på statusförfrågningar.<br>- Kabeln är ansluten till TV:ns 3,5 mm ExLink-uttag (eller Samsungs USB-till-ExLink-dongel) och sitter ordentligt i.<br>- Rätt seriell port har valts.<br><br>Välj **Bekräfta** för att försöka igen. | Core-literal match |
| 12874 | 918955647 | `component::samsung_exlink::config::error::unknown` | Unexpected error | Oväntat fel | Shared reference target checked |
| 12875 | 918955646 | `component::samsung_exlink::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Shared reference target checked |
| 12876 | 918955645 | `component::samsung_exlink::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 12877 | 918942642 | `component::youtube::entity::sensor::latest_video::state_attributes::video_id::name` | Video ID | Video-ID | Core-literal match |
| 12878 | 918942641 | `component::youtube::entity::sensor::latest_video::state_attributes::published_at::name` | Published at | Publicerad | Core-literal match |
| 12879 | 918942640 | `component::youtube::entity::sensor::latest_video::name` | Latest video | Senaste video | Core-literal match |
| 12880 | 918942639 | `component::youtube::entity::sensor::latest_short::state_attributes::video_id::name` | Video ID | Video-ID | Core-literal match |
| 12881 | 918942638 | `component::youtube::entity::sensor::latest_short::state_attributes::published_at::name` | Published at | Publicerad | Core-literal match |
| 12882 | 918942637 | `component::youtube::entity::sensor::latest_short::name` | Latest short | Senaste short | Core-literal match |
| 12883 | 918682105 | `component::tonewinner::entity::media_player::tonewinner::name` | Tonewinner | Tonewinner | Core-literal match |
| 12884 | 918682104 | `component::tonewinner::config::step::user::title` | Set up Tonewinner | Konfigurera Tonewinner | Core-literal match |
| 12885 | 918682103 | `component::tonewinner::config::step::user::description` | Enter the serial port of your Tonewinner AV receiver. | Ange serieporten på din Tonewinner AV-receiver. | Core-literal match |
| 12886 | 918682102 | `component::tonewinner::config::step::user::data_description::serial_port` | Serial port path to connect to | Sökvägen till serieporten som ska användas | Core-literal match |
| 12887 | 918682101 | `component::tonewinner::config::step::user::data::serial_port` | Port | Port | Shared reference target checked |
| 12888 | 918682100 | `component::tonewinner::config::step::reconfigure::title` | Reconfigure Tonewinner | Konfigurera om Tonewinner | Core-literal match |
| 12889 | 918682099 | `component::tonewinner::config::step::reconfigure::description` | Update the serial port for your Tonewinner AV receiver. | Uppdatera serieporten för din Tonewinner AV-receiver. | Core-literal match |
| 12890 | 918682098 | `component::tonewinner::config::step::reconfigure::data_description::serial_port` | Serial port path to connect to | Sökvägen till serieporten som ska användas | Shared reference target checked |
| 12891 | 918682097 | `component::tonewinner::config::step::reconfigure::data::serial_port` | Port | Port | Shared reference target checked |
| 12892 | 918682096 | `component::tonewinner::config::error::unknown` | An unknown error occurred | Ett okänt fel inträffade | Core-literal match |
| 12893 | 918682095 | `component::tonewinner::config::error::cannot_connect` | Cannot connect to the serial port. Please check the port and permissions. | Det går inte att ansluta till serieporten. Kontrollera porten och behörigheterna. | Core-literal match |
| 12894 | 918682094 | `component::tonewinner::config::abort::reconfigure_unload_failed` | The existing configuration could not be unloaded. Please try again. | Den befintliga konfigurationen kunde inte avaktiveras. Försök igen. | Core-literal match |
| 12895 | 918682093 | `component::tonewinner::config::abort::reconfigure_successful` | Reconfiguration was successful | Omkonfigureringen lyckades | Source-path follow-up open |
| 12896 | 918682092 | `component::tonewinner::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Shared reference target checked |
| 12897 | 918279934 | `component::midea::entity::number::water_temp_level::name` | Water temperature level | Vattentemperaturnivå | Core-literal match |
| 12898 | 918279933 | `component::midea::entity::number::water_hardness::name` | Water hardness | Vattenhårdhet | Core-literal match |
| 12899 | 918279932 | `component::midea::entity::number::vacation_days::name` | Vacation days | Semesterdagar | Core-literal match |
| 12900 | 918279931 | `component::midea::entity::number::seat_temp_level::name` | Seat temperature level | Sätestemperaturnivå | Core-literal match |
| 12901 | 918279930 | `component::midea::entity::number::leak_water_protection_value::name` | Leak water protection value | Värde för läckageskydd | Core-literal match |
| 12902 | 918279929 | `component::midea::entity::number::heating_level::name` | Heating level | Värmenivå | Core-literal match |
| 12903 | 918279928 | `component::midea::entity::number::flushing_days::name` | Flushing days | Spolningsdagar | Core-literal match |
| 12904 | 918279927 | `component::midea::entity::number::dry_level::name` | Dry level | Torrhetsnivå | Core-literal match |
| 12905 | 918271700 | `component::unifiprotect::entity::select::infrared_mode::state::manual` | Manual | Manuell | Core-literal match |
| 12906 | 918271699 | `component::unifiprotect::entity::select::infrared_mode::state::custom_filter_only` | Custom (IR filter only) | Anpassad (endast IR-filter) | Core-literal match |
| 12907 | 918181032 | `component::reolink::entity::switch::tamper_enabled::name` | Tamper alarm | Sabotagelarm | Core-literal match |
| 12908 | 918180366 | `component::midea::entity::select::wind_ud_angle::state::up_mid` | Up middle | Övre mitten | Core-literal match |
| 12909 | 918180365 | `component::midea::entity::select::wind_ud_angle::state::up` | Up | Upp | Core-literal match |
| 12910 | 918180364 | `component::midea::entity::select::wind_ud_angle::state::off` | Off | Av | Core-literal match |
| 12911 | 918180363 | `component::midea::entity::select::wind_ud_angle::state::middle` | Middle | Mitten | Core-literal match |
| 12912 | 918180362 | `component::midea::entity::select::wind_ud_angle::state::down_mid` | Down middle | Nedre mitten | Core-literal match |
| 12913 | 918180361 | `component::midea::entity::select::wind_ud_angle::state::down` | Down | Ner | Core-literal match |
| 12914 | 918180360 | `component::midea::entity::select::wind_ud_angle::name` | Airflow vertical | Vertikalt luftflöde | Core-literal match |
| 12915 | 918180359 | `component::midea::entity::select::wind_lr_angle::state::right_mid` | Right middle | Mellan mitten och höger | Core-literal match |
| 12916 | 918180358 | `component::midea::entity::select::wind_lr_angle::state::right` | Right | Höger | Core-literal match |
| 12917 | 918180357 | `component::midea::entity::select::wind_lr_angle::state::off` | Off | Av | Core-literal match |
| 12918 | 918180356 | `component::midea::entity::select::wind_lr_angle::state::middle` | Middle | Mitten | Core-literal match |
| 12919 | 918180355 | `component::midea::entity::select::wind_lr_angle::state::left_mid` | Left middle | Mellan mitten och vänster | Core-literal match |
| 12920 | 918180354 | `component::midea::entity::select::wind_lr_angle::state::left` | Left | Vänster | Core-literal match |
| 12921 | 918180353 | `component::midea::entity::select::wind_lr_angle::name` | Airflow horizontal | Horisontellt luftflöde | Core-literal match |
| 12922 | 918180352 | `component::midea::entity::select::water_level_set::name` | Water level setting | Inställning av vattennivå | Core-literal match |
| 12923 | 918180351 | `component::midea::entity::select::tilting_angle::state::plus_60` | Plus 60 | Plus 60 | Core-literal match |
| 12924 | 918180350 | `component::midea::entity::select::tilting_angle::state::off` | Off | Av | Core-literal match |
| 12925 | 918180349 | `component::midea::entity::select::tilting_angle::state::minus_60` | Minus 60 | Minus 60 | Core-literal match |
| 12926 | 918180348 | `component::midea::entity::select::tilting_angle::name` | Tilting angle | Lutningsvinkel | Core-literal match |
| 12927 | 918180347 | `component::midea::entity::select::silent_level::state::super_silent` | Super silent | Mycket tyst | Core-literal match |
| 12928 | 918180346 | `component::midea::entity::select::silent_level::state::silent` | Silent | Tyst | Core-literal match |
| 12929 | 918180345 | `component::midea::entity::select::silent_level::state::off` | Off | Av | Core-literal match |
| 12930 | 918180344 | `component::midea::entity::select::silent_level::name` | Silent level | Tysthetsnivå | Core-literal match |
| 12931 | 918180343 | `component::midea::entity::select::screen_display::state::off` | Off | Av | Core-literal match |
| 12932 | 918180342 | `component::midea::entity::select::screen_display::state::dim` | Dim | Dämpad | Core-literal match |
| 12933 | 918180341 | `component::midea::entity::select::screen_display::state::bright` | Bright | Ljus | Core-literal match |
| 12934 | 918180340 | `component::midea::entity::select::screen_display::name` | Screen display | Skärmens ljusstyrka | Core-literal match |
| 12935 | 918180339 | `component::midea::entity::select::rate_select::name` | Power rate limit | Begränsning av effekt | Core-literal match |
| 12936 | 918180338 | `component::midea::entity::select::oscillation_mode::state::tilting` | Tilting | Lutning | Core-literal match |
| 12937 | 918180337 | `component::midea::entity::select::oscillation_mode::state::reserved` | Reserved | Reserverad | Core-literal match |
| 12938 | 918180336 | `component::midea::entity::select::oscillation_mode::state::oscillation` | Oscillation | Svängning | Core-literal match |
| 12939 | 918180335 | `component::midea::entity::select::oscillation_mode::state::off` | Off | Av | Core-literal match |
| 12940 | 918180334 | `component::midea::entity::select::oscillation_mode::state::curve_w` | Curve W | Kurva W | Core-literal match |
| 12941 | 918180333 | `component::midea::entity::select::oscillation_mode::state::curve_8` | Curve 8 | Kurva 8 | Core-literal match |
| 12942 | 918180332 | `component::midea::entity::select::oscillation_mode::state::both` | Both | Båda | Core-literal match |
| 12943 | 918180331 | `component::midea::entity::select::oscillation_mode::name` | Oscillation mode | Oscillationsläge | Core-literal match |
| 12944 | 918180330 | `component::midea::entity::select::oscillation_angle::state::off` | Off | Av | Core-literal match |
| 12945 | 918180329 | `component::midea::entity::select::oscillation_angle::name` | Oscillation angle | Oscillationsvinkel | Core-literal match |
| 12946 | 918180328 | `component::midea::entity::select::mode::state::standby` | Standby | Standby | Core-literal match |
| 12947 | 918180327 | `component::midea::entity::select::mode::state::smoke` | Smoke | Rök | Core-literal match |
| 12948 | 918180326 | `component::midea::entity::select::mode::state::sleep` | Sleep | Sömn | Core-literal match |
| 12949 | 918180325 | `component::midea::entity::select::mode::state::manual` | Manual | Manuell | Core-literal match |
| 12950 | 918180324 | `component::midea::entity::select::mode::state::fast` | Fast | Snabb | Core-literal match |
| 12951 | 918180323 | `component::midea::entity::select::mode::state::auto` | Auto | Auto | Core-literal match |
| 12952 | 918180322 | `component::midea::entity::select::mode::name` | Mode | Läge | Core-literal match |
| 12953 | 918180321 | `component::midea::entity::select::fan_speed::state::standby` | Standby | Standby | Core-literal match |
| 12954 | 918180320 | `component::midea::entity::select::fan_speed::state::off` | Off | Av | Core-literal match |
| 12955 | 918180319 | `component::midea::entity::select::fan_speed::state::medium` | Medium | Medel | Core-literal match |
| 12956 | 918180318 | `component::midea::entity::select::fan_speed::state::lowest` | Lowest | Lägsta | Core-literal match |
| 12957 | 918180317 | `component::midea::entity::select::fan_speed::state::low` | Low | Låg | Core-literal match |
| 12958 | 918180316 | `component::midea::entity::select::fan_speed::state::high` | High | Hög | Core-literal match |
| 12959 | 918180315 | `component::midea::entity::select::fan_speed::state::auto` | Auto | Auto | Core-literal match |
| 12960 | 918180314 | `component::midea::entity::select::fan_speed::name` | Fan speed | Fläkthastighet | Core-literal match |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 918682093 | `component::tonewinner::config::abort::reconfigure_successful` | Reconfiguration was successful |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
