# Sparad referensändring i Lokalise – Generic Camera

Datum: 2026-11-20

En svensk options-sträng har sparats via Lokalise API och lästs tillbaka ordagrant från API:t.

- Återställde referensen till `component::generic::config::error::unable_still_load`, så att options-vyn använder den redan verifierade källöversättningen i stället för en föråldrad lokal dubblett.

Ändrad nyckel: `161967443`.

Ingen ny TMX-post skapades: strängen innehåller ingen egen översättning och TMX hålls fri från referensmarkörer.
