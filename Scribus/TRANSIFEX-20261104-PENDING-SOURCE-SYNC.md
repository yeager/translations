# Scribus – väntar på källsynk i Transifex

## Observerat 2026-11-04

Den svenska katalogen laddades ner från Scribus officiella Transifex-resurs,
granskades lokalt och laddades upp igen. Transifex accepterade och uppdaterade
32 aktiva översättningar. En ny asynkron export från samma resurs bekräftar
de uppdateringarna.

22 översättningsenheter i den nedladdade TS-filen saknar däremot en aktiv
motsvarighet i den aktuella Transifex-resursen. De gick inte att uppdatera
och är därför inte markerade som inskickade. Det är en källsynkfråga, inte en
språk- eller uppladdningsvarning.

## Sparad kandidat

`scribus.sv-20261104-transifex-pending-source-sync.ts` innehåller de
terminologiskt granskade kandidaterna. Den ska laddas upp igen först efter att
Scribus har synkroniserat källsträngarna till Transifex.

Berörda områden är Freetype-teckensnittsdiagnostik, streckkodenhetens
färg-/typinställningar, linjalens punktmarkering och cell-/tabellstilar.
Kontrollerade termval omfattar bland annat `teckensnitt`, `glyf`, `teckenkod`,
`färg`, `typ`, `nyans`, `punkt` och `allvarligt fel`.

## Nästa steg

1. Ladda ner en ny svensk export när Scribus-resursen har synkroniserats.
2. Jämför de 22 källsträngarna med kandidatfilen.
3. Kör XML-, platshållar-, term- och språkkontroller igen innan ny uppladdning.
