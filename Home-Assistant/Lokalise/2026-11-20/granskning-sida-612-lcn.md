# Home Assistant Core – Lokalise-granskning, sida 612

Datum: 2026-11-20  
Omfattning: Lokalise API, 20 Core-strängar (`lcn`).

## Sparade ändringar

| Nyckel | Befintlig svensk text | Sparad svensk text | Motivering |
|---|---|---|---|
| `component::lcn::services::lock_keys::fields::state::description` | `Status för nyckellås som sträng (1=på, 2=av, T=växla, -=ingen förändring).` | `Knapplåsstatus som sträng (1=på, 2=av, T=växla, -=ingen ändring).` | Enhetlig term och naturligare formulering. |
| `component::lcn::services::lock_keys::fields::table::description` | `Tabell med nycklar att låsa (måste vara A för intervall).` | `Tabell med knappar som ska låsas (måste vara A för intervall).` | Enhetlig term och korrekt satsstruktur. |
| `component::lcn::services::lock_keys::name` | `Lås nycklar` | `Lås knappar` | Enhetlig term med fältbeskrivningarna. |

## Verifiering

Alla tre ändringar skickades med Lokalise API och återlästes. Referenserna på sidan är giltiga; övriga strängar behöver ingen ändring.

Status: sparat och återläst i Lokalise.
