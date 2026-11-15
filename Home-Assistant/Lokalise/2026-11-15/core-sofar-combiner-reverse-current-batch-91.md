# Home Assistant Core – Sofar, samlingslådans omvända ström

Datum: 2026-11-15

Femton Sofar-fel för överspänning och omvänd ström i samlingslådans grupper
och strängar sparades och återlästes via Lokalise API med `is_unverified=false`.

Kontroller: JSON, l10n-lint, svlang, Hunspell, git-diff och Gitleaks.
`msgfmt` är inte tillämpligt eftersom batchen är JSON för Lokalise API.
