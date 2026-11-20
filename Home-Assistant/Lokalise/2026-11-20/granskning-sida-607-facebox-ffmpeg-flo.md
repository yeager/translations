# Home Assistant Core – Lokalise-granskning, sida 607

Datum: 2026-11-20  
Omfattning: Lokalise API, 20 Core-strängar (`facebox`, `ffmpeg`, `flo`).

## Sparade ändringar

| Nyckel | Sparad svensk text | Motivering |
|---|---|---|
| `component::ffmpeg::services::restart::fields::entity_id::description` | `Namnet på entiteten som ska startas om. Beror på plattform.` | Gör den fristående engelska satsen till naturlig svenska. |
| `component::ffmpeg::services::start::fields::entity_id::description` | `Namnet på entiteten som ska startas. Beror på plattform.` | Samma korrigering. |
| `component::ffmpeg::services::stop::fields::entity_id::description` | `Namnet på entiteten som ska stoppas. Beror på plattform.` | Samma korrigering. |

## Verifiering

Alla tre ändringar skickades med Lokalise API och återlästes. Referenserna på sidan är giltiga; övriga 14 strängar behöver ingen ändring.

Status: sparat och återläst i Lokalise.
