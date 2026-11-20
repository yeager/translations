# Home Assistant Core — granskning sida 479 (JVC Projector, ONVIF och DWD Weather Warnings)

Datum: 2026-11-20  
Status: dokumenterat förslag; **inte sparat i Lokalise**

ONVIF-källtexten kontrollerades mot `homeassistant/components/onvif/strings.json` på Home Assistant Cores `dev`-gren.

| Fullständig nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
|---|---|---|---|
| `component::onvif::config::step::reauth_confirm::description` | `Vissa enheter avvisar autentisering om tiden inte är synkroniserad med mindre än 5 sekunder. Om autentiseringen misslyckas kontrollerar du att tiden på enheten är korrekt och försöker igen.` | `Vissa enheter avvisar autentisering om tiden skiljer sig med mer än 5 sekunder. Om autentiseringen misslyckas kontrollerar du att tiden på enheten är korrekt och försöker igen.` | Den befintliga texten vänder källans villkor ”more than 5 seconds” till ”mindre än 5 sekunder”. |

Övriga 19 nycklar på sidan granskades utan dokumenterat ändringsförslag. Tolv JVC- och två DWD-nycklar är direkta referenser; projektor- och Warncell-texterna bevarar etablerade termer och uppgifter.
