# Recorder: rensning av entiteter

Kontrollerat och sparat i Lokalise 2026-11-19. Efter sparning lästes båda översättningarna åter i projektet. Källtext och nycklar nedan kommer från Lokalise.

## `component::recorder::services::purge_entities::description`

**Engelska:** Starts a purge task to remove the data related to specific entities from your database.

**Tidigare svenska:** Startar en rensningsuppgift för att rensa bort gammal data som är relaterade till specifika entiteter från databasen.

**Sparad svenska:** Startar en rensningsuppgift för att ta bort data som hör till specifika entiteter från databasen.

Källan begränsar inte uttryckligen uppgiften till gammal data.

## `component::recorder::services::purge_entities::fields::keep_days::description`

**Engelska:** Number of days to keep the data for rows matching the filter. Starting today, counting backward. A value of `7` means that everything older than a week will be purged. The default of 0 days will remove all matching rows immediately.

**Tidigare svenska:** Antal dagar som data sparas för rader som matchar filtret. Börjar i dag och räknas bakåt. Ett värde på '7' innebär att all data som är äldre än en vecka kommer att rensas bort. Standardvärdet 0 dagar innebär att all data tas bort omedelbart.

**Sparad svenska:** Antal dagar som data sparas för rader som matchar filtret, räknat bakåt från i dag. Värdet `7` innebär att allt som är äldre än en vecka rensas bort. Standardvärdet 0 dagar innebär att alla matchande rader tas bort omedelbart.

Ändringen förtydligar att standardvärdet gäller de matchande raderna och återställer källans kodmarkering kring talet.
