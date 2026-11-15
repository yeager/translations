# Music Assistant Server – musikrekommendationer, batch 46

Datum: 2026-11-15

Trettioåtta lokalt granskade rubriker och korta förklaringar för
rekommendationer i musikbiblioteket. Svenska UI-termer är konsekventa med
spår, artister, spellistor och poddar i övriga Music Assistant-batcher.

Status: lokalt granskad och arkiverad. En saknad sträng sparades manuellt i
Lokalise 2026-11-15 och lästes tillbaka; övriga strängar granskas mot den
redan sparade översättningen.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken, diffkontroll och Gitleaks. `msgfmt` är inte tillämpligt på
JSON-kataloger. l10n-lint och svlang varnar för idiomatiska konstruktioner med
”på ... på länge” och för korta UI-fragment; de har granskats manuellt.
