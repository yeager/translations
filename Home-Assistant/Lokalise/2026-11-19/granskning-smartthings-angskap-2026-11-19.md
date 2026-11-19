# Home Assistant Core: SmartThings ångskåp

Kontrollerat i Lokalise den 19 november 2026 och jämfört med Home Assistant-minnets ögonblicksbild från 24 oktober. Ingen ändring har gjorts i Lokalise. Filtrerad sökning bevisar inte ofiltrerad ordning.

| Fullständig nyckel | Engelska | Befintlig svenska | Bedömning |
|---|---|---|---|
| `component::smartthings::entity::switch::sanitize::name` | Sanitize | Sanera | Osäkert: överväg ”Desinficering” om det stämmer med Samsungs svenska produktterm. Kontrollera produktdokumentation innan beslut; ”sanera” kan uppfattas bredare. |
| `component::smartthings::entity::switch::auto_cycle_link::name` | Auto Cycle Link | Auto Cycle Link | Behåll tills vidare. Kontrollera om detta är ett produktnamn eller har en etablerad svensk benämning. |
| `component::smartthings::entity::switch::keep_fresh_mode::name` | Keep fresh mode | Håll-färskt-läge | Osäkert förslag: ”Fräschhållningsläge”. Kontrollera Samsungs benämning och lägets funktion före beslut. |
| `component::smartthings::entity::binary_sensor::keep_fresh_mode_active::name` | Keep fresh mode active | Håll-färskt-läge aktivt | Osäkert förslag: ”Fräschhållningsläge aktivt”, om det föregående förslaget väljs. |

Home Assistants [switchimplementation](https://github.com/home-assistant/core/blob/dev/homeassistant/components/smartthings/switch.py) kopplar de tre switcharna till `STEAM_CLOSET`-funktioner, men den fastställer inte Samsungs svenska produktterminologi. De fyra engelska och svenska texterna överensstämmer med den historiska TMX-ögonblicksbilden. Tidigare lokal rapportsökning gav ingen träff på de fullständiga nycklarna. FOSS-termbanken stöder ”läge” och ”aktiv”, men gav ingen direkt träff för ”sanitize” eller ”fresh”. Hunspell-sv och svlang känner inte igen sammansättningen ”fräschhållningsläge”; verktygsträffarna avgör inte om produkttermen är lämplig. Inga platshållare, referenser eller pluralstrukturer förekommer.
