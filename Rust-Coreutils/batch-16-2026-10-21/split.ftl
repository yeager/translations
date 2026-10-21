split-after-help = Skriv delar med fast storlek av INDATA till PREFIXaa, PREFIXab och så vidare; standardstorleken är 1000 och standardprefixet är 'x'. Utan INDATA, eller när INDATA är -, läses standardindata.

  Argumentet SIZE är ett heltal med en valfri enhet, till exempel är 10K 10*1024.
  Enheterna är K,M,G,T,P,E,Z,Y,R,Q, potenser av 1024, eller KB,MB och så vidare,
  potenser av 1000. Binära prefix kan också användas: KiB=K, MiB=M och så vidare.

  CHUNKS kan vara:

    - N dela upp i N filer baserat på indatans storlek
    - K/N skriv ut del K av N till standardutdata
    - l/N dela upp i N filer utan att dela rader eller poster
    - l/K/N skriv ut del K av N till standardutdata utan att dela rader eller poster
    - r/N som 'l', men använd fördelning i tur och ordning
    - r/K/N likadant, men skriv endast ut del K av N till standardutdata
split-error-cannot-read-from-input = { $input }: kan inte läsa från indata: { $error }
