# Home Assistant Core — granskning sida 487 (Last.fm, Rituals Perfume Genie och YouTube)

Datum: 2026-11-20  
Status: dokumenterade förslag; **inte sparade i Lokalise**

| Fullständig nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
|---|---|---|---|
| `component::rituals_perfume_genie::entity::sensor::fill::name` | `Fyll` | `Fyllnadsnivå` | Nyckeln är en sensor; `Fyll` läses som imperativ medan `Fyllnadsnivå` anger mätvärdet. |
| `component::rituals_perfume_genie::entity::sensor::wifi_percentage::name` | `WiFi-signal` | `Wi-Fi-signal` | Varumärkes- och standardskrivningen är `Wi-Fi`. |
| `component::youtube::config::abort::access_not_configured` | `Vänligen läs meddelandet från Google:\n\n{message}` | `Läs meddelandet nedan från Google:\n\n{message}` | Mer idiomatisk och direkt feltext; den tomma raden och `{message}` bevaras. |

Övriga 17 nycklar på sidan granskades utan dokumenterat ändringsförslag. Fem Last.fm- och fem YouTube-nycklar är direkta referenser. Övriga Rituals- och YouTube-sensornamn är sakligt korrekta.
