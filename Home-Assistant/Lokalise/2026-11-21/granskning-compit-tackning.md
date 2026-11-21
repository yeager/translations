# Home Assistant Core – Compit, täckningskontroll

Datum: 2026-11-21

Delgranskningarna täcker nu exakt samtliga 197 aktuella Compit-strängar i Lokalise: 13 konfigurationssträngar, 67 val- och driftlägen, 12 temperaturinställningar, 12 binära sensor-/fläkt-/brytarsträngar och 93 sensorssträngar. Den tidigare automatiska grupperingens enda utelämnade rad, `component::compit::entity::sensor::alarm_code::state::low_battery_level`, återlästes separat som `Låg batterinivå` och är korrekt. Inga återstående Compit-nycklar saknas i granskningen.
