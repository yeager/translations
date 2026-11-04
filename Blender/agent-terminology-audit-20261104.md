# Terminologirevision: Blender Manual, batch 11–16

Datum: 2026-11-04  
Underlag: `TERMINOLOGY.md`, manualdelta batch 11–16 och den aktuella
arkiverade Blender-UI-katalogen.

## Godkända sammanhangsberoende beslut

| Engelskt begrepp | Rekommenderad svensk form | Evidens och avgränsning |
| --- | --- | --- |
| `data-block` | datablock | Finns redan i terminologilistan och återkommer konsekvent i batch 12–13. |
| `default prim` | standardprim | Batch 12: detta är USD:s namngivna standardprim, inte hierarkins rot. |
| `root prim` | rotprim | Batch 13: avser roten i USD-hierarkin. Ska inte normaliseras till *standardprim*. |
| `Point Cloud` | punktmoln | Blender-UI-katalogen använder *Punktmoln*; batch 14 följer den formen. |
| `UsdGeom*`, `Scope`, `allPurpose`, `preview` | exakt källform | Är identifierare eller specifika USD-värden. Förklara dem i svensk löptext, men översätt inte själva identifieraren. |
| `F-stop` | bländartal | Batch 15 följer Blender-UI:ts fackterm. |
| `aperture` i kamerakontext | bländaröppning | Batch 15 gör betydelsen tydlig; använd inte den kortare äldre formen *bländare* när måttet avses. |
| `Depth of field distance` | skärpedjupsavstånd | Batch 15 är den mer precisa formen för kameraegenskapen. |
| `projection type` | projektionstyp | Batch 16 anger korrekt alternativen *perspektivisk eller ortografisk*. |

## Inkonsekvenser och åtgärdsförslag

1. **Batch 11 och batch 15 överlappar för tre kameraegenskaper.** Batch 11
   har äldre formuleringar för `Depth of field distance`, `F-stop` och
   `Sensor size`; batch 15 är den senare och mer precisa granskningen.
   När en samlad uppladdningsfil skapas ska batch 15 vinna för samtliga tre
   `msgid` så att katalogen inte får dubbletter med motstridiga måltexter.

2. **Batch 15 och batch 16 överlappar för `Projection type`.** Batch 16 är
   en uttrycklig följdrättelse efter dubbelgranskning. Den slutliga formen är
   `Projektionstyp (perspektivisk eller ortografisk)`; batch 15:s tidigare
   måltext får inte tas med i en sammanslagen export.

3. **USD-ord behöver ett eget avsnitt i `TERMINOLOGY.md`.** De återkommer nu
   i fler än en batch men saknar fasta, dokumenterade beslut där. Lägg till
   åtminstone *prim*, *rotprim*, *standardprim*, *punktmoln*,
   *strängegenskap*, *tillgänglighetsetikett*, *USD-scen* och
   *uppåtriktning*, med anmärkningen att identitetsvärden och RST-roller
   lämnas oförändrade.

4. **`stage` är ännu inte dokumenterat som term.** Batch 12 använder
   *USD-scen* för källans *stage*, vilket är begripligt i exporterad
   scendokumentationskontext. Beslutet bör dokumenteras som kontextbundet
   i stället för att göra *scen* till en ovillkorlig ersättning för *stage*.

## Kontroll av Blender-UI-stöd

Den arkiverade UI-katalogen styrker bland annat följande:

- `Point Cloud` → `Punktmoln`.
- `data-block` → `datablock` och sammansättningar som `datablocktyp`.
- `action slot` → `åtgärdsslot` i synlig UI-text.
- Blender använder både *biblioteksåsidosättning* och
  *biblioteksöverskrivning* i närliggande sammanhang; de får därför inte
  normaliseras mekaniskt i nästa genomgång av länkade bibliotek.

## Slutsats

Ingen av batch 11–16 behöver dras tillbaka. Däremot måste de två uttryckliga
överlappningarna dedupliceras när uppladdningshäftet byggs, med batch 15 och
16 som auktoritativa efterföljare. Terminologilistan bör utökas innan fler
USD-avsnitt granskas, så att kommande deltabatcher använder samma beslut.
