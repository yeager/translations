# Sparad ändring för Music Assistant

Sparad och återläst i Lokalise 2026-11-19 efter jämförelse med tidigare granskningsrapport.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::music_assistant::services::search::fields::username::description` | Music Assistant username used for searching. Searches respect the user's configured provider filters. Defaults to the Music Assistant user linked to the Home Assistant user making the request. If there is no linked user, the request runs as the default account. | Det Music Assistant-användarnamn som ska användas för sökning. Sökningar respekterar användarens konfigurerade leverantörsfilter. | Music Assistant-användarnamnet som ska användas för sökningen. Sökningar följer användarens konfigurerade leverantörsfilter. Som standard används den Music Assistant-användare som är kopplad till Home Assistant-användaren som gör begäran. Om ingen användare är kopplad används standardkontot. |

Informationen om kopplad användare och standardkonto saknades tidigare.

## Nya felmeddelanden

Sparade och återlästa i Lokalise 2026-11-19. Båda de svenska fälten var tidigare tomma.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::music_assistant::exceptions::server_too_old::message` | This action requires a newer Music Assistant server version. | Tom | Den här åtgärden kräver en nyare version av Music Assistant-servern. |
| `component::music_assistant::exceptions::no_active_queue::message` | The player is not playing from a Music Assistant queue. | Tom | Spelaren spelar inte upp från en Music Assistant-kö. |

Nyckeln `component::music_assistant::exceptions::offset_needs_limit::message` är också tom och behöver jämföras med fältnamnen för offset och limit innan den översätts.

## Favoritfilter och offset

Sparade och återlästa i Lokalise 2026-11-19.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::music_assistant::services::get_library::fields::favorite::name` | Favorite state | Endast favoriter | Favoritstatus |
| `component::music_assistant::services::get_library::fields::favorite::description` | Filter by favorite state. Enable to return only liked items, disable to return only disliked items, or leave the field out to return all items. | Filtrera objekt så att endast favoriter returneras. | Filtrera efter favoritstatus. Aktivera för att bara returnera gillade objekt, inaktivera för att bara returnera ogillade objekt eller lämna fältet tomt för att returnera alla objekt. |
| `component::music_assistant::exceptions::offset_needs_limit::message` | An offset requires a limit greater than 0. | Tom | Offset kräver en gräns större än 0. |

Favorittexten återger nu även inaktiverat och utelämnat fält. Den tidigare öppna offsetfrågan har följts upp mot fältnamnen `get_library::fields::offset::name` (”Offset”) och `get_library::fields::limit::name` (”Gräns”).

## Köfält

Sex tidigare tomma svenska fält sparades och återlästes i Lokalise 2026-11-19.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::music_assistant::services::get_queue::fields::username::description` | Music Assistant username used to request the queue items. The request fails when this user may not access the player. Defaults to the Music Assistant user linked to the Home Assistant user making the request. If there is no linked user, the request runs as the default account. | Tom | Music Assistant-användarnamnet som används för att begära objekten i kön. Begäran misslyckas om användaren inte har åtkomst till spelaren. Som standard används den Music Assistant-användare som är kopplad till Home Assistant-användaren som gör begäran. Om ingen användare är kopplad används standardkontot. |
| `component::music_assistant::services::get_queue::fields::offset::description` | Number of queue items to skip. Requires a limit. | Tom | Antal objekt i kön som ska hoppas över. Kräver en gräns. |
| `component::music_assistant::services::get_queue::fields::limit::description` | Maximum number of queue items to return. Leave at 0 to only return the queue details. | Tom | Maximalt antal objekt i kön som ska returneras. Låt värdet vara 0 för att bara returnera information om kön. |

Följande tre tomma svenska fältnamn fylldes med samma referenser som i den engelska källan. Målen kontrollerades som ”Användarnamn”, ”Offset” och ”Gräns”.

| Fullständig nyckel | Sparad referens |
|---|---|
| `component::music_assistant::services::get_queue::fields::username::name` | `[%key:component::music_assistant::services::get_library::fields::username::name%]` |
| `component::music_assistant::services::get_queue::fields::offset::name` | `[%key:component::music_assistant::services::get_library::fields::offset::name%]` |
| `component::music_assistant::services::get_queue::fields::limit::name` | `[%key:component::music_assistant::services::get_library::fields::limit::name%]` |
