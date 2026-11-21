# Home Assistant Core – WiiM

Datum: 2026-11-21

Alla 28 WiiM-strängar har granskats mot aktuell källa och tidigare backup. Två fel är rättade, sparade och API-återlästa.

| Nyckel | Sparad svenska | Motivering |
| --- | --- | --- |
| `exceptions::direct_url_playback_unsupported::message` | `Direktuppspelning från URL stöds inte på den här enheten.` | Återställer en tydlig svensk återgivning av direkt uppspelning från URL. |
| `exceptions::invalid_track_id::message` | `Ogiltigt medie-ID: {media_id}. Ett giltigt spårindex förväntas.` | Rättar den avbrutna satsen och bevarar platshållaren. |

Övriga konfigurations- och API-felsträngar är korrekta.
