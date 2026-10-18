# Ymir: svenska texter för backupminne

Den lokala Ymir-patchen utökar svenska texter för backupminnesvyn med åtgärder, tabellrubriker och bekräftelser.

- Källkontroll: `git diff --check` utan fel.
- Språkkontroll: svlang utan skrivregelfel; Hunspell träffade inga ord i den granskade satsen.
- Säkerhetskontroll: Gitleaks utan träffar.
- Byggkontroll: `cmake --build out/build/a64-Clang-Debug-MacOS --target ymir-sdl3 -j 1` passerade.
- Patchen är en full, lokal Ymir-diff och är inte skickad uppströms.
