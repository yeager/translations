# Home Assistant frontend – energipanel, batch 5

Datum: 2026-11-16  
Kanal: Lokalise API v2  
Språk: svenska (`sv`)

De sista åtta strängarna i den här batteridialogen: urladdning till hemmet och
elnätet. Formuleringarna fortsätter den etablerade riktningen från batch 1–4.
`Elnät` är bevarat som synligt UI-namn i vägledningen.

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
