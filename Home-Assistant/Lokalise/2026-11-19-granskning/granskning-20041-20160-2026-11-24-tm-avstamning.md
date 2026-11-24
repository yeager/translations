# Home Assistant Core – historisk avstämning 20041–20160

Alla 120 rader fanns i den tidigare radvisa granskningsrapporten. Aktuell källa och livevärden jämfördes igen från Lokalise-exporten 2026-11-24.

## Resultat

- 120/120 rader avstämda. 26 direkta källtexter matchar HA Core-källan; 81 referensanvändningar med 25 mål kontrollerades.
- Saknade referensmål: 0; referensmismatchar: 0; källtextavvikelser: 0; tomma värden: 0; platshållarmismatch: 0.
- 13 nycklar saknar direkt strängväg i aktuell Core-källa och dokumenteras för uppföljning.
- Samtliga 48 äldre förslag finns redan live; inga dubbla skrivningar behövdes.
- Alla 120 historiskt granskade poster synkades retroaktivt till HA Core TM.

## Radinventering

| Ordning | Lokalise-nyckel-ID | Fullständig nyckel | English source | Aktuell svenska | Källkontroll |
|---:|---:|---|---|---|---|
| 20041 | 834983028 | `component::vacuum::triggers::started_returning::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20042 | 834983027 | `component::vacuum::triggers::started_cleaning::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20043 | 834983026 | `component::vacuum::triggers::paused_cleaning::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20044 | 834983025 | `component::vacuum::triggers::errored::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20045 | 834983024 | `component::vacuum::triggers::docked::fields::for::name` | For at least | I minst | Source-path follow-up open |
| 20046 | 834983023 | `component::vacuum::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 20047 | 834983022 | `component::update::triggers::update_became_available::fields::for::name` | For at least | I minst | Source-path follow-up open |
| 20048 | 834983021 | `component::update::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 20049 | 834983020 | `component::temperature::triggers::crossed_threshold::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20050 | 834983019 | `component::temperature::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 20051 | 834983018 | `component::switch::triggers::turned_on::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20052 | 834983017 | `component::switch::triggers::turned_off::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20053 | 834983016 | `component::switch::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 20054 | 834983015 | `component::siren::triggers::turned_on::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20055 | 834983014 | `component::siren::triggers::turned_off::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20056 | 834983013 | `component::siren::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 20057 | 834983012 | `component::schedule::triggers::turned_on::fields::for::name` | For at least | I minst | Source-path follow-up open |
| 20058 | 834983011 | `component::schedule::triggers::turned_off::fields::for::name` | For at least | I minst | Source-path follow-up open |
| 20059 | 834983010 | `component::schedule::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 20060 | 834983009 | `component::remote::triggers::turned_on::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20061 | 834983008 | `component::remote::triggers::turned_off::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20062 | 834983007 | `component::remote::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 20063 | 834983006 | `component::power::triggers::crossed_threshold::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20064 | 834983005 | `component::power::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 20065 | 834983004 | `component::person::triggers::left_home::fields::for::name` | For at least | I minst | Source-path follow-up open |
| 20066 | 834983003 | `component::person::triggers::entered_home::fields::for::name` | For at least | I minst | Source-path follow-up open |
| 20067 | 834983002 | `component::person::common::trigger_for_name` | For at least | I minst | Source-path follow-up open |
| 20068 | 834983001 | `component::occupancy::triggers::detected::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20069 | 834983000 | `component::occupancy::triggers::cleared::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20070 | 834982999 | `component::occupancy::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 20071 | 834982998 | `component::moisture::triggers::detected::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20072 | 834982997 | `component::moisture::triggers::crossed_threshold::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20073 | 834982996 | `component::moisture::triggers::cleared::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20074 | 834982995 | `component::moisture::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 20075 | 834982994 | `component::media_player::triggers::turned_on::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20076 | 834982993 | `component::media_player::triggers::turned_off::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20077 | 834982992 | `component::media_player::triggers::stopped_playing::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20078 | 834982991 | `component::media_player::triggers::started_playing::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20079 | 834982990 | `component::media_player::triggers::paused_playing::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20080 | 834982989 | `component::media_player::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 20081 | 834982988 | `component::lock::triggers::unlocked::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20082 | 834982987 | `component::lock::triggers::opened::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20083 | 834982986 | `component::lock::triggers::locked::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20084 | 834982985 | `component::lock::triggers::jammed::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20085 | 834982984 | `component::lock::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 20086 | 834982983 | `component::light::triggers::turned_on::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20087 | 834982982 | `component::light::triggers::turned_off::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20088 | 834982981 | `component::light::triggers::brightness_crossed_threshold::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20089 | 834982980 | `component::light::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 20090 | 834982979 | `component::lawn_mower::triggers::started_returning::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20091 | 834982978 | `component::lawn_mower::triggers::started_mowing::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20092 | 834982977 | `component::lawn_mower::triggers::paused_mowing::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20093 | 834982976 | `component::lawn_mower::triggers::errored::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20094 | 834982975 | `component::lawn_mower::triggers::docked::fields::for::name` | For at least | I minst | Source-path follow-up open |
| 20095 | 834982974 | `component::lawn_mower::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 20096 | 834982973 | `component::illuminance::triggers::detected::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20097 | 834982972 | `component::illuminance::triggers::crossed_threshold::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20098 | 834982971 | `component::illuminance::triggers::cleared::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20099 | 834982970 | `component::illuminance::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 20100 | 834982969 | `component::humidity::triggers::crossed_threshold::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20101 | 834982968 | `component::humidity::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 20102 | 834982967 | `component::humidifier::triggers::turned_on::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20103 | 834982966 | `component::humidifier::triggers::turned_off::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20104 | 834982965 | `component::humidifier::triggers::started_humidifying::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20105 | 834982964 | `component::humidifier::triggers::started_drying::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20106 | 834982963 | `component::humidifier::triggers::mode_changed::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20107 | 834982962 | `component::humidifier::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 20108 | 834982961 | `component::gate::triggers::opened::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20109 | 834982960 | `component::gate::triggers::closed::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20110 | 834982959 | `component::gate::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 20111 | 834982958 | `component::garage_door::triggers::opened::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20112 | 834982957 | `component::garage_door::triggers::closed::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20113 | 834982956 | `component::garage_door::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 20114 | 834982955 | `component::fan::triggers::turned_on::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20115 | 834982954 | `component::fan::triggers::turned_off::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20116 | 834982953 | `component::fan::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 20117 | 834982952 | `component::door::triggers::opened::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20118 | 834982951 | `component::door::triggers::closed::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20119 | 834982950 | `component::door::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 20120 | 834982949 | `component::device_tracker::triggers::left_home::fields::for::name` | For at least | I minst | Source-path follow-up open |
| 20121 | 834982948 | `component::device_tracker::triggers::entered_home::fields::for::name` | For at least | I minst | Source-path follow-up open |
| 20122 | 834982947 | `component::device_tracker::common::trigger_for_name` | For at least | I minst | Source-path follow-up open |
| 20123 | 834982946 | `component::cover::triggers::shutter_opened::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20124 | 834982945 | `component::cover::triggers::shutter_closed::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20125 | 834982944 | `component::cover::triggers::shade_opened::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20126 | 834982943 | `component::cover::triggers::shade_closed::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20127 | 834982942 | `component::cover::triggers::curtain_opened::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20128 | 834982941 | `component::cover::triggers::curtain_closed::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20129 | 834982940 | `component::cover::triggers::blind_opened::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20130 | 834982939 | `component::cover::triggers::blind_closed::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20131 | 834982938 | `component::cover::triggers::awning_opened::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20132 | 834982937 | `component::cover::triggers::awning_closed::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20133 | 834982936 | `component::cover::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 20134 | 834982935 | `component::counter::triggers::reset::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20135 | 834982934 | `component::counter::triggers::minimum_reached::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20136 | 834982933 | `component::counter::triggers::maximum_reached::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20137 | 834982932 | `component::counter::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 20138 | 834982931 | `component::climate::triggers::turned_on::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20139 | 834982930 | `component::climate::triggers::turned_off::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20140 | 834982929 | `component::climate::triggers::target_temperature_crossed_threshold::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20141 | 834982928 | `component::climate::triggers::target_humidity_crossed_threshold::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20142 | 834982927 | `component::climate::triggers::started_heating::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20143 | 834982926 | `component::climate::triggers::started_drying::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20144 | 834982925 | `component::climate::triggers::started_cooling::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20145 | 834982924 | `component::climate::triggers::hvac_mode_changed::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20146 | 834982923 | `component::climate::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 20147 | 834982922 | `component::battery::triggers::stopped_charging::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20148 | 834982921 | `component::battery::triggers::started_charging::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20149 | 834982920 | `component::battery::triggers::not_low::fields::for::name` | For at least | I minst | Source-path follow-up open |
| 20150 | 834982919 | `component::battery::triggers::low::fields::for::name` | For at least | I minst | Source-path follow-up open |
| 20151 | 834982918 | `component::battery::triggers::level_crossed_threshold::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20152 | 834982917 | `component::battery::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 20153 | 834982916 | `component::assist_satellite::triggers::responding::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20154 | 834982915 | `component::assist_satellite::triggers::processing::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20155 | 834982914 | `component::assist_satellite::triggers::listening::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20156 | 834982913 | `component::assist_satellite::triggers::idle::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20157 | 834982912 | `component::assist_satellite::common::trigger_for_name` | For at least | I minst | Core-literal match |
| 20158 | 834982911 | `component::alarm_control_panel::triggers::triggered::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20159 | 834982910 | `component::alarm_control_panel::triggers::disarmed::fields::for::name` | For at least | I minst | Shared reference target checked |
| 20160 | 834982909 | `component::alarm_control_panel::triggers::armed_vacation::fields::for::name` | For at least | I minst | Shared reference target checked |

## Källägaruppföljning

| Lokalise-nyckel-ID | Fullständig nyckel | English source |
|---:|---|---|---
| 834983024 | `component::vacuum::triggers::docked::fields::for::name` | For at least |
| 834983022 | `component::update::triggers::update_became_available::fields::for::name` | For at least |
| 834983012 | `component::schedule::triggers::turned_on::fields::for::name` | For at least |
| 834983011 | `component::schedule::triggers::turned_off::fields::for::name` | For at least |
| 834983004 | `component::person::triggers::left_home::fields::for::name` | For at least |
| 834983003 | `component::person::triggers::entered_home::fields::for::name` | For at least |
| 834983002 | `component::person::common::trigger_for_name` | For at least |
| 834982975 | `component::lawn_mower::triggers::docked::fields::for::name` | For at least |
| 834982949 | `component::device_tracker::triggers::left_home::fields::for::name` | For at least |
| 834982948 | `component::device_tracker::triggers::entered_home::fields::for::name` | For at least |
| 834982947 | `component::device_tracker::common::trigger_for_name` | For at least |
| 834982920 | `component::battery::triggers::not_low::fields::for::name` | For at least |
| 834982919 | `component::battery::triggers::low::fields::for::name` | For at least |

## Proveniens

- Home Assistant Core dev `6a7129ad8a69b7300cb1af4cda468f91bbffb2e5`.
- Komplett manifest sparat intill denna rapport; snapshot och kanonisk TMX uppdaterade.
