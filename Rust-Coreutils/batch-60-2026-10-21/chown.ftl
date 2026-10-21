chown-about = Ändra filägare och grupp
chown-usage =
  chown [OPTION]... [OWNER][:[GROUP]] FILE...
  chown [OPTION]... --reference=RFILE FILE...

# Hjälpmeddelanden
chown-help-print-help = Skriv ut hjälpinformation.
chown-help-changes = som utförligt läge, men rapportera bara när en ändring görs
chown-help-from =
  ändra ägaren och eller gruppen för varje fil endast om dess
  nuvarande ägare och eller grupp matchar de som anges här.
  Båda kan utelämnas, i vilket fall en matchning inte krävs
  för det utelämnade attributet
chown-help-preserve-root = vägra att arbeta rekursivt på '/'
chown-help-no-preserve-root = behandla inte '/' på något särskilt sätt (standardinställningen)
chown-help-quiet = utelämna de flesta felmeddelandena
chown-help-recursive = arbeta rekursivt på filer och kataloger
chown-help-reference = använd RFILEs ägare och grupp i stället för att ange värden för OWNER:GROUP
chown-help-verbose = visa ett diagnostiskt meddelande för varje bearbetad fil

# Felmeddelanden
chown-error-failed-to-get-attributes = misslyckades med att hämta attribut för { $file }
chown-error-invalid-user = ogiltig användare: { $user }
chown-error-invalid-group = ogiltig grupp: { $group }
chown-error-invalid-spec = ogiltig specifikation: { $spec }

# Varningsmeddelanden
chown-warning-dot-separator = '.' ska vara ':': { $spec }
