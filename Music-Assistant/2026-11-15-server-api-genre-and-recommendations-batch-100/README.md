# Music Assistant Server – API-batch 100

Granskad svensk deltafil för en genre och en rekommendationsetikett, sparad i
Music Assistants Lokalise-projekt den 15 november 2026. `Swing` är avsiktligt
identiskt med källtexten; det är ett etablerat genrenamn på svenska.

Lokal granskning: JSON, l10n-lint, svlang, Hunspell, kontroll av tre lika
konsonanter, git-diff och Gitleaks. `msgfmt` är inte tillämpligt på JSON.

Upstream-status: båda API-uppdateringarna lästes tillbaka med
`is_untranslated: false`. Detta styrker att de sparats i Lokalise, men inte
projektets senare granskning eller publicering.
