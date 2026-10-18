# Ymir – Swedish UI localisation

- Scope: runtime localisation layer plus 109 Swedish strings for the main, debugging and GUI-settings menus.
- The implementation uses the existing `app::ui` namespace and is included in the `ymir-sdl3` CMake target.
- Swedish activates for `LC_ALL`, `LC_MESSAGES` or `LANG` locale values beginning with `sv`; all other UI strings fall back to English.
- ImGui identifiers such as `##vdp1` and format placeholders are preserved.
- `git diff --check`: clean.
- `svlang skrivregler`: no findings.
- Hunspell output was manually reviewed; remaining tokens are format specifiers, abbreviations and hardware terms.
- Gitleaks scanned `apps/ymir-sdl3/src/app`: no leaks found.

This patch supersedes the earlier Ymir menu snapshots from the same date.
