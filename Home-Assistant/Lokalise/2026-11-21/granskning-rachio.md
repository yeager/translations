# Home Assistant Core – Rachio

Datum: 2026-11-21  
Källa: aktuell Core `2fdaa177`, `homeassistant/components/rachio/strings.json`  
Status: samtliga 45 aktuella strängar granskade; en korrigering är sparad och återläst.

Referenssträngarna kontrollerades mot sina svenska motsvarigheter, inklusive
platshållaren `{api_key_url}`, Rachio-namnet och interna nyckelreferenser.
Övriga direkta service-, enhets- och konfigurationssträngar är korrekta.

| Nyckel | Befintlig svensk text | Sparad svensk text | Motivering |
| --- | --- | --- | --- |
| `entity::switch::rain_delay::name` | `Regn fördröjning` | `Regnfördröjning` | Svensk sammansättning skrivs ihop. Sparad och återläst i Lokalise 2026-11-21. |

Den sparade översättningen saknar här ett verifierat Lokalise-översättnings-ID
och läggs därför inte till i det kanoniska TMX-minnet förrän ett sådant ID kan
exporteras spårbart.
