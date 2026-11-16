# Home Assistant Core – Trimlight, batch 1

Datum: 2026-11-16  
Kanal: Lokalise API v2  
Språk: svenska (`sv`)

Nio granskade svenska strängar för Trimlight-integrationen: konfiguration,
automatisk upptäckt och felmeddelanden. Äldre föräldralösa översättningsposter
utan motsvarande Lokalise-nyckel har identifierats och lämnats oförändrade;
den här batchen avser endast aktuella nycklar.

## Kontroller före API-inskick

- JSON-syntax
- l10n-lint mot den rena batchfilen `sv.json`
- svlang för löpande svensk text
- Hunspell-sv
- kontroll av klammerplatshållare
- `msgfmt` är inte tillämpligt: detta är en Lokalise-JSON-batch och ingen
  PO-katalog.

## Upstream-status

Sparad via Lokalise API den 2026-11-16: 9 av 9 strängar accepterades. En
separat API-återläsning bekräftade exakt svensk måltext och att samtliga poster
inte längre är overifierade. Detta bekräftar sparat innehåll, inte
upstream-granskning, merge eller utgivning.
