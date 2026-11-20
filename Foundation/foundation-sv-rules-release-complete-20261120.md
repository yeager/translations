# Foundation – rules.release.json: färdig radgranskning

Granskad: 2026-11-20  
Omfattning: samtliga 61 svenska strängar i `rules.release.json`, hämtade och granskade radvis via Crowdin API.

En godkänd terminologirättning sparades och dokumenterades i del 1:
- *Combatants* → *kämpar*.

Ändringen validerades med `l10n-lint --language sv` och `hunspell -d sv_SE` utan anmärkningar, och sparades i Crowdin med HTTP 201.

Slutkontroll: offset 61 returnerade en sista sträng, och nästa sida (offset 62) saknar strängar.