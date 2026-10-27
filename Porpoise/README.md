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

Ett fjärde häfte rättade ytterligare tio UI-texter om minneskort,
sparfiler, automatisk spelsökning, sandlådeläge och GameCube-menyn.
Samma struktur- och säkerhetskontroller passerade igen, och den aktuella
arkivkopian har SHA-256 `abe948e351bf0420ec22b63fd1cfe75feb9e21e0616b4a7dfa75104aa9312679`.

Ett femte häfte rättade tio instruktioner om egna filer, Wii-skivor,
WiiConnect24, texturpaket och egen Wii-systemdata. JSON, nyckel- och
platshållarjämförelse, tabellgenerering, C++-kompilering, diff och Gitleaks
passerade. Den aktuella arkivkopian har SHA-256
`70c05acfaee140e8bd7313d7c396ee759c7d7fc150e33f7e60a4cafebedb0fea`.

Ett sjätte häfte rättade sju korta UI-etiketter och statusrader, bland annat
av- och påknappar, sökstatus, layoutnamn, filvägsetikett och WiiConnect24.
JSON, nycklar, platsmarkörer, C++-tabellen, diff och Gitleaks passerade igen.
Den aktuella arkivkopian har SHA-256
`bea368301ac7afe134259f264fb9e3912822c79fa1a06bdd5bc4506809ba8e5f`.

Ett sjunde häfte skrev om tre längre instruktioner om jailbreak och appens
sandlåda. Tekniska namn, filer och sökvägar behölls oförändrade. JSON,
nycklar, platsmarkörer, tabellgenerering, C++-kompilering, diff och Gitleaks
passerade. Den aktuella arkivkopian har SHA-256
`b43eb04bf7f957b50fedb2399fda2a5e0fe07ba8d3697f453d69a160b9345413`.

Ett åttonde häfte ersatte åtta engelska UI-termer med etablerad svensk
terminologi: bland annat begränsningsruta, CPU-omkompilator, ljudsträckning,
skanningslinjer och ryggar. Termbanken och översättningsminnet användes som
underlag. JSON, nycklar, platsmarkörer, tabellgenerering, C++-kompilering,
diff och Gitleaks passerade. Den aktuella arkivkopian har SHA-256
`5343849d33fbab85a2f612e5b27c0ed5cb5ba694e4eb0617048c345d811f3c1a`.

Ett nionde häfte översatte tre kontrollrelaterade etiketter till styrkors,
Nunchuk-spak och gyroskop. JSON, nycklar, platsmarkörer, tabellgenerering,
C++-kompilering, diff och Gitleaks passerade. Den aktuella arkivkopian har
SHA-256 `1907c9604155b9c4c048cdf47c6eb46b7bd716f407723a1eba5a5ac030626954`.

Det tionde häftet rättar 31 säkra UI-texter om åtgärdsknappar, sparfiler,
minneskort, bredbild och menyljud. Samtliga nycklar finns i den aktuella
källistan och platsmarkörer är identiska med engelskan. JSON-tolkning,
`l10n-lint`, `svlang`, Hunspell-granskning, termbankskontroll och Gitleaks
passerar. Häftet är en lokal deltafil; ingen uppströms-PR har skapats.

Det elfte häftet rättar elva UI-texter om spelbibliotek, bildåtergivning och
menyljud. Det bevarar platshållare och tekniska produktnamn, men ersätter
felaktiga böjningar och direkta engelskpåverkningar med naturlig svenska.

Det tolfte häftet normaliserar 24 korta åtgärds- och statusrader från tre
punkter till svenska ellipstecken. Inga betydelser eller tekniska termer har
ändrats, och platshållaren `{n}` är bevarad.

Det trettonde häftet rättar fem längre hjälptexter om emuleringshastighet,
automatiska korrigeringar, menymusik och bildruteinterpolering. Det återställer
betydelse som tidigare översättning förlorade och använder naturlig svensk
fackterminologi.
