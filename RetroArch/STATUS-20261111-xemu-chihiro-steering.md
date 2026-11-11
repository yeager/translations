# RetroArch Xemu: Chihiro-styrning

Datum: 11 november 2026

Crowdins svenska Xemu-komponent hade nio oöversatta Chihiro-strängar om
styrrespons, styreffekt och styrningens innerzon. De har granskats i sitt
sammanhang: inställningarna beskriver vänsterspakens responskurva i bland
annat OutRun 2 och Crazy Taxi 3.

Batchen `retroach-sv-xemu-chihiro-steering-batch-20261111.json` innehåller
samtliga nio målspråkstexter. Den parallella PO-filen används för lokal
katalogvalidering. `msgfmt --check`, l10n-lint, diffkontroll och Gitleaks
passerar. Hunspell-SV markerar bara spelnamnen och fackordet `innerzon`.
svlangs återstående varningar gäller kolon i de engelska förlagorna, medan
den svenska texten har skrivits om med normal svensk meningsbyggnad.

Batchen sparades i Crowdins redigerare 2026-11-11. Redigeraren bekräftade
`Successfully added 9 translations`, visade `No unsaved translations` och
läste tillbaka den längsta måltexten exakt. Översättningarna väntar nu på
eventuell uppströmsgranskning, godkännande och release.
