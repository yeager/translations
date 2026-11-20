# Home Assistant Core – Energenie Power Sockets

Datum: 2026-11-20  
Källa: Home Assistant Core `3d340fb5fdf03e7db48b45aec10f9b8da3b31c12`, `homeassistant/components/energenie_power_sockets/strings.json`  
Lokalise: `component::energenie_power_sockets::entity::switch::socket::name`
ändrades, sparades och lästes tillbaka 2026-11-20.

## Ändringsförslag

| Nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- |
| `component::energenie_power_sockets::entity::switch::socket::name` | `Socket {socket_id}` | `Uttag {socket_id}` | Sparad och återläst i Lokalise. `Socket` var kvar på engelska; `Uttag` är den etablerade svenska benämningen för ett eluttag och behåller platshållaren. |

## Kontroll utan förslag

Övriga **åtta aktuella** källsträngar har kontrollerats mot Core-källan.
Avbrottstexter, `Välj en upptäckt enhet.`, produkttiteln och den delade
enhetsreferensen är korrekta. `svlang` godkände den föreslagna etiketten.
Hunspell-träffarna gäller endast produktnamnet och dess sammansättning.

## TMX och Lokalise

Det sparade och återlästa värdet är infört i den kanoniska Home Assistant-TMX:en
med fullständig nyckel, källproveniens och statusen `saved-and-read-back`.
