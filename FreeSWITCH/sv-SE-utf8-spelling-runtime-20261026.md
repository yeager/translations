# FreeSWITCH: runtimekontroll av svensk stavning

## Miljö och omfattning

Den 26 oktober 2026 användes Homebrew FreeSWITCH 1.11.3 på macOS. Den svenska talmodulen byggdes från `mod_say_sv.c` vid FreeSWITCH-head `02857682b56626f06f72b91730415084b892bfee`. En tillfällig testfunktion lades till i en lokal kopia för att anropa modulens befintliga `sv_say_string` med stavningsläget och visa filsträngen. FreeSWITCH kördes isolerat med SQL och automatisk NAT avstängda. Detta är ett riktigt modulanrop, men ingen telefonanslutning och ingen uppspelning av ljudfiler.

## Resultat före korrigering

- `a@b` gav `ascii/97.wav`, `ascii/64.wav`, `ascii/98.wav`.
- UTF-8-texten `åäö` gav sex negativa filnummer: `-61`, `-91`, `-61`, `-92`, `-61`, `-74`. Dessa motsvarar bytevis behandling av tre tvåbytes-tecken och matchar inte paketets svenska filer.
- `q` gav `ascii/113.wav`.

## Lokalt korrigeringsförslag

[Patchen](proposed-swedish-utf8-spelling.patch) känner igen UTF-8 för både gemener och versaler av å, ä och ö och väljer paketets befintliga ID:n 134, 132 och 148. Övriga bytes ges som unsigned char till `tolower`. Korrigeringen har bara tillämpats i testkopian och är inte uppladdad eller införd i FreeSWITCH.

Med testkopian gav `åäöÅÄÖ` filnumren `134, 132, 148, 134, 132, 148`; `a@b` gav fortsatt `97, 64, 98`. Testet visar filval för dessa strängar, inte att ljudfilerna finns i ett installerat paket eller låter rätt. Särskilt `ascii/64.wav` behöver ingå i paketet för att @-testet ska kunna spelas upp.

Kvar: granska hanteringen av andra icke-ASCII-tecken och äldre teckenkodningar, verifiera mot den aktuella konfigurationen och utför riktig uppspelning och regressionstest. Patchen ska inte betraktas som allmän Unicode-hantering.

Patchen har dessutom applicerats med `git apply --unidiff-zero` på en ren kopia av den angivna källversionen och den resulterande modulen har kompilerats mot FreeSWITCH 1.11.3. Detta är ett separat byggprov; det ändrar inte runtime-testets begränsningar ovan.
