# Home Assistant frontend – energipanel, batch 3

Datum: 2026-11-16  
Kanal: Lokalise API v2  
Språk: svenska (`sv`)

Åtta granskade strängar för batteriladdning från elnät och solenergi. Batchen
bygger vidare på energipanelens två första batcher och använder `elnätet`,
`energisensor` och `effektsensor` konsekvent. Det synliga UI-avsnittet
`Electricity grid` har fått den svenska menynamnsformen `Elnät`.

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
