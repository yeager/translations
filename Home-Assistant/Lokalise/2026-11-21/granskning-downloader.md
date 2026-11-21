# Home Assistant Core – Downloader

Datum: 2026-11-21

Alla 23 aktuella strängar jämfördes med Core `2fdaa177` och direkt återlästes från Lokalise. Nedladdningsfält, sökvägar, HTTP-rubriker och `{subdir}`, `{url}` samt `{path}` kontrollerades.

| Nyckel | Befintlig text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `config::step::user::description` | `Installationen ...` | `Konfigurationen ...` | `setup` är konfigurationsflödet. |
| `services::download_file::fields::headers::description` | `HTTP-headers` | `HTTP-rubriker` | Svensk teknisk term. |
| `services::download_file::fields::headers::name` | `Headers` | `HTTP-rubriker` | Svensk teknisk term. |
| `exceptions::download_path_not_found::message` | `Hämtningssökvägen ...` | `Nedladdningssökvägen ...` | Konsekvent med komponentens nedladdningsterminologi. |
| `exceptions::not_loaded::message` | `Hämtaren ...` | `Nedladdaren ...` | Korrekt komponentterm. |

Ändringarna PUT-sparades och direkt återlästes. Det verifierade Core-TMX-minnet validerades efter uppdateringen till 2 095 poster.
