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

Ingen ny Crowdin-ändring skickades i denna kontroll. Vid den senaste
åtkomstkontrollen saknades den tidigare webbsessionen och Crowdin CLI saknade
projektkonfiguration. När en etablerad kanal åter är tillgänglig ska ändringen
sparas och läsas tillbaka innan den räknas som inskickad.
