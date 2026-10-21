dd-after-help = Operander:

  - bs=BYTES : läs och skriv upp till BYTES byte åt gången, standardvärdet är 512; skriver över ibs och obs.
  - cbs=BYTES : konverteringsblockstorleken i byte. Gäller operationerna conv=block och conv=unblock.
  - conv=CONVS : en kommaseparerad lista med konverteringsflaggor eller, av historiska skäl, filflaggor.
  - count=N : sluta läsa indata efter N ibsstora läsningar i stället för att fortsätta till EOF. Se iflag=count_bytes om det är bättre att sluta efter N byte.
  - ibs=N : storleken på bufferten som används för läsning, standardvärdet är 512
  - if=FILE : filen som används för indata. Om den inte anges används stdin.
  - iflag=FLAGS : en kommaseparerad lista med indataflaggor som anger hur indatakällan behandlas. FLAGS kan vara någon av indataflaggorna eller de allmänna flaggorna nedan.
  - skip=N, eller iseek=N : hoppa över N ibsstora poster i indata innan kopiering eller konvertering påbörjas. Se iflag=skip_bytes om det är bättre att söka N byte.
  - obs=N : storleken på bufferten som används för skrivning, standardvärdet är 512
  - of=FILE : filen som används för utdata. Om den inte anges används stdout.
  - oflag=FLAGS : en kommaseparerad lista med utdataflaggor som anger hur utdatakällan behandlas. FLAGS kan vara någon av utdataflaggorna eller de allmänna flaggorna nedan.
  - seek=N, eller oseek=N : sök N obsstora poster i utdata innan kopiering eller konvertering påbörjas. Se oflag=seek_bytes om det är bättre att söka N byte.
  - status=LEVEL : avgör om volym och prestandastatistik skrivs till stderr.

    Om den inte anges skriver dd ut statistik när arbetet är klart. Ett exempel visas nedan.

      6+0 poster in
      16+0 poster ut
      8192 byte, 8,2 kB och 8,0 KiB, kopierade, 0,00057009 s,
      14,4 MB/s

    De två första raderna är volymstatistik och den sista raden är prestandastatistik. Volymstatistiken anger antalet fullständiga och partiella ibsstora läsningar eller obsstora skrivningar som utfördes under kopieringen. Volymstatistikens format är <fullständig>+<partiell>. Om poster har avkortats, se conv=block, innehåller volymstatistiken antalet avkortade poster.

    Möjliga värden för LEVEL är:
      - progress : skriv ut regelbunden prestandastatistik medan kopieringen pågår.
      - noxfer : skriv ut slutlig volymstatistik, men inte prestandastatistik.
      - none : skriv inte ut någon statistik.

    Prestandastatistik skrivs också ut när signalen INFO, om den stöds, eller signalen USR1 tas emot. Om miljövariabeln POSIXLY_CORRECT sätts till ett valfritt värde, även ett tomt värde, ignoreras signalen USR1.

  Konverteringsflaggor:

  - ascii : konvertera från EBCDIC till ASCII. Detta är motsatsen till flaggan ebcdic. Innebär conv=unblock.
  - ebcdic : konvertera från ASCII till EBCDIC. Detta är motsatsen till flaggan ascii. Innebär conv=block.
  - ibm : konvertera från ASCII till EBCDIC och tillämpa konventionerna för [, ] och ~ som anges i POSIX. Innebär conv=block.
  - ucase : konvertera gemener till versaler.
  - lcase : konvertera versaler till gemener.
  - block : ta bort nyraden för varje rad som är kortare än storleken som cbs=BYTES anger och fyll ut med blanksteg till cbs. Rader längre än cbs avkortas.
  - unblock : ta bort avslutande blanksteg för varje indatablock med storleken som cbs=BYTES anger och ersätt dem med ett nyradstecken.
  - sparse : försök att söka i utdata när ett obsstort block endast består av nollor.
  - swab : byt plats på varje par av intilliggande byte. Om antalet byte är udda utelämnas den sista byten.
  - sync : fyll ut varje ibsstort block med nollor. Om block eller unblock anges fylls det i stället ut med blanksteg.
  - excl : utdatafilen måste skapas. Misslyckas om utdatafilen redan finns.
  - nocreat : utdatafilen skapas inte. Misslyckas om utdatafilen inte redan finns.
  - notrunc : utdatafilen avkortas inte. Om denna flagga inte anges avkortas utdata när filen öppnas.
  - noerror : ignorera alla läsfel. Om denna flagga inte anges ignorerar dd endast Error::Interrupted.
  - fdatasync : data skrivs innan programmet avslutas.
  - fsync : data och metadata skrivs innan programmet avslutas.

  Indataflaggor:

  - count_bytes : ett värde för count=N tolkas som byte.
  - skip_bytes : ett värde för skip=N tolkas som byte.
  - fullblock : vänta på ibs byte vid varje läsning. Läsningar med längden noll betraktas fortfarande som EOF.

  Utdataflaggor:

  - append : öppna filen i läget append. Överväg att också ange conv=notrunc.
  - seek_bytes : ett värde för seek=N tolkas som byte.

  Allmänna flaggor:

  - direct : använd direkt I/O för data.
  - directory : misslyckas om inte den angivna indatan, om den används som iflag, eller utdatan, om den används som oflag, är en katalog.
  - dsync : använd synkroniserad I/O för data.
  - sync : använd synkroniserad I/O för data och metadata.
  - nonblock : använd icke blockerande I/O.
  - noatime : uppdatera inte åtkomsttiden.
  - nocache : begär att operativsystemet släpper cacheminnet.
  - noctty : tilldela ingen styrande tty.
  - nofollow : följ inte symboliska länkar.
