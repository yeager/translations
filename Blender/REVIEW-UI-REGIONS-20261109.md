# Blender UI — granskning av redigerare och gränssnittsregioner

Datum: 2026-11-09  
Katalog: `blender-ui-ui-sv (6).po`  
SHA-256: `7cbf644d990d1d648e91fa42b6ed214545661fc4e2db2dba461f49dbfd3a408f`

## Omfattning

43 ändrade poster med *editor*, *header*, *sidebar*, *panel*, *region* eller
*top bar* i källtexten har granskats mot respektive `bpy.types`-sammanhang.
De täcker bland annat nodredigeraren, textredigeraren, sidofält, rubriker,
resurshyllan, visningsområden och tangentmappningsregioner.

## Slutsats

Ingen ny deltafil behövs. Följande termer används med korrekt kontext:

- *editor* → **redigerare** när texten avser en Blender-redigerare.
- *Sidebar* → **sidofält**.
- *Header* → **rubrik** i generella region- och menysammanhang.
- *Asset Shelf Header* → **resurshyllans huvudrad**, eftersom det namnger den
  specifika horisontella UI-regionen på resurshyllan.
- *Viewer Region* → **visningsområde**.
- *region space* → **regionrymd**, som API-nära koordinatbegrepp.

Två tidigare lokala korrigeringar berör samma område: den dubblerade formen
*sekvensredigerarredigeraren* och den mindre läsbara formen
*sekvensredigerarremsor*. De ligger redan i den samlade lokala deltafilen och
ska inte dupliceras här.

Detta dokument visar lokal granskning, inte en verifierad Weblate-import.
