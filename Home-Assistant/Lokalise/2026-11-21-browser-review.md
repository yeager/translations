# Home Assistant – Browser: svensk radgranskning

Datum: 2026-11-21  
Komponent: `browser`  
Omfattning: 4/4 aktuella källsträngar

| Fullständig nyckel | Engelsk källtext | Befintlig svensk text | Föreslagen text | Bedömning |
| --- | --- | --- | --- | --- |
| `component::browser::services::browse_url::description` | Opens a URL in the default browser on the host machine of Home Assistant. | Öppnar en URL i standardwebbläsaren på Home Assistants värddator. | Oförändrad | Korrekt och tydlig. |
| `component::browser::services::browse_url::fields::url::description` | The URL to open. | URL att öppna. | Oförändrad | Avsiktligt kort fältbeskrivning; korrekt i UI-kontext. |
| `component::browser::services::browse_url::fields::url::name` | URL | URL | Oförändrad | Korrekt. Den lokala källan använder en gemensam nyckel; Lokalise returnerade den upplösta källtexten. |
| `component::browser::services::browse_url::name` | Browse | Bläddra | Oförändrad | Etablerad kort UI-etikett i detta tjänstesammanhang. |

## Verifiering

- Aktuell källa och svenska värden hämtades via Lokalise API.
- `l10n-lint`: inga problem.
- `hunspell-sv`: inga stavningsanmärkningar.
- `svlang`: 10,0/10; ”Home Assistant” markeras enbart som produktnamn.
- Inga platshållare, pluralformer eller formateringsmarkörer förekommer.
- Ingen ändring skickades, eftersom de sparade översättningarna redan är korrekta.
