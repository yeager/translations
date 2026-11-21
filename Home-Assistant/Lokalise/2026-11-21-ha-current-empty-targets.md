# Home Assistant — komplettering av aktuella tomma svenska mål

Datum: 2026-11-21  
Plattform: Lokalise API  
Språk: `sv`

## Sparade strängar

| Fullständig nyckel | Engelska | Sparad svenska |
|---|---|---|
| `component::homewizard::issues::migrate_to_v2_api::fix_flow::progress::wait_for_button` | Press the button on the HomeWizard device for two seconds. The reconfiguration continues automatically once the button is pressed. | Tryck på knappen på HomeWizard-enheten i två sekunder. Omkonfigureringen fortsätter automatiskt när knappen har tryckts ned. |
| `component::homewizard::issues::migrate_to_v2_api::fix_flow::step::authorize_timeout::description` | The button on the HomeWizard device was not pressed within five minutes. Select the button below to try again. | Knappen på HomeWizard-enheten trycktes inte ned inom fem minuter. Välj knappen nedan för att försöka igen. |
| `component::homewizard::issues::migrate_to_v2_api::fix_flow::step::authorize_timeout::title` | Authorize | Godkänn |
| `component::irm_kmi::entity::binary_sensor::warning::name` | Warning | Varning |
| `component::irm_kmi::entity::binary_sensor::warning::state_attributes::warnings::name` | Warnings | Varningar |
| `component::irm_kmi::entity::sensor::next_warning::name` | Next warning | Nästa varning |

## Verifiering

- Samtliga sex översättningar lästes tillbaka från Lokalise efter API-sparning.
- Inga platshållare förekommer i de sex källsträngarna.
- API:s återstående svenska ”oöversatta” poster är 32 strukturella plural-/objektbehållare med tomma objekt i både engelska och svenska. De är inte synliga målsträngar och lämnades oförändrade.
- Hela aktuella HomeWizard-källfilen kontrollerades mot Lokalise: 82 av 82 nycklar finns och inga svenska mål är tomma.
- Hela aktuella IRM KMI-källfilen kontrollerades mot Lokalise: 19 av 19 nycklar finns, inga svenska mål är tomma och inga platshållaravvikelser hittades.
