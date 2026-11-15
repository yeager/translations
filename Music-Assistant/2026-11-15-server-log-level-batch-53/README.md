# Music Assistant Server – loggnivåer, batch 53

Datum: 2026-11-15

Åtta lokalt granskade texter för leverantörers loggning. `DEBUG` normaliseras
till *Felsökning*, i linje med projektets befintliga konfigurationskategori.

Status: samtliga åtta strängar verifierades i Lokalise 2026-11-15. De fanns
redan som svenska översättningar och lämnades orörda. Den lokala arkivkopian
har dessutom synkats med den verifierade formuleringen i Lokalise och pushats
till vårt arkiv. Detta är inte ett upstream-godkännande eller en merge.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i översatta värden, diffkontroll och Gitleaks. `msgfmt` är inte
tillämpligt på JSON-kataloger. En korrekt svensk infinitivfras har granskats
manuellt efter svlang-varning.
