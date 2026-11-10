# RPCS3, svensk Crowdin-kontroll

Datum: 11 november 2026

Den inloggade Crowdin-editorn för `rpcs3_template.ts` visar 100 % översatt
och 97 % granskad. Sökning i editorn bekräftar att den befintliga översättningen
av *Hybrid rendering mode* använder **Hybridrenderingsläge**, men att den
efterföljande meningen fortfarande säger *återge ungefärlig grafik*.

Den lokala deltafilen
`rpcs3_sv-SE_crowdin-20261109-rendering-terminology.ts` ändrar bara detta till
*rendera ungefärlig grafik*. XML, l10n-lint och Gitleaks är godkända. svlang
och Hunspell-sv markerar endast XML/källtext och etablerade facktermer.

Ingen ny Crowdin-ändring skickades i denna kontroll. Den externa uppdateringen
väntar på uttryckligt godkännande vid själva publiceringssteget.
