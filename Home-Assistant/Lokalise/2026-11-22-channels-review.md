# Channels: fullständig svensk granskning

Granskad 22 november 2026 mot aktuell källtext och aktuella svenska
översättningar i Lokalise via API. Samtliga åtta strängar i komponenten
`channels` har lästs från Lokalise.

## Tidigare rättningar som verifierats i Lokalise

De sju tjänstetexterna med engelska `seek` hade tidigare felaktigt översatts
som sökning. De använder nu genomgående `hoppa`, vilket avser förflyttning i
uppspelningens tidsposition. Samtliga värden nedan lästes tillbaka från
Lokalise vid denna granskning.

| Fullständig nyckel | Aktuell svensk text |
| --- | --- |
| `component::channels::services::seek_backward::description` | Hoppar bakåt med ett visst antal sekunder. |
| `component::channels::services::seek_backward::name` | Hoppa bakåt |
| `component::channels::services::seek_by::description` | Hoppar med ett angivet antal sekunder. |
| `component::channels::services::seek_by::fields::seconds::description` | Antal sekunder att hoppa. Negativa tal hoppar bakåt. |
| `component::channels::services::seek_by::fields::seconds::name` | Sekunder |
| `component::channels::services::seek_by::name` | Hoppa med |
| `component::channels::services::seek_forward::description` | Hoppar framåt med ett visst antal sekunder. |
| `component::channels::services::seek_forward::name` | Hoppa framåt |

## Verifiering

- Lokalise API: alla åtta svenska översättningar hämtades direkt vid denna
  granskning.
- Riktning, antal sekunder och betydelsen för negativa tal bevaras i samtliga
  strängar.
- `Hoppa` är konsekvent i tjänstnamn och beskrivningar och tydliggör att
  åtgärden inte söker efter innehåll.

Ingen osäker fråga eller oavslutad referens återstår för komponenten.
