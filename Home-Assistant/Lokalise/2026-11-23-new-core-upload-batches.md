# Home Assistant Core – nytillagda Lokalise-poster

Lokalises livefilter för oöversatta Core-poster visade 405 nya poster från
`translations-upload.json`, trots att en äldre lokal export saknade tomma
svenska värden. Därför är den äldre exporten inte ett statusunderlag.

Fyra explicita batcher har granskats och sparats via API den 23 november 2026:

- batch 1–2: 30 poster;
- batch 3: 30 poster;
- batch 4: 30 poster.

Varje PUT följdes av en API-läsning av samma översättnings-id. Efter den
ursprungliga noteringen har batch 5–17 också granskats: Victron GX,
Libre-hubbar, sensorer, KNX IP Secure, väder, A Better Routeplanner, WebDAV,
BLUETTI, Jellyfin, Seafile och radar. Totalt omfattar de dokumenterade
livebatcherna 383 poster.

De är införda i den kanoniska HA Core-TMX:en i
`github.com/yeager/swedish-tm`, grenen `ha-tmx-validator`, med manifest
och stabila Lokalise-id:n. TMX-valideringen efter batch 17 godkände 3 914
poster (3 744 med Lokalise-id).

## Full livekontroll efter batch 22

En sekventiell API-kontroll av samtliga 152 Core-sidor med
`include_translations=1` hittade inga svenska tomma poster med engelsk
källtext. Åtta svenska tomma poster återstår, men samtliga har helt tom
engelsk källtext och kan därför inte översättas i Lokalise:

- `component::sensor::issues::units_changed::description`
- `component::sensor::issues::unsupported_state_class::description`
- `component::sensor::issues::state_class_removed::description`
- `component::roborock::services::set_vacuum_goto_position::fields::x_coord::description`
- `component::roborock::services::set_vacuum_goto_position::fields::y_coord::description`
- `component::sensor::issues::mean_type_changed::description`
- `component::vacuum::issues::segments_changed::description`
- `component::vacuum::issues::segments_mapping_not_configured::description`

De är källprojektets tomma metadata, inte saknade svenska översättningar.

## Semantiska rättningar efter kökontrollen

En separat jämförelse av återkommande korta källsträngar identifierade och
verifierade 34 svenska inkonsekvenser. De berörde knapptriggers
(långtryck, tryck, släpp samt dubbel- till femklick), `AI tools`,
`Add conversation agent`, `Account name`, autentiseringsutgång och en
avvikande slutpunkt i `Account is already configured`, samt
`Actions on turn off`, larmklocka, upplevd temperatur och
applikationsuppgifter. Varje ändring sparades via
Lokalise API, lästes tillbaka och fördes in i den kanoniska TMX:en.

Arbetet fortsätter med återstående liveposter; detta dokument gör inget
anspråk på att Core är helt färdiggranskat.
