# Lokal PDF-byggning

Den 29 oktober 2026 byggdes en svensk läsutgåva från den aktuella
DocBook-katalogen och den granskade svenska PO-filen.

Resultat:

- `Ada_Zangemann-reading.sv.dbk.pdf` är en 10-sidig PDF.
- DocBook-sammanslagning med `itstool`, XSLT-profilering och ODT-export med
  `pandoc` passerade.
- PDF-exporten gjordes lokalt med LibreOffice.
- Första, femte och sista sidan renderades till PNG och kontrollerades
  visuellt. Rubriker, svensk text och sidnumrering är läsbara utan klippning.

Detta är projektets läsutgåva, inte den illustrerade tryckutgåvan. Den senare
kräver Scribus-mallarna och de språkberoende illustrationerna.
