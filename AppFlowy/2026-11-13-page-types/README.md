# AppFlowy, nya sidtyper, 13 november 2026

Den första avgränsade batchen för den aktuella AppFlowy-resursen fyller 178
grundläggande, synliga UI-texter i `sv-SE.json`:

- nytt dokument
- nytt rutnät
- ny kalender
- ny tavla
- tomt sidinnehåll
- färgväljarens 11 namn och alternativ
- relativa datum: i går, i dag, i morgon och en vecka
- datumväljaren: format, slutdatum och 13 påminnelsealternativ
- påminnelseaviseringens rubrik, meddelande och statusåtgärder
- favoritsidornas tomläge, instruktion och sidofältsåtgärder
- återkoppling vid öppning av filer och delning av loggfiler
- snabbanteckningar: etiketter, visningsläge, tomvy och borttagning
- kortdetaljer och redigerarens platshållare för listor, citat och rubriker
- titelradens fält och ikoner
- precisering till ”Sidans ikon” enligt befintlig svensk termbank
- redigerarens snabbinfogningsmeny för hänvisningar, datum och påminnelser
- åtkomstbegäran till en sida, inklusive inloggningslänkar och statusmeddelanden
- godkännande av begäran, medlemsantal och abonnemangsgräns för arbetsytan
- inbjudan till arbetsyta, medlemsantal och felåtgärder för konto
- ikonuppladdaren och dialogen Sök och ersätt
- meddelandecentralen: status, arkivering, läst-markering och filter

Den engelska resursen har 94 toppnivåsektioner medan den svenska har 44.
Resterande sektioner, bland annat kontoinställningar, AI-chatt och
redigeraren, behöver därför behandlas komponentvis med sammanhang och kan inte
rimligen betraktas som färdiggranskade genom den här batchen.

Kontroller:

- JSON-parsning och samtliga 178 nycklarna verifierade mot `en-US.json`
- l10n-lint: godkänd
- Hunspell-sv: inga träffar i de nya formuleringarna
- svlang: tidigare resurs har befintliga V2-varningar; inga nya varningar från
  batchen
- diffkontroll och Gitleaks för deltat: godkända
- msgfmt: inte tillämpligt på JSON

Upstream: [AppFlowy PR #9132](https://github.com/AppFlowy-IO/AppFlowy/pull/9132),
öppen den 13 november 2026. Den är inskickad men inte granskad eller mergad.

Upstreamkontroller: Ninja-i18n och Sourcery har godkänt den senaste revisionen.
En tidigare Ninja-i18n-körning stoppades före lintning eftersom dess
`pull_request_target`-konfiguration tillfälligt inte fick checka ut fork-kod.
Det var en workflowbegränsning, inte en rapporterad översättningsbrist.
Ninja-i18n:s tidigare varning för `colors.orange` är en medveten svensk
identisk översättning och är förklarad i PR:n. CLA-boten bekräftar att samtliga
commitförfattare har signerat. PR:n väntar på projektets granskning och merge.
