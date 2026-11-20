# Home Assistant Core – BMW Connected Drive

Datum: 2026-11-20

En tidigare notering om saknade Lokalise-nycklar var felaktig: sökningen använde exaktmatchning med en ofullständig komponentnyckel. Nedanstående fullnyckelsgranskning ersätter den noteringen.

| Nyckel | Källa | Svenska | Bedömning |
| --- | --- | --- | --- |
| `component::bmw_connected_drive::issues::integration_removed::title` | `The BMW Connected Drive integration has been removed` | `BMW Connected Drive-integrationen har tagits bort` | Verifierad befintlig, korrekt rubrik (ID 826404719). |
| `component::bmw_connected_drive::issues::integration_removed::description` | `The BMW Connected Drive integration has been removed from Home Assistant.\n\nIn September 2025, BMW blocked third-party access to their servers by adding additional security measures. For EU-registered cars, a community-developed [custom component]({custom_component_url}) using BMW's CarData API is available as an alternative.\n\nTo resolve this issue, please remove the (now defunct) integration entries from your Home Assistant setup. [View your existing BMW Connected Drive integration entries]({entries}).` | `Integrationen BMW Connected Drive har tagits bort från Home Assistant.\n\nI september 2025 blockerade BMW tredjepartsåtkomst till sina servrar genom ytterligare säkerhetsåtgärder. För EU-registrerade bilar finns en communityutvecklad [anpassad komponent]({custom_component_url}) som använder BMW:s CarData API som alternativ.\n\nFör att lösa problemet tar du bort de numera obrukbara integrationsposterna från din Home Assistant-konfiguration. [Visa dina befintliga BMW Connected Drive-integrationsposter]({entries}).` | Sparad och återläst i Lokalise (ID 826404718). Språket är förtydligat och båda Markdown-plats­hållarna är bevarade. |
