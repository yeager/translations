# HP-skrivarens avancerade inställningar, batch 30

Sju värden sparades direkt i Home Assistant Core-projektet på Lokalise och
återlästes 2026-11-14.

| Nyckel | Svenska efter återläsning |
| --- | --- |
| `component::hp_printer::config::step::user::sections::advanced_settings::data_description::port` | Porten för skrivarens webbgränssnitt. Lämna tomt för att använda 80 eller 443 med SSL. |
| `component::hp_printer::config::step::reconfigure::sections::advanced_settings::data_description::port` | Porten för skrivarens webbgränssnitt. Lämna tomt för att använda 80 eller 443 med SSL. |
| `component::hp_printer::config::step::user::sections::advanced_settings::data::ssl` | Använder ett SSL-certifikat |
| `component::hp_printer::config::step::reconfigure::sections::advanced_settings::data::ssl` | Använder ett SSL-certifikat |
| `component::hp_printer::config::step::user::sections::advanced_settings::data::port` | Port |
| `component::hp_printer::config::step::reconfigure::sections::advanced_settings::data::port` | Port |
| `component::hp_printer::config::step::reconfigure::data_description::host` | Värdnamnet eller IP-adressen för din HP-skrivare. |

Fyra av värdena använder Lokalise-nyckelreferenser till etablerade,
gemensamma Home Assistant-värden. Referenserna sparades i stället för att
duplicera den engelska källtexten och den upplösta svenska texten återlästes.

Kontroll: värdena sparades i Lokalise och återlästes. `msgfmt`, l10n-lint,
svlang och Hunspell är inte tillämpliga på denna direktredigerade,
exportlösa JSON-batch. Arkivets diffkontroll och Gitleaks kördes före push.

Status: sparad i projektets etablerade upstreamkanal. Granskning,
synkronisering och release är inte verifierade.
