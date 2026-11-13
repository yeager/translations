# PCSX2: avstämning mellan TS- och XLIFF-export

Datum: 13 november 2026

Den nedladdade Qt TS-exporten och den samtidiga Crowdin-XLIFF-exporten har
jämförts rad för rad mot den tidigare granskade katalogen. Tio avvikelser
hittades i TS-filen: ett brutet HTML-avslut, ett em-streck för `--`, en
försämrad hjälptext för inmatningsprofiler, fem oavslutade grafiktexter,
en skadad installationsguide och en felaktig USB-översättning.

XLIFF-exporten innehåller redan de korrekta översättningarna för nio av
avvikelserna, inklusive de fem poster som TS-filen märker som oavslutade.
Den enda XLIFF-posten som behöver en import är därför USB-etiketten `B 1`:
`pcsx2-sv-usb-b1-regression-repair-20261113.xliff` (sträng-ID 7213).

Den lokala arbetskatalogen kompilerar med Qt `lrelease`: 5 297 färdiga och
0 oavslutade översättningar. XLIFF-filen är XML-validerad. l10n-lint har
0 fel; dess 149 varningar är exakt samma som i den tidigare granskade
basen. svlang ger endast katalogomfattande träffar från HTML, platshållare
och tekniska uttryck. Hunspell-SV godkänner de ändrade svenska fraserna;
katalogens övriga träffar består främst av filändelser, formatnamn och
produktnamn. `msgfmt --check` är inte tillämpligt på Qt TS eller XLIFF.
Diffkontroll och Gitleaks passerar för deltafilen.

Ingen import har gjorts i denna avstämning. Den verifierade XLIFF-exporten
visar att nio av tio korrigeringar redan finns upstream; endast sträng 7213
återstår att importera om Crowdin inte redan har uppdaterats sedan exporten.
Detta är lokal granskning och arkivering, inte ett upstream-inskick eller en
upstream-granskning.
