# Home Assistant Core – Profiler

Datum: 2026-11-21  
Status: samtliga 42 aktuella bladnycklar är radgranskade mot Core `2fdaa177` och Lokalise.

| Nyckel | Källa | Svenska | Bedömning |
| --- | --- | --- | --- |
| `component::profiler::services::dump_log_objects::name` | Dump log objects | Dumpa loggobjekt | Verifierad i Lokalise (ID `349141079`). |
| `component::profiler::services::dump_log_objects::description` | Lets the Profiler dump the repr of all matching objects to the log. | Låter Profiler dumpa `repr` för alla matchande objekt till loggen. | Verifierad i Lokalise (ID `349141076`); `repr` är en Python-term. |
| `component::profiler::services::dump_log_objects::fields::type::name` | Type | Typ | Verifierad i Lokalise (ID `349141078`). |
| `component::profiler::services::dump_log_objects::fields::type::description` | The type of objects to dump to the log. | Vilken typ av objekt som ska dumpas till loggen. | Verifierad i Lokalise (ID `349141077`). |
| `component::profiler::services::dump_sockets::name` | Dump used sockets | Dumpa använda sockets | Verifierad i Lokalise (ID `715580159`); `sockets` behålls som etablerad teknisk term i detta utvecklargränssnitt. |
| `component::profiler::services::dump_sockets::description` | Lets the Profiler log information about all currently used sockets. | Låter Profiler logga information om alla sockets som används för närvarande. | Verifierad i Lokalise (ID `715580158`). |
| `component::profiler::services::log_current_tasks::name` | Log current asyncio tasks | Logga aktuella asyncio-uppgifter | Verifierad i Lokalise (ID `473725729`). |
| `component::profiler::services::log_current_tasks::description` | Lets the Profiler log all the current asyncio tasks. | Låter Profiler logga alla aktuella asyncio-uppgifter. | Verifierad i Lokalise (ID `473725728`). |
| `component::profiler::services::log_event_loop_scheduled::name` | Log event loop scheduled | Logga vad som är schemalagt i händelseloopen | Verifierad i Lokalise (ID `349141081`). |
| `component::profiler::services::log_event_loop_scheduled::description` | Lets the Profiler log what is scheduled in the event loop. | Låter Profiler logga vad som är schemalagt i händelseloopen. | Verifierad i Lokalise (ID `349141080`). |
| `component::profiler::services::log_thread_frames::name` | Log thread frames | Logga stackramar för alla trådar | Sparad och API-återläst 2026-11-21. |
| `component::profiler::services::log_thread_frames::description` | Lets the Profiler log the current frames for all threads. | Låter Profiler logga aktuella stackramar för alla trådar. | Verifierad i Lokalise (ID `349141082`). |
| `component::profiler::services::lru_stats::name` | Log LRU stats | Logga LRU-statistik | Verifierad i Lokalise (ID `349141085`). |
| `component::profiler::services::lru_stats::description` | Lets the Profiler log the stats of all LRU caches. | Låter Profiler logga statistiken för alla LRU-cacher. | Verifierad i Lokalise (ID `349141084`). |
| `component::profiler::services::memory::name` | Create memory profile | Skapa minnesprofil | Verifierad i Lokalise (ID `349141089`). |
| `component::profiler::services::memory::description` | Lets the Profiler create a memory profile for a specified number of seconds. | Låter Profiler skapa en minnesprofil under ett angivet antal sekunder. | Verifierad i Lokalise (ID `349141086`). |
| `component::profiler::services::set_asyncio_debug::name` | Set asyncio debug | Ställ in asyncio-felsökning | Verifierad i Lokalise (ID `456993395`). |
| `component::profiler::services::set_asyncio_debug::description` | Lets the Profiler enable or disable asyncio debug. | Låter Profiler aktivera eller inaktivera asyncio-felsökning. | Verifierad i Lokalise (ID `456993392`). |
| `component::profiler::services::set_asyncio_debug::fields::enabled::name` | Enabled | `[%key:common::state::enabled%]` | Verifierad referens i Lokalise (ID `456993394`) till den gemensamma översättningen. |
| `component::profiler::services::set_asyncio_debug::fields::enabled::description` | Whether to enable or disable asyncio debug. | Om asyncio-felsökning ska aktiveras eller inaktiveras. | Sparad och API-återläst 2026-11-21. |
| `component::profiler::services::start::name` | Create system profile | Skapa systemprofil | Verifierad i Lokalise (ID `349141093`). |
| `component::profiler::services::start::description` | Lets the Profiler create a system profile for a specified number of seconds. | Låter Profiler skapa en systemprofil under ett angivet antal sekunder. | Verifierad i Lokalise (ID `349141090`). |
| `component::profiler::services::start::fields::seconds::name` | Seconds | Sekunder | Verifierad i Lokalise (ID `349141092`). |
| `component::profiler::services::start::fields::seconds::description` | The number of seconds to run the Profiler. | Antal sekunder som Profiler ska köras. | Sparad och API-återläst 2026-11-21; samma direkta text uppdaterades även för minnesprofilen. |
| `component::profiler::services::start_log_object_sources::name` | Start logging object sources | Börja logga objektkällor | Verifierad i Lokalise (ID `349141099`). |
| `component::profiler::services::start_log_object_sources::description` | Starts the Profiler logging sources of new objects in memory. | Startar Profiler-loggning av källorna till nya objekt i minnet. | Verifierad i Lokalise (ID `349141094`). |
| `component::profiler::services::start_log_object_sources::fields::max_objects::name` | Maximum objects | Maximalt antal objekt | Verifierad i Lokalise (ID `349141096`). |
| `component::profiler::services::start_log_object_sources::fields::max_objects::description` | The maximum number of objects to log. | Maximalt antal objekt som ska loggas. | Verifierad i Lokalise (ID `349141095`). |
| `component::profiler::services::start_log_object_sources::fields::scan_interval::name` | Scan interval | Skanningsintervall | Verifierad i Lokalise (ID `349141098`). |
| `component::profiler::services::start_log_object_sources::fields::scan_interval::description` | `[%key:component::profiler::services::start_log_objects::fields::scan_interval::description%]` | `[%key:component::profiler::services::start_log_objects::fields::scan_interval::description%]` | Verifierad referens till den direkta, nedanstående strängen. |
| `component::profiler::services::start_log_objects::name` | Start logging objects | Börja logga objekt | Verifierad i Lokalise (ID `349141103`). |
| `component::profiler::services::start_log_objects::description` | Starts the Profiler logging growth of objects in memory. | Startar Profiler-loggning av objektökningar i minnet. | Verifierad i Lokalise (ID `349141100`). |
| `component::profiler::services::start_log_objects::fields::scan_interval::description` | The number of seconds between logging objects. | Antalet sekunder mellan loggning av objekt. | Verifierad i Lokalise (ID `349141101`). |
| `component::profiler::services::start_log_objects::fields::scan_interval::name` | Scan interval | Skanningsintervall | Verifierad i Lokalise (ID `349141102`). |
| `component::profiler::services::stop_log_object_sources::name` | Stop logging object sources | Sluta logga objektkällor | Verifierad i Lokalise (ID `349141105`). |
| `component::profiler::services::stop_log_object_sources::description` | Stops the Profiler logging sources of new objects in memory. | Stoppar Profiler-loggning av källorna till nya objekt i minnet. | Verifierad i Lokalise (ID `349141104`). |
| `component::profiler::services::stop_log_objects::name` | Stop logging objects | Sluta logga objekt | Verifierad i Lokalise (ID `349141107`). |
| `component::profiler::services::stop_log_objects::description` | Stops the Profiler logging growth of objects in memory. | Stoppar Profiler-loggning av objektökningar i minnet. | Verifierad i Lokalise (ID `349141106`). |
| `component::profiler::config::step::user::description` | `[%key:common::config_flow::description::confirm_setup%]` | `[%key:common::config_flow::description::confirm_setup%]` | Gemensam referens; ingen komponentspecifik översättning. |
| `component::profiler::services::memory::fields::seconds::{name,description}` | Referenser till `services::start::fields::seconds` | Motsvarande referenser | Granskade mot de direkta start-fälten ovan. |

Alla 42 bladnycklar i aktuell Core-källas `profiler/strings.json` är granskade. De fyra motsvarande måltexterna är sparade, återlästa och införda i TMX-minnet.
