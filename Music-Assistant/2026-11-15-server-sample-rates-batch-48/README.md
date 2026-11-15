# Music Assistant Server – samplingsfrekvenser, batch 48

Datum: 2026-11-15

Arton lokalt granskade inställningstexter för spelarens samplingsfrekvens och
bitdjup. Tekniska värden är oförändrade, medan svenska decimaltecken och enheter
används i den synliga texten.

Status: en tidigare snabbkontroll räckte inte för radvis verifiering. Samtliga
arton strängar ska därför granskas på nytt i Lokalise innan batchen kan räknas
som klar.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är inte
tillämpligt på JSON-kataloger.
