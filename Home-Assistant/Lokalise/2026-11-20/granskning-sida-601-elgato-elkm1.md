# Home Assistant Core – Lokalise-granskning, sida 601

Datum: 2026-11-20  
Omfattning: Lokalise API, 20 Core-strängar (`ecobee`, `elgato`, `elkm1`).

## Sparade ändringar

| Nyckel | Befintlig svensk text | Sparad svensk text | Motivering |
|---|---|---|---|
| `component::elgato::services::identify::description` | `Identifierar en Elgato-lampa. Blinkar ljuset, vilket kan vara användbart för visuell identifiering.` | `Identifierar en Elgato-lampa. Blinkar ljuset, vilket kan vara användbart som visuell avisering.` | Återger att blinkningen är en notifiering, inte en identifiering. |
| `component::elkm1::services::alarm_arm_home_instant::name` | `Larm aktivera hem omedelbart` | `Aktivera larmet i hemmaläge direkt` | Rätt svensk ordföljd och tydligt lägesnamn. |
| `component::elkm1::services::alarm_arm_night_instant::name` | `Larma till läge direkt natt` | `Aktivera larmet i nattläge direkt` | Rätt svensk ordföljd och tydligt lägesnamn. |

## Verifiering

Varje ändring skickades med Lokalise API och återlästes. Lokalise-referenserna på sidan är giltiga; övriga 17 strängar behöver ingen ändring.

Status: sparat och återläst i Lokalise.
