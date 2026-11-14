# HP-skrivare och La Marzocco, batch 29

Fem värden sparades direkt i Home Assistant Core-projektet på Lokalise och
återlästes 2026-11-14.

| Nyckel | Svenska efter återläsning |
| --- | --- |
| `component::lamarzocco::issues::missing_bluetooth_token::fix_flow::step::confirm::title` | Bluetooth-token saknas för `{name}` |
| `component::hp_printer::config::step::user::sections::advanced_settings::name` | Avancerade inställningar |
| `component::hp_printer::config::step::reconfigure::sections::advanced_settings::name` | Avancerade inställningar |
| `component::hp_printer::config::step::user::sections::advanced_settings::data_description::ssl` | Anslut till skrivarens webbgränssnitt via HTTPS. |
| `component::hp_printer::config::step::reconfigure::sections::advanced_settings::data_description::ssl` | Anslut till skrivarens webbgränssnitt via HTTPS. |

La Marzocco-rubriken och HP-skrivarens omkonfigurationsvärden använder
Lokalise-nyckelreferenser till de direkta värdena. De direkta svenska
värdena sparades och den upplösta svenska texten återlästes för respektive
referens. `{name}` är en avsiktligt bevarad platshållare.

Kontroll: värdena sparades i Lokalise och återlästes. `msgfmt`, l10n-lint,
svlang och Hunspell är inte tillämpliga på denna direktredigerade,
exportlösa JSON-batch. Arkivets diffkontroll och Gitleaks kördes före push.

Status: sparad i projektets etablerade upstreamkanal. Granskning,
synkronisering och release är inte verifierade.
