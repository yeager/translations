# Home Assistant Core – pyLoad

Datum: 2026-11-21  
Status: pågående radgranskning mot aktuell Core-källa `2fdaa177`; konfigurationsdelens första 33 Lokalise-poster är kontrollerade.

## Osparat förslag

| Nyckel | Källa | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- | --- |
| `component::pyload::config::step::user::data_description::api_key` | The API key to authenticate with pyLoad. To create a new API key, navigate to **Settings > Users > Actions > Manage API Keys** and select **Generate**. | Innehåller synliga `&gt;`-entiteter och `**Skapa**`. | API-nyckeln för att autentisera med pyLoad. För att skapa en ny API-nyckel går du till **Inställningar > Användare > Åtgärder > Hantera API-nycklar** och väljer **Generera**. | Rättar bokstavligt visade HTML-entiteter, följer källans navigeringskedja och återger “Generate” korrekt. Fetstil ska bevaras exakt vid Lokalise-sparning. Lokalise-ID `853560491`. |

## Verifierat i första delen

- API-nyckel-, användarnamns-, lösenords-, URL- och SSL-referenser för användar-, reautentiserings-, hassio- och omkonfigureringsflöden är bevarade där de motsvarar aktuell källa.
- `{addon}` i hassio-beskrivningen och `{example_url}` i URL-beskrivningen är bevarade.
- Texterna för URL, SSL-validering samt föråldrade användarnamn- och lösenordsfält är språkligt korrekta.
- `Home Assistant` är oförändrat i pyLoad via Home Assistant-appen och hassio-beskrivningen.

Den fortsatta granskningen omfattar återstående aktuella entiteter, reglage, knappar och undantag. Förslaget ovan är inte sparat och finns inte i TMX-minnet.
