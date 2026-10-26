# Mactrack: terminologi

2026-10-26: Åtta strängar uppdaterades i Weblate: graph översätts med graf, polling process med insamlingsprocess och poll som verb med avfråga i dessa sammanhang. msgfmt och l10n-lint passerade. Hunspell flaggade produktnamn, förkortningar och böjningar av avfråga, vilka granskades manuellt. Kvarvarande kontroller och hela komponentens övriga terminologi behöver granskas. Senaste release v4.8 publicerades 2024-10-16.

Cycle undantogs från nytt arbete eftersom senaste release v4.1 publicerades 2018-04-01, mer än 48 månader före granskningen.

2026-10-26: Sex par varningar om punkt och frågetecken avfärdades efter granskning. Två svenska uppmaningar avslutas korrekt med punkt trots frågetecken i källan; fyra svenska frågor avslutas korrekt med frågetecken trots punkt i källan. Weblate visar därefter 21 strängar med kvarvarande kontroller.

2026-10-26: Sex kontroller för återanvänd översättning avfärdades efter jämförelse: två varianter av hämtning av OUI-databasen, två varianter av samma rubrikrad samt avsändarnamn och avsändaradress jämförda med motsvarande fält i Monitor. Weblate visar därefter 15 strängar med kvarvarande kontroller.

2026-10-26: Varningar för MAC-adresser, IP-adresser och senaste skanning granskades mot motsvarande engelska varianter och avfärdades där betydelsen är densamma. Inkonsekvensvarningen för MAC Addresses kvarstår för jämförelse mellan komponenter. Weblate visar nu åtta strängar med aktiva kontroller.

2026-10-26: Sex ytterligare återanvändningskontroller avfärdades efter jämförelse av likvärdiga varianter för verktyg, autentisering, antal IP-adresser och OID-gräns. Två strängar har kvarvarande varningar: Watch Name/Alert Name behöver kontextjämförelse, och MAC Addresses behöver jämföras mellan komponenter.

2026-10-26: Syslog ”Alert Name” ändrades till ”Larmnamn”, medan Mactrack ”Watch Name” behåller ”Bevakningens namn”. Uppladdning i Weblate bekräftade en uppdaterad sträng. msgfmt och l10n-lint godkända.

2026-10-26: Weblates aktuella vy visar MAC Addresses, Mac Addresses och MAC's som ”MAC-adresser” i Mactrack. Den äldre arkivfilen innehöll singular för Mac Addresses, men den aktuella översättningen är redan rättad. Weblate visar ändå en inkonsekvensvarning; orsaken är ännu inte verifierad och varningen har inte avfärdats.

2026-10-26: Intropage: ”Disable panel move/enable copy text from panel” rättades så att kopiering aktiveras. Weblate bekräftade en uppdaterad sträng. msgfmt, l10n-lint och Hunspell kontrollerades. Senaste release v4.0.4: 2024-04-26.

Senare kontroll 2026-10-26: Mactracks svenska översikt visar 758 översatta strängar och ingen kategori för aktiva felande kontroller; 50 strängar har avfärdade kontroller. Den tidigare MAC-varningen visas alltså inte längre som aktiv i översikten. Översikten visar inte varför den försvann och detta innebär inte en ny fullständig radgranskning.

2026-10-26: De tio poster som Weblate märker som automatiskt översatta jämfördes med sina källtexter i bläddringsvyn: Errors/Fel, Unauthorized/Obehörig, Dashboard/Instrumentpanel, days/dagar, Duration/Varaktighet, Rows/Rader, Size/Storlek, Table/Tabell, Invalid request. Please try again./Ogiltig begäran. Försök igen. och Issues/Problem. Formuleringarna bedömdes fungera och inga ändringar eller etikettändringar gjordes. Detta gäller dessa tio poster, inte hela komponenten.

2026-10-26: Aktuell CSV-export med 758 enheter granskades rad för rad. Filen `cacti-mactrack-line-review-20261026.po` innehåller 27 rättelser; Weblate bekräftade 27 uppdaterade, 0 överhoppade och 0 saknade. Ordvalet för lagringstid, SNMP-communitysträng, skanning och intervall samordnades; i källkoden är intervallet för ”Every %d Days” två dagar. msgfmt passerade, l10n-lint gav 0 fel och en bedömd skiljeteckenvarning. Den numeriska informationsvarningen gäller omräkningen av 12:00 AM till 00:00. svlang rapporterade inga skrivregelfel; Hunspells träffar på produktnamn, förkortningar och sammansättningar granskades. Gitleaks fann inga hemligheter i arbetskatalogen. Efter importen visar Weblate tre aktiva kontrollvarningar: en slutpunkt och två återanvändningsvarningar, vilka återstår att granska.

2026-10-26: De tre kontrollvarningarna efter importen granskades och avfärdades. Källkoden visar att Communities och Read Strings båda avser SNMP-communitysträngar för läsåtkomst. Den svenska fullständiga meningen behåller avslutande punkt även om källtexten saknar punkt. Weblates översikt visar 758 översatta strängar och inga aktiva kontrollvarningar.

2026-10-26: Jämförelse av 94 poster i arkiverade `cacti-mactrack-sv-*-20261026.po` med standardgrenen i Cactis källförråd. Vid filcommit `f0a0a5f606dac7c723fad2f27e88e1c20aa0eb30` (11:45 UTC) fanns alla källtexter och kontexter; 39 måltexter inklusive pluralformer var identiska och 55 skilde sig. Filerna innehåller även äldre förslag som kan ha ersatts av senare ändringar, så siffrorna visar inte hur många aktuella Weblate-översättningar som saknas upstream. Jämförelse med en aktuell Weblate-export återstår.

2026-10-26: Weblates databasexport av Mactrack kl. 14:30 lokal tid jämfördes per exakt källtext och kontext med GitHub-filen vid commit `f0a0a5f606dac7c723fad2f27e88e1c20aa0eb30`. Av exportens 758 poster överensstämde 645 måltexter med källförrådets första målform, 102 skilde sig och 11 källtexter med kontext saknades. CSV-exporten visar inte ytterligare pluralformer. Weblate visar 758 översatta strängar utan aktiva kontrollvarningar. Jämförelsen gäller dessa tidpunkter och bevisar inte om de 102 skillnaderna fortfarande väntar på synkronisering.

2026-10-26: Weblates komponentinformation anger GitHub-grenen `develop`, fjärrrevision `f0817de` och Weblates arkivrevision `d6235ac76d13f19040008cc3495f4410849e7b69`. Den offentliga Weblate-Gitkatalogen hämtades och dess svenska PO-fil jämfördes med CSV-exporten från 14:30: samma 645 första målformer stämde, 102 skilde sig och 11 saknade exakt källa och kontext. GitHubs `develop` gav samma antal. Exporten kan innehålla databasändringar som ännu inte skrivits till Git; jämförelsen ensam fastställer inte exakt vilka ändringar som väntar eller när synkronisering sker. Ingen förrådsåtgärd utfördes.
