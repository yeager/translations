# Home Assistant Core – Media Source

Datum: 2026-11-22

Alla sex Media Source-strängar är kontrollerade mot aktuell källtext och
återlästa via Lokalise API.

| Nyckel | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::media_source::exceptions::browse_media_failed::message` | Det gick inte att bläddra bland media med innehålls-ID {media_content_id}: {error} | Oförändrad | Korrekt. |
| `component::media_source::exceptions::resolve_media_failed::message` | Det gick inte att matcha media med innehålls-ID {media_content_id}: {error} | Det gick inte att hitta media med innehålls-ID {media_content_id}: {error} | *Hitta* är tydligt för användaren; *matcha media* är tvetydigt. |
| `component::media_source::exceptions::unknown_media_source::message` | Okänd mediekälla: {domain} | Oförändrad | Korrekt. |
| `component::media_source::common::sources_default` | Mediekällor | Oförändrad | Korrekt. |
| `component::media_source::exceptions::search_media_failed::message` | Det gick inte att söka efter media med innehålls-ID {media_content_id}: {error} | Oförändrad | Korrekt. |
| `component::media_source::exceptions::search_not_supported::message` | Sökning stöds inte för media med innehålls-ID {media_content_id} | Oförändrad | Korrekt. |

Platshållarna `{media_content_id}`, `{error}` och `{domain}` är
bevarade. Inga pluralformer eller markup berörs. Verktygsträffar gäller
endast platshållarnas identifierare.
