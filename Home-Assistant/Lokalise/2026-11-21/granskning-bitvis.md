# Home Assistant Core – Bitvis

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/bitvis/strings.json`, tidigare radrapport och Lokalise API med direkt återläsning.

Status: samtliga 31 aktuella bladsträngar och referensmål är radgranskade och återlästa. Ingen ny ändring behövs.

Den tidigare sparade korrigeringen `HAN-buffertöverflöden` för `entity::sensor::han_msg_buffer_overflow::name` är fortfarande korrekt. Konfigurationsflödet använder konsekvent `Konfigurera`, `Värdnamn`, `MAC-adress` och `Tidsgränsen överskreds`. De elektriska mätarnamnen har granskats som en grupp: aktiv/reaktiv energi och effekt, import/export, fasström och fasspänning. Platshållarna `{name}`, `{host}` och `{phase}` är bevarade i samtliga relevanta strängar.

Den detaljerade föregående radgranskningen finns i `2026-11-19-granskning/granskning-9901-10140.md`; dess föreslagna sammanskrivning av `HAN-buffertöverflöden` är redan sparad i Lokalise och finns dokumenterad i `2026-11-19/sparade-andringar-rejseplanen-teslemetry-metoffice.md`.
