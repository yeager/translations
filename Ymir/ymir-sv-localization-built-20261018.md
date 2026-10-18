# Ymir: svensk lokalisering, byggkontrollerad sats

Den lokala Ymir-patchen innehåller de svenska gränssnittstexter som har arbetats fram hittills, inklusive inställningsflikar, uppdaterings- och välkomstdialoger, inmatningsfångst samt centrala videoreglage.

- Källkontroll: `git diff --check` utan fel.
- Säkerhetskontroll: Gitleaks utan träffar i `apps/ymir-sdl3/src/app`.
- Byggkontroll: `cmake --preset a64-Clang-Debug-MacOS` och `cmake --build ... --target ymir-sdl3 -j 1` passerade.
- Länkaren rapporterade endast projektets befintliga dubblettlänkbibliotek för SDL3, zlib och zstd.
- Patchen är en full, lokal Ymir-diff och är inte skickad uppströms.
