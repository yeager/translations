# Intropage: terminologi, 2026-10-26

31 strängar om insamling ändrades och skickades till Cacti Weblate. Weblate rapporterade 31 uppdaterade, noll överhoppade och noll saknade. PO-filen passerade msgfmt och l10n-lint med svensk terminologikontroll utan varningar; en informationsnotering gäller avsiktlig skillnad i avslutande mellanslag mellan två källsträngar. Weblate visade därefter sju kontrollvarningar för återanvänd översättning, mot fem före uppladdningen; dessa behöver granskas. Senaste GitHub-release vid kontrollen var v4.0.4, publicerad 2024-04-26. Övriga termer återstår att granska.

Uppföljning: ”Poller Information” och ”Poller Details” hade fått samma svenska formulering. ”Poller Details” korrigerades till ”Detaljer om insamlingsprocessen”; Weblate rapporterade en uppdaterad sträng och antalet kontrollvarningar återgick till fem. Korrigeringsfilen passerade msgfmt och l10n-lint. De fem tidigare varningarna återstår att granska.

Ytterligare uppföljning: källkoden i `panellib/top5.php` beräknar polling ratio som `failed_polls / total_polls`. Den tidigare formuleringen ”insamlingsförhållande” ersattes därför med ”andel misslyckade insamlingar”. Sammanlagt sex kompletterande strängar skickades upp och Weblate rapporterade sex uppdaterade. Filen passerade msgfmt och l10n-lint.
