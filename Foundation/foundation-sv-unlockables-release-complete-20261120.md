# Foundation – unlockables.release.json: färdig radgranskning

Granskad: 2026-11-20  
Omfattning: samtliga 98 svenska strängar i unlockables.release.json, hämtade och granskade radvis via Crowdin API.

Godkända förbättringar har dokumenterats i del 1–5 och sparats direkt i Crowdin. De omfattar byggnadstermer, Hospitium, Cloister, Keep, Company, Combatant, City Belfry, vägnamn och svenska gränssnittsformer.

Varje ändringspaket validerades med l10n-lint --language sv och hunspell -d sv_SE; platshållare och formatering bevarades. Sparningar bekräftades med HTTP 201. Dubblettsvar dokumenterades där motsvarande förslag redan fanns i Crowdin.

Slutkontroll: offset 100 returnerade 0 strängar.