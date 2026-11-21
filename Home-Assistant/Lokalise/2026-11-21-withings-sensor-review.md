# Home Assistant Core – Withings: sensorer

Datum: 2026-11-21

Tre sensoretiketter har rättats, sparats och API-återlästs: intensitet för andningsstörningar, träningspassets varaktighet och paus under träningspasset. De fem segmentmätningarna för fett använder nu korrekt `Fettmassa` i stället för `Fettansamling`, och kroppsfettets andel använder `Fettprocent`. Antalet snarkningsepisoder använder nu en medicinskt tydlig term. De tre elektrodermala aktivitetsmätningarna använder nu korrekt preposition för fötterna. `Soft activity` använder den naturliga svenska graden `Lätt aktivitet`. Träningsformerna `Dog walking`, `Lift weights`, `Baby wearing`, `Toddler wearing` och `Pushing a stroller` använder nu konsekventa svenska aktivitetsnamn. OAuth-upptäckten har också fått tillbaka källans viktiga varning om den mer omfattande konfigurationen. Instruktionen för applikationsuppgifter använder nu korrekt `klient-ID` och bevarar exakta knapptexter, länk och `{redirect_url}`. Den fullständiga Withings-komponenten omfattar 264 strängar; träningsformernas långlista granskas och dokumenteras separat för att undvika dubbelarbete med tidigare batcher.
# Tillägg: träningsetiketter

Följande tre etiketter sparades i Lokalise den 2026-11-21 efter API-återläsning:

- `component::withings::entity::sensor::workout_active_calories_burnt::name`: `Förbrända kalorier senaste träningspasset` → `Förbrända kalorier under senaste träningspasset`.
- `component::withings::entity::sensor::workout_distance::name`: `Tillryggalagd sträcka senaste träningspasset` → `Tillryggalagd sträcka under senaste träningspasset`.
- `component::withings::entity::sensor::workout_type::name`: `Typ på senaste träningspasset` → `Typ av senaste träningspasset`.

Manifestet `Home-Assistant/2026-11-21-withings-workout-labels-verified.json` och den kanoniska TMX-filen är uppdaterade i `yeager/swedish-tm` (commit `982b570`); TMX validerades till 2 443 poster.

