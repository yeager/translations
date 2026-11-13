# AppFlowy, nya sidtyper, 13 november 2026

Den första avgränsade batchen för den aktuella AppFlowy-resursen fyller 42
grundläggande, synliga UI-texter i `sv-SE.json`:

- nytt dokument
- nytt rutnät
- ny kalender
- ny tavla
- tomt sidinnehåll
- färgväljarens 11 namn och alternativ
- relativa datum: i går, i dag, i morgon och en vecka
- datumväljaren: format, slutdatum och 13 påminnelsealternativ

Den engelska resursen har 94 toppnivåsektioner medan den svenska har 44.
Resterande sektioner, bland annat kontoinställningar, AI-chatt, meddelanden och
redigeraren, behöver därför behandlas komponentvis med sammanhang och kan inte
rimligen betraktas som färdiggranskade genom den här batchen.

Kontroller:

- JSON-parsning och samtliga 42 nycklarna verifierade mot `en-US.json`
- l10n-lint: godkänd
- Hunspell-sv: inga träffar i de nya formuleringarna
- svlang: tidigare resurs har befintliga V2-varningar; inga nya varningar från
  batchen
- diffkontroll och Gitleaks för deltat: godkända
- msgfmt: inte tillämpligt på JSON

Upstream: [AppFlowy PR #9132](https://github.com/AppFlowy-IO/AppFlowy/pull/9132),
öppen den 13 november 2026. Den är inskickad men inte granskad eller mergad.
