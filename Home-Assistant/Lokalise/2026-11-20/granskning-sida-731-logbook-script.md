# Home Assistant Core – sida 731: granskningsstatus

Datum: 2026-11-20. Den lokala Lokalise-sessionen återställdes under sista referensvalideringen. Den här filen skiljer därför verifierat sparade ändringar från ett kvarstående förslag.

## Verifierat sparade och återlästa; TMX-synkning väntar

| Fullständig nyckel | Före | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::logbook::services::log::fields::domain::description` | Ikonen illustrerar integrationsdomänen relaterad till denna loggbokspost. | Ikonen illustrerar integrationsdomänen som är kopplad till loggboksposten. | Idiomatisk svensk relation. |
| `component::logbook::services::log::fields::message::description` | Meddelande från loggboksposten. | Meddelande för loggboksposten. | Rätt preposition. |
| `component::logbook::services::log::fields::name::description` | Anpassat namn för en entitet, kan refereras till med hjälp av 'Entitets-ID'-fältet. | Anpassat namn för en entitet. Det kan refereras till med fältet ”Entitets-ID”. | Fullständig mening och konsekvent citattecken. |
| `component::logbook::services::log::name` | Loggaktivitet | Logga aktivitet | Åtgärdsform i stället för substantivsammanställning. |
| `component::script::services::reload::name` | `[%key:common::action::reload%] script` | `[%key:common::action::reload%] skript` | Bevarad referenssyntax; översatt svans. |

## Kvarstående, ej påstått synkad ändring

| Fullständig nyckel | Senast lästa svenska | Föreslagen svenska | Orsak |
| --- | --- | --- | --- |
| `component::script::services::toggle::name` | `[%key:common::action::toggle%] script` | `[%key:common::action::toggle%] skript` | Samma engelska läcka som i reload-rubriken. Slutlig API-återläsning saknas efter miljöåterställningen. |

## Blockerad verifiering

Lokalise-API-hjälparna och den tillhörande autentiserade browserytan rensades i miljöomstarten. Ingen ytterligare Lokalise-skrivning eller TMX-synkning görs förrän en ny autentiserad API-session finns. `/tmp` används inte för fortsatt arbete.
