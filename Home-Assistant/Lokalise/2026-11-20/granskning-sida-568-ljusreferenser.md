# Home Assistant Core – Lokalisegranskning, sida 568

Granskad: 2026-11-20  
Källa: Lokalise API, Home Assistant Core, svenska (`sv`)  
Status: sparat och återläst i Lokalise

17 svenska fält hade gamla `component::light::services::turn_on`-referenser trots att källtexten använder centrala `component::light::common`-nycklar. Följande grupper har synkroniserats och återlästs från keys-endpointen:

- `light.services.toggle`: effect, flash, hs_color, kelvin, profile, rgb_color, transition, white och xy_color (berörda namn och beskrivningar)
- `light.services.turn_off.fields.flash.description`

`toggle.fields.kelvin.name` var redan korrekt. I övrigt kontrollerades färgnamnen samt tjänstnamn och -beskrivningar utan ändring. Referenser förs inte in i TMX eftersom de inte utgör fristående käll-/målsegment.
