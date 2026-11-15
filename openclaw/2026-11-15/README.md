# OpenClaw – svenska native-etiketter

Den aktuella native-källan i `openclaw/openclaw:main` har 4 873 unika
översättningsnycklar. Svenska har 4 873 nycklar, utan tomma, saknade eller
extra värden vid kontroll 2026-11-15.

Projektet är aktivt: den senaste stabila utgåvan, `v2026.11.3`, publicerades
2026-11-10.

`openclaw-native-sv-status-labels-20261115.patch` kompletterar hundratjugoen
synliga etiketter som tidigare stod kvar på engelska. Ändringen omfattar
Färdigheter, sessionssökning, sessionshistorik, webbsökning, Git-incheckning,
pull-begäran, Stöd, anslutningsstatus och frånkopplad Gateway i Android- och
Apple-gränssnitten samt System (automatiskt) på macOS. Batchen omfattar också
de synliga verktygsnamnen sök, stäng, uppdatera, sessionsstatus, uppdatera mål,
vänta på agenter och skicka till session. Den senaste batchen täcker också
vanliga verktygsnamn, bland annat fäst, importera, ange grupper, roller,
avisera, verktygsanrop, hämta mål, röst, skärmbild, dator, bifoga och
händelser. Även synliga åtgärder för uppgifter, media och konversationer är
nu på svenska, exempelvis fråga användaren, avfärda uppgift, konsol, lägg till,
föreslå uppgift, kameraklipp, videogenerering, mobilgränssnitt och
transkriptioner. Den senaste batchen kompletterar vanliga åtgärder för
starta, avsluta, godkänna, generera, spara, köra, skapa mål, publicera på
GitHub, behörigheter och strukturerat resultat. Batchen omfattar nu också
hämta minne, bildgenerering, ladda upp, hantera roller, visa bild, spela in
skärm, skärmavbildning och tidsgräns. Kodord, kommandon och produktnamn är
medvetet orörda.

En uppföljande native-batch omfattar trettionio systemetiketter i Android-, Apple-
och macOS-gränssnitten: Kodkörning, Tillägg, INCHECKNING, Ansluten och
Frånkopplad samt Få stöd. Statusfraserna har granskats i respektive
källkodsvy; det befintliga tankstrecket i den engelska källtexten har
behållits i den svenska frånkopplingsfrasen. Den omfattar även verktygsetiketterna
Kameralista, PTZ-kamera, Närvaro och Underagent. Den omfattar även de synliga
verktygsnamnen kanal, redigera, emojilista, skapa händelse, omröstning,
presentera, reaktioner, klistermärke, stoppa, flikar, skapa tråd och väck.
De synliga anslutningsetiketterna och räknarna använder dessutom nu Ansluten,
Frånkopplad och anslutna i stället för online och offline.
Sessionsvyn använder också ändring och ändringsjämförelse i stället för patch.

`openclaw-ui-sv-core-labels-20261115.md` dokumenterar en liten batch för
Control UI:s översättningsminne. Den ersätter de gemensamma etiketterna
`Support`, `Skills`, `Auto` och `Trending` med Stöd, Färdigheter, Automatiskt
och Populära. Den förbättrar också formuleringar för ändringar och
heartbeat-övervakning och gör Git-terminologin konsekvent med den befintliga
svenska termen incheckning. Batchen omfattar nu även närvarolistan
`Online` → Anslutna och statusen `Offline` → Frånkopplad. Etthundrasextio
delade poster används på minst 195 ställen i webbgränssnittet. Där skiljs också
inläsning av vyer och resurser från nedladdning av filer. I samma batch
normaliseras fjorton synliga förekomster av GitHub-termen pull request till
pull-begäran. Upstream-PR
[#199526](https://github.com/openclaw/openclaw/pull/199526) skapades
2026-11-15 och väntar på granskning. JSONL-filen parsar, de nya svenska
orden passerar Hunspell-sv och svlang bedömer de två senaste etiketterna utan
anmärkning. En fokuserad Gitleaks-kontroll av ändringarna hittade inga
hemligheter. `l10n-lint` stöder inte översättningsminnets JSONL-format och
räknas därför inte som en passerad kontroll. Den senaste batchen normaliserar
också den direkta stödlänken och statusetiketterna med Stöd, Ansluten och
Frånkopplad, samt beskriver ändringar som gjorts utan anslutning på svenska.
Synlig hjälptext använder också Tilläggs-ID och ägartillägg i stället för
plugin som ett vanligt svenskt ord. Den senaste uppföljningen normaliserar
även de återstående korta gränssnittsetiketterna: Tillägg, Tillägg: {id},
Tilläggspanelen och Tilläggsappar.
Navigering, sök, kategorier och inställningar använder också Tillägg
konsekvent i sina synliga texter.
Samma ordval används nu i installationsförloppets status- och felmeddelanden.
Det gäller även katalogladdning, kompatibilitetsmeddelanden, ClawHub-sökning
och beskrivningar av tilläggsvyer.
PR:en kräver fortfarande
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

Uppföljning 2026-11-16: båda öppna PR:erna har nu nyare commits än den
senaste beständiga ClawSweeper-granskningen. Robotens aktuella instruktion är
att kommentera `@clawsweeper re-review` först när respektive huvudrevision är
redo. Det tidigare kravet på verkligt körningsbevis för ett svenskt Android-
eller Apple-gränssnitt kvarstår dock, så någon ny granskningsbegäran har inte
skickats ännu. PR #199519 och PR #199526 är fortfarande öppna och saknar
formellt granskningsbeslut.
