# Telegram Bot, Deluge, Elk-M1 och Nederlandse Spoorwegen

Källor kontrollerade mot aktuell Home Assistant Core den 24 november 2026. Ändrade strängar sparades och lästes tillbaka via Lokalise API. Sexton poster synkades också till Home Assistant-minnets snapshot, PO och TMX.

| Fullständig nyckel | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::telegram_bot::services::send_chat_action::fields::target::description` | `En matris med förauktoriserade chatt ID:n att skicka chattåtgärden till. Om det inte finns är det första tillåtna chatt ID standard.` | `En lista med förhandsgodkända chatt-ID:n som chattåtgärden ska skickas till. Om ingen lista anges används det första tillåtna chatt-ID:t.` | Naturligare term och rättade sammansättningar/böjning. |
| `component::telegram_bot::services::send_chat_action::fields::config_entry_id::description` | `Konfigurationsposten som representerar Telegram boten för att skicka chattåtgärden.` | `Konfigurationsposten som representerar Telegram-botten som ska skicka chattåtgärden.` | Korrigerad sammansättning och ordföljd. |
| `component::telegram_bot::selector::chat_action::options::record_voice` | `Röstinspelning` | `Spelar in röstmeddelande` | Pågående aktivitet som visas av Telegram-botten. |
| `component::telegram_bot::selector::chat_action::options::record_video_note` | `Spela in en videoanteckning` | `Spelar in videoanteckning` | Tempus och aspekt anpassade till statusåtgärden; Telegrams objektnamn bevaras. |
| `component::telegram_bot::selector::chat_action::options::record_video` | `Spela in video` | `Spelar in video` | Pågående aktivitet. |
| `component::telegram_bot::selector::chat_action::options::find_location` | `Hitta plats` | `Söker efter plats` | Pågående aktivitet. |
| `component::telegram_bot::selector::chat_action::options::choose_sticker` | `Välja klistermärke` | `Väljer klistermärke` | Pågående aktivitet. |
| `component::deluge::entity::sensor::seeding_count::name` | `Antal delningar` | `Antal torrenter som delas` | Sensorn räknar torrenter som seedas; den korta texten kunde avse antal händelser. |
| `component::deluge::entity::sensor::downloading_count::name` | `Antal pågående nedladdningar` | `Antal torrenter som laddas ner` | Enheten är uttryckligen torrent; nuvarande formulering kunde avse nedladdningsprocesser. |
| `component::elkm1::config::step::reconfigure::title` | `Konfigurera om ELK M1 Control` | `Konfigurera om Elk-M1 Control` | Följer officiell produktstavning i källan. |
| `component::elkm1::config::abort::reconfigure_successful` | `ELK M1-integrationen har omkonfigurerats.` | `Elk-M1-integrationen konfigurerades om` | Följer produktnamnet och naturlig resultattext. |
| `component::nederlandse_spoorwegen::config_subentries::route::step::user::description` | `Välj dina avgångs och destinationsstationer från rullgardinslistorna.` | `Välj avgångsstation och destinationsstation i rullgardinslistorna.` | Korrigerar två felaktiga konstruktioner. |
| `component::nederlandse_spoorwegen::config_subentries::route::step::user::data::to` | `Destinations station` | `Destinationsstation` | Korrigerad sammansättning. |
| `component::nederlandse_spoorwegen::config_subentries::route::step::user::data::name` | `Rutt namn` | `Ruttnamn` | Korrigerad sammansättning. |
| `component::nederlandse_spoorwegen::config::step::user::description` | `Ställ in din Nederlandse Spoorwegen integration.` | `Konfigurera din Nederlandse Spoorwegen-integration.` | Korrigerad sammansättning och UI-idiom. |
| `component::nederlandse_spoorwegen::issues::deprecated_yaml_import_issue_unknown::title` | `Nederlandse Spoorwegen YAML- onfiguration utfasad` | `Nederlandse Spoorwegen YAML-konfiguration är utfasad` | Rättar stavfel och återanvänder det gemensamma målet som redan finns på de tre parallella titlarna. |

## Kvar för källkontroll

Rapporten innehåller även äldre nycklarna `component::nederlandse_spoorwegen::issues::deprecated_yaml_import_issue_{invalid_auth,invalid_station,cannot_connect,unknown}::description` samt titlarna `invalid_auth`, `invalid_station` och `cannot_connect`. Dessa finns i Lokalise, men deponitillgängliga aktuella `strings.json`-filerna innehåller inte längre motsvarande YAML-importnycklar. Deras formuleringar bör inte omklassas som granskade mot aktuell källa förrän nycklarna återfinns i aktuell upstream-version. Fyra befintliga titlar har samma svenska måltext; det tydliga stavfelet i titeln `unknown` ovan är nu rättat.
