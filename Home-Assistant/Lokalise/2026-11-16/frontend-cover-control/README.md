# Home Assistant Frontend: skyddsreglage

Datum: 16 november 2026

Elva svenska strängar för skyddets reglage i informationsdialogen hade
verklig engelsk källtext och saknade svensk måltext. De har granskats i
nycklarnas UI-kontext, sparats via Lokalise API och lästs tillbaka med samma
måltext och platshållare.

Lokalises korrekta svenska filter returnerar nu 0 oöversatta frontendposter.
Kontroller: JSON, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks.
`msgfmt` är inte tillämpligt på JSON-resursen.
