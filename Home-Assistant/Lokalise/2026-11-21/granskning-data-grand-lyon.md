# Home Assistant Core – Data Grand Lyon

Datum: 2026-11-21

Alla 99 aktuella strängar jämfördes med Core `2fdaa177` och direkt återlästes från Lokalise. Inga platshållare eller referenser berördes.

| Nyckel | Befintlig text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `config_subentries::stop::step::user::data::stop_id` | `Stopp` | `Hållplats` | Kollektivtrafikens `Stop` avser hållplats. |
| `config_subentries::park_and_ride::entry_type` | `Park & ride` | `Infartsparkering` | Svensk trafikterm. |
| `config_subentries::park_and_ride::initiate_flow::user` | `Lägg till park & ride` | `Lägg till infartsparkering` | Samma term. |
| `config_subentries::park_and_ride::step::user::data::park_id` | `Park & ride` | `Infartsparkering` | Samma term. |
| `config_subentries::park_and_ride::step::user::data_description::park_id` | `...ett park & ride-ID...` | `...ett infartsparkerings-ID...` | Samma term och korrekt sammansättning. |
| `entity::sensor::next_departure_1_direction::name` | `Nästa avgång 1 riktning` | `Riktning för nästa avgång 1` | Svensk ordföljd. |
| `entity::sensor::next_departure_1_type::name` | `Nästa avgång 1 typ` | `Typ för nästa avgång 1` | Svensk ordföljd. |
| `entity::sensor::next_departure_2_direction::name` | `Nästa avgång 2 riktning` | `Riktning för nästa avgång 2` | Svensk ordföljd. |
| `entity::sensor::next_departure_2_type::name` | `Nästa avgång 2 typ` | `Typ för nästa avgång 2` | Svensk ordföljd. |
| `entity::sensor::next_departure_3_direction::name` | `Nästa avgång 3 riktning` | `Riktning för nästa avgång 3` | Svensk ordföljd. |
| `entity::sensor::next_departure_3_type::name` | `Nästa avgång 3 typ` | `Typ för nästa avgång 3` | Svensk ordföljd. |
| `exceptions::update_failed_park_and_ride::message` | `...park & ride...` | `...infartsparkering...` | Konsekvent svensk trafikterm. |

Ändringarna PUT-sparades och direkt återlästes. Det verifierade Core-TMX-minnet validerades efter uppdateringen till 2 038 poster.
