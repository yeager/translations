# HomeWizard: auktorisering och tidsgräns

Kontrollerat i Home Assistant Core i Lokalise den 19 november 2026. Alla fyra svenska måltexter var tomma. Förslagen nedan är **inte sparade i Lokalise**.

| Fullständig nyckel | Engelsk källtext | Befintlig svenska | Lokalt förslag |
|---|---|---|---|
| `component::homewizard::config::step::authorize_timeout::title` | `[%key:component::homewizard::config::step::authorize::title%]` | Tom | `[%key:component::homewizard::config::step::authorize::title%]` |
| `component::homewizard::config::step::authorize_timeout::description` | The button on the HomeWizard device was not pressed within five minutes. Select the button below to try again. | Tom | Knappen på HomeWizard-enheten trycktes inte in inom fem minuter. Välj knappen nedan för att försöka igen. |
| `component::homewizard::config::progress::wait_for_button` | Press the button on the HomeWizard device for two seconds. Setup continues automatically once the button is pressed. | Tom | Håll knappen på HomeWizard-enheten intryckt i två sekunder. Konfigurationen fortsätter automatiskt när du har tryckt på knappen. |
| `component::homewizard::config::abort::flow_closed` | The setup was closed before the device was authorized. | Tom | Konfigurationen stängdes innan enheten auktoriserades. |

Referensmålet `component::homewizard::config::step::authorize::title` kontrollerades i Lokalise och är ”Authorize” / ”Auktorisera”. Första förslaget bevarar källans nyckelreferens i stället för att hårdkoda måltexten. Texterna har inga platshållare eller pluralformer. Hunspell markerade produktnamnet i sammansättningen ”HomeWizard-enheten”; det är ett egennamn, inte ett belagt stavfel. Kontrollera aktuella värden igen före eventuell användning.
