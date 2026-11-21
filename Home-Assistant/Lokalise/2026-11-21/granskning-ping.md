# Home Assistant Core – Ping

Datum: 2026-11-21

## Delgranskning

| Nyckel | Källa | Svenska | Bedömning |
| --- | --- | --- | --- |
| `component::ping::config::step::user::title` | Add Ping | Lägg till Ping | Verifierad i Lokalise (ID `408083810`). |
| `component::ping::config::step::user::description` | Ping allows you to check the availability of a host. | Med Ping kan du kontrollera om en värd är tillgänglig. | Verifierad i Lokalise (ID `408083809`). |
| `component::ping::config::step::user::data_description::host` | The hostname or IP address of the device you want to ping. | Värdnamn eller IP-adress för den enhet som du vill pinga. | Verifierad i Lokalise (ID `413416014`). |
| `component::ping::config::abort::invalid_ip_address` | Invalid IP address. | Ogiltig IP-adress. | Verifierad i Lokalise (ID `408083806`). |
| `component::ping::entity::sensor::round_trip_time_mdev::name` | Round-trip time mean deviation | Medelavvikelse för tur- och returtid | Verifierad i Lokalise (ID `450694479`). Teknisk benämning är sakligt korrekt. |
| `component::ping::options::step::init::data_description::consider_home` | Seconds to wait till marking a device tracker as not home after not being seen. | Antal sekunder att vänta innan en enhetsspårare som inte har setts markeras som inte hemma. | Sparad och återläst i Lokalise (ID `421388213`). Rättar den tidigare otydliga satsen och gör tidpunkten för statusändringen tydlig. |
| `component::ping::entity::sensor::jitter::name` | Jitter | Jitter | Verifierad i Lokalise (ID `689731845`); etablerad teknisk term. |
| `component::ping::entity::sensor::loss::name` | Packet loss | Paketförlust | Verifierad i Lokalise (ID `768917830`). |
| `component::ping::entity::sensor::round_trip_time_avg::name` | Round-trip time average | Genomsnittlig tur- och returtid | Verifierad i Lokalise (ID `450694477`). |
| `component::ping::entity::sensor::round_trip_time_max::name` | Round-trip time maximum | Max tur- och returtid | Verifierad i Lokalise (ID `450694478`). |
| `component::ping::entity::sensor::round_trip_time_min::name` | Round-trip time minimum | Minsta tur- och returtid | Verifierad i Lokalise (ID `450694480`). |
| `component::ping::options::step::init::data::consider_home` | Consider home interval | Intervall för att betraktas som hemma | Verifierad i Lokalise (ID `421388212`). |
| `component::ping::options::step::init::data::count` | Ping count | Antal pingar | Verifierad i Lokalise (ID `408083812`). |
| `component::ping::options::abort::invalid_ip_address` | `[%key:component::ping::config::abort::invalid_ip_address%]` | Samma referens | Verifierad i Lokalise (ID `408083811`); referensmålet bevaras exakt. |

Samtliga direkta aktuella Ping-strängar och dess interna felreferens är nu granskade. Återstående gemensamma referenser är återanvända Core-nycklar och ändras inte här.

