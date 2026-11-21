# Home Assistant Core – Android TV Remote

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/androidtv_remote/strings.json`, tidigare rapporter och Lokalise API med direkt återläsning.

Status: samtliga 40 aktuella bladsträngar är radgranskade. Två korrigeringar är sparade och återlästa.

| Nyckel | Befintlig text | Sparad text | Motivering |
|---|---|---|---|
| `component::androidtv_remote::config::step::zeroconf_confirm::description` | `Vill du lägga till Android TV ({name}) till Home Assistant? Den slås på och en parkopplingskod kommer att visas på den som du måste ange på nästa skärm.` | `Vill du lägga till Android TV ({name}) i Home Assistant? Den slås på och en parkopplingskod kommer att visas på den som du måste ange på nästa skärm.` | På svenska lägger man till en enhet *i* Home Assistant. |
| `component::androidtv_remote::options::step::apps::data_description::app_name` | `Applikationens namn som du vill att det ska visas i Home Assistant.` | `Namnet på applikationen som du vill ska visas i Home Assistant.` | Tar bort den otydliga syftningen i den svenska meningen. |

Tidigare granskningar av appikon, parkopplingskod och undantagstexter har kontrollerats mot den aktuella källan. Alla platshållare och tekniska sökvägar är intakta. Produktnamnet Home Assistant är bevarat. Tre äldre Lokalise-poster som inte längre förekommer i komponentens `strings.json` ingår inte i den aktuella omfattningen. Direkt API-återläsning bekräftade de sparade ändringarna. TMX-ledgern är uppdaterad och validerad (1 676 poster).
