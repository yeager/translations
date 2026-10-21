expr-after-help = En tom rad nedan avgränsar grupper med ökande prioritet.

  UTTRYCK kan vara:

  ARG1 | ARG2
        ARG1 om det varken är null eller 0, annars ARG2

  ARG1 & ARG2
        ARG1 om inget argument är null eller 0, annars 0

  ARG1 < ARG2
        ARG1 är mindre än ARG2

  ARG1 <= ARG2
        ARG1 är mindre än eller lika med ARG2

  ARG1 = ARG2
        ARG1 är lika med ARG2

  ARG1 != ARG2
        ARG1 är inte lika med ARG2

  ARG1 >= ARG2
        ARG1 är större än eller lika med ARG2

  ARG1 > ARG2
        ARG1 är större än ARG2

  ARG1 + ARG2
        aritmetisk summa av ARG1 och ARG2

  ARG1 - ARG2
        aritmetisk differens mellan ARG1 och ARG2

  ARG1 * ARG2
        aritmetisk produkt av ARG1 och ARG2

  ARG1 / ARG2
        aritmetisk kvot av ARG1 dividerat med ARG2

  ARG1 % ARG2
        aritmetisk rest av ARG1 dividerat med ARG2

  STRING : REGEXP
        förankrad mönsterträff för REGEXP i STRING

  match STRING REGEXP
        samma som STRING : REGEXP

  substr STRING POS LENGTH
        delsträng av STRING, med POS räknat från 1

  index STRING CHARS
        index i STRING där något av CHARS hittas, eller 0

  length STRING
        längden på STRING

  + TOKEN
        tolka TOKEN som en sträng, även om det är ett nyckelord som match eller en operator som /

  ( UTTRYCK )
        värdet av UTTRYCK

  Observera att många operatorer måste skyddas eller citeras i skal.
  Jämförelser är aritmetiska om båda ARG är tal, annars lexikografiska.
  Mönsterträffar returnerar strängen som matchas mellan \( och \), eller null. Om
  \( och \) inte används returneras antalet matchade tecken eller 0.

  Avslutningsstatus är 0 om UTTRYCK varken är null eller 0, 1 om UTTRYCK
  är null eller 0, 2 om UTTRYCK är syntaktiskt ogiltigt och 3 om ett
  fel inträffar.

  Miljövariabler:

    - EXPR_DEBUG_TOKENS=1: skriv ut uttryckets token
    - EXPR_DEBUG_RPN=1: skriv ut uttrycket i omvänd polsk notation
    - EXPR_DEBUG_SYA_STEP=1: skriv ut varje tolkningssteg
    - EXPR_DEBUG_AST=1: skriv ut uttrycket som ett abstrakt syntaxträd

  Fel rapporteras med uttrycket återgivet och en cirkumflex under det
  felaktiga argumentet när standardfel är en terminal. Allt annat som läser
  standardfel får det vanliga enradsmeddelandet.
