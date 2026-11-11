# RPCS3, svensk Crowdin-kontroll

Datum: 11 november 2026

Den inloggade Crowdin-editorn för `rpcs3_template.ts` visar 100 % översatt
och 97 % granskad. Sökning i editorn bekräftar att den befintliga översättningen
av *Hybrid rendering mode* använder **Hybridrenderingsläge**, men att den
efterföljande meningen fortfarande säger *återge ungefärlig grafik*.

Den lokala deltafilen
`rpcs3_sv-SE_crowdin-20261109-rendering-terminology.ts` använder *rendera
ungefärlig grafik* och den projektspecifikt konsekventa termen *tolken* för
*interpreter*. XML, l10n-lint och Gitleaks är godkända. svlang och Hunspell-sv
markerar endast XML/källtext och etablerade facktermer.

De återkommande besluten finns samlade i `TERMINOLOGY.md`.

## Inskick 2026-11-11

Den granskade rättelsen för den sammansatta Tooltip-posten sparades i Crowdins
redigerare med kontot `yeagersthlm`. Redigeraren visade den nya texten som
sparad av kontot för några sekunder sedan och den exakta måltexten lästes
tillbaka. En separat osparad post som redan fanns i redigeraren lämnades
orörd. Detta bekräftar ett sparat översättningsförslag, men inte
granskning, godkännande eller release uppströms.

## Omkontroll 2026-11-11

Deltafilen kontrollerades på nytt med XML-validering, l10n-lint, svlangs
svengelskakontroll och skrivregler, diffkontroll och Gitleaks. Samtliga
kontroller passerar.

## API-kontroll 2026-11-11

Crowdins API kontrollerades med den etablerade projektåtkomsten. Den svenska
projektstatusen är 3 712 av 3 712 strängar och 20 847 av 20 847 ord
översatta, alltså 100 %. Granskningsgraden är 97 %: 3 663 strängar och
20 356 ord är godkända. API:ts filprogress hade inga svenska filer med
ofullständig översättning.

Det finns därför ingen ny oöversatt batch att skapa eller skicka. De återstående
skillnaderna mellan översatt och godkänd status hör till projektets egna
granskningsflöde och ändrades inte.
