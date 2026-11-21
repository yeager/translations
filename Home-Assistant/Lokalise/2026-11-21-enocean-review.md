# Core — EnOcean

Datum: 2026-11-21

Alla 15 strängar har hämtats från Lokalise och granskats mot källtexten. En ändring sparades direkt i Lokalise och lästes sedan tillbaka:

| Nyckel | Före | Efter | Motivering |
| --- | --- | --- | --- |
| `component::enocean::config::step::usb_confirm::description` | `{manufacturer} USB-dongel upptäckt vid {device}. Vill du konfigurera den här enheten?` | `{manufacturer} USB-dongel hittades på {device}. Vill du konfigurera den här enheten?` | Naturligare svensk sats och korrekt preposition för enhetens sökväg. |

Platshållarna `{manufacturer}` och `{device}` har kontrollerats och bevarats. Den verifierade posten är införd i Home Assistant-minnets TMX och dess formatkontroll passerade.
