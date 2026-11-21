# Home Assistant Core – Android TV

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/androidtv/strings.json`, tidigare delgranskningar och Lokalise API med direkt återläsning.

Status: samtliga 64 aktuella bladsträngar är radgranskade. Två korrigeringar är sparade och återlästa.

| Nyckel | Befintlig text | Sparad text | Motivering |
|---|---|---|---|
| `component::androidtv::config::step::user::sections::more_options::data::adbkey` | `Sökväg till din ADB-nyckelfil (låt vara tomt för att automatiskt generera)` | `Sökväg till din ADB-nyckelfil (lämna fältet tomt för automatisk generering)` | Naturlig och entydig svensk fältinstruktion. |
| `component::androidtv::config::step::reconfigure::sections::more_options::data::adbkey` | `Sökväg till din ADB-nyckelfil (lämna tomt för att skapa den automatiskt)` | `Sökväg till din ADB-nyckelfil (lämna fältet tomt för automatisk generering)` | Samma engelska källtext ska ha samma tydliga svenska formulering i omkonfigureringen. |

Tidigare sparade korrigeringar och rapporter har jämförts med nuvarande källa. Referenser till gemensamma fält och återanvända tjänstetexter är intakta; platshållarna `{address}`, `{adb_server}`, `{adbkey}`, `{cmd}`, `{app_id}` och `{rule_id}` är bevarade. ADB, Android TV, Fire TV, Home Assistant och `sendevent` har bedömts som tekniska namn. Direkt API-återläsning bekräftade båda ändringarna. TMX-ledgern är uppdaterad och validerad (1 674 poster).
