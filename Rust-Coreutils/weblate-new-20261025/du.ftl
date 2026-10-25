du-after-help =
    Visade värden anges i enheter från det första tillgängliga värdet för STORLEK
    från --block-size och miljövariablerna DU_BLOCK_SIZE, BLOCK_SIZE och BLOCKSIZE.
    Annars används 1 024 byte, eller 512 om POSIXLY_CORRECT är satt.

    STORLEK är ett heltal med valfri enhet, till exempel är 10M lika med 10*1024*1024.
    Enheterna K, M, G, T, P, E, Z och Y är potenser av 1024; KB, MB med flera
    är potenser av 1000. Enheter kan vara decimala, hexadecimala, oktala eller binära.

    MÖNSTER tillåter avancerade undantag. Följande syntaxer stöds
    till exempel:

      - ? matchar exakt ett tecken
      - { "*" } matchar noll eller fler tecken
      - { "{" }a,b{ "}" } matchar a eller b
