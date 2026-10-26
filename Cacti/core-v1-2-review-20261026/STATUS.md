# Cacti core v1.2: granskning 2026-10-26

Pågående arbete. Två deltafiler innehåller 753 ändrade strängar vardera. Weblate bekräftade att den första filens 753 strängar uppdaterades. Den andra har delats upp i fyra filer med 200, 200, 200 respektive 153 strängar.

Alla fyra mindre filer har skickats men deras svar nådde inte fram före tidsgränsen. Flera strängar ur den första av dessa syntes därefter uppdaterade direkt i Weblate; fullständiga kvitton saknas för samtliga fyra. Kontrollera uppladdningarna före eventuella nya försök. Weblates nedladdade PO kan släpa efter väntande databasändringar.

`msgfmt --check --check-format` passerade för delarna. l10n-lint rapporterade 0 fel och 36 varningar på det fullständiga underlaget. Hunspell, svlang och terminologikällorna har använts; ytterligare bedömning av träffar och Weblates kontroller återstår.

Stickprov efter uppladdningarna: ”Operation successful” från del 2-2 och ”Finish Editing Tree” från del 2-4 visar de nya översättningarna direkt i Weblate. Detta bekräftar enskilda strängar, inte hela filerna. Vid kontroll av närliggande strängar upptäcktes ytterligare äldre språkfel, bland annat pluralformen för ”Duplicate Data Source Profile”; granskningen är därför inte färdig.

En kompletterande fil med åtta rättelser skickades via webbläsaren. Weblate bekräftade 8 uppdaterade, 0 överhoppade och 0 saknade. PO-filen klarade msgfmt --check --check-format.

Tio ytterligare terminologirättelser skickades via webbläsaren. Weblate bekräftade 10 uppdaterade, 0 överhoppade och 0 saknade. PO-filen klarade msgfmt --check --check-format.

Granskning av Weblates skiljeteckenskontroller: alla 21 träffar för slutpunkt och alla 5 för frågetecken undersöktes i bläddringsvyn. Avvikelserna gäller kompletta svenska meningar där källan saknar punkt eller frågor där källan har punkt/utropstecken. Svenska skiljetecken behålls; dessa kontrollvarningar behöver inte innebära översättningsfel. Övriga kontrollkategorier återstår.
