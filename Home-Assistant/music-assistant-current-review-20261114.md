# Home Assistant Core – Music Assistant

**Datum:** 2026-11-14

## Omfattning

Den arkiverade batchen `home-assistant-core-sv-20261023-music-assistant-and-services-batch-1.json` innehåller 16 svenska strängar för Home Assistant Cores `music_assistant`-integration.

Den aktuella källfilen på Home Assistant Cores `dev`-gren jämfördes rad för rad. Alla 16 nycklar finns kvar. Femton har fortsatt en egen engelsk källtext och den arkiverade svenska texten är fortfarande kontextuellt giltig. Nyckeln `config::abort::no_url_available` använder nu den gemensamma referensen `common::config_flow::abort::oauth2_no_url_available`; den äldre integrationsspecifika svenska texten ska därför inte skickas in igen.

## Kanal och upstream

Home Assistants dokumentation anger Lokalise i webbläsaren som kanal för gränssnittstext. Det finns inget verifierat inskickskvitto för den historiska Music Assistant-batchen och ingen åtkomlig Lokalise-session eller API-behörighet i denna arbetsmiljö. Batchen är alltså lokalt granskad, men inte verifierat inskickad.

En separat Home Assistant-rättning, `Preview` till `Förhandsgranskning`, är fortfarande markerad som väntande efter ett tidigare Lokalise-svar med HTTP 403. Den spärren är inte bevis för att Music Assistant-batchen har avvisats.

## Aktuell källa

Home Assistant Core senaste release vid kontrollen var `2026.11.1`, publicerad 2026-11-09.

## Nästa steg

När en inloggad Lokalise-session är tillgänglig: jämför de 15 kvarvarande nycklarna med aktuella svenska måltexter och spara endast saknade eller förbättrade texter. Ändra inte den gemensamma `no_url_available`-nyckeln genom en integrationsbatch.
