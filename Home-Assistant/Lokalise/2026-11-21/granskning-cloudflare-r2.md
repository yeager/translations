# Home Assistant Core – Cloudflare R2

Datum: 2026-11-21

Källa: Home Assistant Core `2fdaa177`, `homeassistant/components/cloudflare_r2/strings.json`, tidigare förslag och direkt återläsning via Lokalise API.

Samtliga 20 aktuella strängar granskades. Fem säkra korrigeringar sparades och återlästes; tekniska värden, länken och exempelvägen bevarades.

| Fullständig nyckel | Befintlig svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::cloudflare_r2::config::error::invalid_credentials` | Bucket kan inte nås med det angivna åtkomstnyckel-ID:t och hemligheten. | Bucketen kan inte nås med det angivna åtkomstnyckel-ID:t och hemligheten. | Korrekt bestämd form. |
| `component::cloudflare_r2::exceptions::invalid_credentials::message` | Bucket kan inte nås med det angivna åtkomstnyckel-ID:t och hemligheten. | Bucketen kan inte nås med det angivna åtkomstnyckel-ID:t och hemligheten. | Korrekt bestämd form. |
| `component::cloudflare_r2::config::error::invalid_endpoint_url` | Ogiltig URL för slutpunkt. Ange en giltig URL för Cloudflare R2-slutpunkt. | Ogiltig URL för slutpunkten. Ange en giltig URL för Cloudflare R2-slutpunkten. | Korrekt bestämd form. |
| `component::cloudflare_r2::exceptions::invalid_endpoint_url::message` | Ogiltig URL för slutpunkt. Ange en giltig URL för Cloudflare R2-slutpunkt. | Ogiltig URL för slutpunkten. Ange en giltig URL för Cloudflare R2-slutpunkten. | Korrekt bestämd form. |
| `component::cloudflare_r2::config::step::user::data_description::prefix` | Valfri mappsökväg inuti bucket. Exempel: backups/homeassistant | Valfri mappsökväg i bucketen. Exempel: backups/homeassistant | Svensk grammatik. |

De fem språkparen är sparade i den kanoniska Home Assistant-TMX-filen med API-återläsning som källa. TMX-valideraren godkände 1 967 poster.
