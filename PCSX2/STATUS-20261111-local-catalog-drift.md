# PCSX2: lokal katalog avviker från verifierad Crowdin-status

Datum: 11 november 2026

Den lokala filen `pcsx2-qt_sv-SE.ts` kontrollerades inför nästa
kvalitetsgranskning. Den innehåller 4 057 meddelanden, varav 202 är markerade
`unfinished`. `l10n-lint` rapporterar därför 202 saknade översättningar, men
även 52 gränsteckenavvikelser, 45 procentmellanrumsvarningar, 27 lika
käll- och måltexter, 18 längdförhållanden och 8 konsekvensfynd.

Detta motsäger den senaste autentiserade Crowdin-kontrollen, som visar 5 313
av 5 313 översatta fraser i den aktiva svenska filen. Den lokala TS-filen är
alltså inte en tillräckligt aktuell källa för att skapa eller skicka en ny
deltafil. Inga översättningar har ändrats eller skickats i denna kontroll.

`svlang check --file` och Hunspell-SV på den fullständiga lokala katalogen
avbröts efter 30 sekunder utan resultat. De behöver köras mot en ny,
avgränsad export eller en mindre granskningsbatch. Detta är ett verktygs- och
inmatningsomfångsproblem, inte ett godkänt språktest.

Nästa steg är att hämta en färsk Crowdin-export, jämföra den mot denna
arkiverade fil och först därefter granska faktiska QA-fynd rad för rad.
