# Home Assistant Core – Dropbox

Datum: 2026-11-21

Alla 25 aktuella strängar jämfördes med Core `2fdaa177` och direkt återlästes från Lokalise. OAuth/OAuth2, återautentisering, behörigheter och `{docs_url}`, `{error}`, `{name}` och `{service}` kontrollerades.

| Nyckel | Befintlig text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `exceptions::oauth2_implementation_unavailable::message` | `OAuth2-implementation kan ej nås, försöker igen` | `OAuth2-implementeringen är inte tillgänglig. Försöker igen.` | Korrekt svensk sats och betydelse för `unavailable`. |
| `exceptions::cannot_connect::message` | `Fel på kommunikationen med Dropbox` | `Fel vid kommunikationen med Dropbox.` | Idiomatisk svensk feltext. |

Ändringarna PUT-sparades och direkt återlästes. Det verifierade Core-TMX-minnet validerades efter uppdateringen till 2 106 poster.
