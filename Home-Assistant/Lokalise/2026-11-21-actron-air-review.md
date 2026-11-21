# Home Assistant – Actron Air: svensk radgranskning

Datum: 2026-11-21  
Projekt: Home Assistant Core i Lokalise  
Komponent: `actron_air`

## Underlag

- Aktuellt lokalt källträd: `sources/home-assistant-core-current` vid `2fdaa177`.
- Lokalise API: 37/37 exakta komponentnycklar.
- Tidigare oöversattkontroll identifierade en strukturell tom pluralbehållare för komponenten; den är inte en synlig engelsk källsträng och har inte fyllts med påhittad text.

## Sparade och återlästa ändringar

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- | --- |
| `component::actron_air::config::progress::wait_for_authorization` | The login attempt will time out after {expires_minutes} minutes. | Inloggningsförsöket kommer att ta en timeout efter {expires_minutes} minuter. | Inloggningsförsöket upphör efter {expires_minutes} minuter. | Tar bort den felaktiga anglicismen ”ta en timeout”; alla platshållare och kodblock bevarades. |
| `component::actron_air::config::step::reauth_confirm::title` | Authentication expired | Autentisering löpt ut | Autentiseringen har löpt ut | Återställer en fullständig svensk sats. |

Båda ändringarna skickades via Lokalise API och lästes tillbaka från samma nycklar.

## Övrig kontroll

Termer som `avfrostningsläge`, `kompressorkapacitet`, `bortaläge`, `turboläge` och `Actron-Air-API:et` kontrollerades och behölls. Inga ytterligare säkra ändringar identifierades.

## Status

Komponenten är granskad mot aktuell Lokalise-data. Den dokumenterade strukturella pluralbehållaren är en referensfråga, inte en svensk översättningslucka.