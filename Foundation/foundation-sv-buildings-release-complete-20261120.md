# Foundation — buildings.release — komplett

Granskad: 2026-11-20  
Komponent: `buildings.release.json` (Crowdin fil-ID 64)

Samtliga 365 strängar har radgranskats via Crowdin API. Slutkontroll: offset 365 returnerade 0 strängar.

Godkända förbättringar har skickats direkt till Crowdin och dokumenterats i del 1–6. De omfattar Foundation-termerna *Abbatial*, *Keep*, *Company*, *Combatant* och *City Belfry*, samt språkliga preciseringar för byggnadsnamn och beskrivningar.

Varje ändringsdel validerades med `l10n-lint --language sv` och `hunspell -d sv_SE`, utan kvarvarande anmärkningar. Alla sparningar bekräftades med HTTP 201.