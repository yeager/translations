# Cataclysm-DDA, svensk Transifex-granskning

Cataclysm-DDA har aktuella experimentella utgåvor och är ett aktivt projekt.
Den 12 november 2026 granskades och skickades den första svenska batchen med
tio UI- och statussträngar i komponenten `master-cataclysm-dda`. Strängarna
omfattar prestationer, vapenfunktioner, autokörning och interaktiva åtgärder.

Alla C-formatplatshållare och den inledande radbrytningen kontrollerades före
uppladdning. En pluralsträng skickades med separata svenska former för en och
flera. Transifex API bekräftade 10 uppdateringar utan fel och varje enskild
sträng lästes tillbaka efter indexering.

Arbetet är lokalt granskat, arkiverat, pushat till detta arkiv och uppladdat
till Transifex. Upstreamgranskning eller publicering är inte verifierad.
Återstående arbete: efter nio batcher om sammanlagt 90 strängar visade en
sidindelad API-avläsning fortfarande 1 000 oöversatta svenska strängar på var
och en av de första 21 sidorna. Huvudkomponenten har alltså minst 21 000
oöversatta svenska strängar; den exakta mängden kräver att hela
sidindelningen läses färdigt. Arbetet fortsätter i separata batcher.
