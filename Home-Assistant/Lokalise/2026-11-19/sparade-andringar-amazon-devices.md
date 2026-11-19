# Amazon Devices: inloggningskod

Kontrollerat, sparat och återläst i Lokalise den 19 november 2026.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::amazon_devices::common::data_description_code` | The one-time password to log in to your account. Currently, only tokens from OTP applications are supported. | Engångslösenordet för att logga in på ditt konto. För närvarande stöds endast tokens från OTP-program. | Engångslösenordet för att logga in på ditt konto. För närvarande stöds endast engångskoder från autentiseringsappar. |

Syftet är att beskriva de engångskoder som användaren får från en autentiseringsapp. De två observerade referenserna till den gemensamma texten behölls. Lokalise visar en generell QA-markering vid det svenska ordet ”autentiseringsappar”; inget fel i textens innehåll konstaterades.

## Uppföljning av gemensamma referensmål

Kontrollerat i Lokalise: `data_description_username` = ”E-postadressen för ditt Amazon-konto.”, `data_description_password` = ”Lösenordet för ditt Amazon-konto.”, `data_description_country` = ”Landet för ditt Amazon-konto.” och `data_country` = ”Landskod”. De svenska referenserna från konfigurationsflödet motsvarar källreferenserna. Engångskodens beskrivning har dokumenterats ovan.

Fältetiketten `component::amazon_devices::config::step::user::data::code` hänvisar i både engelska och svenska till `component::amazon_devices::common::data_description_code`, alltså en hel beskrivning. Det separata mål som ser ut som en fältetikett är `component::amazon_devices::common::data_code`: ”One-time password (OTP code)” / ”Engångslösenord (OTP-kod)”. Detta är en möjlig källavvikelse och ändrades inte enbart på svenska. Ett försök att läsa `homeassistant/components/amazon_devices/strings.json` på Home Assistant Cores aktuella utvecklingsgren gav 404; kontrollera projektets version och källans status innan en uppströmsändring föreslås.
