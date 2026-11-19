# Squeezebox: sparade ändringar i Lokalise

Den 19 november 2026 jämfördes källtext och tidigare svensk text i Lokalise. Ändringarna nedan sparades och återlästes där. Platshållarna bevarades.

| Fullständig nyckel | Engelsk källtext | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::squeezebox::exceptions::init_timeout::message` | Timeout connecting to LMS {host}. | Timeout vid anslutning till LMS {host}. | Tidsgränsen överskreds vid anslutning till LMS {host}. |
| `component::squeezebox::exceptions::init_missing_uuid::message` | LMS {host} status response missing essential data (UUID). | LMS {host} status-svar saknar väsentliga data (UUID). | Statussvaret från LMS {host} saknar nödvändiga uppgifter (UUID). |
| `component::squeezebox::exceptions::init_get_status_failed::message` | Failed to get status from LMS {host} (HTTP status: {http_status}). Will retry. | Misslyckades med att hämta status från LMS {host} (HTTP-status: {http_status}). Försöker igen. | Det gick inte att hämta status från LMS {host} (HTTP-status: {http_status}). Försöker igen. |

| `component::squeezebox::exceptions::init_auth_failed::message` | Authentication failed with {host}. | Autentisering misslyckades för {host}. | Autentiseringen mot {host} misslyckades. |

Den fjärde ändringen sparades och återlästes i Lokalise; `{host}` är bevarad.
