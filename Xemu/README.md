# Xemu – PR #2837

Uppströms-PR: <https://github.com/xemu-project/xemu/pull/2837>

Den 26 oktober 2026 kompletterades grenen `i18n-sv-xui` med commit
`03e0e9a6a3`, som behandlar de kvarvarande paketeringsproblemen för den nya
gettext-baserade XUI-lokaliseringen:

- uppdateraren kan skapa kataloger och föräldrakataloger när den extraherar
  framtida paket;
- Windows-paketen hålls platta under övergången, så redan utgivna uppdaterare
  inte avbryts av katalogposter i ZIP-filen;
- katalogbygget är fortsatt valfritt när gettext inte finns.

Kontroller: `bash -n build.sh`, `git diff --check` och avgränsad
Gitleaks-kontroll godkända. Full lokal byggning kräver beroenden som inte
finns i denna miljö; `clang-format` saknas också lokalt.

2026-10-27: Uppströmskontrollen är arkiverad i
`upstream-check-20261027.md`.

2026-10-29: CI visade att Debianpaketeringen försökte installera `.mo`-filer
utan att katalogmålet byggdes. Commit `fd9af4c93a` gör gettext till ett
uttalat byggberoende, bygger katalogmålet via den valda byggbackendens
Make-ingång och inkluderar katalogerna i Windows-, macOS- och Debianpaket.
Exakt patch finns i `xemu-pr-2837-catalog-shipping-20261029.patch`.
Kontroller: `bash -n build.sh`, `msgfmt --check-format --check-domain`,
`l10n-lint`, `svlang skrivregler`, diffkontroll och avgränsad
Gitleaks-kontroll godkända. PR:n väntar på ny CI och underhållargranskning.

Samma dag skapades CI-körningen för `fd9af4c93a`, men GitHub avslutade den
innan några jobb startade med statusen `action_required`. En underhållare i
`xemu-project/xemu` måste godkänna arbetsflödeskörning från forken innan den
kan ge CI-resultat.

2026-11-16: PR:n var öppen med två nya granskningsanmärkningar och sattes
till utkast under rättningen. Commit `a5d7eac` isolerar XUI i gettext-domänen
`xemu`: Meson bygger `xemu-gmo`, paketeringen installerar `xemu.mo` och
XUI binder till samma domän. Därmed kolliderar katalogen inte med QEMU:s
`qemu.mo` i Debian. Den C-specifika deklarationsheadern `qemu/cutils.h` har
också tagits bort från det C++-inkluderade `common.hh`; den enda nödvändiga
deklarationen finns lokalt i `main.cc`. Patchen är arkiverad i
`xemu-pr-2837-dedicated-catalog-domain-20261116.patch`.

Kontroller: `msgfmt --check-format --check-domain`, `bash -n build.sh`,
`git diff --check`, Gitleaks, byggmålet `xemu-gmo` och kompilering av
`ui_xui_main.cc.o` godkända lokalt. Ändringen är pushad till PR-grenen;
CI och underhållargranskning är fortfarande separata, overifierade steg.

NXEMU #489 granskades samtidigt. Underhållaren flyttar gränssnittet till
RmlUi och vill därefter använda `.po`-filer med språkval; ingen ytterligare
ändring är lämplig på den nuvarande PR:n.
