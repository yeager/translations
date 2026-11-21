# Home Assistant Core – VegeHub

Datum: 2026-11-21

Alla 19 VegeHub-strängar har granskats mot den äldre rapporten och aktuell källa. Tre förbättringar är sparade och API-återlästa.

| Nyckel | Sparad svenska | Motivering |
| --- | --- | --- |
| `config::abort::timeout_connect` | `Tidsgränsen för anslutningen överskreds ...` | Exakt och idiomatiskt felmeddelande. |
| `config::step::user::data_description::ip_address` | `IP-adressen till den VegeHub som ska anslutas` | Ersätter den otydliga sammansättningen `mål-VegeHub`. |
| `config::step::user::description` | `Vill du konfigurera den här VegeHub-enheten?` | Naturlig svensk produktbeteckning. |

Zeroconf-texten hade redan den korrekta enhetsformen och är oförändrad. Inga platshållare ändrades.
