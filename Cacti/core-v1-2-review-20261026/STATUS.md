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
