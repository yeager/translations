# Home Assistant Core – Watergate

Datum: 2026-11-21

Alla 45 Watergate-strängar har granskats mot aktuell källa och tidigare backup. Två fel är rättade, sparade och API-återlästa.

| Nyckel | Sparad svenska | Motivering |
| --- | --- | --- |
| `entity::event::auto_shut_off_duration::name` | `Automatisk avstängning efter varaktighet` | Naturlig svensk ordföljd och tydlig händelseorsak. |
| `entity::event::auto_shut_off_volume::name` | `Automatisk avstängning efter volym` | Naturlig svensk ordföljd och tydlig händelseorsak. |

Övriga enhets-, mätar- och nätverkssträngar är korrekta. Den tidigare sparade termen `Automatisk avstängning` är bevarad.
