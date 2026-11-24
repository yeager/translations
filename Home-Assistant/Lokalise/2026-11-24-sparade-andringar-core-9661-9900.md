# Home Assistant Core – OpenEVSE, batch 9661–9900

Datum: 2026-11-24

- Fullständig nyckel: `component::openevse::entity::select::override_state::name`
- Engelska: Override state
- Före: Åsidosätt tillstånd
- Sparad svenska: Åsidosättningens tillstånd
- Motivering: källan är en namngiven väljare. Den tidigare formuleringen var ett imperativ; nominalfrasen anger vad väljaren styr.
- Lokalise key ID: `935706926`; translation ID: `9759250601`. API-write och readback verifierade.
- Besen `Low voltage` behåller `Lågspänning`; sammansättningen bekräftas av Hunspell och HA-TM. Discogs beskrivning använder den senare sparade formen `Konfiguration av …` enligt granskningskvittot från 21 november.
