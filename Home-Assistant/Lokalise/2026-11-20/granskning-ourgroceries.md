# Home Assistant Core – OurGroceries

Datum: 2026-11-20  
Källa: Home Assistant Core `3d340fb5fdf03e7db48b45aec10f9b8da3b31c12`, `homeassistant/components/ourgroceries/strings.json`  
Lokalise: de två obligatoriska referenserna återställdes, sparades och lästes
tillbaka 2026-11-20.

## Ändringsförslag

| Nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- |
| `component::ourgroceries::config::step::reauth_confirm::title` | `Autentiseringen har upphört för {name}` | `[%key:common::config_flow::title::reauth%]` | Sparad och återläst i Lokalise. Aktuell Core-källa använder den obligatoriska gemensamma referensen; den fria texten hade dessutom den ogrundade platshållaren `{name}`. |
| `component::ourgroceries::config::step::reauth_confirm::data::password` | `Lösenord` | `[%key:common::config_flow::data::password%]` | Sparad och återläst i Lokalise. Aktuell Core-källa kräver den gemensamma lösenordsreferensen. |

## Kontroll utan förslag

Övriga **sju aktuella** källsträngar är kontrollerade mot Core-källan.
`OurGroceries-lösenordet för {username} är inte längre giltigt. Ange det nya
lösenordet.` är korrekt och bevarar `{username}`. Inloggningsfelet och de
övriga delade referenserna är också korrekta.

## TMX och Lokalise

De två sparade och återlästa referenserna är införda i den kanoniska Home
Assistant-TMX:en med fullständig nyckel, källproveniens och statusen
`saved-and-read-back`.
