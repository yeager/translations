# Home Assistant Core – Tankerkoenig, del 2

Datum: 2026-11-20  
Källa: Home Assistant Core `3d340fb5fdf03e7db48b45aec10f9b8da3b31c12`,
`homeassistant/components/tankerkoenig/strings.json`  
Lokalise: radläsning av `component::tankerkoenig::config::` och
`component::tankerkoenig::entity::`.

## Granskade rader

Konfigurationsraderna för region, radie, bränsletyper och val av stationer är
korrekta. De delade referenserna till gemensamma datafält,
`already_configured`, `reauth_successful`, plats och API-nyckel är identiska
med Core-källan. `config::error::invalid_auth` och `no_stations` har korrekt
svensk innebörd; ingen ändring behövs.

Samtliga synliga sensorattribut kontrollerades. De direkta svenska etiketterna
`Märke`, `Stad`, `Bränsletyp`, `Husnummer`, `Postnummer`, `Stationens namn`
och `Gata` är korrekta. Barnsensorernas referenser till E5-attributen och
referenserna för latitud/longitud är korrekta. `Super` är också korrekt.

## Resultat

Inga nya ändringar upptäcktes i denna del. Tidigare sparade ändringar från del
1 är lästa tillbaka och finns i den verifierade TMX-overlayen. De tre extra
Lokalise-raderna jämfört med de 69 aktuella Core-löven hanteras som historiska
eller referensrelaterade tills en API-export kan ge fullständig ID-proveniens.
