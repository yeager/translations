# Home Assistant Core, Lokalise, svenska: Voice-batch 4

Datum: 2026-11-14

Tre ytterligare Voice-strängar har granskats i Lokalise, sparats direkt
upstream och återlästs i redigeraren:

- `component::voice_support::issues::app_setup_failed::description`
  - Home Assistant kunde inte installera eller starta Voice-appen, som behövs för nästa generations röstsystem. Kontrollera appen i appbutiken och starta sedan om Home Assistant för att försöka igen.
- `component::voice_support::exceptions::unsupported_version::message`
  - { name } { version } använder protokollversion { api_version }, men den här versionen av Home Assistant kräver version { supported_api_version }. Uppdatera appen eller Home Assistant.
- `component::voice_support::exceptions::cannot_connect::message`
  - Det går inte att ansluta till Voice-appen på { url }.

Platshållarna bevarades oförändrade i versions- och anslutningsfelen.

Kontroller: diffkontroll och Gitleaks för arkivändringen. Resursfilbaserade
kontroller kräver en exporterad lokaliseringsfil och är därför inte tillämpliga
på denna direkt sparade Lokalise-batch.

Status: sparad och verifierad upstream i Lokalise. Detta är en avgränsad batch,
inte en fullständig genomgång av projektet.
