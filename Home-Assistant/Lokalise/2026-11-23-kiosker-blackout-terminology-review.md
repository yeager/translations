# Kiosker: blackout-termer

Datum: 2026-11-23. Kiosker använder *blackout* för appens styrda mörkläggningsskärm, inte för ett strömavbrott. Samtliga nedanstående nycklar lästes direkt via Lokalise API, sparades och återlästes.

| Fullständig nyckel | Befintlig svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::kiosker::entity::button::blackout_clear::name` | `Rensa blackout` | `Avsluta mörkläggningsläge` | Åtgärden avslutar läget. |
| `component::kiosker::services::set_blackout::description` | `Ställ in blackout-skärm med anpassat meddelande` | `Visa mörkläggningsskärm med anpassat meddelande` | Översätter funktionsnamnet. |
| `component::kiosker::services::set_blackout::fields::dismissible::description` | `Om blackouten kan avfärdas genom användarinteraktion` | `Om mörkläggningsläget kan avfärdas genom användarinteraktion` | Samma funktionsbetydelse. |
| `component::kiosker::services::set_blackout::fields::expire::description` | `Tid i sekunder innan blackouten löper ut` | `Tid i sekunder innan mörkläggningsläget upphör` | Samma funktionsbetydelse. |
| `component::kiosker::services::set_blackout::fields::text::description` | `Text som ska visas på avstängningsskärmen` | `Text som ska visas på mörkläggningsskärmen` | Enhetlig term. |
| `component::kiosker::services::set_blackout::fields::visible::description` | `Anger om blackouten ska vara synlig` | `Anger om mörkläggningsläget är synligt` | Enhetlig term och idiomatisk formulering. |
| `component::kiosker::services::set_blackout::name` | `Ställ in blackout` | `Aktivera mörkläggningsläge` | Tydlig tjänsteåtgärd. |
| `component::kiosker::entity::binary_sensor::blackout_dismissible::name` | `Blackout som kan avfärdas` | `Mörkläggningsläge kan avfärdas` | Aktiv binär sensors etikett. |
| `component::kiosker::entity::sensor::blackout_background::name` | `Bakgrundsfärg för blackout` | `Bakgrundsfärg för mörkläggningsläget` | Enhetlig term. |
| `component::kiosker::entity::sensor::blackout_button_background::name` | `Bakgrundsfärg för blackout-knapp` | `Bakgrundsfärg för knappen i mörkläggningsläget` | Förtydligar knappens sammanhang. |
| `component::kiosker::entity::sensor::blackout_button_foreground::name` | `Förgrundsfärg för blackout-knapp` | `Förgrundsfärg för knappen i mörkläggningsläget` | Förtydligar knappens sammanhang. |
| `component::kiosker::entity::sensor::blackout_button_text::name` | `Text på blackout-knapp` | `Knapptext i mörkläggningsläget` | Idiomatisk etikett. |
| `component::kiosker::entity::sensor::blackout_expire::name` | `Giltighetstid för blackout` | `Mörkläggningslägets giltighetstid` | Enhetlig term. |
| `component::kiosker::entity::sensor::blackout_foreground::name` | `Förgrundsfärg för blackout` | `Förgrundsfärg för mörkläggningsläget` | Enhetlig term. |
| `component::kiosker::entity::sensor::blackout_icon::name` | `Blackout ikon` | `Ikon för mörkläggningsläget` | Svensk ordföljd och term. |
| `component::kiosker::entity::sensor::blackout_sound::name` | `Blackout ljud` | `Ljud för mörkläggningsläget` | Svensk ordföljd och term. |
| `component::kiosker::entity::sensor::blackout_text::name` | `Text för strömavbrott` | `Text för mörkläggningsläget` | Rättar den felaktiga betydelsen strömavbrott. |

De 17 live-posterna är infogade i den kanoniska Home Assistant-TMX:en, som validerades efter uppdateringen.
