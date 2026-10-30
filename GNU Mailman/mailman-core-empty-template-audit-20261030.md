# GNU Mailman Core – granskning av tomma mallposter 2026-10-30

Weblates filter `state:empty` visar tre svenska poster i komponenten
**Mailman Core**. De är avsiktligt tomma rubrikmallar och ska inte översättas
eller fyllas med filnamn:

- `list:member:digest:header.txt`
- `list:member:regular:header.txt`
- `list:user:notice:goodbye.txt`

Samtliga har tom engelsk källtext och tom svensk måltext. Weblate visar för
varje post den avfärdade kontrollen *Har blivit översatt* och en tidigare,
felaktig översättning av själva sökvägen. Posterna är innehållsreferenser till
textmallar, inte översättningsbart gränssnittsinnehåll. Den korrekta åtgärden
är därför att behålla dem tomma.

Ingen ändring sparades i Weblate vid denna granskning.
