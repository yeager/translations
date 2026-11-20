# Home Assistant Core – PG LAB Electronics

Datum: 2026-11-20  
Källa: Home Assistant Core `3d340fb5fdf03e7db48b45aec10f9b8da3b31c12`, `homeassistant/components/pglab/strings.json`  
Lokalise: läsning av `component::pglab`; inga skrivningar har gjorts.

## Resultat

Samtliga **9 aktuella** källsträngar har lästs i Lokalise och jämförts med
aktuell Core-källa. Inga ändringsförslag har identifierats.

- Entitetsnamnen `Lucka {shutter_id}`, `Temperatur`, `Körtid`,
  `MPU-spänning` och `Relä {relay_id}` är korrekta och behåller
  platshållarna.
- MQTT-instruktionen är tydlig och använder den etablerade produkttermen
  `MQTT-broker`.
- Båda avbrottstexterna och bekräftelsefrågorna är idiomatiska.

`svlang` godkände frågetexten. Hunspell-träffarna gäller tekniska identifierare
och platshållare, inte svenska stavfel.

## Historisk Lokalise-rad

`component::pglab::config::abort::single_instance_allowed` visas i Lokalise
men saknas i aktuell `strings.json`. Den behandlas som historisk.

## TMX och Lokalise

Inga värden har sparats eller återlästs som ändrade i Lokalise. Home
Assistant-TMX:en ändras därför inte.
