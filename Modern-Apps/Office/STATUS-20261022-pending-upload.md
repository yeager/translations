# Modern Apps Office – väntande rättning

Kontrollerat rad för rad i Hosted Weblate 2026-10-22.

- Nio aktuella kontrollposter granskades.
- Åtta är riktiga oförändrade filformatnamn: Word, Excel, PowerPoint, EPUB, Rich Text, Flat ODF, Text och LaTeX.
- `default_font_size_pt` har en verklig XML-formatavvikelse. Källan placerar `pt` direkt efter den avslutande XML-taggen. Den svenska måltexten hade ett mellanslag före `pt`.
- `office-sv-pending-maintenance-20261022.xml` tar bort mellanslaget och innehåller inga andra ändringar.

Kontroller: XML-tolkning, `svlang skrivregler`, Hunspell-granskning och Gitleaks. Hunspellträffarna är filändelser, produktnamn och etablerade tekniska termer.

Hosted Weblate är i underhållsläge och har låst sparning och import. Exporten ska jämföras med en färsk serverexport och skickas in först när spärren har släppts.
