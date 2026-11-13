# Audacity: kontrollpunkt för hela aktiva katalogen

- Datum: 2026-11-13
- Källcommit: `aafcdf6` är PR-grenens enda commit efter att den tidigare, röriga commitserien konsoliderades. Den omfattar också den sista CodeRabbit-åtgärden: frekvensformatets tusentalsavskiljare är nu mellanslag, medan decimalmarkören fortfarande ger svenskt kommatecken.
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: hela den aktiva svenska PO-katalogen.

Den aktiva katalogen har 4 443 översatta poster och 0 oöversatta poster. Den har gåtts igenom rad för rad i den löpande granskningscykeln. Resterande 1 338 `#~`-poster är föråldrade historiska poster och ingår inte i den importerbara katalogen.

Siffran 1 716 i projektstatusen betyder poster som faktiskt har ändrats i de 134 dokumenterade granskningsbatcherna. Den är inte ett mått på hur många poster som lästs i den fullständiga genomgången.

Kontroller för hela katalogen: `msgfmt` godkänner 4 443 översatta poster; diffkontroll och Gitleaks passerar; inga em dashar eller otillåtna följder av tre identiska konsonanter finns i aktiva översättningar. Hunspell-sv ger 814 unika råträffar, främst formatmarkörer, produktnamn, filformat och etablerade facktermer. `l10n-lint` ger 365 rader och `svlang` 545 rader för befintliga breda heuristikvarningar, bland annat markup, formatmarkörer, källtextlika namn och korta UI-etiketter. De verktygen har körts avgränsat på varje ändringsbatch; inga aktuella ändrade poster träffas där.

PR #12759 gjordes redo för upstreamgranskning den 13 november 2026 efter den fullständiga manuella genomgången. Den har nu en enda, tydlig commit. CodeRabbit lämnade först ett granskningssvar utan nya generella kommentarer, men pekade därefter ut det kvarvarande frekvensformatet; det är åtgärdat i `aafcdf6`. Den vanliga CodeRabbit-kontrollen passerar. En uttryckligen begärd helomgranskning kunde däremot inte starta eftersom den ändrade PO-filen är större än botens granskningsgräns. PR:n har inte fått någon mänsklig upstreamgranskning, inget godkännande och är inte mergad.
