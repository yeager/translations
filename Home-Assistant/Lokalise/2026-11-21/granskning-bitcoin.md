# Home Assistant Core – Bitcoin

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/bitcoin/strings.json`, tidigare radrapporter samt Lokalise API med direkt återläsning.

Status: samtliga 36 aktuella bladsträngar och deras referensmål är radgranskade. En korrigering sparades och återlästes från Lokalise; övriga aktiva värden är korrekta.

| Nyckel | Befintlig text | Sparad text | Motivering |
|---|---|---|---|
| `entity::sensor::btc_mined::name` | `Utbruten` | `Utvunnet` | Sensorvärdet saknar explicit substantiv; neutrumformen ger en korrekt och begriplig UI-etikett. |

De direkt återlästa värdena för YAML-varningarna bevarar `{integration_title}`, `{currency}` och ``{domain}`` samt radbrytningarna. Mätarnamnen använder etablerade termer, bland annat `Växelkurs`, `Hashhastighet`, `Svårighetsgrad`, `Utbrutna block` och `Handelsvolym`. Referenser för omkonfigurering är upplösta mot de aktuella valutafälten och har kontrollerats.

Tidigare radgranskningar för oförändrade strängar finns i `2026-11-19-granskning/granskning-2701-2940.md`, `granskning-2941-3180.md` och `granskning-5101-5340.md`. TMX-ledgern innehåller den sparade korrigeringen med Lokalise-ID `10168428932` och är validerad efter uppdateringen.
