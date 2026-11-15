# OpenClaw – svenska native-etiketter

Den aktuella native-källan i `openclaw/openclaw:main` har 4 873 unika
översättningsnycklar. Svenska har 4 873 nycklar, utan tomma, saknade eller
extra värden vid kontroll 2026-11-15.

Projektet är aktivt: den senaste stabila utgåvan, `v2026.11.3`, publicerades
2026-11-10.

`openclaw-native-sv-status-labels-20261115.patch` kompletterar fyrtio
synliga etiketter som tidigare stod kvar på engelska. Ändringen omfattar
Färdigheter, sessionssökning, sessionshistorik, webbsökning, Git-incheckning,
pull-begäran, Stöd, anslutningsstatus och frånkopplad Gateway i Android- och
Apple-gränssnitten samt System (automatiskt) på macOS. Batchen omfattar också
de synliga verktygsnamnen sök, stäng, uppdatera, sessionsstatus, uppdatera mål,
vänta på agenter och skicka till session. Kodord, kommandon och produktnamn är
medvetet orörda.

`openclaw-ui-sv-core-labels-20261115.md` dokumenterar en liten batch för
Control UI:s översättningsminne. Den ersätter de gemensamma etiketterna
`Support`, `Skills`, `Auto` och `Trending` med Stöd, Färdigheter, Automatiskt
och Populära. Den förbättrar också formuleringar för ändringar och
heartbeat-övervakning och gör Git-terminologin konsekvent med den befintliga
svenska termen incheckning. Batchen omfattar nu även närvarolistan
`Online` → Anslutna och statusen `Offline` → Frånkopplad. De fyrtio
posterna används på sammanlagt 60 ställen i webbgränssnittet. Där skiljs också
inläsning av vyer och resurser från nedladdning av filer. I samma batch
normaliseras fjorton synliga förekomster av GitHub-termen pull request till
pull-begäran. Upstream-PR
[#199526](https://github.com/openclaw/openclaw/pull/199526) skapades
2026-11-15 och väntar på granskning. JSONL-filen parsar, de nya svenska
orden passerar Hunspell-sv och svlang bedömer de två senaste etiketterna utan
anmärkning. En fokuserad Gitleaks-kontroll av ändringarna hittade inga
hemligheter. `l10n-lint` stöder inte översättningsminnets JSONL-format och
räknas därför inte som en passerad kontroll. PR:en kräver fortfarande
skärmbildsbevis från ett byggt svenskt Control UI före merge.

Kontroller: JSON-parsning, Hunspell-sv, svlang för de enskilda tillagda
etiketterna och en fokuserad Gitleaks-kontroll av de nya värdena passerar.
Upstream-PR
[#199519](https://github.com/openclaw/openclaw/pull/199519) skapades
2026-11-15 och väntar på granskning. PR:ens kontroll för sammanhang och
underlag passerade efter att problemformulering och testunderlag lagts till.
Den aktuella PR-revisionen har resursverifierats i en isolerad arbetskopia:
`native:i18n:sync` och `native:i18n:verify` passerade för samtliga 4 873
native-nycklar utan motsägelser. Genereringen bekräftade Android-, Apple- och
84 InfoPlist-resurser, och de berörda svenska värdena finns i de genererade
Android-, iOS- och macOS-katalogerna.
Den övergripande statusen `openclaw/ci-gate` är fortfarande röd med den
generiska uppmaningen att CI måste slutföras. Den hänvisade körningen för
säkerhetsgranskning passerade. ClawSweeper har därefter begärt körningsbevis
från svenska Android- eller Apple-vyer före merge. I en isolerad arbetskopia
passerade `native:i18n:verify`, och den lokala resursgenereringen förde in
värdena i Android-, iOS- och macOS-resurserna. Ett lokalt macOS-bygge hann
inte starta kompileringen eftersom SwiftPM:s Node-probe avslutades av systemet.
Det är inte ett påstående om att den svenska UI-återgivningen har verifierats;
PR:n står därför kvar öppen för skärmbildsbevis.
