# OpenClaw – svenska native-etiketter

Den aktuella native-källan i `openclaw/openclaw:main` har 4 873 unika
översättningsnycklar. Svenska har 4 873 nycklar, utan tomma, saknade eller
extra värden vid kontroll 2026-11-15.

`openclaw-native-sv-status-labels-20261115.patch` kompletterar tio
användarvända etiketter som tidigare stod kvar på engelska. Ändringen omfattar
Färdigheter, Stöd, anslutningsstatus och frånkopplad Gateway i Android- och
Apple-gränssnitten samt System (automatiskt) på macOS. Kodord, kommandon och
produktnamn är medvetet orörda.

Kontroller: JSON-paritet, `git diff --check`, svlang, Hunspell-sv,
l10n-lint och Gitleaks passerar. Upstream-PR
[#199519](https://github.com/openclaw/openclaw/pull/199519) skapades
2026-11-15 och väntar på granskning. PR:ens kontroll för sammanhang och
underlag passerade efter att problemformulering och testunderlag lagts till.
Den övergripande statusen `openclaw/ci-gate` är fortfarande röd med den
generiska uppmaningen att CI måste slutföras. Den hänvisade körningen för
säkerhetsgranskning passerade, men någon separat testkörning för denna
katalogändring startades inte.
