# Home Assistant Core — granskning sida 466 (Workday)

Datum: 2026-11-20  
Status: dokumenterade förslag; **inte sparade i Lokalise**

Aktuell källtext kontrollerad mot `homeassistant/components/workday/strings.json` på Home Assistant Cores `dev`-gren. Backticks runt den tekniska nyckeln och avgränsaren bevaras.

| Fullständig nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
|---|---|---|---|
| `component::workday::config::step::options::data_description::add_holidays` | `Lägg till anpassade helgdagar som ÅÅÅÅ-MM-DD, eller som intervall med ',' som avgränsare` | `Lägg till anpassade helgdagar som ÅÅÅÅ-MM-DD eller som intervall med \`,\` som avgränsare` | Tar bort felaktigt kommatecken före alternativet och bevarar källans kodformatering för avgränsaren. |
| `component::workday::config::step::options::data_description::days_offset` | `Dagars förskjutning från aktuell dag` | `Förskjutning i dagar från aktuell dag` | Mer idiomatisk svensk formulering utan oklar genitivkonstruktion. |
| `component::workday::config::step::options::data_description::excludes` | `Välj vilka veckodagar som ska exkluderas som arbetsdagar. \n"Helgdagar" lägger till de för det konfigurerade landet, anpassningsbara med alla inställningarna nedan. Läs dokumentationen om hur du använder dem på rätt sätt.` | `Välj vilka veckodagar som ska exkluderas som arbetsdagar. Nyckeln \`holidays\` lägger till helgdagar för det konfigurerade landet och kan anpassas med alla inställningarna nedan. Läs dokumentationen om hur de används korrekt.` | `holidays` är en konfigurationsnyckel i källtexten, inte det svenska ordet ”Helgdagar”; förslaget bevarar den tekniska referensen och förtydligar satsen. |

Övriga 17 nycklar på sidan granskades utan dokumenterat ändringsförslag. Tre referensnycklar (306206714–306206716) och åtta referensbaserade optionsnycklar (306206718–306206724) ändras inte; deras mål ska följas via respektive ursprungsnyckel.
