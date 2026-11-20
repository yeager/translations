# Home Assistant Core – Lokalise-granskning, sida 604

Datum: 2026-11-20  
Omfattning: Lokalise API, 20 Core-strängar (`elkm1`, `environment_canada`, `envisalink`).

## Sparade ändringar

| Nyckel | Befintlig svensk text | Sparad svensk text | Motivering |
|---|---|---|---|
| `component::elkm1::services::speak_word::name` | `Tala ord` | `Läs upp ord` | Naturlig åtgärdsform. |
| `component::envisalink::services::alarm_keypress::fields::entity_id::description` | `Namn på larmpanelen som ska utlösas.` | `Namn på larmpanelen som ska styras.` | Panelen styrs med knapptryckningar; den utlöses inte nödvändigtvis. |
| `component::envisalink::services::alarm_keypress::name` | `Larm knapptryckning` | `Larmknapptryckning` | Rätt sammansättning. |
| `component::envisalink::services::invoke_custom_function::description` | `Tillåter användare med DSC-paneler att trigga en PGM-utgång (1-4). Observera att du måste ange larmpanelens "kod"-parameter för att detta ska fungera.` | `Gör det möjligt för användare med DSC-paneler att aktivera en PGM-utgång (1–4). Observera att larmpanelens parameter "code" måste anges för att detta ska fungera.` | Naturligare term och parameteridentifieraren måste behållas. |
| `component::envisalink::services::invoke_custom_function::fields::partition::description` | `Larmpanelens partition för att utlösa PGM-utgången på. Vanligtvis är detta bara "1".` | `Partition på larmpanelen där PGM-utgången ska aktiveras. Vanligen är det "1".` | Rätt svensk satsstruktur. |
| `component::envisalink::services::invoke_custom_function::fields::pgm::description` | `PGM-numret som ska utlösas på larmpanelen.` | `PGM-numret som ska aktiveras på larmpanelen.` | Rätt term för en PGM-utgång. |

## Verifiering

Alla sex ändringar skickades via Lokalise API och återlästes. Referenserna för `prefix` är giltiga; övriga 12 strängar behöver ingen ändring.

Status: sparat och återläst i Lokalise.
