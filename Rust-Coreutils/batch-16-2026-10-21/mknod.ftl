mknod-after-help = Obligatoriska argument till långa flaggor är obligatoriska även för korta flaggor.
  -m, --mode=MODE ställ filbehörighetsbitar till MODE, inte a=rw - umask

  Både MAJOR och MINOR måste anges när TYPE är b, c eller u, och de måste
  utelämnas när TYPE är p. Om MAJOR eller MINOR börjar med 0x eller 0X tolkas
  värdet som hexadecimalt, annars som oktalt om det börjar med 0 och annars
  som decimalt. TYPE kan vara:

    - b skapa en blockbaserad specialfil med buffring
    - c, u skapa en teckenbaserad specialfil utan buffring
    - p skapa en FIFO

  OBS: Ditt skal kan ha en egen version av mknod som vanligtvis har företräde
  framför versionen som beskrivs här. Läs skalets dokumentation för uppgifter
  om de flaggor som versionen stöder.
