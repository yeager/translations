# Home Assistant: retroaktiv 1-Wire-översättning

`component::onewire::entity::binary_sensor::sensed_id::name` korrigerades från `Kände {id}` till `Ingångskanal {id}` och verifierades live i Lokalise. Nyckeln finns kvar i den aktuella Core-källan. Home Assistants dokumentation anger att Sensed är tillståndet för en ingångskanal; platsbaserad granskning i äldre rapporter hittades inte, därför användes den fullständiga nyckeln vid kontroll. TM-manifestet bevarar `{id}`.

Källa: [Home Assistant 1-Wire](https://www.home-assistant.io/integrations/onewire).
