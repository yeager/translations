# Sparade ändringar för my-PV

Tre tidigare tomma fält sparades och återlästes i Lokalise 2026-11-19.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::my_pv::config::step::reconfigure_auth::title` | {name} password | Tom | Lösenord för {name} |
| `component::my_pv::config::step::reconfigure::title` | Reconfigure {name} | Tom | Konfigurera om {name} |

Referensen för `component::my_pv::config::step::reconfigure_auth::data_description::password` var tom och sparades som `[%key:component::my_pv::common::password_description%]`, samma referens som källan. Måltexten kontrollerades i Lokalise.

Övriga tre tomma referenser i omkonfigurationsgruppen behöver kontroll av måltexterna. Platshållaren `{name}` bevarades i båda rubrikerna.

## Värdbeskrivning

`component::my_pv::config::step::reconfigure::data_description::host` hade tom svensk text och sparades samt återlästes 2026-11-19 med källans referens `[%key:component::my_pv::config::step::user::data_description::host%]`. Måltexten kontrollerades: ”IP-adressen eller värdnamnet för din my-PV-enhet.”

Två gemensamma referensmål för fältnamnen värd och lösenord återstår att kontrollera direkt. Referensändringen är inte ett separat textsegment i TMX.

## Gemensamma fältnamn

Två tidigare tomma fält sparades och återlästes i Lokalise 2026-11-19. De engelska källorna använder samma referenser.

| Fullständig nyckel | Sparad svensk referens | Kontrollerat mål |
|---|---|---|
| `component::my_pv::config::step::reconfigure_auth::data::password` | `[%key:common::config_flow::data::password%]` | Password / Lösenord |
| `component::my_pv::config::step::reconfigure::data::host` | `[%key:common::config_flow::data::host%]` | Host / Värd |

Målen kontrollerades direkt med exakt nyckelsökning. De sex my-PV-fälten i omkonfigurationsgruppen är därmed ifyllda.
