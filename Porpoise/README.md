# Porpoise – svensk lokalisering

Grunden är projektets egen JSON-baserade lokalisering, hämtad från commit
`61f38f6079a3011abba88e8f4f1cb0ddc0ed27a8` den 25 oktober 2026.

## Innehåll

- `porpoise-sv-20261026.json` innehåller 1 803 svenska strängar.
- `porpoise-sv-flags-20261026.png` utökar språkvalsbilden med en svensk flagga.
- `porpoise-sv-localization-20261026.patch` dokumenterar ändringarna i
  språkramverket och den genererade tabellen.

Svenska läggs sist i språkuppräkningen, så befintliga sparade språkval behåller
sina nummer. PS5:s svenska systemvärde, 13, väljer svenska automatiskt.
Användaren kan också välja svenska manuellt och lägga lokala rättelser i
`/data/porpoise/lang/sv.txt`.

## Kontroller

- `tools/make-i18n.py --check`: 1 803 av 1 803 svenska strängar.
- Alla platshållare i `{…}` jämfördes med engelska källsträngar.
- `src/ui_i18n.cpp` kompilerades med C++17 och strikta varningar.
- Språkvalsbilden verifierades till 1 632 × 64 pixlar, alltså 17 flaggceller.
- Gitleaks hittade inga hemligheter i den svenska katalogen.

Detta är ett komplett tekniskt första utkast. De längre hjälpraderna behöver
fortfarande en separat språklig rad-för-rad-granskning innan en uppströms-PR
skapas.

Den 27 oktober rättades de första bekräftade språkfelen: avtryckare,
konfiguration, korrigeringsfiler, ljudlucka och Wii NAND-säkerhetskopior.
Den genererade i18n-tabellen byggdes om och katalogkontrollen bekräftar
fortfarande 1 803 av 1 803 strängar. Resterande längre hjälprader granskas
separat innan en uppströms-PR skapas.

Samma granskningsomgång rättade även ordval för sparfiler och spartillstånd i
GameCube- och Wii-flödena. Kontrollkedjan omfattade JSON-tolkning,
`make-i18n.py --check`, diffkontroll och Gitleaks.

Nästa häfte normaliserade gränssnittets lägesnamn, bredbildsalternativ och
Wii-fjärrkontrollens förinställningar. Katalogens nyckeluppsättning och alla
platsmarkörer jämfördes med den engelska källistan utan avvikelser.

Ytterligare hjälprader för bredbild, ljudläge, rörelsekontroll, sandlådeläge
och spelinställningar har skrivits om från engelska till konsekvent svenska.
PR skapas först när samma radgranskning har täckt återstående hjälptexter.

Vanliga återstående engelska etiketter har också granskats och översatts,
däribland ljud, teckensnitt, enheter, kontrollbilder, MMU och
GameCube-startanimation.

Den 27 oktober granskades och rättades ytterligare fjorton längre hjälptexter
om uppdateringar, återställning, Wii-kontroller, spartillstånd och
bildgenerering. Katalogen innehåller fortsatt 1 803 av 1 803 svenska texter;
nyckeluppsättning och platsmarkörer stämmer med projektets källista, den
genererade C++-tabellen kompilerar med strikta varningar och Gitleaks är ren.
`l10n-lint` kan ännu inte jämföra projektets lista av källposter med dess
objektbaserade språkkatalog och ger därför katalogfel som inte motsvarar
projektets faktiska format. Ingen uppströms-PR är skapad: återstående längre
hjälptexter ska fortfarande granskas rad för rad.

Ett efterföljande häfte samma dag rättade sju återstående tydliga fel i
återställningsmeddelanden, styrspaksalternativ och uppdateringstexter.
Kontrollerna för JSON, alla nycklar, platsmarkörer, genererad C++-tabell,
diff och Gitleaks passerade igen. Hunspell-SV för de sju rättade texterna gav
bara avsiktliga produktnamn, filnamn och GitHub-adresser. Den aktuella granskningskopian är
`porpoise-sv-review-20261027.json`.

Ett tredje häfte rättade nio synliga fel i minneskortsvarningar,
texturpaket, appens sandlådemeddelanden och GameCube-kontrollportens hjälptext.
Efteråt passerade JSON-tolkning, komplett nyckel- och platshållarjämförelse,
generering och kompilering av C++-tabellen, diffkontroll och Gitleaks.
