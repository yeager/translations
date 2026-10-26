# Cacti core: svensk radgranskning

2026-10-26 granskades 5 198 exporterade poster. Den bifogade deltafilen innehåller 732 ändrade poster, inklusive åtta med pluralformer. En annan redaktörs ändring lämnades orörd och tre förslag fanns redan i den hämtade PO-filen.

Uppladdningen via webbläsaren gav först ett 502-fel. Weblates kvitto visades senare och bekräftar 732 uppdaterade, 0 överhoppade och 0 saknade. En efterföljande Weblate-CSV från databasen visar att samtliga 732 poster har den avsedda svenska texten i den form CSV visar. CSV visar bara första pluralformen. En senare PO-export jämfördes med deltafilen: båda formerna för samtliga åtta pluralposter överensstämmer. Weblates övriga kontrollvarningar återstår att granska.

msgfmt --check --check-format och Gitleaks passerade. l10n-lint rapporterade 0 fel och 37 bedömda varningar; svlang, Hunspell och jämförelse med den svenska termbanken kördes. Termbanken innehåller äldre och kontextberoende förslag som inte har ersatt den manuella bedömningen. Den engelska texten om inaktivering vid import är fortsatt oklar och behöver kontroll mot hela kodkedjan.

Kontroll 2026-10-26: Weblates enda återstående PHP-formatvarning gällde InnoDB-texten med bokstavliga procenttal. Källkoden i lib/utility.php anropar __() utan formatargument, och global_languages.php returnerar i det fallet texten direkt. Weblate tolkade delar av vanlig text som formatmarkörer; kontrollen avfärdades. Översikt före åtgärden: 212 strängar med kontrollvarningar, inklusive denna PHP-varning, 59 om slutpunkt och 144 om återanvänd översättning (kategorier kan överlappa).

2026-10-26: de sex kontrollerna för oförändrad översättning granskades och avfärdades i Weblate. GNU General Public License är licensens namn, AutoM8, Boost och Spine är funktions- eller produktnamn, ”operation” är svenska och ”Community:” avser SNMP community (bekräftat i utilities.php). Övriga typer av kontrollvarningar kvarstår.

2026-10-26: fyra återstående varningar om identiska pluralformer granskades och avfärdades i Weblate. ”Paket” och ”paketförråd” har samma form i singular och plural; uppmaningarna är därför korrekta i båda formerna. Andra kontrolltyper kvarstår.

2026-10-26: Granskade samtliga sju varningar om omatchat frågetecken i core. De svenska frågorna har korrekt frågetecken trots punkt i källan, och en beskrivning har korrekt punkt trots frågetecken i källan. Avfärdade de sju frågeteckensvarningarna och sju motsvarande punktvarningarna i Weblate. Översättningarnas text ändrades inte. Översikten visade därefter 194 strängar med återstående kontroller, varav 52 med omatchad slutpunkt och 144 med återanvänd översättning; kategorierna kan överlappa.
