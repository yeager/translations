# Home Assistant Core – Whirlpool: tillagningslägen

Datum: 2026-11-21

De 15 felaktiga select-etiketterna för ugnens tillagningslägen har rättats, sparats och API-återlästs. Ändringarna gäller huvud-, övre och nedre ugn och synkroniserar `Luftfritering`, `Konvektionsbakning`, `Konvektionsgrillning`, `Konvektionsstekning` och `Varmhållning` med komponentens redan korrekta sensorvärden. Ytterligare nio select-värden har samordnats för `Grädda`, `Grilla` och `Viloläge`, och tre ugnsetiketter använder nu korrekt genitiv för nedre och övre ugn. De två avvecklingsmeddelandena och deras titlar har också rättats; Markdown, `{entity_id}`, `{entity_name}` och `{items}` är bevarade. De tre kontolåsmeddelandena använder nu korrekt `kontot` i stället för felaktigt `den`.

Fullständig granskning av Whirlpool fortsätter; återstående strängar och TMX-verifieringsmanifest behandlas separat.
