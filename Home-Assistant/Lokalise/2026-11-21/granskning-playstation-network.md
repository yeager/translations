# Home Assistant Core – PlayStation Network

Datum: 2026-11-21

| Nyckel | Källa | Befintlig svenska | Svenska efter granskning | Bedömning |
| --- | --- | --- | --- | --- |
| `component::playstation_network::config::step::reconfigure::title` | Update PlayStation Network configuration | Uppdatera PlayStation Network-konfiguration | Uppdatera konfigurationen för PlayStation Network | Sparad och återläst i Lokalise (ID `671798178`). Undviker den svårtolkade sammansättningen med varumärket. |
| `component::playstation_network::config::step::user::data_description::npsso` | The NPSSO token is generated upon successful login of your PlayStation Network account and is used to authenticate your requests within Home Assistant. | NPSSO-token genereras vid lyckad inloggning på ditt PlayStation Network-konto och används för att autentisera dina förfrågningar i Home Assistant. | Verifierad i Lokalise (ID `668990843`). |
| `component::playstation_network::config::step::user::description` | To obtain your NPSSO token, log in to your [PlayStation account]({psn_link}) first. Then [retrieve your token]({npsso_link}).\n\nNote: Do not log out of your PlayStation account after obtaining the NPSSO token. | För att hämta din NPSSO-token, logga först in på ditt [PlayStation-konto]({psn_link}). Klicka sedan [här]({npsso_link}) för att hämta token.\n\nOBS! Logga inte ut från ditt PlayStation-konto efter att du har hämtat din NPSSO-token. | Verifierad i Lokalise (ID `668990844`); länkar och radbrytning bevarade. |
| `component::playstation_network::config_subentries::friend::step::user::data_description::account_id` | Select a friend from your friend list to track their online status. | Välj en vän från din vänlista för att spåra deras onlinestatus. | Verifierad i Lokalise (ID `688374477`). |

## Osparat förslag

| Nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- |
| `component::playstation_network::config::step::reauth_confirm::description` | NPSSO-koden för **{name}** har gått ut. För att få en ny måste du först logga in på ditt [PlayStation-konto]({psn_link}). Klicka sedan [här]({npsso_link}) för att hämta koden.\n\nObs! Logga inte ut från ditt PlayStation-konto efter att du har hämtat NPSSO-koden, eftersom detta gör koden ogiltig. | NPSSO-token för **{name}** har gått ut. För att få en ny måste du först logga in på ditt [PlayStation-konto]({psn_link}). Klicka sedan [här]({npsso_link}) för att hämta token.\n\nObs! Logga inte ut från ditt PlayStation-konto efter att du har hämtat NPSSO-token, eftersom detta gör token ogiltig. | Samma tekniska begrepp som i källtexten och övriga flödessträngar; Markdown, platshållare och radbrytning är oförändrade. Lokalise-ID `669331682`. |

