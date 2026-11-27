# GNOME Usage — main/po

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/gnome-usage/main/po/sv/>
- Hela katalogen radgranskades 2026-11-24. En riktad uppföljning 2026-11-27 rättade den då noterade grammatikbristen.
- Damned Lies-POT hämtad 2026-11-27: 70 poster; SHA-256 `3ecbe0992216bef4cc23680050d418110303f0a3910bd9076d897062ac60e4f5`.
- Aktuell PO/API-statistik: 70 översatta, 0 fuzzy, 0 oöversatta. POT-matchning verifierad med `msgcmp`.
- Den aktuella PO-filen har fyra andra översättningar som skiljer sig från vår arkiverade granskning. De jämfördes igen och våra formuleringar behölls: *use of system resources* (med och utan punkt), *processing power* (”processorkraft”, inte ”ström”) och tröskelvärdet *load* (”belastning”).
- Ändringar mot PO-filen hämtad 2026-11-27: 4 befintliga översättningar behållna efter kvalitetsjämförelse och 1 grammatisk rättning; 5 ändrade PO-poster totalt.
- Rättad rad: `The time span for up to which ...` → `Tidsintervallet (ms) som processor- och minnesdiagrammen på prestandafliken och i sidopanelen visar bakåt i tiden.`

## Validering

- `msgcmp --use-fuzzy` mot senaste POT: godkänd.
- `msgfmt --check --check-format`: godkänd.
- `l10n-lint --language sv`: 0 fel och 0 varningar; fyra informationsnotiser om tekniskt format, längd och konsekvens.
- Verktyget `hunspell-sv` saknas; systemets Hunspell `sv_SE` kontrollerade den nya formuleringen. `processor-` flaggas när det delas vid bindestreck; sammansättningen `processor- och minnesdiagrammen` är avsiktlig och idiomatisk.
- Pluralformer, formatering och tekniska värden oförändrade.

## Inskickning

Inskickning är blockerad av Damned Lies: aktuell aktivitetssida visar `No current actions` och säger att inloggning samt medlemskap i svenska teamet krävs. Den tillgängliga API-statistiken är läsbar men inga uppladdningsåtgärder exponeras. Ingen uppladdning har gjorts. Senaste POT, aktuell PO, API-statistik och aktivitetssida sparas som kontrollunderlag.
