# Heroic Games Launcher – Globals, batch 001

- Datum: 2026-11-15
- Källa: Heroic Games Launcher `main`, `public/locales/en/translation.json`
- Weblate-komponent: `heroic-games-launcher/globals`, svenska
- Omfattning: 40 saknade strängar och 4 tidigare fuzzy-strängar (44 unika Weblate-enheter)
- Status: uppladdad och återläst 2026-11-15. Weblate rapporterar 863 översatta strängar och 0 fuzzy-strängar av 1 096.

Terminologi följer projektets `TERMINOLOGI-sv.md`. Produktnamn och tekniska namn som Heroic, Steam, GOG, Proton, DXVK, D7VK, NVIDIA, OpenGL, Vulkan, API, URL och SteamGridDB har bevarats. Platshållaren `{{age}}` och formatet `NYCKEL=VÄRDE` har kontrollerats mot källan.

Kontroller: `jq empty`, `l10n-lint`, `git diff --check` och `gitleaks detect --no-git --redact` passerade. `msgfmt` är inte tillämpligt för i18next-JSON. Hunspell kördes inte eftersom dess CPU-belastning uttryckligen är begränsad i det här arbetet.

## Batch 002

- Omfattning: 27 saknade strängar för NVIDIA/AMD-grafik, handkontroller, Steam-genvägar, tomt spelbibliotek, tillgänglighet och hämtningshanteraren.
- Status: uppladdad och återläst 2026-11-15. Weblate rapporterar 890 översatta strängar, 0 fuzzy-strängar och 1 096 totalt.
- Särskilt kontrollerat: i18next-markupen `<0>…</0>`, platshållaren `{{game}}`, två svenska pluralformer för `{{count}}` samt tekniska produktnamn.

## Batch 003

- Omfattning: 47 saknade strängar för experimentella funktioner, Wine/Proton, prefix, cacher, körtidsmiljöer och inställningsavsnitt.
- Status: uppladdad och återläst 2026-11-15. Weblate rapporterar 937 översatta strängar, 0 fuzzy-strängar och 1 096 totalt.
- Särskilt kontrollerat: `{{numOfCores}}`, `{{percentUsed}}` och `{{usedGib}}`/`{{totalGib}}`, samt bevarande av Wine, Proton, CrossOver, BattlEye och EasyAntiCheat.

## Batch 004

- Omfattning: 36 saknade strängar för GOG-affiliatlänkar, grafik- och prestandaalternativ, Steam-genvägar, itch.io-installationsprogram och inmatning i webbvyn.
- Status: uppladdad och återläst 2026-11-15. Weblate rapporterar 973 översatta strängar, 0 fuzzy-strängar och 1 096 totalt.
- Särskilt kontrollerat: `{{title}}`, `{{exe}}` och `{{path}}`; bevarade tekniska namn och formatering för AVX, Rosetta, DirectX, Vulkan, DXVK, DLSS, UMU, HTTPS, CDN, eventfd, futex, Wayland, HDR och MangoHud.

## Batch 005

- Omfattning: 43 saknade strängar för stödvyn, donationsformer, Steam-molnsparning och återställning vid fel.
- Status: uppladdad och återläst 2026-11-15. Weblate rapporterar 1 016 översatta strängar, 0 fuzzy-strängar och 1 096 totalt.
- Särskilt kontrollerat: båda svenska pluralformerna, `{{game}}`, `{{files}}` och `{{details}}`, samt bevarande av Steam, GOG, GitHub, Ko-fi, Patreon och PayPal.
