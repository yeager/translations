# Källkontroll: introduktion till röstbrevlådan

Kontrollerad FreeSWITCH-version: `02857682b56626f06f72b91730415084b892bfee`.

Det engelska frasregistret `docs/phrase/phrase_en.xml` innehåller `vm-tutorial_yes_no.wav`. Där leder knapp 1 till introduktion och inställning av röstbrevlådan, medan knapp 2 hoppar över. Det svenska utkastet för `voicemail/vm-valkommen-introduktion.wav` uttrycker inte gränsen mellan dessa val tillräckligt tydligt.

Förslag till svenskt manus, under förutsättning att filen används för samma funktion:

> Välkommen till din nya röstbrevlåda. För att lyssna på en introduktion och ställa in din röstbrevlåda, tryck 1. För att hoppa över, tryck 2.

Kopplingen mellan de två filnamnen är inte bevisad. `vm-valkommen-introduktion` saknas i det tidigare granskade svenska `sounds.xml`, och den kontrollerade `mod_voicemail.c` innehåller ingen träff på `tutorial`. Andra moduler, konfigurationer eller äldre flöden kan ändå använda filen. Förslaget är därför ett manusutkast, inte en fastställd filkoppling eller ett godkänt ljud.

Källor: [engelskt frasregister](https://github.com/signalwire/freeswitch/blob/02857682b56626f06f72b91730415084b892bfee/docs/phrase/phrase_en.xml), [svenska röstbrevlådemakron](https://github.com/signalwire/freeswitch/blob/02857682b56626f06f72b91730415084b892bfee/conf/vanilla/lang/sv/vm/sounds.xml), [mod_voicemail.c](https://github.com/signalwire/freeswitch/blob/02857682b56626f06f72b91730415084b892bfee/src/mod/applications/mod_voicemail/mod_voicemail.c).
