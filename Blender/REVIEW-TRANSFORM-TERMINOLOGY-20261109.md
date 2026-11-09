# Blender UI — granskning av transformterminologi

Datum: 2026-11-09  
Katalog: `blender-ui-ui-sv (6).po`  
SHA-256: `7cbf644d990d1d648e91fa42b6ed214545661fc4e2db2dba461f49dbfd3a408f`

## Omfattning

62 ändrade poster med *transform* i källtexten har kontrollerats i Blender-
API-kontext. Området omfattar objekt- och posetransformationer,
transformationsorienteringar, geometriattribut, visningstransformering,
UV-operatorer och importer/exporter.

## Slutsats

Ingen ny deltafil behövs. Den aktuella fördelningen är riktig:

- **transformera** för verbet och **transformation** för objektets eller
  benets läge, rotation och skala.
- **transformationsorientering** för Blenders särskilda orienteringsval.
- **visningstransformering** och **rymdtransformering** för färghantering
  respektive import/export, där den tekniska processen är central.
- **deltatransformation** som UI-etikett, medan den längre egenskapstexten
  använder **deltatransformeringsvärden** enligt den redan lokala deltafilen.

Detta är en lokal granskningspost och ingen importbekräftelse.
