# Sparade ändringar – 2026-11-19 (granskning 4861–5100)

Samtliga sju poster matchade aktuell Lokalise-källa och lästes tillbaka efter sparning.

## `component::gree_infrared::config::step::reconfigure::title`

**Engelska:** Reconfigure Gree AC

**Befintlig svenska:** Konfigurera om Gree luftkonditionering

**Sparad svenska:** Konfigurera om Gree-luftkonditionering

**Motivering:** Förbättrar svensk terminologi eller formulering utan betydelseförändring.

## `component::gree_infrared::config::step::reconfigure::description`

**Engelska:** Change the infrared entities and the supported modes of your Gree AC.

**Befintlig svenska:** Ändra infrarödsentiteterna och de lägen som stöds för din Gree luftkonditionering.

**Sparad svenska:** Ändra de infraröda entiteterna och de lägen som stöds för din Gree-luftkonditionering.

**Motivering:** Förbättrar svensk terminologi eller formulering utan betydelseförändring.

## `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::speed_up`

**Engelska:** Speed up

**Befintlig svenska:** Hastighet upp

**Sparad svenska:** Öka hastigheten

**Motivering:** Förbättrar svensk terminologi eller formulering utan betydelseförändring.

## `component::led_infrared::entity::event::received_command::state_attributes::event_type::state::speed_down`

**Engelska:** Speed down

**Befintlig svenska:** Hastighet ned

**Sparad svenska:** Minska hastigheten

**Motivering:** Förbättrar svensk terminologi eller formulering utan betydelseförändring.

## `component::unifiprotect::issues::last_event_sensor_deprecated::description`

**Engelska:** The entity `{entity_id}` is deprecated and will be removed in a future release. Use the event entity `{replacement}` with the **Event received** trigger instead. The event entity's state is the time of the last event Home Assistant received.

Update the following automations and scripts:
{items}

**Befintlig svenska:** Händelseentiteten `{entity_id}` är föråldrad och tas bort i en framtida version. Använd händelseentiteten `{replacement}` med utlösaren **Händelse mottagen** i stället. Händelseentitetens tillstånd är tidpunkten för den senaste händelse som Home Assistant tog emot.

Uppdatera följande automatiseringar och skript:
{items}

**Sparad svenska:** Entiteten `{entity_id}` är föråldrad och tas bort i en framtida version. Använd händelseentiteten `{replacement}` med utlösaren **Händelse mottagen** i stället. Händelseentitetens tillstånd är tidpunkten för den senaste händelse som Home Assistant tog emot.

Uppdatera följande automatiseringar och skript:
{items}

**Motivering:** Förbättrar svensk terminologi eller formulering utan betydelseförändring.

## `component::nest::issues::pubsub_subscription_not_found::description`

**Engelska:** The Nest integration entry **{entry_title}** could not connect to its Pub/Sub subscription. The subscription or its topic may have been deleted or misconfigured.

To fix this, go to **Settings > Devices & services > Nest**, open the entry menu, and select **Reconfigure** to select or create a Pub/Sub topic and subscription.

**Befintlig svenska:** Det gick inte att ansluta Nest-integreringsposten **{entry_title}** till dess Pub/Sub-prenumeration. Prenumerationen eller dess ämne kan ha tagits bort eller vara felkonfigurerat.

Åtgärda detta genom att gå till **Inställningar > Enheter och tjänster > Nest**, öppna postens meny och välj **Konfigurera om** för att välja eller skapa ett Pub/Sub-ämne och en prenumeration.

**Sparad svenska:** Det gick inte att ansluta Nest-integrationsposten **{entry_title}** till dess Pub/Sub-prenumeration. Prenumerationen eller dess ämne kan ha tagits bort eller vara felkonfigurerat.

Åtgärda detta genom att gå till **Inställningar > Enheter och tjänster > Nest**, öppna postens meny och välja **Konfigurera om** för att välja eller skapa ett Pub/Sub-ämne och en prenumeration.

**Motivering:** Förbättrar svensk terminologi eller formulering utan betydelseförändring.

## `component::nest::issues::legacy_pubsub_topic::description`

**Engelska:** Your Nest integration (**"{entry_title}"**) needs to be reconfigured before **November 30, 2026** to continue receiving realtime updates, camera events, and doorbell presses. It currently uses a legacy Google-hosted Cloud Pub/Sub topic that Google is retiring in favor of a Pub/Sub topic in your own Google Cloud project.

To update it, go to **Settings > Devices & services > Nest**, open the menu next to **"{entry_title}"**, and select **Reconfigure**. Home Assistant will create the new Pub/Sub topic in your Google Cloud project and guide you through updating the Nest Device Access Console.

**Befintlig svenska:** Nest-integreringsposten **{entry_title}** tar emot enhetshändelser från ett Pub/Sub-ämne som Google tillhandahåller. Google slutar publicera händelser i sådana ämnen den 30 november 2026. Efter detta datum tar Home Assistant inte längre emot realtidsuppdateringar, kamerahändelser eller dörrklocketryckningar för posten.

Åtgärda detta genom att gå till **Inställningar > Enheter och tjänster > Nest**, öppna postens meny och välj **Konfigurera om**. Home Assistant skapar ett Pub/Sub-ämne i Google Cloud-projektet och vägleder dig genom uppdateringen av Device Access Console.

**Sparad svenska:** Din Nest-integration (**”{entry_title}”**) behöver konfigureras om före den 30 november 2026 för att fortsätta ta emot realtidsuppdateringar, kamerahändelser och dörrklockstryckningar. Den använder för närvarande ett äldre Cloud Pub/Sub-ämne som Google tillhandahåller och avvecklar till förmån för ett Pub/Sub-ämne i ditt eget Google Cloud-projekt.

Uppdatera integrationen genom att gå till **Inställningar > Enheter och tjänster > Nest**, öppna menyn bredvid **”{entry_title}”** och välja **Konfigurera om**. Home Assistant skapar det nya Pub/Sub-ämnet i ditt Google Cloud-projekt och vägleder dig genom uppdateringen av Nest Device Access Console.

**Motivering:** Förbättrar svensk terminologi eller formulering utan betydelseförändring.