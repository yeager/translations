# Cacti core: svensk radgranskning

2026-10-26 granskades 5 198 exporterade poster. Den bifogade deltafilen innehåller 732 ändrade poster, inklusive åtta med pluralformer. En annan redaktörs ändring lämnades orörd och tre förslag fanns redan i den hämtade PO-filen.

Uppladdningen via webbläsaren gav först ett 502-fel. Weblates kvitto visades senare och bekräftar 732 uppdaterade, 0 överhoppade och 0 saknade. En efterföljande Weblate-CSV från databasen visar att samtliga 732 poster har den avsedda svenska texten i den form CSV visar. CSV visar bara första pluralformen. En senare PO-export jämfördes med deltafilen: båda formerna för samtliga åtta pluralposter överensstämmer. Weblates övriga kontrollvarningar återstår att granska.

msgfmt --check --check-format och Gitleaks passerade. l10n-lint rapporterade 0 fel och 37 bedömda varningar; svlang, Hunspell och jämförelse med den svenska termbanken kördes. Termbanken innehåller äldre och kontextberoende förslag som inte har ersatt den manuella bedömningen. Den engelska texten om inaktivering vid import är fortsatt oklar och behöver kontroll mot hela kodkedjan.

Kontroll 2026-10-26: Weblates enda återstående PHP-formatvarning gällde InnoDB-texten med bokstavliga procenttal. Källkoden i lib/utility.php anropar __() utan formatargument, och global_languages.php returnerar i det fallet texten direkt. Weblate tolkade delar av vanlig text som formatmarkörer; kontrollen avfärdades. Översikt före åtgärden: 212 strängar med kontrollvarningar, inklusive denna PHP-varning, 59 om slutpunkt och 144 om återanvänd översättning (kategorier kan överlappa).

2026-10-26: de sex kontrollerna för oförändrad översättning granskades och avfärdades i Weblate. GNU General Public License är licensens namn, AutoM8, Boost och Spine är funktions- eller produktnamn, ”operation” är svenska och ”Community:” avser SNMP community (bekräftat i utilities.php). Övriga typer av kontrollvarningar kvarstår.

2026-10-26: fyra återstående varningar om identiska pluralformer granskades och avfärdades i Weblate. ”Paket” och ”paketförråd” har samma form i singular och plural; uppmaningarna är därför korrekta i båda formerna. Andra kontrolltyper kvarstår.

2026-10-26: Granskade samtliga sju varningar om omatchat frågetecken i core. De svenska frågorna har korrekt frågetecken trots punkt i källan, och en beskrivning har korrekt punkt trots frågetecken i källan. Avfärdade de sju frågeteckensvarningarna och sju motsvarande punktvarningarna i Weblate. Översättningarnas text ändrades inte. Översikten visade därefter 194 strängar med återstående kontroller, varav 52 med omatchad slutpunkt och 144 med återanvänd översättning; kategorierna kan överlappa.

2026-10-26: Granskade nio ytterligare punktvarningar i core. Svenska hela meningar har fått behålla slutpunkt även där källtexten saknar punkt. Avfärdade även två varningar för återanvändning där engelska källor bara skiljer sig i uttrycket ”with id” respektive ”with id of” och har samma betydelse. Weblate visade därefter 185 strängar med kontroller: 43 punktvarningar och 142 återanvändningsvarningar. Ingen översättningstext ändrades.

2026-10-26: Granskade nio ytterligare punktvarningar och avfärdade dem: de svenska texterna är hela meningar med korrekt slutpunkt trots att källorna saknar slutpunkt. Exempelvärdet 2.00 och HTML-element behölls. Weblate visade därefter 176 strängar med kontroller, varav 34 punktvarningar och 142 återanvändningsvarningar. Ingen översättningstext ändrades.

2026-10-26: Granskade ytterligare åtta punktvarningar. Sju avfärdades eftersom svenska texten korrekt avslutas med punkt. I den åttonde rättades dessutom formuleringen om hur utförligt loggdetaljer visas; filen cacti-core-log-fix.po laddades upp och Weblate rapporterade en uppdaterad sträng. msgfmt --check godkände filen. Hunspell kunde inte köras eftersom sv_SE-ordlistan inte hittades av installationen.

Kompletterande verktygskontroll 2026-10-26: den svenska Hunspell-ordlistan fanns lokalt på work/hunspell-sv/sv_SE; den uppdaterade texten gav inga stavningsträffar. l10n-lint med terminologikontroll gav noll fel och en punktvarning: den svenska hela meningen avslutas med punkt medan källtexten saknar slutpunkt. svlang gav 10/10 för naturlighet men flaggade fem vanliga ord som saknade i frekvenslistan; de har bedömts manuellt. Den tidigare noteringen om att ordlistan inte hittades avsåg standardinställningen och är nu åtgärdad för kontrollen.

2026-10-26: Granskade och avfärdade åtta punktvarningar, bland annat för loggdetaljer, XML-fel och en saknad inkluderingsfil. De svenska meningarna ska avslutas med punkt; tekniska identifierare och platshållare bevarades. Weblate visade därefter 161 strängar med kontroller: 19 punktvarningar och 142 återanvändningsvarningar. Ingen översättningstext ändrades vid denna granskning.

2026-10-26: Granskade nio punktvarningar till och avfärdade dem. Svenska meningar avslutas korrekt med punkt även om källan saknar punkt; versions- och filnamnsplatshållare har kontrollerats mot källan. Weblate visade därefter 152 strängar med kontroller: 10 punktvarningar och 142 återanvändningsvarningar. Ingen översättningstext ändrades.

2026-10-26: Granskade de tio återstående punktvarningarna och avfärdade dem. Svenska hela meningar har korrekt slutpunkt; policytexternas HTML och skillnaderna mellan behörighetsvillkor har kontrollerats mot källorna. Weblate visade därefter inga punktvarningar och 142 strängar med återanvändningsvarning. Ingen översättningstext ändrades.

2026-10-26: Ytterligare åtta varningar om återanvänd översättning granskades och avfärdades i Weblate. De gäller likvärdiga källtexter samt singular och plural av nätverk, som har samma obestämda form på svenska. Inga översättningstexter ändrades. Varningen för Poller/Pollers lämnades kvar för kontroll av pluralformen; 130 återanvändningsvarningar återstod enligt Weblates översikt.

2026-10-26, fortsatt granskning: Korrigering av föregående anteckning: ”insamlare” har samma form i obestämd singular och plural. Poller/Pollers-varningen avfärdades därför efter kontroll. Även Total IP Addresses/Total IPs och Run Limit/Timeout avfärdades; källkoden anger maximal körtid för Run Limit. Tre varningar avfärdades, 127 återstod. Data Collector/Collectors lämnades tills sammanhanget har jämförts. Ingen översättningstext ändrades.
