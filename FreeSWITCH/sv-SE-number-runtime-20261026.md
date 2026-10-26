# Svenska tal: runtimekontroll av filval

Den 26 oktober 2026 kördes Homebrew FreeSWITCH 1.11.3 isolerat på macOS med en lokal testkopia av `mod_say_sv.c` från PR #3243, head `02857682b56626f06f72b91730415084b892bfee`. Testkopian har en extra API-funktion som anropar modulens `sv_say_string` med typen `SST_NUMBER`, metoden `SSM_PRONOUNCED` och filändelsen `wav`. Den innehåller även den separata lokala UTF-8-korrigeringen för stavning. Testet visar modulens genererade filsträng, inte ljuduppspelning.

| Indata | Valda filer i ordning |
|---|---|
| 21 | `digits/20.wav`, `digits/n-1.wav` |
| 100 | `digits/n-1.wav`, `digits/100.wav` |
| 1001 | `digits/n-1.wav`, `digits/tusen.wav`, `digits/n-1.wav` |
| 12345 | `digits/12.wav`, `digits/tusen.wav`, `digits/3.wav`, `digits/100.wav`, `digits/40.wav`, `digits/5.wav` |
| 1000000 | `digits/u-1.wav`, `digits/miljon.wav` |
| 2000000 | `digits/2.wav`, `digits/miljoner.wav` |

Detta bekräftar filvalet för dessa sex tal, inklusive singular och plural för miljoner. Det bevisar inte att filerna finns i ett installerat paket, har rätt uttal eller ger naturlig rytm när de spelas upp. Andra tal, genus, räkneord och datum behöver också kontrolleras. Uppstarten rapporterade saknade `CORE_PCM_MODULE` och `CORE_SPEEX_MODULE`; därför kan detta prov inte användas som bevis för fungerande ljuduppspelning.
