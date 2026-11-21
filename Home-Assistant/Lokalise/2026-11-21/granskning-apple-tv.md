# Home Assistant Core – Apple TV

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/apple_tv/strings.json`, tidigare delgranskning och Lokalise API med direkt återläsning.

Status: pågående radgranskning. Konfigurationsflödet är granskat; tre korrigeringar är sparade och återlästa.

| Nyckel | Sparad text | Motivering |
|---|---|---|
| `config::step::pair_no_pin::description` | `Parkoppling krävs för tjänsten `{protocol}`. Ange PIN-kod {pin} på din enhet för att fortsätta.` | Bevarar den tekniska kodmarkeringen i källan. |
| `config::step::password::description` | `Protokollet `{protocol}` kräver ett lösenord. Detta stöds ännu inte. Inaktivera lösenordet för att fortsätta.` | Tydlig svensk satsstruktur med protokollet som subjekt. |
| `config::step::restore_device::title` | `Omkonfigurera enheten` | Naturlig handlingsrubrik. |

Platshållarna `{protocol}`, `{pin}`, `{name}` och `{type}` samt Markdown-markeringar har kontrollerats. Den återstående omfattningen är entiteter, tjänster, undantag och problem. TMX-ledgern är uppdaterad och validerad (1 701 poster).
