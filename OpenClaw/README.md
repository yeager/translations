# OpenClaw – svenska native-etiketter

Den aktuella native-källan i `openclaw/openclaw:main` har 4 873 unika
översättningsnycklar. Svenska har 4 873 nycklar, utan tomma, saknade eller
extra värden vid kontroll 2026-11-15.

Projektet är aktivt: den senaste stabila utgåvan, `v2026.11.3`, publicerades
2026-11-10.

`openclaw-native-sv-status-labels-20261115.patch` kompletterar tio synliga
etiketter som tidigare stod kvar på engelska. Ändringen omfattar
Färdigheter, Stöd, anslutningsstatus och frånkopplad Gateway i Android- och
Apple-gränssnitten samt System (automatiskt) på macOS. Kodord, kommandon och
produktnamn är medvetet orörda.

`openclaw-ui-sv-core-labels-20261115.md` dokumenterar en liten batch för
Control UI:s översättningsminne. Den ersätter de gemensamma etiketterna
`Support`, `Skills`, `Auto` och `Trending` med Stöd, Färdigheter, Automatiskt
och Populära. Den förbättrar också formuleringar för ändringar och
heartbeat-övervakning och gör Git-terminologin konsekvent med den befintliga
svenska termen incheckning. De femton posterna används på sammanlagt 34
ställen i webbgränssnittet. Upstream-PR
[#199526](https://github.com/openclaw/openclaw/pull/199526) skapades
2026-11-15 och väntar på granskning. PR:ens kontroll för sammanhang och
underlag passerar. Även här är den övergripande statusen `openclaw/ci-gate`
röd med en generell CI-spärr, medan gransknings- och säkerhetskontrollerna
passerar.

Kontroller: JSON-paritet, `git diff --check`, svlang, Hunspell-sv,
l10n-lint och Gitleaks passerar. Upstream-PR
[#199519](https://github.com/openclaw/openclaw/pull/199519) skapades
2026-11-15 och väntar på granskning. PR:ens kontroll för sammanhang och
underlag passerade efter att problemformulering och testunderlag lagts till.
Den övergripande statusen `openclaw/ci-gate` är fortfarande röd med den
generiska uppmaningen att CI måste slutföras. Den hänvisade körningen för
säkerhetsgranskning passerade, men någon separat testkörning för denna
katalogändring startades inte.
