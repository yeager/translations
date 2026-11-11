# RetroAchievements: ärendeflöde, svensk batch 05

- Plattform: Crowdin, språk `sv`, komponent `en_US.json` (fil-id `14`).
- Avläst status: 97 % översatt, 58 % godkänt och 243 återstående ord.
- Omfattning: 48 sammanhängande oöversatta UI-strängar i arbetsflödet för rapporterade prestationer och topplistor.
- Granskad lokal delta: `retroachievements-sv-20261111-ticket-workflow-batch-05.json`.
- Terminologibeslut: `TERMINOLOGY.md`.

Strängarna använder `ärende` och `rapportör` konsekvent. För den kontextbundna arbetsfördelningen används `reservation` i stället för det tvetydiga `anspråk`. `Nedgradera` behålls för statusändringen av prestationer och topplistor, enligt tidigare projektgranskning.

Kontroller: JSON-parse och antal (48), l10n-lint (0 fel, 0 varningar), Hunspell-SV, svlangs skrivregler och svengelskakontroll, diffkontroll och Gitleaks. Hunspell-SV markerar enbart platshållarnamnen `duration`, `name`, `percentage`, `reason`, `title` och `user`. Svlangs naturlighetsanalys körd på den sammanfogade UI-mängden ger förväntade falsklarm för platshållare och fristående knappar/etiketter; skrivregler och svengelskakontroll är godkända.

Ingen post har sparats i Crowdin. Vid den senaste åtkomstkontrollen saknades
den tidigare webbsessionen och Crowdin CLI saknade projektkonfiguration. När en
etablerad kanal åter är tillgänglig ska batchen sparas och både lagrade måltexter
och uppdaterat strängantal verifieras.

## Omkontroll 2026-11-11

Batchen kontrollerades på nytt efter Blender-importen: JSON-parsning bekräftar
48 poster och kontroll av samtliga 48 nyckel-/måltextpar bekräftar att
platshållare och taggar är oförändrade. `l10n-lint`, svlangs
svengelskakontroll och skrivregler, diffkontroll och Gitleaks passerar. Ingen
Crowdin-ändring har gjorts av denna omkontroll.
