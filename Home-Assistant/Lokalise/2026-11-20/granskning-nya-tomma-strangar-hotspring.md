# Home Assistant Core – nya tomma strängar: HotSpring med följdposter

Datum: 2026-11-20. Granskning mot Lokalise och aktuell Core-källa. Raden `total_power` sparades och återlästes 2026-11-20; återstående rader är dokumenterade förslag.

## Förslag

| Fullständig nyckel | Engelsk källtext | Föreslagen svenska | Motivering |
| --- | --- | --- | --- |
| `component::hotspring::entity::sensor::total_power::name` | Total apparent power | Total skenbar effekt | Sparad och återläst i Lokalise (ID 984458735); Home Assistant-minnet använder *skenbar effekt* för *apparent power*. |
| `component::hotspring::entity::sensor::small_loads_power::name` | Small loads apparent power | Skenbar effekt för små laster | Sparad och återläst i Lokalise (ID 984458734); teknisk ordföljd och facktermen *skenbar effekt*. |
| `component::hotspring::entity::sensor::small_loads_current::name` | Small loads current | Ström för små laster | Sparad och återläst i Lokalise (ID 984458733); samma termstruktur som effektvärdet. |
| `component::hotspring::entity::sensor::jet3_power::name` | Jet 3 apparent power | Skenbar effekt för jet 3 | Sparad och återläst i Lokalise (ID 984458732); behåller komponentnamnet *jet* och översätter mätvärdet. |
| `component::hotspring::entity::sensor::jet3_current::name` | Jet 3 current | Ström för jet 3 | Sparad och återläst i Lokalise (ID 984458731); parallell med föregående sensor. |
| `component::hotspring::entity::sensor::jet1_jet2_blower_power::name` | Jets 1, 2, and blower apparent power | Skenbar effekt för jet 1, 2 och fläkt | Sparad och återläst i Lokalise (ID 984458730); konsekvent sensorbenämning. |
| `component::hotspring::entity::sensor::jet1_jet2_blower_current::name` | Jets 1, 2, and blower current | Ström för jet 1, 2 och fläkt | Sparad och återläst i Lokalise (ID 984458729); parallell med effektvärdet. |
| `component::hotspring::entity::sensor::heater_power::name` | Heater power | Värmarens effekt | Sparad och återläst i Lokalise (ID 984458728); naturlig svensk genitivform för en enhetssensor. |
| `component::hotspring::entity::sensor::heater_current::name` | Heater current | Värmarens ström | Sparad och återläst i Lokalise (ID 984458727); naturlig svensk genitivform för en enhetssensor. |
| `component::evohome::exceptions::api_credentials_invalid::message` | The vendor's API rejected the username or password | Leverantörens API avvisade användarnamnet eller lösenordet | Sparad och återläst i Lokalise (ID 984451507); tydlig feltext och etablerade svenska termer. |
| `component::tankerkoenig::services::get_opening_times::name` | Get opening times | Hämta öppettider | Åtgärdsform för tjänstnamn. Verifierad oförändrad i Lokalise (ID 984279363). |
| `component::tankerkoenig::services::get_opening_times::description` | Retrieves the opening times of a gas station and their temporary changes. | Hämtar en bensinstations öppettider och tillfälliga ändringar. | Korrekt genitiv och objekt. Verifierad oförändrad i Lokalise (ID 984279362). |
| `component::timer_list::triggers::timer_unpaused::name` | Timer resumed | Timer återupptagen | Kort händelserubrik utan onödigt hjälpverb. |
| `component::timer_list::triggers::timer_unpaused::description` | Triggers when a timer is resumed on a timer list. | Utlöses när en timer återupptas i en timerlista. | Bevarar triggerperspektivet och skiljer *timerlista* från en vanlig lista. |

## Käll- och verktygskontroll

- Lokalise visade nycklarna som nya, tomma svenska poster med nyckel-ID:n 984458727–984458735 (HotSpring), 984451507 (Evohome), 984279362–984279363 (Tankerkoenig) och 984043161–984043162 (Timer list).
- Aktuell Core-källa bekräftar Tankerkoenig- och Timer list-källtexterna. HotSpring-posterna finns i Lokalise men inte i Core-commit `3d340fb5fdf03e7db48b45aec10f9b8da3b31c12`; de behandlas därför som importerade, ännu ej publicerade källsträngar och är markerade för ny källkontroll före eventuell sparning.
- `swedish-tm` har flera tidigare, kontextuella poster som översätter *apparent power* till *skenbar effekt*. Hunspell godkänner beståndsdelarna i de svenska förslagen; inga nya generella ord behöver läggas till i ordboken.
- `svlang` gav 10/10 i naturlighetsheuristiken för `Skenbar effekt för jet 1, 2 och fläkt.` och fann inga skrivregelsfel i felmeddelandet. Dessutom fann `check` inga problem i Tankerkoenig-beskrivningen. Resultaten är granskningsstöd, inte ett ersättningsbeslut för komponentkontexten.

## Uppföljning

HotSpring-källan har därefter publicerats i Core och dess nio sensorposter är sparade och återlästa. Evohome-raden är också sparad och återläst. Tankerkoenig-raderna var redan korrekt översatta i Lokalise och verifierades oförändrade; ingen duplicerande skrivning gjordes.
