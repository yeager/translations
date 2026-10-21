test-after-help = Avsluta med den status som EXPRESSION bestämmer.

  En utelämnad EXPRESSION får standardvärdet falskt.
  I annat fall är EXPRESSION sant eller falskt och anger avslutningsstatusen.
  Det är ett av följande:

  ( EXPRESSION )
        EXPRESSION är sant

  ! EXPRESSION
        EXPRESSION är falskt

  EXPRESSION1 -a EXPRESSION2
        både EXPRESSION1 och EXPRESSION2 är sanna

  EXPRESSION1 -o EXPRESSION2
        antingen EXPRESSION1 eller EXPRESSION2 är sant

  Strängåtgärder:

  -n STRING
        längden på STRING är skild från noll

  STRING
        motsvarar -n STRING

  -z STRING
        längden på STRING är noll

  STRING1 = STRING2
        strängarna är lika

  STRING1 != STRING2
        strängarna är olika

  STRING1 > STRING2
        STRING1 är större än STRING2 i den aktuella språkversionen

  STRING1 < STRING2
        STRING1 är mindre än STRING2 i den aktuella språkversionen

  Heltalsjämförelser:

  INTEGER1 -eq INTEGER2
        INTEGER1 är lika med INTEGER2

  INTEGER1 -ge INTEGER2
        INTEGER1 är större än eller lika med INTEGER2

  INTEGER1 -gt INTEGER2
        INTEGER1 är större än INTEGER2

  INTEGER1 -le INTEGER2
        INTEGER1 är mindre än eller lika med INTEGER2

  INTEGER1 -lt INTEGER2
        INTEGER1 är mindre än INTEGER2

  INTEGER1 -ne INTEGER2
        INTEGER1 är inte lika med INTEGER2

  Filåtgärder:

  FILE1 -ef FILE2
        FILE1 och FILE2 har samma enhetsnummer och inodnummer

  FILE1 -nt FILE2
        FILE1 är nyare, ändringsdatum, än FILE2

  FILE1 -ot FILE2
        FILE1 är äldre än FILE2

  -b FILE
        FILE finns och är en blockspecialfil

  -c FILE
        FILE finns och är en teckenspecialfil

  -d FILE
        FILE finns och är en katalog

  -e FILE
        FILE finns

  -f FILE
        FILE finns och är en vanlig fil

  -g FILE
        FILE finns och har set-group-ID

  -G FILE
        FILE finns och ägs av effektivt grupp-ID

  -h FILE
        FILE finns och är en symbolisk länk, samma som -L

  -k FILE
        FILE finns och har stickybiten angiven

  -L FILE
        FILE finns och är en symbolisk länk, samma som -h

  -N FILE
        FILE finns och har ändrats sedan den senast lästes

  -O FILE
        FILE finns och ägs av effektivt användar-ID

  -p FILE
        FILE finns och är ett namngivet rör

  -r FILE
        FILE finns och läsbehörighet har beviljats

  -s FILE
        FILE finns och har en storlek större än noll

  -S FILE
        FILE finns och är en socket

  -t FD
        filbeskrivaren FD är öppnad på en terminal

  -u FILE
        FILE finns och dess set-user-ID-bit är angiven

  -w FILE
        FILE finns och skrivbehörighet har beviljats

  -x FILE
        FILE finns och körbehörighet eller sökbehörighet har beviljats

  Med undantag för -h och -L derefererar, följer, alla filrelaterade tester symboliska länkar.
  Observera att parenteser måste skyddas, till exempel med omvänt snedstreck, i skal.
  INTEGER kan också vara -l STRING, vilket beräknas till längden på STRING.

  OBS: Binära -a och -o är i sig tvetydiga.
  Använd test EXPR1 && test EXPR2 eller test EXPR1 || test EXPR2 i stället.

  OBS: {"["} hanterar flaggorna --help och --version, men test gör det inte.
  test behandlar dem som vilken annan sträng STRING som helst som inte är tom.

  OBS: Ditt skal kan ha en egen version av test eller {"["}, som vanligtvis har företräde
  framför versionen som beskrivs här. Läs skalets dokumentation för uppgifter
  om de flaggor som versionen stöder.

  Fel rapporteras med uttrycket återgivet och en cirkumflex under det felaktiga
  argumentet när standardfel är en terminal. Allt annat som läser standardfel
  får det vanliga enradsmeddelandet.
