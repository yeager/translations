pr-help-double-space =
  Skapa utdata med dubbelt radavstånd. Ett extra tecken `<newline>` skrivs ut
                  efter varje `<newline>` i indata.
pr-help-number-lines =
  Ange radnumrering med width siffror. Om width inte anges är standardvärdet
                  5. Numret upptar de första width kolumnpositionerna i varje textkolumn
                  eller varje rad i utdata med -m. Om char, ett valfritt tecken som inte
                  är en siffra, anges läggs det till radnumret för att skilja det från det
                  som följer. Standardvärdet för char är tecknet `<tab>`. Radnummer som är
                  längre än width kolumner avkortas.
pr-help-form-feed =
  Använd `<form-feed>` för nya sidor i stället för standardbeteendet som
                  använder en följd av `<newline>`.
pr-help-across =
  Ändra funktionen för flaggan -COLUMN så att kolumner fylls på tvären över
                  sidan i turordning. När column till exempel är 2 blir den första
                  indataraden den första raden i kolumn 1, den andra indataraden den första
                  raden i kolumn 2 och den tredje indataraden den andra raden i kolumn 1.
pr-help-column-char-separator =
  Avgränsa textkolumner med det enskilda tecknet char i stället för lämpligt
                  antal `<space>`s. Standardvärdet för char är tecknet `<tab>`.
pr-help-column-string-separator =
  avgränsa kolumner med STRING,
                  utan -S: standardavgränsaren är `<TAB>` med -J och `<space>`
                  annars, samma som -S\" \", påverkar inte kolumnflaggor
pr-help-indent =
  Varje utdatarad ska föregås av offset `<space>`s. Om flaggan -o inte
                  anges är standardvärdet för offset noll. Det upptagna utrymmet kommer
                  utöver utdataradens bredd, se flaggan -w nedan.
