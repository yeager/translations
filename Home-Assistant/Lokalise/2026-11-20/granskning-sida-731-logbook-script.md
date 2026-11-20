# Home Assistant Core – sida 731: granskningsstatus

Datum: 2026-11-20. Den lokala Lokalise-sessionen återställdes under sista referensvalideringen. Den här filen skiljer därför verifierat sparade ändringar från ett kvarstående förslag.

## Verifierat sparade och återlästa; synkade till TMX

| Fullständig nyckel | Före | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::logbook::services::log::fields::domain::description` | Ikonen illustrerar integrationsdomänen relaterad till denna loggbokspost. | Ikonen illustrerar integrationsdomänen som är kopplad till loggboksposten. | Idiomatisk svensk relation. |
| `component::logbook::services::log::fields::message::description` | Meddelande från loggboksposten. | Meddelande för loggboksposten. | Rätt preposition. |
| `component::logbook::services::log::fields::name::description` | Anpassat namn för en entitet, kan refereras till med hjälp av 'Entitets-ID'-fältet. | Anpassat namn för en entitet. Det kan refereras till med fältet ”Entitets-ID”. | Fullständig mening och konsekvent citattecken. |
| `component::logbook::services::log::name` | Loggaktivitet | Logga aktivitet | Åtgärdsform i stället för substantivsammanställning. |
| `component::script::services::reload::name` | `[%key:common::action::reload%] script` | `[%key:common::action::reload%] skript` | Bevarad referenssyntax; översatt svans. |

Samtliga fem poster ovan återlästes på nytt i Lokalise den 2026-11-20 och synkades därefter till Home Assistant-minnet med respektive Lokalise-översättnings-ID.

## Verifierat sparad och synkad referenssträng

| Fullständig nyckel | Tidigare text | Verifierad svenska | Orsak |
| --- | --- | --- | --- |
| `component::script::services::toggle::name` | `[%key:common::action::toggle%] script` | `[%key:common::action::toggle%] skript` | Samma engelska läcka som i reload-rubriken. Återläst i Lokalise och synkad till TMX. |

## Verifieringsunderlag

Den autentiserade Lokalise-läsytan återetablerades. Varje post ovan kontrollerades mot aktuell engelsk källtext och det visade svenska målvärdet innan synkning. Ingen Lokalise-skrivning har gjorts. `/tmp` används inte för fortsatt arbete.
