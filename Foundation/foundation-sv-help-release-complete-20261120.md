# Foundation – help.release.json: färdig radgranskning

Granskad: 2026-11-20  
Omfattning: samtliga 430 svenska strängar i `help.release.json`, hämtade och granskade radvis via Crowdin API.

Godkända ändringar finns arkiverade i del 1–20 och har skickats direkt till Crowdin. De omfattar konsekventa Foundation-termer för bland annat *Company*, *Combatant*, *Keep*, *Hospitium*, *City Charter*, *Approval*, *Might*, *Density* och tjänster.

Varje ändringspaket validerades med `l10n-lint --language sv` och `hunspell -d sv_SE`. Formatering och platshållare bevarades. Crowdin-sparningar bekräftades med HTTP 201; enstaka dubblettsvar dokumenterades där samma förslag redan fanns i projektet.

Slutkontroll: `strings?fileId=74&offset=430` returnerade 0 strängar.