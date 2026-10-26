# Cacti core: jämförelse med core 1.2

Den aktuella core-exporten jämfördes med arkiverade, granskade ändringar för core 1.2 utifrån exakt kontext, källtext och pluralform. 1 446 poster överlappade; 64 hade olika översättningar. Efter granskning valdes 53 för uppladdning. Weblate rapporterade 10 uppdaterade och 43 som inte hittades. Exemplet “Autocomplete Enabled” finns i exporten men en sökning i Weblates core-komponent gav inga träffar. De 43 ska inte räknas som inskickade och behöver kontrolleras mot aktuella aktiva strängar innan de används igen.

Filen kontrollerades med msgfmt, l10n-lint (0 fel, en bedömd skiljeteckenvarning), svlang, Hunspell och Gitleaks (inga fynd). Övriga skillnader kräver separat bedömning. Granskningen är inte fullständig.

PHP-formatvarningen för strängen med 80 % av systemminnet avfärdades i Weblate 2026-10-26. Kontroll mot Cactis support.php visar att översättningen skrivs ut direkt med __() utan printf-formatering; procenttecknet är bokstavligt.

Kalendergranskningen rättade 15 namn på veckodagar och månader till liten bokstav samt två fälttexter. Weblate bekräftade 17 uppdaterade, inga saknade eller överhoppade. msgfmt passerade, l10n-lint rapporterade inga fel och sju versalvarningar som är avsiktliga enligt svensk stavning; svlang, Hunspell och Gitleaks kördes, utan läckagefynd.

Uppföljning 2026-10-26: aktuell core-export jämfördes med de 16 ändringarna för datafrågor i core 1.2. Samtliga 16 källsträngar och översättningar överensstämmer; ingen separat uppladdning gjordes. Fortsatt granskning samlas per komponent och laddas upp när komponentfilen är färdig.
