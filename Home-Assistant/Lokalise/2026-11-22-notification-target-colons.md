# Målplatshållare i notifieringar

Två notifieringsfel verifierades och rättades via Lokalise API den 22 november
2026. Båda ändringarna har lästs tillbaka efter sparning.

| Nyckel | Före | Efter | Motivering |
| --- | --- | --- | --- |
| `component::message_bird::exceptions::send_message_failed::message` | `Det gick inte att skicka MessageBird-meddelandet till: {targets}.` | `Det gick inte att skicka MessageBird-meddelandet till {targets}.` | Kolon efter prepositionen *till* är fel i svensk löpande text. |
| `component::twilio_call::exceptions::call_failed::message` | `Det gick inte att ringa: {targets}.` | `Det gick inte att ringa {targets}.` | Kolon efter verbet *ringa* är fel i denna sats. |

Platshållaren `{targets}` är oförändrad i båda strängarna.
