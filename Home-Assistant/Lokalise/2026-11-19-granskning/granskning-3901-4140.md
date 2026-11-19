# Home Assistant Core – granskning 3901–4140

Sortering: ”Last added” vid insamlingen. Inget har ändrats i Lokalise. Referenser vars mål inte finns i underlaget markeras för senare kontroll.

## 3901. `component::template::config::step::media_player::data_description::turn_off`

**Engelska:** Defines actions to run when the media player is turned off.

**Befintlig svenska:** Anger vilka åtgärder som ska utföras när mediaspelaren stängs av.

**Bedömning:** Ingen ändring föreslås.

## 3902. `component::template::config::step::media_player::data_description::state`

**Engelska:** Defines a template to get the state of the media player. Valid values are `off`, `on`, `idle`, `playing`, `paused`, and `buffering`. If not set, the state is optimistic and follows the actions.

**Befintlig svenska:** Definierar en mall för att hämta mediaspelarens status. Giltiga värden är `av`, `på`, `vilar`, `spelar`, `pausad` och `buffrar`. Om inget värde anges är statusen optimistisk och följer åtgärderna.

**Förslag:** Definierar en mall som anger mediespelarens tillstånd. Giltiga värden är `off`, `on`, `idle`, `playing`, `paused` och `buffering`. Om mallen inte anges är tillståndet optimistiskt och följer åtgärderna.

## 3903. `component::template::config::step::media_player::data_description::source_list`

**Engelska:** Defines a template to get the list of sources supported by the media player.

**Befintlig svenska:** Definierar en mall för att hämta listan över källor som stöds av mediaspelaren.

**Bedömning:** Ingen ändring föreslås.

## 3904. `component::template::config::step::media_player::data_description::source`

**Engelska:** Defines a template to get the current source of the media player. The source must be in the source list.

**Befintlig svenska:** Definierar en mall för att hämta mediaspelarens aktuella källa. Källan måste finnas med i källförteckningen.

**Bedömning:** Ingen ändring föreslås.

## 3905. `component::template::config::step::media_player::data_description::select_source`

**Engelska:** Defines actions to run when the media player is given a command to select a source. Receives variable `source`. Requires a source list.

**Befintlig svenska:** Definierar åtgärder som ska utföras när mediaspelaren får ett kommando att välja en källa. Tar emot variabeln `source`. Kräver en källförteckning.

**Bedömning:** Ingen ändring föreslås.

## 3906. `component::template::config::step::media_player::data_description::media_stop`

**Engelska:** Defines actions to run when the media player is stopped.

**Befintlig svenska:** Anger vilka åtgärder som ska utföras när mediaspelaren stoppas.

**Bedömning:** Ingen ändring föreslås.

## 3907. `component::template::config::step::media_player::data_description::media_previous_track`

**Engelska:** Defines actions to run when the media player is given a 'Previous track' command.

**Befintlig svenska:** Definierar åtgärder som ska utföras när mediaspelaren får kommandot ”Föregående spår”.

**Bedömning:** Ingen ändring föreslås.

## 3908. `component::template::config::step::media_player::data_description::media_play`

**Engelska:** Defines actions to run when the media player is given a 'Play' command.

**Befintlig svenska:** Definierar åtgärder som ska utföras när mediaspelaren får kommandot ”Spela upp”.

**Bedömning:** Ingen ändring föreslås.

## 3909. `component::template::config::step::media_player::data_description::media_pause`

**Engelska:** Defines actions to run when the media player is paused.

**Befintlig svenska:** Definierar åtgärder som ska utföras när mediaspelaren pausas.

**Bedömning:** Ingen ändring föreslås.

## 3910. `component::template::config::step::media_player::data_description::media_next_track`

**Engelska:** Defines actions to run when the media player is given a 'Next track' command.

**Befintlig svenska:** Definierar åtgärder som ska utföras när mediaspelaren får kommandot ”Nästa spår”.

**Bedömning:** Ingen ändring föreslås.

## 3911. `component::template::config::step::media_player::data_description::is_volume_muted`

**Engelska:** Defines a template to get whether the media player is muted.

**Befintlig svenska:** Definierar en mall för att avgöra om mediaspelarens ljud är avstängt.

**Bedömning:** Ingen ändring föreslås.

## 3912. `component::template::config::step::media_player::data_description::device_id`

**Engelska:** [%key:component::template::common::device_id_description%]

**Befintlig svenska:** [%key:component::template::common::device_id_description%]

**Bedömning:** Ingen ändring föreslås.

## 3913. `component::template::config::step::media_player::data::volume_up`

**Engelska:** Actions on volume up

**Befintlig svenska:** Åtgärder vid volymökning

**Bedömning:** Ingen ändring föreslås.

## 3914. `component::template::config::step::media_player::data::volume_set`

**Engelska:** Actions on set volume

**Befintlig svenska:** Åtgärder vid inställd volym

**Förslag:** Åtgärder vid inställning av volym

## 3915. `component::template::config::step::media_player::data::volume_mute`

**Engelska:** Actions on mute

**Befintlig svenska:** Åtgärder vid ljudavstängning

**Bedömning:** Ingen ändring föreslås.

## 3916. `component::template::config::step::media_player::data::volume_level`

**Engelska:** Volume level

**Befintlig svenska:** Volymnivå

**Bedömning:** Ingen ändring föreslås.

## 3917. `component::template::config::step::media_player::data::volume_down`

**Engelska:** Actions on volume down

**Befintlig svenska:** Åtgärder vid volymsänkning

**Bedömning:** Ingen ändring föreslås.

## 3918. `component::template::config::step::media_player::data::turn_on`

**Engelska:** [%key:component::template::common::turn_on%]

**Befintlig svenska:** Åtgärder vid påslagning

**Kontextkontroll:** Kontrollera referensmålet `component::template::common::turn_on`; det ingår ännu inte i det insamlade underlaget.

## 3919. `component::template::config::step::media_player::data::turn_off`

**Engelska:** [%key:component::template::common::turn_off%]

**Befintlig svenska:** Åtgärder vid avstängning

**Kontextkontroll:** Kontrollera referensmålet `component::template::common::turn_off`; det ingår ännu inte i det insamlade underlaget.

## 3920. `component::template::config::step::media_player::data::state`

**Engelska:** [%key:component::template::common::state%]

**Befintlig svenska:** Tillstånd

**Kontextkontroll:** Kontrollera referensmålet `component::template::common::state`; det ingår ännu inte i det insamlade underlaget.

## 3921. `component::template::config::step::media_player::data::source_list`

**Engelska:** Source list

**Befintlig svenska:** Källista

**Bedömning:** Ingen ändring föreslås.

## 3922. `component::template::config::step::media_player::data::source`

**Engelska:** Source

**Befintlig svenska:** Källa

**Bedömning:** Ingen ändring föreslås.

## 3923. `component::template::config::step::media_player::data::select_source`

**Engelska:** Actions on select source

**Befintlig svenska:** Åtgärder vid val av källa

**Bedömning:** Ingen ändring föreslås.

## 3924. `component::template::config::step::media_player::data::name`

**Engelska:** [%key:common::config_flow::data::name%]

**Befintlig svenska:** Namn

**Kontextkontroll:** Kontrollera referensmålet `common::config_flow::data::name`; det ingår ännu inte i det insamlade underlaget.

## 3925. `component::template::config::step::media_player::data::media_stop`

**Engelska:** Actions on stop

**Befintlig svenska:** Åtgärder vid stopp

**Bedömning:** Ingen ändring föreslås.

## 3926. `component::template::config::step::media_player::data::media_previous_track`

**Engelska:** Actions on previous track

**Befintlig svenska:** Åtgärder vid föregående spår

**Bedömning:** Ingen ändring föreslås.

## 3927. `component::template::config::step::media_player::data::media_play`

**Engelska:** Actions on play

**Befintlig svenska:** Åtgärder vid uppspelning

**Bedömning:** Ingen ändring föreslås.

## 3928. `component::template::config::step::media_player::data::media_pause`

**Engelska:** Actions on pause

**Befintlig svenska:** Åtgärder vid paus

**Bedömning:** Ingen ändring föreslås.

## 3929. `component::template::config::step::media_player::data::media_next_track`

**Engelska:** Actions on next track

**Befintlig svenska:** Åtgärder vid nästa spår

**Bedömning:** Ingen ändring föreslås.

## 3930. `component::template::config::step::media_player::data::is_volume_muted`

**Engelska:** Muted

**Befintlig svenska:** Ljud av

**Bedömning:** Ingen ändring föreslås.

## 3931. `component::template::config::step::media_player::data::device_id`

**Engelska:** [%key:common::config_flow::data::device%]

**Befintlig svenska:** [%key:common::config_flow::data::device%]

**Bedömning:** Ingen ändring föreslås.

## 3932. `component::template::config::step::media_player::data::device_class`

**Engelska:** [%key:component::template::common::device_class%]

**Befintlig svenska:** [%key:component::template::common::device_class%]

**Bedömning:** Ingen ändring föreslås.

## 3933. `component::template::config::error::volume_up_and_down_required`

**Engelska:** Volume up and volume down actions must be set together.

**Befintlig svenska:** Åtgärder för att höja och sänka volymen måste ställas in tillsammans.

**Bedömning:** Ingen ändring föreslås.

## 3934. `component::template::config::error::source_list_required`

**Engelska:** A source list is required when a source or the select source actions are set.

**Befintlig svenska:** En källförteckning krävs när en källa eller åtgärderna för val av källa har angetts.

**Bedömning:** Ingen ändring föreslås.

## 3935. `component::libresync::exceptions::not_connected::message`

**Engelska:** The hub is not connected, so the command was not sent.

**Befintlig svenska:** Hubben är inte ansluten, så kommandot skickades inte.

**Bedömning:** Ingen ändring föreslås.

## 3936. `component::libresync::exceptions::not_confirmed::message`

**Engelska:** The hub did not confirm the command in time, so it may not have taken effect.

**Befintlig svenska:** Hubben bekräftade inte kommandot i tid, så det kan hända att det inte trädde i kraft.

**Bedömning:** Ingen ändring föreslås.

## 3937. `component::libresync::exceptions::invalid_source::message`

**Engelska:** The hub has no source named {source}.

**Befintlig svenska:** Hubben har ingen källa med namnet {source}.

**Bedömning:** Ingen ändring föreslås.

## 3938. `component::libresync::exceptions::cannot_connect::message`

**Engelska:** The hub at {host} did not answer on ports 50006 and 7777.

**Befintlig svenska:** Hubben på {host} svarade inte på portarna 50006 och 7777.

**Bedömning:** Ingen ändring föreslås.

## 3939. `component::libresync::entity::media_player::hub::state_attributes::source::state::usb`

**Engelska:** USB

**Befintlig svenska:** USB

**Bedömning:** Ingen ändring föreslås.

## 3940. `component::libresync::entity::media_player::hub::state_attributes::source::state::streaming`

**Engelska:** Streaming

**Befintlig svenska:** Streaming

**Bedömning:** Ingen ändring föreslås.

## 3941. `component::libresync::entity::media_player::hub::state_attributes::source::state::pc_mac`

**Engelska:** PC/Mac

**Befintlig svenska:** PC/Mac

**Bedömning:** Ingen ändring föreslås.

## 3942. `component::libresync::entity::media_player::hub::state_attributes::source::state::optical_3`

**Engelska:** Optical 3

**Befintlig svenska:** Optisk 3

**Bedömning:** Ingen ändring föreslås.

## 3943. `component::libresync::entity::media_player::hub::state_attributes::source::state::optical_2`

**Engelska:** Optical 2

**Befintlig svenska:** Optisk 2

**Bedömning:** Ingen ändring föreslås.

## 3944. `component::libresync::entity::media_player::hub::state_attributes::source::state::optical_1`

**Engelska:** Optical 1

**Befintlig svenska:** Optisk 1

**Bedömning:** Ingen ändring föreslås.

## 3945. `component::libresync::entity::media_player::hub::state_attributes::source::state::line`

**Engelska:** Line

**Befintlig svenska:** Linje

**Bedömning:** Ingen ändring föreslås.

## 3946. `component::libresync::entity::media_player::hub::state_attributes::source::state::hdmi`

**Engelska:** HDMI

**Befintlig svenska:** HDMI

**Bedömning:** Ingen ändring föreslås.

## 3947. `component::libresync::entity::media_player::hub::state_attributes::source::state::earc`

**Engelska:** eARC

**Befintlig svenska:** eARC

**Bedömning:** Ingen ändring föreslås.

## 3948. `component::libresync::entity::media_player::hub::state_attributes::source::state::coaxial`

**Engelska:** Coaxial

**Befintlig svenska:** Koaxial

**Bedömning:** Ingen ändring föreslås.

## 3949. `component::libresync::entity::media_player::hub::state_attributes::source::state::bluetooth`

**Engelska:** Bluetooth

**Befintlig svenska:** Bluetooth

**Bedömning:** Ingen ändring föreslås.

## 3950. `component::libresync::entity::media_player::hub::state_attributes::source::state::aux`

**Engelska:** AUX

**Befintlig svenska:** AUX

**Bedömning:** Ingen ändring föreslås.

## 3951. `component::libresync::config::step::user::data_description::host`

**Engelska:** The hostname or IP address of the hub, for example 192.168.1.50.

**Befintlig svenska:** Hubbens värdnamn eller IP-adress, till exempel 192.168.1.50.

**Bedömning:** Ingen ändring föreslås.

## 3952. `component::libresync::config::step::user::data::host`

**Engelska:** [%key:common::config_flow::data::host%]

**Befintlig svenska:** [%key:common::config_flow::data::host%]

**Bedömning:** Ingen ändring föreslås.

## 3953. `component::libresync::config::step::discovery_confirm::description`

**Engelska:** Do you want to set up {name}?

**Befintlig svenska:** Vill du konfigurera {name}?

**Bedömning:** Ingen ändring föreslås.

## 3954. `component::libresync::config::error::no_identity`

**Engelska:** The hub answers, but its UPnP service on port 38400 does not, so it cannot identify itself. Check that nothing blocks that port, then unplug the hub from the mains, plug it back in, wait a minute, and try again.

**Befintlig svenska:** Hubben svarar, men dess UPnP-tjänst på port 38400 gör det inte och kan därför inte identifiera sig. Kontrollera att inget blockerar porten. Koppla sedan ur hubben från elnätet, anslut den igen, vänta en minut och försök på nytt.

**Förslag:** Hubben svarar, men dess UPnP-tjänst på port 38400 svarar inte, så hubben kan inte identifiera sig. Kontrollera att inget blockerar porten. Koppla sedan ur hubben från elnätet, anslut den igen, vänta en minut och försök på nytt.

## 3955. `component::libresync::config::error::cannot_connect`

**Engelska:** [%key:common::config_flow::error::cannot_connect%]

**Befintlig svenska:** [%key:common::config_flow::error::cannot_connect%]

**Bedömning:** Ingen ändring föreslås.

## 3956. `component::libresync::config::abort::cannot_connect`

**Engelska:** [%key:common::config_flow::error::cannot_connect%]

**Befintlig svenska:** [%key:common::config_flow::error::cannot_connect%]

**Bedömning:** Ingen ändring föreslås.

## 3957. `component::libresync::config::abort::already_configured`

**Engelska:** [%key:common::config_flow::abort::already_configured_device%]

**Befintlig svenska:** [%key:common::config_flow::abort::already_configured_device%]

**Bedömning:** Ingen ändring föreslås.

## 3958. `component::sofar::entity::event::fault::state_attributes::occurred_at::name`

**Engelska:** Occurred at

**Befintlig svenska:** Inträffade

**Bedömning:** Ingen ändring föreslås.

## 3959. `component::sofar::entity::event::fault::state_attributes::fault_id::name`

**Engelska:** Fault ID

**Befintlig svenska:** Fel-ID

**Bedömning:** Ingen ändring föreslås.

## 3960. `component::sofar::entity::event::fault::state_attributes::event_type::state::wrong_input_mode_setting`

**Engelska:** Wrong input mode setting

**Befintlig svenska:** Felaktig inställning av ingångsläge

**Bedömning:** Ingen ändring föreslås.

## 3961. `component::sofar::entity::event::fault::state_attributes::event_type::state::wifi_fault`

**Engelska:** Wi-Fi fault

**Befintlig svenska:** Wi-Fi-fel

**Bedömning:** Ingen ändring föreslås.

## 3962. `component::sofar::entity::event::fault::state_attributes::event_type::state::weak_light_detection_failure`

**Engelska:** Low light detection failure

**Befintlig svenska:** Fel vid detektering av svagt ljus

**Bedömning:** Ingen ändring föreslås.

## 3963. `component::sofar::entity::event::fault::state_attributes::event_type::state::wave_by_wave_current_limit`

**Engelska:** Wave-by-wave current limit

**Befintlig svenska:** Strömbegränsning våg för våg

**Bedömning:** Ingen ändring föreslås.

## 3964. `component::sofar::entity::event::fault::state_attributes::event_type::state::voltage_loading`

**Engelska:** Voltage load increase

**Befintlig svenska:** Ökad spänningsbelastning

**Bedömning:** Ingen ändring föreslås.

## 3965. `component::sofar::entity::event::fault::state_attributes::event_type::state::voltage_down_load`

**Engelska:** Voltage derating

**Befintlig svenska:** Effektreducering på grund av spänning

**Bedömning:** Ingen ändring föreslås.

## 3966. `component::sofar::entity::event::fault::state_attributes::event_type::state::usb_fault`

**Engelska:** USB fault

**Befintlig svenska:** USB-fel

**Bedömning:** Ingen ändring föreslås.

## 3967. `component::sofar::entity::event::fault::state_attributes::event_type::state::sudden_grid_phase_change`

**Engelska:** Grid phase jump

**Befintlig svenska:** Plötslig fasändring i elnätet

**Bedömning:** Ingen ändring föreslås.

## 3968. `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_9_2`

**Engelska:** String 9 fuse 2 open circuit

**Befintlig svenska:** Avbrott i säkring 2 för sträng 9

**Bedömning:** Ingen ändring föreslås.

## 3969. `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_9_1`

**Engelska:** String 9 fuse 1 open circuit

**Befintlig svenska:** Avbrott i säkring 1 för sträng 9

**Bedömning:** Ingen ändring föreslås.

## 3970. `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_8_2`

**Engelska:** String 8 fuse 2 open circuit

**Befintlig svenska:** Avbrott i säkring 2 för sträng 8

**Bedömning:** Ingen ändring föreslås.

## 3971. `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_8_1`

**Engelska:** String 8 fuse 1 open circuit

**Befintlig svenska:** Avbrott i säkring 1 för sträng 8

**Bedömning:** Ingen ändring föreslås.

## 3972. `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_7_2`

**Engelska:** String 7 fuse 2 open circuit

**Befintlig svenska:** Avbrott i säkring 1 för sträng 8

**Förslag:** Avbrott i säkring 2 för sträng 7

## 3973. `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_7_1`

**Engelska:** String 7 fuse 1 open circuit

**Befintlig svenska:** Avbrott i säkring 2 för sträng 7

**Förslag:** Avbrott i säkring 1 för sträng 7

## 3974. `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_6_2`

**Engelska:** String 6 fuse 2 open circuit

**Befintlig svenska:** Avbrott i säkring 1 för sträng 7

**Förslag:** Avbrott i säkring 2 för sträng 6

## 3975. `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_6_1`

**Engelska:** String 6 fuse 1 open circuit

**Befintlig svenska:** Avbrott i säkring 2 för sträng 6

**Förslag:** Avbrott i säkring 1 för sträng 6

## 3976. `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_5_2`

**Engelska:** String 5 fuse 2 open circuit

**Befintlig svenska:** Avbrott i säkring 1 för sträng 6

**Förslag:** Avbrott i säkring 2 för sträng 5

## 3977. `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_5_1`

**Engelska:** String 5 fuse 1 open circuit

**Befintlig svenska:** Avbrott i säkring 2 för sträng 5

**Förslag:** Avbrott i säkring 1 för sträng 5

## 3978. `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_4_2`

**Engelska:** String 4 fuse 2 open circuit

**Befintlig svenska:** Avbrott i säkring 1 för sträng 5

**Förslag:** Avbrott i säkring 2 för sträng 4

## 3979. `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_4_1`

**Engelska:** String 4 fuse 1 open circuit

**Befintlig svenska:** Avbrott i säkring 2 för sträng 4

**Förslag:** Avbrott i säkring 1 för sträng 4

## 3980. `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_3_2`

**Engelska:** String 3 fuse 2 open circuit

**Befintlig svenska:** Avbrott i säkring 1 för sträng 4

**Förslag:** Avbrott i säkring 2 för sträng 3

## 3981. `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_3_1`

**Engelska:** String 3 fuse 1 open circuit

**Befintlig svenska:** Avbrott i säkring 2 för sträng 3

**Förslag:** Avbrott i säkring 1 för sträng 3

## 3982. `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_2_2`

**Engelska:** String 2 fuse 2 open circuit

**Befintlig svenska:** Avbrott i säkring 1 för sträng 3

**Förslag:** Avbrott i säkring 2 för sträng 2

## 3983. `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_2_1`

**Engelska:** String 2 fuse 1 open circuit

**Befintlig svenska:** Avbrott i säkring 2 för sträng 2

**Förslag:** Avbrott i säkring 1 för sträng 2

## 3984. `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_1_2`

**Engelska:** String 1 fuse 2 open circuit

**Befintlig svenska:** Avbrott i säkring 1 för sträng 2

**Förslag:** Avbrott i säkring 2 för sträng 1

## 3985. `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_1_1`

**Engelska:** String 1 fuse 1 open circuit

**Befintlig svenska:** Avbrott i säkring 2 för sträng 1

**Förslag:** Avbrott i säkring 1 för sträng 1

## 3986. `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_16_2`

**Engelska:** String 16 fuse 2 open circuit

**Befintlig svenska:** Avbrott i säkring 2 för sträng 16

**Bedömning:** Ingen ändring föreslås.

## 3987. `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_16_1`

**Engelska:** String 16 fuse 1 open circuit

**Befintlig svenska:** Avbrott i säkring 1 för sträng 16

**Bedömning:** Ingen ändring föreslås.

## 3988. `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_15_2`

**Engelska:** String 15 fuse 2 open circuit

**Befintlig svenska:** Avbrott i säkring 2 för sträng 15

**Bedömning:** Ingen ändring föreslås.

## 3989. `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_15_1`

**Engelska:** String 15 fuse 1 open circuit

**Befintlig svenska:** Avbrott i säkring 1 för sträng 15

**Bedömning:** Ingen ändring föreslås.

## 3990. `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_14_2`

**Engelska:** String 14 fuse 2 open circuit

**Befintlig svenska:** Avbrott i säkring 2 för sträng 14

**Bedömning:** Ingen ändring föreslås.

## 3991. `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_14_1`

**Engelska:** String 14 fuse 1 open circuit

**Befintlig svenska:** Avbrott i säkring 1 för sträng 14

**Bedömning:** Ingen ändring föreslås.

## 3992. `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_13_2`

**Engelska:** String 13 fuse 2 open circuit

**Befintlig svenska:** Avbrott i säkring 2 för sträng 13

**Bedömning:** Ingen ändring föreslås.

## 3993. `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_13_1`

**Engelska:** String 13 fuse 1 open circuit

**Befintlig svenska:** Avbrott i säkring 1 för sträng 13

**Bedömning:** Ingen ändring föreslås.

## 3994. `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_12_2`

**Engelska:** String 12 fuse 2 open circuit

**Befintlig svenska:** Avbrott i säkring 2 för sträng 12

**Bedömning:** Ingen ändring föreslås.

## 3995. `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_12_1`

**Engelska:** String 12 fuse 1 open circuit

**Befintlig svenska:** Avbrott i säkring 1 för sträng 12

**Bedömning:** Ingen ändring föreslås.

## 3996. `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_11_2`

**Engelska:** String 11 fuse 2 open circuit

**Befintlig svenska:** Avbrott i säkring 2 för sträng 11

**Bedömning:** Ingen ändring föreslås.

## 3997. `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_11_1`

**Engelska:** String 11 fuse 1 open circuit

**Befintlig svenska:** Avbrott i säkring 1 för sträng 11

**Bedömning:** Ingen ändring föreslås.

## 3998. `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_10_2`

**Engelska:** String 10 fuse 2 open circuit

**Befintlig svenska:** Avbrott i säkring 2 för sträng 10

**Bedömning:** Ingen ändring föreslås.

## 3999. `component::sofar::entity::event::fault::state_attributes::event_type::state::string_fuse_open_circuit_10_1`

**Engelska:** String 10 fuse 1 open circuit

**Befintlig svenska:** Avbrott i säkring 1 för sträng 10

**Bedömning:** Ingen ändring föreslås.

## 4000. `component::sofar::entity::event::fault::state_attributes::event_type::state::spi_communication_error_dc`

**Engelska:** SPI communication error (DC)

**Befintlig svenska:** SPI-kommunikationsfel (DC)

**Bedömning:** Ingen ändring föreslås.

## 4001. `component::sofar::entity::event::fault::state_attributes::event_type::state::spi_communication_error_ac`

**Engelska:** SPI communication error (AC)

**Befintlig svenska:** SPI-kommunikationsfel (AC)

**Bedömning:** Ingen ändring föreslås.

## 4002. `component::sofar::entity::event::fault::state_attributes::event_type::state::software_version_inconsistency`

**Engelska:** Software version inconsistency

**Befintlig svenska:** Programvaruversionerna stämmer inte överens

**Bedömning:** Ingen ändring föreslås.

## 4003. `component::sofar::entity::event::fault::state_attributes::event_type::state::serial_number_model_error`

**Engelska:** Serial number model error

**Befintlig svenska:** Fel i serienummermodell

**Bedömning:** Ingen ändring föreslås.

## 4004. `component::sofar::entity::event::fault::state_attributes::event_type::state::serial_number_error`

**Engelska:** Serial number error

**Befintlig svenska:** Fel i serienummer

**Bedömning:** Ingen ändring föreslås.

## 4005. `component::sofar::entity::event::fault::state_attributes::event_type::state::sci_error_fuse`

**Engelska:** SCI error (fuse)

**Befintlig svenska:** SCI-fel (säkring)

**Bedömning:** Ingen ändring föreslås.

## 4006. `component::sofar::entity::event::fault::state_attributes::event_type::state::sci_error_dc`

**Engelska:** SCI error (DC)

**Befintlig svenska:** SCI-fel (DC)

**Bedömning:** Ingen ändring föreslås.

## 4007. `component::sofar::entity::event::fault::state_attributes::event_type::state::sci_error_ac`

**Engelska:** SCI error (AC)

**Befintlig svenska:** SCI-fel (AC)

**Bedömning:** Ingen ändring föreslås.

## 4008. `component::sofar::entity::event::fault::state_attributes::event_type::state::safety_version_error`

**Engelska:** Safety version error

**Befintlig svenska:** Fel i säkerhetsversion

**Bedömning:** Ingen ändring föreslås.

## 4009. `component::sofar::entity::event::fault::state_attributes::event_type::state::rtc_clock_fault`

**Engelska:** RTC clock fault

**Befintlig svenska:** Fel i RTC-klocka

**Bedömning:** Ingen ändring föreslås.

## 4010. `component::sofar::entity::event::fault::state_attributes::event_type::state::resonance_protection`

**Engelska:** Resonance protection

**Befintlig svenska:** Resonansskydd

**Bedömning:** Ingen ändring föreslås.

## 4011. `component::sofar::entity::event::fault::state_attributes::event_type::state::remote_shutdown`

**Engelska:** Remote shutdown

**Befintlig svenska:** Fjärravstängning

**Bedömning:** Ingen ändring föreslås.

## 4012. `component::sofar::entity::event::fault::state_attributes::event_type::state::relay_permanent_failure`

**Engelska:** Relay permanent failure

**Befintlig svenska:** Bestående reläfel

**Bedömning:** Ingen ändring föreslås.

## 4013. `component::sofar::entity::event::fault::state_attributes::event_type::state::relay_detection_failure`

**Engelska:** Relay detection failure

**Befintlig svenska:** Reläidentifiering misslyckades

**Bedömning:** Ingen ändring föreslås.

## 4014. `component::sofar::entity::event::fault::state_attributes::event_type::state::pv_uneven_flow_fault`

**Engelska:** PV uneven current fault

**Befintlig svenska:** Fel med ojämn ström i PV

**Bedömning:** Ingen ändring föreslås.

## 4015. `component::sofar::entity::event::fault::state_attributes::event_type::state::pv_undervoltage`

**Engelska:** PV undervoltage

**Befintlig svenska:** PV-underspänning

**Bedömning:** Ingen ändring föreslås.

## 4016. `component::sofar::entity::event::fault::state_attributes::event_type::state::pv_transient_software_overcurrent`

**Engelska:** PV transient software overcurrent

**Befintlig svenska:** Tillfällig programvaruöverström i PV

**Bedömning:** Ingen ändring föreslås.

## 4017. `component::sofar::entity::event::fault::state_attributes::event_type::state::pv_software_overcurrent_protection`

**Engelska:** PV software overcurrent protection

**Befintlig svenska:** Programvaruskydd mot PV-överström

**Bedömning:** Ingen ändring föreslås.

## 4018. `component::sofar::entity::event::fault::state_attributes::event_type::state::pv_parallel_uneven_current`

**Engelska:** PV parallel uneven current

**Befintlig svenska:** Ojämn parallellström i PV

**Bedömning:** Ingen ändring föreslås.

## 4019. `component::sofar::entity::event::fault::state_attributes::event_type::state::pv_overvoltage`

**Engelska:** PV overvoltage

**Befintlig svenska:** PV-överspänning

**Bedömning:** Ingen ändring föreslås.

## 4020. `component::sofar::entity::event::fault::state_attributes::event_type::state::pv_low_impedance_to_ground`

**Engelska:** PV low impedance to ground

**Befintlig svenska:** Låg PV-impedans mot jord

**Bedömning:** Ingen ändring föreslås.

## 4021. `component::sofar::entity::event::fault::state_attributes::event_type::state::pv_hardware_overcurrent`

**Engelska:** PV hardware overcurrent

**Befintlig svenska:** Maskinvaruöverström i PV

**Bedömning:** Ingen ändring föreslås.

## 4022. `component::sofar::entity::event::fault::state_attributes::event_type::state::pv_branch_overcurrent_default_on`

**Engelska:** PV string overcurrent (default on)

**Befintlig svenska:** Överström i PV-sträng (på som standard)

**Bedömning:** Ingen ändring föreslås.

## 4023. `component::sofar::entity::event::fault::state_attributes::event_type::state::pv_branch_overcurrent_default_off`

**Engelska:** PV string overcurrent (default off)

**Befintlig svenska:** Överström i PV-sträng (av som standard)

**Bedömning:** Ingen ändring föreslås.

## 4024. `component::sofar::entity::event::fault::state_attributes::event_type::state::power_station_communication_failure_shutdown`

**Engelska:** Power station communication failure shutdown

**Befintlig svenska:** Avstängning på grund av kommunikationsfel med kraftstation

**Bedömning:** Ingen ändring föreslås.

## 4025. `component::sofar::entity::event::fault::state_attributes::event_type::state::plc_module_heartbeat_lost`

**Engelska:** PLC module heartbeat lost

**Befintlig svenska:** Pulssignal från PLC-modul saknas

**Bedömning:** Ingen ändring föreslås.

## 4026. `component::sofar::entity::event::fault::state_attributes::event_type::state::pid_repair_failure`

**Engelska:** PID repair failure

**Befintlig svenska:** Fel vid PID-reparation

**Bedömning:** Ingen ändring föreslås.

## 4027. `component::sofar::entity::event::fault::state_attributes::event_type::state::pid_abnormal_output`

**Engelska:** PID abnormal output

**Befintlig svenska:** Onormal PID-utgång

**Bedömning:** Ingen ändring föreslås.

## 4028. `component::sofar::entity::event::fault::state_attributes::event_type::state::phase_loss_failure`

**Engelska:** Phase loss failure

**Befintlig svenska:** Fasbortfall

**Bedömning:** Ingen ändring föreslås.

## 4029. `component::sofar::entity::event::fault::state_attributes::event_type::state::parallel_error`

**Engelska:** Parallel error

**Befintlig svenska:** Parallellfel

**Bedömning:** Ingen ändring föreslås.

## 4030. `component::sofar::entity::event::fault::state_attributes::event_type::state::overload_protection_3`

**Engelska:** Overload protection 3

**Befintlig svenska:** Överlastskydd 3

**Bedömning:** Ingen ändring föreslås.

## 4031. `component::sofar::entity::event::fault::state_attributes::event_type::state::overload_protection_2`

**Engelska:** Overload protection 2

**Befintlig svenska:** Överlastskydd 2

**Bedömning:** Ingen ändring föreslås.

## 4032. `component::sofar::entity::event::fault::state_attributes::event_type::state::overload_protection_1`

**Engelska:** Overload protection 1

**Befintlig svenska:** Överlastskydd 1

**Bedömning:** Ingen ändring föreslås.

## 4033. `component::sofar::entity::event::fault::state_attributes::event_type::state::over_temperature_load_shedding`

**Engelska:** Overtemperature derating

**Befintlig svenska:** Effektnedreglering vid övertemperatur

**Bedömning:** Ingen ändring föreslås.

## 4034. `component::sofar::entity::event::fault::state_attributes::event_type::state::output_transient_overcurrent_fault`

**Engelska:** Output transient overcurrent fault

**Befintlig svenska:** Fel med strömspik vid utgång

**Bedömning:** Ingen ändring föreslås.

## 4035. `component::sofar::entity::event::fault::state_attributes::event_type::state::output_transient_current_protection`

**Engelska:** Output transient current protection

**Befintlig svenska:** Skydd mot strömspik vid utgång

**Bedömning:** Ingen ändring föreslås.

## 4036. `component::sofar::entity::event::fault::state_attributes::event_type::state::output_current_unbalance`

**Engelska:** Output current unbalance

**Befintlig svenska:** Obalans i utgångsström

**Bedömning:** Ingen ändring föreslås.

## 4037. `component::sofar::entity::event::fault::state_attributes::event_type::state::neutral_ground_fault`

**Engelska:** Neutral ground fault

**Befintlig svenska:** Fel mellan neutralledare och jord

**Bedömning:** Ingen ändring föreslås.

## 4038. `component::sofar::entity::event::fault::state_attributes::event_type::state::network_voltage_sampling_error_dc`

**Engelska:** Grid voltage sampling error (DC)

**Befintlig svenska:** Samplingsfel för nätspänning (DC)

**Bedömning:** Ingen ändring föreslås.

## 4039. `component::sofar::entity::event::fault::state_attributes::event_type::state::network_voltage_sampling_error_ac`

**Engelska:** Grid voltage sampling error (AC)

**Befintlig svenska:** Samplingsfel för nätspänning (AC)

**Bedömning:** Ingen ändring föreslås.

## 4040. `component::sofar::entity::event::fault::state_attributes::event_type::state::net_voltage_consistency_error`

**Engelska:** Grid voltage consistency error

**Befintlig svenska:** Konsistensfel för nätspänning

**Bedömning:** Ingen ändring föreslås.

## 4041. `component::sofar::entity::event::fault::state_attributes::event_type::state::n_line_open_circuit_fault`

**Engelska:** Neutral line open circuit

**Befintlig svenska:** Avbrott i neutralledaren

**Bedömning:** Ingen ändring föreslås.

## 4042. `component::sofar::entity::event::fault::state_attributes::event_type::state::module_temperature_difference_too_large`

**Engelska:** Module temperature difference too large

**Befintlig svenska:** Temperaturskillnaden mellan modulerna är för stor

**Bedömning:** Ingen ändring föreslås.

## 4043. `component::sofar::entity::event::fault::state_attributes::event_type::state::module_3_temperature_protection`

**Engelska:** Module 3 temperature protection

**Befintlig svenska:** Temperaturskydd för modul 3

**Bedömning:** Ingen ändring föreslås.

## 4044. `component::sofar::entity::event::fault::state_attributes::event_type::state::module_2_temperature_protection`

**Engelska:** Module 2 temperature protection

**Befintlig svenska:** Temperaturskydd för modul 2

**Bedömning:** Ingen ändring föreslås.

## 4045. `component::sofar::entity::event::fault::state_attributes::event_type::state::module_1_temperature_protection`

**Engelska:** Module 1 temperature protection

**Befintlig svenska:** Temperaturskydd för modul 1

**Bedömning:** Ingen ändring föreslås.

## 4046. `component::sofar::entity::event::fault::state_attributes::event_type::state::modify_ovp`

**Engelska:** OVP modified

**Befintlig svenska:** OVP har ändrats

**Bedömning:** Ingen ändring föreslås.

## 4047. `component::sofar::entity::event::fault::state_attributes::event_type::state::meter_communication_error`

**Engelska:** Meter communication error

**Befintlig svenska:** Kommunikationsfel med mätare

**Bedömning:** Ingen ändring föreslås.

## 4048. `component::sofar::entity::event::fault::state_attributes::event_type::state::low_temperature_load_shedding`

**Engelska:** Low temperature derating

**Befintlig svenska:** Effektnedreglering vid låg temperatur

**Bedömning:** Ingen ändring föreslås.

## 4049. `component::sofar::entity::event::fault::state_attributes::event_type::state::low_penetration_error`

**Engelska:** Low voltage ride-through error

**Befintlig svenska:** Fel vid lågspänningsgenomgång

**Bedömning:** Ingen ändring föreslås.

## 4050. `component::sofar::entity::event::fault::state_attributes::event_type::state::low_insulation_impedance`

**Engelska:** Low insulation impedance

**Befintlig svenska:** Låg isolationsimpedans

**Bedömning:** Ingen ändring föreslås.

## 4051. `component::sofar::entity::event::fault::state_attributes::event_type::state::llcbus_overvoltage_protection`

**Engelska:** LLC bus overvoltage protection

**Befintlig svenska:** Överspänningsskydd för LLC-buss

**Bedömning:** Ingen ändring föreslås.

## 4052. `component::sofar::entity::event::fault::state_attributes::event_type::state::llc_busbar_hardware_overvoltage`

**Engelska:** LLC bus hardware overvoltage

**Befintlig svenska:** Maskinvaruöverspänning på LLC-buss

**Bedömning:** Ingen ändring föreslås.

## 4053. `component::sofar::entity::event::fault::state_attributes::event_type::state::lithium_battery_4_communication_failure`

**Engelska:** Lithium battery 4 communication failure

**Befintlig svenska:** Kommunikationsfel för litiumbatteri 4

**Bedömning:** Ingen ändring föreslås.

## 4054. `component::sofar::entity::event::fault::state_attributes::event_type::state::lithium_battery_3_communication_failure`

**Engelska:** Lithium battery 3 communication failure

**Befintlig svenska:** Kommunikationsfel för litiumbatteri 3

**Bedömning:** Ingen ändring föreslås.

## 4055. `component::sofar::entity::event::fault::state_attributes::event_type::state::lithium_battery_2_communication_failure`

**Engelska:** Lithium battery 2 communication failure

**Befintlig svenska:** Kommunikationsfel för litiumbatteri 2

**Bedömning:** Ingen ändring föreslås.

## 4056. `component::sofar::entity::event::fault::state_attributes::event_type::state::lithium_battery_1_communication_failure`

**Engelska:** Lithium battery 1 communication failure

**Befintlig svenska:** Kommunikationsfel för litiumbatteri 1

**Bedömning:** Ingen ändring föreslås.

## 4057. `component::sofar::entity::event::fault::state_attributes::event_type::state::lightning_protection_dc_permanent`

**Engelska:** Lightning protection permanent fault (DC)

**Befintlig svenska:** Bestående fel i åskskyddet (DC)

**Bedömning:** Ingen ändring föreslås.

## 4058. `component::sofar::entity::event::fault::state_attributes::event_type::state::lightning_protection_dc`

**Engelska:** Lightning protection (DC)

**Befintlig svenska:** Åskskydd (DC)

**Bedömning:** Ingen ändring föreslås.

## 4059. `component::sofar::entity::event::fault::state_attributes::event_type::state::lightning_protection_ac_permanent`

**Engelska:** Lightning protection permanent fault (AC)

**Befintlig svenska:** Bestående fel i åskskyddet (AC)

**Bedömning:** Ingen ändring föreslås.

## 4060. `component::sofar::entity::event::fault::state_attributes::event_type::state::lightning_protection_ac`

**Engelska:** Lightning protection (AC)

**Befintlig svenska:** Åskskydd (AC)

**Bedömning:** Ingen ändring föreslås.

## 4061. `component::sofar::entity::event::fault::state_attributes::event_type::state::leakage_current_faults`

**Engelska:** Leakage current fault

**Befintlig svenska:** Läckströmsfel

**Bedömning:** Ingen ändring föreslås.

## 4062. `component::sofar::entity::event::fault::state_attributes::event_type::state::leakage_current_consistency_error`

**Engelska:** Leakage current consistency error

**Befintlig svenska:** Konsistensfel för läckström

**Bedömning:** Ingen ändring föreslås.

## 4063. `component::sofar::entity::event::fault::state_attributes::event_type::state::islanding_error`

**Engelska:** Islanding error

**Befintlig svenska:** Ödriftsfel

**Bedömning:** Ingen ändring föreslås.

## 4064. `component::sofar::entity::event::fault::state_attributes::event_type::state::inverter_voltage_error`

**Engelska:** Inverter voltage error

**Befintlig svenska:** Spänningsfel i växelriktare

**Bedömning:** Ingen ändring föreslås.

## 4065. `component::sofar::entity::event::fault::state_attributes::event_type::state::inverter_transient_overvoltage`

**Engelska:** Inverter transient overvoltage

**Befintlig svenska:** Tillfällig överspänning i växelriktare

**Bedömning:** Ingen ändring föreslås.

## 4066. `component::sofar::entity::event::fault::state_attributes::event_type::state::inverter_soft_start_failure_fault`

**Engelska:** Inverter soft start failure fault

**Befintlig svenska:** Fel vid mjukstart av växelriktare

**Bedömning:** Ingen ändring föreslås.

## 4067. `component::sofar::entity::event::fault::state_attributes::event_type::state::inverter_soft_start_failure`

**Engelska:** Inverter soft start failure

**Befintlig svenska:** Fel vid mjukstart av växelriktare

**Bedömning:** Ingen ändring föreslås.

## 4068. `component::sofar::entity::event::fault::state_attributes::event_type::state::inverter_rms_current_protection`

**Engelska:** Inverter RMS current protection

**Befintlig svenska:** RMS-strömskydd för växelriktare

**Bedömning:** Ingen ändring föreslås.

## 4069. `component::sofar::entity::event::fault::state_attributes::event_type::state::inverter_bus_hardware_overvoltage`

**Engelska:** Inverter bus hardware overvoltage

**Befintlig svenska:** Maskinvaruöverspänning på växelriktarens likströmsbuss

**Bedömning:** Ingen ändring föreslås.

## 4070. `component::sofar::entity::event::fault::state_attributes::event_type::state::input_reversal_error`

**Engelska:** Input reversal error

**Befintlig svenska:** Felaktig polaritet vid ingång

**Bedömning:** Ingen ändring föreslås.

## 4071. `component::sofar::entity::event::fault::state_attributes::event_type::state::input_overcurrent_fault`

**Engelska:** Input overcurrent fault

**Befintlig svenska:** Överströmsfel vid ingång

**Bedömning:** Ingen ändring föreslås.

## 4072. `component::sofar::entity::event::fault::state_attributes::event_type::state::input_mode_setting_fault`

**Engelska:** Input mode setting fault

**Befintlig svenska:** Fel i inställning av ingångsläge

**Bedömning:** Ingen ändring föreslås.

## 4073. `component::sofar::entity::event::fault::state_attributes::event_type::state::input_hardware_overcurrent_fault`

**Engelska:** Input hardware overcurrent fault

**Befintlig svenska:** Maskinvaruöverström vid ingång

**Bedömning:** Ingen ändring föreslås.

## 4074. `component::sofar::entity::event::fault::state_attributes::event_type::state::input_fuse_open_circuit_9`

**Engelska:** Input fuse 9 open circuit

**Befintlig svenska:** Avbrott i ingångssäkring 9

**Bedömning:** Ingen ändring föreslås.

## 4075. `component::sofar::entity::event::fault::state_attributes::event_type::state::input_fuse_open_circuit_8`

**Engelska:** Input fuse 8 open circuit

**Befintlig svenska:** Avbrott i ingångssäkring 8

**Bedömning:** Ingen ändring föreslås.

## 4076. `component::sofar::entity::event::fault::state_attributes::event_type::state::input_fuse_open_circuit_7`

**Engelska:** Input fuse 7 open circuit

**Befintlig svenska:** Avbrott i ingångssäkring 7

**Bedömning:** Ingen ändring föreslås.

## 4077. `component::sofar::entity::event::fault::state_attributes::event_type::state::input_fuse_open_circuit_6`

**Engelska:** Input fuse 6 open circuit

**Befintlig svenska:** Avbrott i ingångssäkring 6

**Bedömning:** Ingen ändring föreslås.

## 4078. `component::sofar::entity::event::fault::state_attributes::event_type::state::input_fuse_open_circuit_5`

**Engelska:** Input fuse 5 open circuit

**Befintlig svenska:** Avbrott i ingångssäkring 5

**Bedömning:** Ingen ändring föreslås.

## 4079. `component::sofar::entity::event::fault::state_attributes::event_type::state::input_fuse_open_circuit_4`

**Engelska:** Input fuse 4 open circuit

**Befintlig svenska:** Avbrott i ingångssäkring 4

**Bedömning:** Ingen ändring föreslås.

## 4080. `component::sofar::entity::event::fault::state_attributes::event_type::state::input_fuse_open_circuit_3`

**Engelska:** Input fuse 3 open circuit

**Befintlig svenska:** Avbrott i ingångssäkring 3

**Bedömning:** Ingen ändring föreslås.

## 4081. `component::sofar::entity::event::fault::state_attributes::event_type::state::input_fuse_open_circuit_2`

**Engelska:** Input fuse 2 open circuit

**Befintlig svenska:** Avbrott i ingångssäkring 2

**Bedömning:** Ingen ändring föreslås.

## 4082. `component::sofar::entity::event::fault::state_attributes::event_type::state::input_fuse_open_circuit_15`

**Engelska:** Input fuse 15 open circuit

**Befintlig svenska:** Avbrott i ingångssäkring 15

**Bedömning:** Ingen ändring föreslås.

## 4083. `component::sofar::entity::event::fault::state_attributes::event_type::state::input_fuse_open_circuit_14`

**Engelska:** Input fuse 14 open circuit

**Befintlig svenska:** Avbrott i ingångssäkring 14

**Bedömning:** Ingen ändring föreslås.

## 4084. `component::sofar::entity::event::fault::state_attributes::event_type::state::input_fuse_open_circuit_13`

**Engelska:** Input fuse 13 open circuit

**Befintlig svenska:** Avbrott i ingångssäkring 13

**Bedömning:** Ingen ändring föreslås.

## 4085. `component::sofar::entity::event::fault::state_attributes::event_type::state::input_fuse_open_circuit_12`

**Engelska:** Input fuse 12 open circuit

**Befintlig svenska:** Avbrott i ingångssäkring 12

**Bedömning:** Ingen ändring föreslås.

## 4086. `component::sofar::entity::event::fault::state_attributes::event_type::state::input_fuse_open_circuit_11`

**Engelska:** Input fuse 11 open circuit

**Befintlig svenska:** Avbrott i ingångssäkring 11

**Bedömning:** Ingen ändring föreslås.

## 4087. `component::sofar::entity::event::fault::state_attributes::event_type::state::input_fuse_open_circuit_10`

**Engelska:** Input fuse 10 open circuit

**Befintlig svenska:** Avbrott i ingångssäkring 10

**Bedömning:** Ingen ändring föreslås.

## 4088. `component::sofar::entity::event::fault::state_attributes::event_type::state::input_fuse_open_circuit_1`

**Engelska:** Input fuse 1 open circuit

**Befintlig svenska:** Avbrott i ingångssäkring 1

**Bedömning:** Ingen ändring föreslås.

## 4089. `component::sofar::entity::event::fault::state_attributes::event_type::state::input_fuse_open_circuit_0`

**Engelska:** Input fuse 0 open circuit

**Befintlig svenska:** Avbrott i ingångssäkring 0

**Bedömning:** Ingen ändring föreslås.

## 4090. `component::sofar::entity::event::fault::state_attributes::event_type::state::input_current_sampling_error`

**Engelska:** Input current sampling error

**Befintlig svenska:** Samplingsfel för ingångsström

**Bedömning:** Ingen ändring föreslås.

## 4091. `component::sofar::entity::event::fault::state_attributes::event_type::state::high_penetration_error`

**Engelska:** High voltage ride-through error

**Befintlig svenska:** Fel vid högspänningsgenomgång

**Bedömning:** Ingen ändring föreslås.

## 4092. `component::sofar::entity::event::fault::state_attributes::event_type::state::heatsink_6_temperature_protection`

**Engelska:** Heatsink 6 temperature protection

**Befintlig svenska:** Temperaturskydd för kylfläns 6

**Bedömning:** Ingen ändring föreslås.

## 4093. `component::sofar::entity::event::fault::state_attributes::event_type::state::heatsink_5_temperature_protection`

**Engelska:** Heatsink 5 temperature protection

**Befintlig svenska:** Temperaturskydd för kylfläns 5

**Bedömning:** Ingen ändring föreslås.

## 4094. `component::sofar::entity::event::fault::state_attributes::event_type::state::heatsink_4_temperature_protection`

**Engelska:** Heatsink 4 temperature protection

**Befintlig svenska:** Temperaturskydd för kylfläns 4

**Bedömning:** Ingen ändring föreslås.

## 4095. `component::sofar::entity::event::fault::state_attributes::event_type::state::heatsink_3_temperature_protection`

**Engelska:** Heatsink 3 temperature protection

**Befintlig svenska:** Temperaturskydd för kylfläns 3

**Bedömning:** Ingen ändring föreslås.

## 4096. `component::sofar::entity::event::fault::state_attributes::event_type::state::heatsink_2_temperature_protection`

**Engelska:** Heatsink 2 temperature protection

**Befintlig svenska:** Temperaturskydd för kylfläns 2

**Bedömning:** Ingen ändring föreslås.

## 4097. `component::sofar::entity::event::fault::state_attributes::event_type::state::heatsink_1_temperature_protection`

**Engelska:** Heatsink 1 temperature protection

**Befintlig svenska:** Temperaturskydd för kylfläns 1

**Bedömning:** Ingen ändring föreslås.

## 4098. `component::sofar::entity::event::fault::state_attributes::event_type::state::hardware_version_mismatch`

**Engelska:** Hardware version mismatch

**Befintlig svenska:** Maskinvaruversionerna stämmer inte överens

**Bedömning:** Ingen ändring föreslås.

## 4099. `component::sofar::entity::event::fault::state_attributes::event_type::state::hardware_differential_overcurrent`

**Engelska:** Hardware differential overcurrent

**Befintlig svenska:** Differentiell maskinvaruöverström

**Bedömning:** Ingen ändring föreslås.

## 4100. `component::sofar::entity::event::fault::state_attributes::event_type::state::grounding_error`

**Engelska:** Grounding error

**Befintlig svenska:** Jordningsfel

**Bedömning:** Ingen ändring föreslås.

## 4101. `component::sofar::entity::event::fault::state_attributes::event_type::state::ground_zero_voltage_too_high`

**Engelska:** Neutral-to-ground voltage too high

**Befintlig svenska:** Spänningen mellan neutralledare och jord är för hög

**Bedömning:** Ingen ändring föreslås.

## 4102. `component::sofar::entity::event::fault::state_attributes::event_type::state::grid_voltage_unbalance`

**Engelska:** Grid voltage unbalance

**Befintlig svenska:** Obalans i nätspänning

**Bedömning:** Ingen ändring föreslås.

## 4103. `component::sofar::entity::event::fault::state_attributes::event_type::state::grid_undervoltage`

**Engelska:** Grid undervoltage

**Befintlig svenska:** Nätunderspänning

**Bedömning:** Ingen ändring föreslås.

## 4104. `component::sofar::entity::event::fault::state_attributes::event_type::state::grid_underfrequency`

**Engelska:** Grid underfrequency

**Befintlig svenska:** Underfrekvens i nätet

**Bedömning:** Ingen ändring föreslås.

## 4105. `component::sofar::entity::event::fault::state_attributes::event_type::state::grid_relay_fault`

**Engelska:** Grid relay fault

**Befintlig svenska:** Fel i nätrelä

**Bedömning:** Ingen ändring föreslås.

## 4106. `component::sofar::entity::event::fault::state_attributes::event_type::state::grid_overfrequency`

**Engelska:** Grid overfrequency

**Befintlig svenska:** Överfrekvens i nätet

**Bedömning:** Ingen ändring föreslås.

## 4107. `component::sofar::entity::event::fault::state_attributes::event_type::state::grid_over_voltage`

**Engelska:** Grid overvoltage

**Befintlig svenska:** Nätöverspänning

**Bedömning:** Ingen ändring föreslås.

## 4108. `component::sofar::entity::event::fault::state_attributes::event_type::state::grid_line_voltage_error`

**Engelska:** Grid line voltage error

**Befintlig svenska:** Fel i nätets linjespänning

**Bedömning:** Ingen ändring föreslås.

## 4109. `component::sofar::entity::event::fault::state_attributes::event_type::state::grid_instantaneous_value_overvoltage_2`

**Engelska:** Grid instantaneous overvoltage 2

**Befintlig svenska:** Momentan nätöverspänning 2

**Bedömning:** Ingen ändring föreslås.

## 4110. `component::sofar::entity::event::fault::state_attributes::event_type::state::grid_instantaneous_value_overvoltage_1`

**Engelska:** Grid instantaneous overvoltage 1

**Befintlig svenska:** Momentan nätöverspänning 1

**Bedömning:** Ingen ändring föreslås.

## 4111. `component::sofar::entity::event::fault::state_attributes::event_type::state::grid_frequency_change_protection`

**Engelska:** Grid frequency change protection

**Befintlig svenska:** Skydd mot nätfrekvensändring

**Bedömning:** Ingen ändring föreslås.

## 4112. `component::sofar::entity::event::fault::state_attributes::event_type::state::grid_current_sampling_error`

**Engelska:** Grid current sampling error

**Befintlig svenska:** Samplingsfel för nätström

**Bedömning:** Ingen ändring föreslås.

## 4113. `component::sofar::entity::event::fault::state_attributes::event_type::state::gfci_sampling_error_dc`

**Engelska:** GFCI sampling error (DC)

**Befintlig svenska:** GFCI-samplingsfel (DC)

**Bedömning:** Ingen ändring föreslås.

## 4114. `component::sofar::entity::event::fault::state_attributes::event_type::state::gfci_sampling_error_ac`

**Engelska:** GFCI sampling error (AC)

**Befintlig svenska:** GFCI-samplingsfel (AC)

**Bedömning:** Ingen ändring föreslås.

## 4115. `component::sofar::entity::event::fault::state_attributes::event_type::state::frequency_loading`

**Engelska:** Frequency load increase

**Befintlig svenska:** Frekvensstyrd lastökning

**Bedömning:** Ingen ändring föreslås.

## 4116. `component::sofar::entity::event::fault::state_attributes::event_type::state::frequency_down_load`

**Engelska:** Frequency derating

**Befintlig svenska:** Frekvensnedreglering

**Bedömning:** Ingen ändring föreslås.

## 4117. `component::sofar::entity::event::fault::state_attributes::event_type::state::forced_shutdown`

**Engelska:** Forced shutdown

**Befintlig svenska:** Tvingad avstängning

**Bedömning:** Ingen ändring föreslås.

## 4118. `component::sofar::entity::event::fault::state_attributes::event_type::state::fly_span_capacitor_under_voltage_protection`

**Engelska:** Flying capacitor undervoltage protection

**Befintlig svenska:** Underspänningsskydd för flygande kondensator

**Bedömning:** Ingen ändring föreslås.

## 4119. `component::sofar::entity::event::fault::state_attributes::event_type::state::fly_span_capacitor_overvoltage_protection`

**Engelska:** Flying capacitor overvoltage protection

**Befintlig svenska:** Överspänningsskydd för flygande kondensator

**Bedömning:** Ingen ändring föreslås.

## 4120. `component::sofar::entity::event::fault::state_attributes::event_type::state::fan_7_fault`

**Engelska:** Fan 7 fault

**Befintlig svenska:** Fel på fläkt 7

**Bedömning:** Ingen ändring föreslås.

## 4121. `component::sofar::entity::event::fault::state_attributes::event_type::state::fan_6_fault`

**Engelska:** Fan 6 fault

**Befintlig svenska:** Fel på fläkt 6

**Bedömning:** Ingen ändring föreslås.

## 4122. `component::sofar::entity::event::fault::state_attributes::event_type::state::fan_5_fault`

**Engelska:** Fan 5 fault

**Befintlig svenska:** Fel på fläkt 5

**Bedömning:** Ingen ändring föreslås.

## 4123. `component::sofar::entity::event::fault::state_attributes::event_type::state::fan_4_fault`

**Engelska:** Fan 4 fault

**Befintlig svenska:** Fel på fläkt 4

**Bedömning:** Ingen ändring föreslås.

## 4124. `component::sofar::entity::event::fault::state_attributes::event_type::state::fan_3_fault`

**Engelska:** Fan 3 fault

**Befintlig svenska:** Fel på fläkt 3

**Bedömning:** Ingen ändring föreslås.

## 4125. `component::sofar::entity::event::fault::state_attributes::event_type::state::fan_2_fault`

**Engelska:** Fan 2 fault

**Befintlig svenska:** Fel på fläkt 2

**Bedömning:** Ingen ändring föreslås.

## 4126. `component::sofar::entity::event::fault::state_attributes::event_type::state::fan_1_fault`

**Engelska:** Fan 1 fault

**Befintlig svenska:** Fel på fläkt 1

**Bedömning:** Ingen ändring föreslås.

## 4127. `component::sofar::entity::event::fault::state_attributes::event_type::state::eps_battery_overcurrent_fault`

**Engelska:** EPS battery overcurrent fault

**Befintlig svenska:** EPS-batteriöverströmsfel

**Bedömning:** Ingen ändring föreslås.

## 4128. `component::sofar::entity::event::fault::state_attributes::event_type::state::drms0_shutdown`

**Engelska:** DRM0 shutdown

**Befintlig svenska:** DRM0-avstängning

**Bedömning:** Ingen ändring föreslås.

## 4129. `component::sofar::entity::event::fault::state_attributes::event_type::state::dcv_sampling_error`

**Engelska:** DCV sampling error

**Befintlig svenska:** DCV-samplingsfel

**Bedömning:** Ingen ändring föreslås.

## 4130. `component::sofar::entity::event::fault::state_attributes::event_type::state::dci_sampling_error_dc`

**Engelska:** DCI sampling error (DC)

**Befintlig svenska:** DCI-samplingsfel (DC)

**Bedömning:** Ingen ändring föreslås.

## 4131. `component::sofar::entity::event::fault::state_attributes::event_type::state::dci_sampling_error_ac`

**Engelska:** DCI sampling error (AC)

**Befintlig svenska:** DCI-samplingsfel (AC)

**Bedömning:** Ingen ändring föreslås.

## 4132. `component::sofar::entity::event::fault::state_attributes::event_type::state::dci_overcurrent_protection`

**Engelska:** DCI overcurrent protection

**Befintlig svenska:** DCI-överströmsskydd

**Bedömning:** Ingen ändring föreslås.

## 4133. `component::sofar::entity::event::fault::state_attributes::event_type::state::dci_consistency_error`

**Engelska:** DCI consistency error

**Befintlig svenska:** DCI-konsistensfel

**Bedömning:** Ingen ändring föreslås.

## 4134. `component::sofar::entity::event::fault::state_attributes::event_type::state::dcdc_fault`

**Engelska:** DC/DC fault

**Befintlig svenska:** DC/DC-fel

**Bedömning:** Ingen ändring föreslås.

## 4135. `component::sofar::entity::event::fault::state_attributes::event_type::state::ct_error`

**Engelska:** CT error

**Befintlig svenska:** CT-fel

**Bedömning:** Ingen ändring föreslås.

## 4136. `component::sofar::entity::event::fault::state_attributes::event_type::state::communication_board_flash_error`

**Engelska:** Communication board flash error

**Befintlig svenska:** Flashfel på kommunikationskortet

**Bedömning:** Ingen ändring föreslås.

## 4137. `component::sofar::entity::event::fault::state_attributes::event_type::state::communication_board_eeprom_error`

**Engelska:** Communication board EEPROM error

**Befintlig svenska:** EEPROM-fel på kommunikationskortet

**Bedömning:** Ingen ändring föreslås.

## 4138. `component::sofar::entity::event::fault::state_attributes::event_type::state::combiner_uv_gp_9`

**Engelska:** Combiner group 9 undervoltage

**Befintlig svenska:** Låg spänning i samlingslådans grupp 9

**Bedömning:** Ingen ändring föreslås.

## 4139. `component::sofar::entity::event::fault::state_attributes::event_type::state::combiner_uv_gp_8`

**Engelska:** Combiner group 8 undervoltage

**Befintlig svenska:** Låg spänning i samlingslådans grupp 8

**Bedömning:** Ingen ändring föreslås.

## 4140. `component::sofar::entity::event::fault::state_attributes::event_type::state::combiner_uv_gp_7`

**Engelska:** Combiner group 7 undervoltage

**Befintlig svenska:** Låg spänning i samlingslådans grupp 7

**Bedömning:** Ingen ändring föreslås.
