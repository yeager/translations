# Home Assistant Core: kompletterande granskning av SwitchBot-fel

Kontrollerat i Lokalise den 19 november 2026. Ingen ändring har gjorts i Lokalise. Denna uppföljning är inte ett påstående om sammanhängande positionsgranskning.

| Fullständig nyckel | Engelska i Lokalise | Befintlig svenska | Bedömning |
|---|---|---|---|
| `component::switchbot::exceptions::operation_error::message` | An error occurred while performing the action: {error} | Ett fel uppstod när åtgärden utfördes: {error} | Behåll. Platshållaren är oförändrad. |
| `component::switchbot::exceptions::model_not_determined_error::message` | Could not determine the model of Switchbot {sensor_type} with address {address} from its Bluetooth advertisements; an actively scanning Bluetooth adapter or proxy in range may be required: {reason} | Det gick inte att fastställa modellen för Switchbot {sensor_type} med adressen {address} utifrån Bluetooth-annonseringar. En Bluetooth-adapter eller proxy som aktivt skannar och finns inom räckvidd kan krävas: {reason} | Ändrad bedömning jämfört med `granskning-2701-2940.md`: föreslå ”Det gick inte att fastställa modellen för SwitchBot-enheten av typen {sensor_type} med adressen {address} utifrån dess Bluetooth-annonseringar. Det kan krävas en Bluetooth-adapter eller proxy inom räckvidd som aktivt skannar: {reason}”. Konstruktionen tydliggör sensortypen och följer varumärkets skrivning. |

Platshållarna jämfördes mot källan. Hunspell-sv markerade varumärkessammansättningen och delar av platshållarna; svlang markerade varumärket och platshållarna som ord utanför frekvenslistan. Dessa träffar kräver ingen ändring. Övrig terminologi och minnesträffar har inte kontrollerats på nytt för denna uppföljning.
