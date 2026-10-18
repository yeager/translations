# Ymir – Swedish main-menu localisation

- Scope: initial runtime localisation layer plus 65 Swedish main-menu strings.
- Locale selection reads `LC_ALL`, then `LC_MESSAGES`, then `LANG`; Swedish is selected for locale values beginning with `sv`. English remains the fallback.
- The patch adds the localisation source files to the `ymir-sdl3` CMake target and routes the translated menu labels through the lookup function.
- The upstream repository has no prior localisation framework or locale catalogs. Its remaining UI strings stay in English until they are routed through the same layer.
- `git diff --check`: clean.
- `svlang skrivregler`: no findings.
- Hunspell output was manually reviewed; no non-dictionary Swedish wording requires correction.
- Gitleaks scanned `apps/ymir-sdl3/src/app`: no leaks found.
