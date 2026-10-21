du-after-help = Visa värden i enheter enligt första tillgängliga STORLEK från --block-size,
  och miljövariablerna DU_BLOCK_SIZE, BLOCK_SIZE och BLOCKSIZE.
  Annars används 1024 byte som standard, eller 512 om POSIXLY_CORRECT är satt.

  STORLEK är ett heltal med valfri enhet, till exempel är 10M lika med 10*1024*1024.
  Enheterna är K, M, G, T, P, E, Z, Y, potenser av 1024, eller KB, MB, ...,
  potenser av 1000. Enheter kan vara decimala, hexadecimala, oktala eller binära.

  MÖNSTER möjliggör vissa avancerade undantag. Följande syntaxer
  stöds:

    - ? matchar exakt ett tecken
    - { "*" } matchar noll eller fler tecken
    - {"{"}a,b{"}"} matchar a eller b
