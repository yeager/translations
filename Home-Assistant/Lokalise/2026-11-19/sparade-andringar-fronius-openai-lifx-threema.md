# Sparade svenska översättningar: Fronius, OpenAI, LIFX och Threema

Datum: 2026-11-19

Alla poster nedan har sparats via Lokalise API och lästs tillbaka efter uppdateringen.

## Ändringar

### `component::fronius::config::step::user::data_description::auto_revert_power_limit`

- Engelska: The inverter drops the AC power limit and the battery charge and discharge limits an hour after it last received them, and returns to its own settings. Home Assistant sends active limits again every 15 minutes, so this only takes effect once it stops sending - because Home Assistant is down, or because the integration was removed. The battery minimum reserve and grid charging are not affected.
- Tidigare svenska: Växelriktaren tar bort AC-effektgränsen en timme efter att den senast tog emot den och återgår till sina egna inställningar. Home Assistant skickar gränsen igen var femtonde minut, så detta får bara effekt när systemet slutar skicka den eftersom Home Assistant är nere eller integreringen tagits bort. Batteriernas börvärden påverkas inte. Växelriktaren har ingen tidsgräns för dem.
- Sparad svenska: Växelriktaren tar bort gränsen för växelströmseffekt och gränserna för batteriets laddning och urladdning en timme efter att den senast tog emot dem och återgår till sina egna inställningar. Home Assistant skickar aktiva gränser igen var femtonde minut, så detta sker först när Home Assistant slutar skicka dem, till exempel när Home Assistant är nere eller integreringen har tagits bort. Batteriets lägsta reservnivå och laddning från elnätet påverkas inte.

### `component::fronius::config::step::user::data::auto_revert_power_limit`

- Engelska: Revert the power and battery limits if Home Assistant stops
- Tidigare svenska: Återställ gränsen för AC-effekt om Home Assistant stoppas
- Sparad svenska: Återställ effekt- och batterigränserna om Home Assistant stannar

### `component::openai_conversation::config::step::reconfigure::description`

- Engelska: Enter your updated OpenAI API key.
- Tidigare svenska: Ange din uppdaterade OpenAI API-nyckel.
- Sparad svenska: Ange din uppdaterade OpenAI-API-nyckel.

### `component::lifx::config::step::user::data_description::serial`

- Engelska: The twelve-character serial number printed on your LIFX device. On its own, it is resolved by broadcasting to your network.
- Tidigare svenska: Det tolvsiffriga serienumret som är tryckt på LIFX-enheten. Serienumret identifieras automatiskt via utsändning i nätverket.
- Sparad svenska: Serienumret med tolv tecken som är tryckt på LIFX-enheten. Om endast serienumret anges hittas enheten genom en utsändning i nätverket.

### `component::threema::config_subentries::recipient::step::user::data_description::recipient`

- Engelska: The 8-character Threema ID of the recipient.
- Tidigare svenska: Mottagarens åttateckens-Threema-ID.
- Sparad svenska: Mottagarens Threema-ID med åtta tecken.

### `component::threema::config::step::setup_new::description`

- Engelska: Your keys have been generated. Save them now before continuing!

Public key: `{public_key}`
Private key: `{private_key}`

When registering at gateway.threema.ch, paste the public key as shown above. Store the private key securely — it cannot be recovered.
- Tidigare svenska: Nycklarna har genererats. Spara dem innan du fortsätter!

Offentlig nyckel: `{public_key}`
Privat nyckel: `{private_key}`

När du registrerar på gateway.threema.ch klistrar du in den offentliga nyckeln enligt ovan. Förvara den privata nyckeln säkert. Den går inte att återställa.
- Sparad svenska: Nycklarna har genererats. Spara dem innan du fortsätter!

Offentlig nyckel: `{public_key}`
Privat nyckel: `{private_key}`

När du registrerar dig på gateway.threema.ch klistrar du in den offentliga nyckeln enligt ovan. Förvara den privata nyckeln säkert. Den går inte att återställa.
