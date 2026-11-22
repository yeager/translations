# Launch Library: fullständig komponentgranskning

Samtliga åtta svenska strängar lästes från Lokalise API och granskades rad för
rad den 22 november 2026. Sju var korrekta.
`component::launch_library::entity::sensor::starship_event::name` rättades från
`Nästa Starship-event` till `Nästa Starship-händelse`, i linje med
terminologibankens rekommendation *Event* → *Händelse*. Ändringen sparades och
lästes tillbaka via API.

Oförändrade nycklar: `config::step::user::description`, `launch_mission`,
`launch_probability`, `launch_status`, `launch_time`, `next_launch` och
`starship_launch`.
