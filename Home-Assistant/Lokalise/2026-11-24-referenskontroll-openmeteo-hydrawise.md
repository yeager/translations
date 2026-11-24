# HA Core: referenskontroll av Open-Meteo och Hydrawise

Datum: 2026-11-24  
Källa: Home Assistant Core `origin/dev`, checkout hämtad 2026-11-24.  
Kontroll: Lokalise API, svenska och engelska värden återlästa.  
TM: Home Assistant Core-minnet i `swedish-tm`, snapshot, PO och TMX.

## Resultat

Kontrollerade källans `strings.json` för Open-Meteo och Hydrawise mot vartenda referensmål i den aktuella batchen `granskning-6061-6300.md`. Kontrollerna omfattar återanvända zonfält, användarbeskrivningar och Hydrawises gemensamma fältnamn i både omkonfigurering och återautentisering. 22 Lokalise-poster har synkats till Home Assistant-minnet med käll-ID, mål-ID och granskningsstatus; snapshot, PO och TMX har validerats mot API-värdena.

## Sparad ändring

- Fullständig nyckel: `component::hydrawise::config::step::reconfigure::data_description::api_key` (Lokalise key ID `958394137`).
- Befintlig svenska: `Du kan skapa en API-nyckel i avsnittet ”Kontouppgifter” i Hydrawise-appen.`
- Sparad svenska: `Du kan generera en API-nyckel i avsnittet ”Kontodetaljer” i Hydrawise-appen`
- Motivering: Källan refererar uttryckligen till användarflödets `data_description::api_key`. Den levande svenska referensen finns på key ID `599804055` och har nu återanvänts ordagrant, inklusive punktuationen i källmålet. Lokalise PUT följdes av API-återläsning.

## Verifierade befintliga poster

Ingen ändring behövdes för posterna nedan; deras svenska text matchar referensmålet eller står självständigt korrekt. De har markerats `verified-existing` i TM.

- Open-Meteo referensmål: `component::open_meteo::config::step::user::data_description::zone` (`951251386`) → `Zonen att hämta väderprognosen för.`; `component::open_meteo::config::step::user::data::zone` (`134530578`) → `Zon`.
- Open-Meteo konsumenter: `component::open_meteo::config::step::reconfigure::data_description::zone` (`958450440`) och `component::open_meteo::config::step::reconfigure::data::zone` (`958450439`).
- Hydrawise referensmål: `component::hydrawise::config::step::user::data_description::username` (`952156665`) → `E-postadressen som du använder för att logga in på ditt Hydrawise-konto.`; `...::password` (`952156664`) → `Lösenordet för ditt Hydrawise-konto.`; `...::api_key` (`599804055`) → `Du kan generera en API-nyckel i avsnittet ”Kontodetaljer” i Hydrawise-appen`.
- Hydrawise konsumenter i `reconfigure`: `...::reconfigure::data_description::username` (`958394139`), `...::password` (`958394138`), `...::api_key` (`958394137`), `...::data::username` (`958394136`), `...::data::password` (`958394135`), `...::data::api_key` (`958394134`).
- Hydrawise konsumenter i `reauth_confirm`: `...::reauth_confirm::data_description::username` (`958394133`), `...::password` (`952156663`), `...::api_key` (`599804053`), `...::data::username` (`958394132`), `...::data::password` (`598150236`), `...::data::api_key` (`599804052`).
- Gemensamma referensmål: `common::config_flow::data::username` (`39798296`) → `Användarnamn`; `...::password` (`39798295`) → `Lösenord`; `...::api_key` (`42787587`) → `API-nyckel`.

Källfiler kontrollerade: `homeassistant/components/open_meteo/strings.json` och `homeassistant/components/hydrawise/strings.json`. Inga osäkra fall återstår inom just dessa referensgrupper. Detta verifierar inte övriga nycklar i Core-batchen.
