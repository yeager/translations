# Cacti core v1.2: granskning 2026-10-26

Pågående arbete. Två deltafiler innehåller 753 ändrade strängar vardera. Weblate bekräftade att den första filens 753 strängar uppdaterades. Den andra har delats upp i fyra filer med 200, 200, 200 respektive 153 strängar.

Alla fyra mindre filer har skickats men deras svar nådde inte fram före tidsgränsen. Flera strängar ur den första av dessa syntes därefter uppdaterade direkt i Weblate; fullständiga kvitton saknas för samtliga fyra. Kontrollera uppladdningarna före eventuella nya försök. Weblates nedladdade PO kan släpa efter väntande databasändringar.

`msgfmt --check --check-format` passerade för delarna. l10n-lint rapporterade 0 fel och 36 varningar på det fullständiga underlaget. Hunspell, svlang och terminologikällorna har använts; ytterligare bedömning av träffar och Weblates kontroller återstår.

Stickprov efter uppladdningarna: ”Operation successful” från del 2-2 och ”Finish Editing Tree” från del 2-4 visar de nya översättningarna direkt i Weblate. Detta bekräftar enskilda strängar, inte hela filerna. Vid kontroll av närliggande strängar upptäcktes ytterligare äldre språkfel, bland annat pluralformen för ”Duplicate Data Source Profile”; granskningen är därför inte färdig.

En kompletterande fil med åtta rättelser skickades via webbläsaren. Weblate bekräftade 8 uppdaterade, 0 överhoppade och 0 saknade. PO-filen klarade msgfmt --check --check-format.

Tio ytterligare terminologirättelser skickades via webbläsaren. Weblate bekräftade 10 uppdaterade, 0 överhoppade och 0 saknade. PO-filen klarade msgfmt --check --check-format.

Granskning av Weblates skiljeteckenskontroller: alla 21 träffar för slutpunkt och alla 5 för frågetecken undersöktes i bläddringsvyn. Avvikelserna gäller kompletta svenska meningar där källan saknar punkt eller frågor där källan har punkt/utropstecken. Svenska skiljetecken behålls; dessa kontrollvarningar behöver inte innebära översättningsfel. Övriga kontrollkategorier återstår.

Fyra cache- och loggtexter skickades via webbläsaren och Weblate bekräftade fyra uppdaterade. En upprepning i cachetexten rättades sedan direkt i Weblate. Den senaste versionen finns i cachefilen. De fem varningarna om oförändrad översättning avser en logisk operation, funktionsnamnen AutoM8, Boost och Spine samt SNMP-community; de har bedömts i sitt sammanhang.

Två licenstexter och en knapphänvisning rättades och skickades via webbläsaren. Weblate bekräftade 3 uppdaterade, 0 överhoppade och 0 saknade. PO-filen klarade msgfmt --check --check-format. Granskningen av återanvändningsvarningar återstår.

Fem rättelser av objekt- och prefixterminologi skickades via webbläsaren. Weblate bekräftade 5 uppdaterade, 0 överhoppade och 0 saknade. PO-filen klarade msgfmt --check --check-format. Återanvändningsvarningarna granskas vidare.

Återanvändningskontrollen: sidorna 2–4 i bläddringsvyn har granskats översiktligt. Träffarna gäller bland annat singular och plural som har samma svenska form, likvärdiga engelska formuleringar och identiska knapptexter. Kontroll av respektive motsträng och sammanhang återstår för en fullständig bedömning; inga varningar har avfärdats.

Tre hjälptexter om resurscache, statistik och RRD-filer rättades. Weblate bekräftade 3 uppdaterade, 0 överhoppade och 0 saknade. PO-filen klarade msgfmt --check --check-format.

De två kvarvarande pluralvarningarna för ”Avpublicera träd” och ”Lås upp träd” granskades och avfärdades i Weblate: träd har samma obestämda form i singular och plural. Sökningen efter identiska pluralformer visar därefter inga träffar.

Fjorton rättelser av konfigurations- och databastekster skickades via webbläsaren. Weblate bekräftade 14 uppdaterade, 0 överhoppade och 0 saknade. PHP-variabelnamn återställdes och PO-filen klarade msgfmt --check --check-format. Granskningen fortsätter.

Femton ytterligare rättelser av insticksmoduler, graftexter och databashjälp skickades via webbläsaren. Weblate bekräftade 15 uppdaterade, 0 överhoppade och 0 saknade. PO-filen klarade msgfmt --check --check-format. En ny varning om slutpunkt gäller en fullständig svensk mening vars källa saknar punkt. Granskningen fortsätter.

Sju hjälptexter om aviseringar, cache och datainsamling rättades och skickades via webbläsaren. Weblate bekräftade 7 uppdaterade, 0 överhoppade och 0 saknade. PO-filen klarade msgfmt --check --check-format. Granskningen fortsätter.

Efterkontroll av de tre senaste rättelsefilerna (config, plugin och settings): l10n-lint rapporterade 0 fel och 4 skiljeteckenvarningar, vilka bedömdes mot källtexten. Hunspell med yeager/hunspell-sv, svlang och terminologibanken användes; träffarna innehåller tekniska termer och möjliga falska positiva. Gitleaks skannade den lokala granskningskatalogen utan fynd.

Sju texter om insamling och cache rättades och skickades via webbläsaren. Weblate bekräftade 7 uppdaterade, 0 överhoppade och 0 saknade. msgfmt och l10n-lint rapporterade inga fel. Granskningen fortsätter.

Sammanhanget för Run Limit visar att Tidsgräns är korrekt; återanvändningsvarningen har inte avfärdats. Fem närliggande upptäcktstexter rättades och skickades via webbläsaren: 5 uppdaterade, 0 överhoppade och 0 saknade. msgfmt och l10n-lint passerade.

Fyra texter om autentisering, LDAP och filåtkomst rättades och skickades via webbläsaren. Weblate bekräftade 4 uppdaterade, 0 överhoppade och 0 saknade. msgfmt och l10n-lint passerade.

Tre intervalltexter för sekunder, minuter och timmar rättades efter kontroll av värdena i include/global_arrays.php och include/global_settings.php. Weblate bekräftade 3 uppdaterade, 0 överhoppade och 0 saknade. msgfmt och l10n-lint passerade.

TLS-alternativen Hard och Demand rättades till Strikt och Kräv efter kontroll av LDAP-konstanterna och inställningens sammanhang i källkoden. Weblate bekräftade 2 uppdaterade, 0 överhoppade och 0 saknade. msgfmt och l10n-lint passerade.

Fem status- och inställningstexter rättades. Fail kontrollerades mot användningen i host.php och översattes till Misslyckades. Weblate bekräftade 5 uppdaterade, 0 överhoppade och 0 saknade. msgfmt och l10n-lint passerade.

Fyra databas- och installationstexter rättades, inklusive variabelnamnet $rdatabase_username. Weblate bekräftade 4 uppdaterade, 0 överhoppade och 0 saknade. msgfmt och l10n-lint passerade.

Fem texter om grafer, datakällor, loggning och installation rättades. Weblate bekräftade 5 uppdaterade, 0 överhoppade och 0 saknade. msgfmt och l10n-lint passerade.

- Weblate: fem ändringar för fjärrinsamling och insticksmoduler uppladdade 2026-10-26; fem uppdaterade, inga saknades. Jämför gemensamma källsträngar och sammanhang med core innan ändringar återanvänds.

Kalendernamn och två avsändarbeskrivningar granskades: 17 uppdaterade i Weblate, inga saknade eller överhoppade. msgfmt, svlang, Hunspell och Gitleaks kördes. l10n-lint gav 0 fel och 9 varningar om avsiktliga små bokstäver respektive meningsslut. Två övriga fälttexter hade redan uppdaterats i båda komponenterna.
