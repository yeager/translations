# Home Assistant Core – Eight Sleep

Datum: 2026-11-20

En tidigare notering om saknade Lokalise-nycklar var felaktig: sökningen använde exaktmatchning med en ofullständig komponentnyckel. Nedanstående fullnyckelsgranskning ersätter den noteringen.

| Nyckel | Källa | Svenska | Bedömning |
| --- | --- | --- | --- |
| `component::eight_sleep::issues::integration_removed::title` | `The Eight Sleep integration has been removed` | `Eight Sleep-integrationen har tagits bort` | Verifierad befintlig rubrik (ID 398666686). |
| `component::eight_sleep::issues::integration_removed::description` | `The Eight Sleep integration has been removed from Home Assistant.\n\nThe Eight Sleep API has changed and now requires a unique secret which is inaccessible outside of their apps.\n\nTo resolve this issue, please remove the (now defunct) integration entries from your Home Assistant setup. [View your existing Eight Sleep integration entries]({entries}).` | `Eight Sleep-integrationen har tagits bort från Home Assistant.\n\nEight Sleep API har ändrats och kräver nu en unik hemlighet som inte är åtkomlig utanför deras appar.\n\nFör att lösa problemet tar du bort de numera obrukbara integrationsposterna från din Home Assistant-konfiguration. [Visa dina befintliga Eight Sleep-integrationsposter]({entries}).` | Sparad och återläst i Lokalise (ID 398666685). Den oöversatta termen `secret`, felaktigt singular och otydlig länktext har rättats; platshållaren är bevarad. |
