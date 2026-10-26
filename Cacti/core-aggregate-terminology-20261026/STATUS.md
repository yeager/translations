# Cacti core: grafaggregering

51 granskade strängar med aggregerad graf. msgfmt och l10n-lint passerade; Hunspell-träffarna granskades. Svlang gav 0/10 och flaggade vanliga ord och imperativ som V2-fel, vilket kräver manuell bedömning. Weblate-uppladdning väntar; systemets filväljare kunde inte styras från Codex.

2026-10-26: Filen skickades upp till Cacti core i Weblate. Kvittot visar 51 uppdaterade, 0 överhoppade och 0 saknade strängar. Weblate visade 53 återstående kontrollvarningar för komponenten.

2026-10-26: Aktuell export av core v1.2.x visade att 19 gemensamma ändringar redan fanns där. Tolv versionsspecifika förekomster av ”aggregatgraf” ändrades till ”aggregerad graf” eller motsvarande böjning. Weblate bekräftade 12 uppdaterade, 0 överhoppade och 0 saknade strängar. msgfmt och l10n-lint passerade; Hunspell flaggade endast ”grafmallen”, som bedömts korrekt. Efter uppladdningen visar Weblate 90 kontrollvarningar i komponenten, jämfört med 86 före; dessa återstår att granska.

Uppföljning: Varningen om återanvänd översättning för ”Click 'Continue' to delete the following Aggregate Graph(s).” jämfördes med en annan källsträng som har samma betydelse och avfärdades i Weblate. Övriga varningar är ännu inte granskade i denna uppföljning.

Ytterligare granskning: Fyra varningar om återanvänd översättning avfärdades efter jämförelse av likvärdiga källtexter: borttagning av grafer, konvertering av aggregerade grafer, koppling av grafer och borttagning av aggregatmallar. En femte avfärdades för borttagning av enheter. Varningen för ”Pollers” jämfört med ”Poller” och ”Collector” lämnades kvar för kontextgranskning.

Kontroll av ”Pollers”: I core 1.2 använder automation_devices.php etiketten för en väljare med poller_id; pollers.php hämtar samma poller-tabell. script_server.php beskriver poller-id som id för en datainsamlare. ”Insamlare” fungerar både som singular och plural i detta sammanhang. Varningen om återanvänd översättning avfärdades i Weblate; ingen översättning ändrades.

Fortsatt granskning av core 1.2: Sex varningar om återanvändning avfärdades efter jämförelse med källtexterna. Två gällde varianter av ”Item # %d” med samma betydelse; fyra gällde singular/plural-varianter för borttagning eller duplicering av data-, graf- och GPRINT-mallar/förinställningar. Inga översättningar ändrades.

Ytterligare fem varningar om återanvändning avfärdades efter jämförelse av likvärdiga källsträngar: duplicera grafmallar och grafer, skapa aggregerad graf samt aktivera och inaktivera enheter. Inga översättningstexter ändrades.

Ytterligare fem varningar avfärdades efter jämförelse: rensa enheters statistik, synkronisera enheter, bekräfta borttagning av enhetsmallar samt ta bort respektive duplicera enhetsmallar. Källtexterna uttrycker samma åtgärder med alternativa pluralformer eller formuleringar. Inga översättningstexter ändrades.

Terminologisk precisering: Cactis dokumentation skiljer på datainsamlare och den pollerprocess som hämtar data, men använder också ”remote poller” för fjärransluten datainsamlare. Tre strängar som uttryckligen avser pollerprocesser ändrades till ”insamlingsprocess” i core 1.2. msgfmt och l10n-lint passerade; Hunspell flaggade tekniska namn och sammansättningar, som granskades. Weblate bekräftade tre uppdateringar utan bortfall. Den tidigare avfärdade Pollers-varningen gäller en väljare för datainsamlare och den bedömningen står fast i just det sammanhanget. Se https://docs.cacti.net/Principles-of-Operation.md och https://docs.cacti.net/Data-Collectors.md.
