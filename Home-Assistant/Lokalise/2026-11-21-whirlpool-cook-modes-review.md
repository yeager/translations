# Home Assistant Core – Whirlpool

Datum: 2026-11-21

Alla 210 Whirlpool-strängar har granskats mot aktuell källa och tidigare backup. 35 fel är rättade, sparade och API-återlästa.

De 15 felaktiga select-etiketterna för ugnens tillagningslägen har rättats. Ändringarna gäller huvud-, övre och nedre ugn och synkroniserar `Luftfritering`, `Konvektionsbakning`, `Konvektionsgrillning`, `Konvektionsstekning`, `Varmhållning`, `Grädda`, `Grilla` och `Viloläge` med komponentens redan korrekta sensorvärden. Ugnsetiketterna använder korrekt genitiv för nedre och övre ugn. De två avvecklingsmeddelandena och deras titlar har också rättats; Markdown, `{entity_id}`, `{entity_name}` och `{items}` är bevarade. De tre kontolåsmeddelandena använder korrekt `kontot` i stället för felaktigt `den`.
