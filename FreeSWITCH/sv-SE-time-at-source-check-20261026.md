# Källkontroll av time/at och @

I FreeSWITCH-version `02857682b56626f06f72b91730415084b892bfee` spelar [mod_say_en.c](https://github.com/signalwire/freeswitch/blob/02857682b56626f06f72b91730415084b892bfee/src/mod/say/mod_say_en/mod_say_en.c) `time/at` mellan en datumangivelse och ett klockslag. Det talar för en tidsbetydelse i den engelska implementationen, exempelvis ”klockan” i en svensk fras, men fastställer inte hur en äldre eller extern svensk konfiguration använder filen.

Den granskade [mod_say_sv.c](https://github.com/signalwire/freeswitch/blob/02857682b56626f06f72b91730415084b892bfee/src/mod/say/mod_say_sv/mod_say_sv.c) anropar inte `time/at` direkt. Vid vanlig stavning använder den däremot `ascii/%d` för andra tecken än siffror; ASCII-värdet för @ är 64. Därför är `ascii/64` relevant för snabel-a vid stavning. Användaren tyckte att ett isolerat snabel-a-prov lät bra, men detta innebär inte att `time/at.wav` ska innehålla samma ord.

Nästa steg är att kontrollera faktisk svensk runtime och eventuella externa eller äldre flöden innan `time/at.wav` får ett slutligt manus. Den tidigare texten ”åt” är inte verifierad och bör inte anses godkänd enbart utifrån filnamnet.
