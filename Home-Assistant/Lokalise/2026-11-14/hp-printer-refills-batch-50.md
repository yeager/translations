# HP Printer: påfyllningsräknare, batch 50

Datum: 2026-11-14

Tio diagnostiska, ackumulerande räknare för patronpåfyllningar kontrollerades
mot den aktuella komponentkoden och HP:s dokumentation om äkta, påfyllda och
förfalskade patroner. Alla sparades i Lokalise och återlästes separat.

Formen "[äkta/förfalskade] påfyllningar för [färg] patron" beskriver
räknarens kategori utan att göra källtextens HP-specifika kategorisering
till ett obelagt varumärkespåstående i den svenska texten.

Fälten gäller svart, cyan, magenta, trefärg och gul patron, med en räknare
för äkta och en för förfalskade påfyllningar per patron.

Kontroller före sparning: l10n-lint, individuell svlang-kontroll,
Hunspell-sv, diffkontroll och Gitleaks. Hunspell-sv saknar sammansättningen
"trefärgspatron"; svlang bedömer den till 10/10 och den är accepterad som
normal svensk sammansättning i denna konkreta UI-kontext. `msgfmt` är inte
tillämpligt eftersom Lokalise hanterar JSON-nycklar, inte en PO-fil.
