# Home Assistant Core – sida 734: granskningsstatus

Datum: 2026-11-21  
Plattform: Lokalise API  
Omfattning: 100 aktiva nycklar, sida 734 av 752 (`limit=100`)

## Sparade och återlästa ändringar

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- | --- |
| `component::voice_support::config::step::zeroconf_confirm::description` | Do you want to connect to {name} at {host}? | Vill du ansluta till { name } på { host }? | Vill du ansluta till {name} på {host}? | Mellanslag inne i platshållarna bryter Home Assistant-referenserna. |
| `component::voice_support::exceptions::unsupported_version::message` | {name} {version} speaks protocol version {api_version}, but this Home Assistant needs version {supported_api_version}. Update the app or Home Assistant. | `{ name }`, `{ version }`, `{ api_version }`, `{ supported_api_version }` | `{name}`, `{version}`, `{api_version}`, `{supported_api_version}` | Samtliga fyra platshållare återställda exakt; övrig svensk formulering bevarad. |

## Kontroll

- De två ändringarna sparades genom Lokalise API och lästes tillbaka via respektive svenska översättnings-ID.
- Batchen täcker Voice Support, Hot Spring, Overseerr, HomeKit, Matter, Sofar, VeSync, ViCare, Arcam FMJ, Shelly, Silvercrest Infrared, Energi, Plugwise, Satel Integra och LIFX.
- De övriga 98 svenska målen granskades mot aktuell engelsk källa. Inga ytterligare säkra ändringar krävdes.
- Teknisk terminologi som `MAC-adress`, `HTTP`, `RPC`, `H.264`, `iCloud+`, `OEM` och `LED` bevarades.

## Resultat

Sida 734 är radgranskad. Två formatfel är rättade och verifierade; inga tomma synliga mål återstår i batchen.
