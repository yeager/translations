cut-about = Extrahera delar från varje rad i filer.
cut-after-help = Om ingen FIL anges läses standardindata. Använd '-' som FIL argument för att inkludera standardindata.

  LIST är en kommaseparerad lista med tal eller intervall:

    N           endast kolumn N
    N-          kolumner från N till radens slut
    N-M         kolumner från N till M
    -M          kolumner från 1 till M

  Exempel:

    cut -f 2,5-7 file.txt             extrahera fält 2, 5, 6 och 7
    cut -f 3- file.txt                extrahera fält 3 till radens slut
    cut --complement -f 4-6 file.txt  extrahera alla fält utom 4, 5 och 6
    cut -d',' -f1 file.csv            extrahera första fältet från en CSV
cut-help-delimiter = använd DELIM som fältavgränsare, standardvärdet är tabulator
cut-help-whitespace-delimited = använd valfria blanktecken, mellanslag eller tabulator, som avgränsare; ignorera inledande och avslutande blanksteg med 'trimmed'
cut-error-write-error = fel vid skrivning
