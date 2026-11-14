# Dwarf Fortress 50.* `lua`: granskning av sfäradjektiv

15 november 2026. De oöversatta värdena i `random_sphere_adjective`, till exempel `agricultural`, `animal` och `artistic`, har granskats i sin konkreta kodkontext i `data/init/globals.lua`.

Värdet hämtas av `get_random_sphere_adjective()` och används för procedurgenererade änglars namn. Namnskriptet sammanfogar samma enda sträng med både varelseform i singular, plural och adjektivform. Den engelska formen kan stå oförändrad framför alla tre, medan svenska adjektiv normalt måste böjas efter form och genus.

Transifex erbjuder endast ett enda översättningsfält och saknar separat böjningsinformation för dessa poster. Att automatiskt översätta till exempel `agricultural` till *jordbrukande* eller *jordbruks-* skulle därför ge fel eller onaturliga genererade namn i minst en av formerna.

Beslut: lämna dessa namnled oöversatta tills spelet erbjuder svensk grammatikhantering eller separata former. Det är ett medvetet undantag, inte en missad normal UI-översättning. Inget har ändrats eller skickats upstream i denna granskning.

Underlag: Dwarf Fortress Wiki beskriver att `get_random_sphere_adjective()` returnerar en enda sträng, och änglaskriptet visar att den sätts före tre olika namnformer.
