# Historikstatistik: återställda referenser

Kontrollerat och sparat i Lokalise den 19 november 2026. De engelska texterna innehåller samma referenser som de nu sparade svenska texterna.

| Fullständig nyckel | Tidigare svenska | Sparad svenska |
|---|---|---|
| `component::history_stats::config::step::state::data_description::state` | De tillstånd du vill spåra från entiteten. | `[%key:component::history_stats::config::step::user::data_description::state%]` |
| `component::history_stats::config::step::state::data_description::entity_id` | Enhet att hämta statistik från. | `[%key:component::history_stats::config::step::user::data_description::entity_id%]` |
| `component::history_stats::config::step::state::data::state` | Tillstånd | `[%key:component::history_stats::config::step::user::data::state%]` |
| `component::history_stats::config::step::state::data::entity_id` | Enhet | `[%key:component::history_stats::config::step::user::data::entity_id%]` |

Måltexterna kontrollerades: ”De tillstånd som du vill spåra från entiteten.”, ”Entitet att hämta statistik från.”, ”Tillstånd” respektive ”Entitet”. De övriga referensmålen för typ har texten ”Typen av sensor, antingen 'tid', 'kvot' eller 'antal'” och ”Typ”; kontrollera separat om dessa uppräknade värden är användarsynliga etiketter eller tekniska värden innan beskrivningen ändras. Lokalise visade tidigare varningar om referensavvikelse för de fyra ändrade nycklarna; de återlästa texterna innehåller nu motsvarande referenser.

## Uppföljning: typvärden

Kontrollerat mot [Home Assistants konfigurationsflöde](https://github.com/home-assistant/core/blob/dev/homeassistant/components/history_stats/config_flow.py) och [källsträngar](https://github.com/home-assistant/core/blob/dev/homeassistant/components/history_stats/strings.json): väljaren använder interna värden med en översättningsnyckel, och användargränssnittets alternativ har separata etiketter. Lokalise visar dessa etiketter som ”Tid”, ”Kvot” och ”Antal”. Den svenska beskrivningens ”tid”, ”kvot” och ”antal” motsvarar därför de synliga alternativen och behölls. Inga ytterligare ändringar gjordes i Lokalise vid kontrollen. Källversionerna var blobbarna `004694177a07940943233a9bb354f2b5f1a11d3b` respektive `1a33911307342df71a0a04fdc922ffda72d64493`.
