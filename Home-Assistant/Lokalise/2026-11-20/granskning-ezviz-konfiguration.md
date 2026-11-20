# Home Assistant Core – Ezviz: konfiguration

Datum: 2026-11-20. Samtliga **35** aktuella konfigurationssträngar lästes i Lokalise och kontrollerades mot `homeassistant/components/ezviz/strings.json` i Core-commit `3d340fb5fdf03e7db48b45aec10f9b8da3b31c12`. Lokalise visar dessutom den historiska nyckeln `config::abort::reauth_successful`, som saknas i aktuell källa.

## Tydliga ändringsförslag: återställ referenser

| Fullständig nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- |
| `component::ezviz::config::step::reconfigure::data::url` | URL | `[%key:common::config_flow::data::url%]` | Sparad och återläst i Lokalise. Källan är en obligatorisk referens till den gemensamma nyckeln. |
| `component::ezviz::config::step::reconfigure::data::password` | Lösenord | `[%key:common::config_flow::data::password%]` | Sparad och återläst i Lokalise. Återställer den obligatoriska gemensamma referensen. |
| `component::ezviz::config::error::unknown` | Oväntat fel | `[%key:common::config_flow::error::unknown%]` | Sparad och återläst i Lokalise. Återställer den obligatoriska gemensamma referensen. |

## Bedömning av övriga rader

De återstående 32 aktuella raderna är korrekta. Samtliga gemensamma referenser för användarnamn, lösenord, URL och återautentisering är bevarade. De specifika svenska formuleringarna för MFA, konton, region-URL, RTSP-uppgifter och kameraupptäckt motsvarar källtexten. Platshållarna `{username}`, `{serial}` och `{ip_address}` är oförändrade.

## Validering och minneshantering

- Referensmålen jämfördes med aktuell Core-källfil; de tre förslagen återställer exakt respektive källreferens.
- Lokalise visar uttryckligen formatavvikelse för alla tre befintliga svenska värden.
- Alla tre referenser är sparade, återlästa och införda i det kanoniska
  HA-TMX-minnet.
