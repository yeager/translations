# Terminologi: Dwarf Fortress `text_set` och `hardcoded_steam`

| Engelska | Svenska | Sammanhang | Beslut |
| --- | --- | --- | --- |
| plump helmet | fetthjälm | Dwarf Fortress-svamp; berättelserader | Projektspecifik sammansättning. Termen behandlas som ett växtnamn och skrivs med gemen. |
| home-tree | hemträd | Alvernas träd och hemvist i berättelserader | Översätts som sammansättningen `hemträd`; bestämd form `hemträdet`. |
| bone mill | benkvarn | Föremål eller anläggning i hotfull replik | Översätts bokstavligt och idiomatiskt som sammansättningen `benkvarn`. |
| Transifex-taggar | bevaras strukturellt | DF:s dynamiska text, till exempel `[C:2:0:0]`, `[BP:…]`, `[ATTACK_VERB:…]` och `[PREFSTRING:…]` | Behåll hakparenteser, kolon, versala fältnamn, antal fält och mellanslag runt taggen. Översätt endast taggens små bokstavsdelar när de är naturligt språk. |
| standard plural (`STP`) | svensk pluralform | Taggar som skapar plural av engelsk form | Ersätt `STP` med korrekt svensk plural när taggen kräver en uttrycklig form. |
| 3rd-person verb | tredje person singular | Verbtaggar med engelsk ändelse `-s` | Det engelska `-s` är verbform, inte plural; ange svensk grundform och tredje person enligt taggens semantik. |
| generated names | böjningsneutrala formuleringar | Bok- och artefaktnamn med `[NAME]`, `[NO_ART_NAME]`, `[ADJ]` och `[NOUN]` | Undvik svenska konstruktioner som kräver okänt genus eller böjning hos en infogad variabel. |
| stockpile | förråd | Förvaringsyta och logistik i fästningsläget | Använd `förråd` konsekvent i UI där spelets särskilda lagringsyta avses. |
| track stop | spårstopp | Gruvvagnsrutter; stopp som lastar och lossar ett fordon | `Spårstopp` används som projektspecifik sammansättning. Den beskriver objektets funktion och undviker den svenska järnvägsbetydelsen av signalstopp. |
| water-powered trip hammer | vattendriven fallhammare | Teknikhistorisk bok- eller kunskapstext | `Fallhammare` är den etablerade svenska tekniska termen; vattenkraften uttrycks som ett attribut. |
| Charge Attack | rusningsattack | Valbar stridsåtgärd | Översätts som en sammanhållen åtgärdsbenämning, inte som en allmän uppmaning att anfalla. |

## Källor och avgränsning

`plump helmet` är en namngiven svamp i spelet. Det saknades en etablerad svensk översättning i den tillgängliga översättningshistoriken och i den svenska översättningsminneskontrollen. `Fetthjälm` används därför konsekvent i denna batch, men ska omprövas om projektet senare fastställer en officiell svensk term.

Produktnamnet Dwarf Fortress och kodsyntaxen `[PRO_POS]` översätts inte.

Riktlinjerna i [DFInts Translation Tips and Transifex Usage Recommendations](https://github.com/dfint/.github/wiki/Translation-Tips-and-Transifex-Usage-Recommendations) används för taggar, synliga mellanslag, plural- och personformer. Dwarf Fortress-wikin om [språkdata](https://dwarffortresswiki.org/index.php/language) bekräftar att de fördefinierade spel­språken saknar egentlig morfologi och främst används för namn; det är därför olämpligt att låta svensk syntax förutsätta böjning eller genus hos namnvariabler.
