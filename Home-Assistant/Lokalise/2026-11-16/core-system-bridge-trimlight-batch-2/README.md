# Home Assistant Core – System Bridge och Trimlight, batch 2

Datum: 2026-11-16  
Kanal: Lokalise API v2  
Språk: svenska (`sv`)

Åtta aktuella Core-strängar: en transporttyp, två System Bridge-meddelanden
och fem Trimlight-konfigurationsfel. Produktnamnet System Bridge är bevarat,
medan övrig användartext har skrivits på idiomatisk svenska.

## Kontroller före API-inskick

- JSON-syntax
- l10n-lint mot den rena batchfilen `sv.json`
- svlang för löpande svensk text
- Hunspell-sv
- kontroll av klammerplatshållare
- `msgfmt` är inte tillämpligt: detta är en Lokalise-JSON-batch och ingen
  PO-katalog.

## Upstream-status

Sparad via Lokalise API den 2026-11-16: 8 av 8 strängar accepterades. En
separat API-återläsning bekräftade exakt svensk måltext och att samtliga poster
inte längre är overifierade. Detta bekräftar sparat innehåll, inte
upstream-granskning, merge eller utgivning.
