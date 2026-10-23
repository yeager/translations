du-help-print-help = Skriv ut hjälpinformation.

du-after-help = Visade värden anges i enheter från det första tillgängliga STORLEK från --block-size,
    och miljövariablerna DU_BLOCK_SIZE, BLOCK_SIZE och BLOCKSIZE.
    Annars används 1 024 byte som standardenhet, eller 512 om POSIXLY_CORRECT är satt.

    STORLEK är ett heltal med en valfri enhet, till exempel är 10M lika med 10*1024*1024.
    Enheterna är K, M, G, T, P, E, Z, Y, som är potenser av 1024, eller KB, MB,...,
    som är potenser av 1000. Enheter kan vara decimala, hexadecimala, oktala eller binära.

    MÖNSTER tillåter vissa avancerade undantag. Följande syntaxer
    stöds till exempel:

      - ? matchar exakt ett tecken
      - { "*" } matchar noll eller fler tecken
      - { "{" }a,b{ "}" } matchar a eller b
