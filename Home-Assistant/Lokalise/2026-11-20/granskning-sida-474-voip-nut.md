# Home Assistant Core — granskning sida 474 (KNX, VoIP och NUT)

Datum: 2026-11-20  
Status: dokumenterade förslag; **inte sparade i Lokalise**

VoIP- och NUT-källtexten kontrollerades mot respektive `strings.json` på Home Assistant Cores `dev`-gren.

| Fullständig nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
|---|---|---|---|
| `component::voip::config::step::user::description` | `Ta emot röst över IP-samtal för att interagera med Assist.` | `Ta emot VoIP-samtal för att interagera med Assist.` | `VoIP` är den etablerade svenska tekniska termen; den nuvarande ordalydelsen blir otydlig. |
| `component::nut::device_automation::action_type::shutdown_return` | `Stäng av lasten, eventuellt efter en fördröjning, och återställ när strömmen är tillbaka` | `Stäng av lasten, eventuellt efter en fördröjning, och slå på den igen när strömmen är tillbaka` | Källans ”return” innebär att lasten slås på igen; ”återställ” anger inte tydligt vad som sker. |

Övriga 18 nycklar på sidan granskades utan dokumenterat ändringsförslag. KNX-telegramsensorn och NUT-åtgärderna har konsekvent terminologi för UPS, last, förbikopplingsläge och körtidskalibrering.
