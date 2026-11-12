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
Återstående arbete: huvudkomponenten har fortfarande fler än 1 000 oöversatta
svenska strängar och fortsätter i separata batcher.
