# Home Assistant frontend – energipanel, batch 2

Datum: 2026-11-16  
Kanal: Lokalise API v2  
Språk: svenska (`sv`)

Åtta granskade följdsträngar från dialogen som konfigurerar batteriets
energiflöden. Översättningarna är kontrollerade tillsammans med batch 1 så att
benämningarna för elnät, solenergi, laddning och urladdning är konsekventa.

## Kontroller före API-inskick

- JSON-syntax
- l10n-lint mot den rena batchfilen `sv.json`
- svlang för löpande svensk text
- Hunspell-sv
- `msgfmt` är inte tillämpligt: detta är en Lokalise-JSON-batch och ingen
  PO-katalog.

## Upstream-status

Sparad via Lokalise API den 2026-11-16: 8 av 8 strängar accepterades. En
separat API-återläsning bekräftade exakt svensk måltext och att samtliga poster
inte längre är overifierade. Detta bekräftar sparat innehåll, inte
upstream-granskning, merge eller utgivning.
