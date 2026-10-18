# Ymir – Swedish main menu and debugging localisation

- Scope: initial runtime localisation layer plus 96 Swedish strings for the main menu and debugging menus.
- The patch preserves ImGui identifiers such as `##vdp1` and leaves all untranslated labels in English through the fallback path.
- Swedish is selected for locale values beginning with `sv`; English is the fallback.
- `git diff --check`: clean.
- `svlang skrivregler`: no findings.
- Hunspell output was manually reviewed; remaining terms are hardware acronyms and technical vocabulary.
- Gitleaks scanned `apps/ymir-sdl3/src/app`: no leaks found.
