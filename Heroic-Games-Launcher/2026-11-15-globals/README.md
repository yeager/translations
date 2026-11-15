# Heroic Games Launcher – Globals, batch 001

- Datum: 2026-11-15
- Källa: Heroic Games Launcher `main`, `public/locales/en/translation.json`
- Weblate-komponent: `heroic-games-launcher/globals`, svenska
- Omfattning: 40 saknade strängar och 4 tidigare fuzzy-strängar (44 unika Weblate-enheter)
- Status: uppladdad och återläst 2026-11-15. Weblate rapporterar 863 översatta strängar och 0 fuzzy-strängar av 1 096.

Terminologi följer projektets `TERMINOLOGI-sv.md`. Produktnamn och tekniska namn som Heroic, Steam, GOG, Proton, DXVK, D7VK, NVIDIA, OpenGL, Vulkan, API, URL och SteamGridDB har bevarats. Platshållaren `{{age}}` och formatet `NYCKEL=VÄRDE` har kontrollerats mot källan.

Kontroller: `jq empty`, `l10n-lint`, `git diff --check` och `gitleaks detect --no-git --redact` passerade. `msgfmt` är inte tillämpligt för i18next-JSON. Hunspell kördes inte eftersom dess CPU-belastning uttryckligen är begränsad i det här arbetet.
