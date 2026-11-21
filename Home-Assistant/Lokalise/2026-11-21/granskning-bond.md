# Home Assistant Core – Bond

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/bond/strings.json` och Lokalise API med direkt återläsning.

Status: samtliga 50 aktuella Lokalise-poster för komponentens bladsträngar och referensmål är radgranskade. En korrigering är sparad och återläst.

| Nyckel | Befintlig text | Sparad text | Motivering |
|---|---|---|---|
| `config::step::reconfigure::data_description::host` | `IP-adressen till din Bond-hubb.` | `IP-adressen till din Bond-hub.` | Samma produktbenämning används i användar- och omkonfigureringssteget. |

Konfiguration, autentisering, firmwarefel, undantag och samtliga tjänster för spårat fläkt-, ljusstyrke- och effekttillstånd är kontrollerade. Referenser och platshållaren `{host}` är bevarade. TMX-ledgern innehåller den API-återlästa korrigeringen och är validerad.
