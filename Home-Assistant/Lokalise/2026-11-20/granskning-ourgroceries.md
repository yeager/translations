# Home Assistant Core – OurGroceries

Datum: 2026-11-20  
Källa: Home Assistant Core `3d340fb5fdf03e7db48b45aec10f9b8da3b31c12`, `homeassistant/components/ourgroceries/strings.json`  
Lokalise: läsning av `component::ourgroceries`; inga skrivningar har gjorts.

## Ändringsförslag

| Nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- |
| `component::ourgroceries::config::step::reauth_confirm::title` | `Autentiseringen har upphört för {name}` | `[%key:common::config_flow::title::reauth%]` | Aktuell Core-källa använder en obligatorisk gemensam referens. Den fria texten har dessutom den ogrundade platshållaren `{name}` och ger Lokalise QA-fel. |
| `component::ourgroceries::config::step::reauth_confirm::data::password` | `Lösenord` | `[%key:common::config_flow::data::password%]` | Aktuell Core-källa kräver den gemensamma lösenordsreferensen; den fria texten ger Lokalise QA-fel. |

## Kontroll utan förslag

Övriga **sju aktuella** källsträngar är kontrollerade mot Core-källan.
`OurGroceries-lösenordet för {username} är inte längre giltigt. Ange det nya
lösenordet.` är korrekt och bevarar `{username}`. Inloggningsfelet och de
övriga delade referenserna är också korrekta.

## TMX och Lokalise

Förslagen är lokala och ännu inte sparade i Lokalise. Home Assistant-TMX:en
ändras därför inte.
