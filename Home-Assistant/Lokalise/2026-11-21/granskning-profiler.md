# Home Assistant Core – Profiler

Datum: 2026-11-21  
Status: pågående radgranskning mot `origin/dev`.

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
| `component::profiler::services::log_thread_frames::name` | Log thread frames | Logga trådars stackramar → **Logga stackramar för alla trådar** | Osparat förslag (Lokalise-ID `349141083`); förslaget följer komponentens egen beskrivning och blir tydligare än genitivkedjan. |
| `component::profiler::services::log_thread_frames::description` | Lets the Profiler log the current frames for all threads. | Låter Profiler logga aktuella stackramar för alla trådar. | Verifierad i Lokalise (ID `349141082`). |
| `component::profiler::services::lru_stats::name` | Log LRU stats | Logga LRU-statistik | Verifierad i Lokalise (ID `349141085`). |
| `component::profiler::services::lru_stats::description` | Lets the Profiler log the stats of all LRU caches. | Låter Profiler logga statistiken för alla LRU-cacher. | Verifierad i Lokalise (ID `349141084`). |
