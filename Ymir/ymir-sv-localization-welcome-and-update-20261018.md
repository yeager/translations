# Ymir: svensk översättning av välkomst- och uppdateringsdialoger

Den lokala Ymir-patchen utökar den svenska översättningen med välkomstflödet för IPL-ROM-filer och dialogen för automatiska uppdateringskontroller.

- Svenskt språkläge väljs via `LC_ALL`, `LC_MESSAGES` eller `LANG` med prefixet `sv`.
- Kontroll av källändringarna: `git diff --check` utan fel, svlang utan skrivregelfel och Gitleaks utan träffar.
- Hunspell träffade endast projekt- och tekniktermerna `Ymir` och `IPL-ROM`.
- CMake-konfigurering kan inte köras i den lokala klonen eftersom den saknar `vcpkg/scripts/buildsystems/vcpkg.cmake` och Ninja.
- Patchen är en full, lokal Ymir-diff och är inte skickad uppströms.
