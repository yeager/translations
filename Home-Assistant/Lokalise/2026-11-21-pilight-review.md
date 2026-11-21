# Home Assistant – Pilight: svensk radgranskning

Datum: 2026-11-21  
Komponent: `pilight`  
Omfattning: 4/4 aktuella källsträngar

| Fullständig nyckel | Engelsk källtext | Befintlig svensk text | Föreslagen text | Bedömning |
| --- | --- | --- | --- | --- |
| `component::pilight::services::send::description` | Sends RF code to Pilight device. | Skickar RF-kod till Pilight-enheten. | Oförändrad | Korrekt. |
| `component::pilight::services::send::fields::protocol::description` | Protocol that Pilight recognizes. See {pilight_protocols_docs_url} for supported protocols and additional parameters that each protocol supports. | Protokoll som Pilight känner igen. Se {pilight_protocols_docs_url} för en lista över protokoll som stöds samt ytterligare parametrar som varje protokoll stöder. | Oförändrad | Tydlig formulering; platshållaren är bevarad. |
| `component::pilight::services::send::fields::protocol::name` | Protocol | Protokoll | Oförändrad | Korrekt. |
| `component::pilight::services::send::name` | Send | Skicka | Oförändrad | Korrekt UI-verb. |

## Verifiering

- Aktuell källa och svenska värden hämtades via Lokalise API.
- `l10n-lint`: inga problem, inklusive platshållarkontroll.
- `hunspell-sv`: inga relevanta stavningsanmärkningar.
- `svlang`: 10,0/10; Pilight och `{pilight_protocols_docs_url}` är förväntade produkt-/tekniska beteckningar.
- Inga pluralformer eller ytterligare formateringsmarkörer förekommer.
- Ingen ändring skickades, eftersom de sparade översättningarna redan är korrekta.
