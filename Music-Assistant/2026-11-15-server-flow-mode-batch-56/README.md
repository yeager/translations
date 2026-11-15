# Music Assistant Server – köflödesläge, batch 56

Datum: 2026-11-15

Två synliga konfigurationstexter för köflödesläge. Funktionen skickar alla
spår i kön som en enda sammanhängande ljudström för spelare som saknar stöd
för sömlös uppspelning eller övertoning.

Terminologi: *Flow Mode* återges konsekvent som *köflödesläge*, enligt
projektets terminologilista. *Sömlös uppspelning*, *övertoning* och
*sammanhängande ljudström* beskriver den konkreta ljudfunktionen.

Status: beskrivningen korrigerades och sparades manuellt i Lokalise
2026-11-15. Etiketten fanns redan som korrekt svensk översättning och
verifierades i Lokalise. Denna arkivkopia har pushats till vårt arkiv; detta
är inte en upstream-merge eller ett upstream-godkännande.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är
inte tillämpligt på JSON-kataloger.
