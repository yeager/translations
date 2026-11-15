# Music Assistant Server – poddkategorier, batch 50

Datum: 2026-11-15

Nitton lokalt granskade kategorirubriker i podcastvyn. Den etablerade
genrebeteckningen *True crime* har behållits; övriga rubriker är svenska och
konsekventa med bibliotekets terminologi.

Status: samtliga nitton strängar verifierades i Lokalise 2026-11-15. De fanns
redan som svenska upstream-översättningar och lämnades orörda. Arkivering och
push pågår.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är inte
tillämpligt på JSON-kataloger. Hunspell-varningen för den etablerade
genrebeteckningen har granskats manuellt.
