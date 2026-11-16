# Home Assistant Core: `>`-strängar, batch 129

Alla 58 då tomma svenska strängar med `>` i källtexten. 52 återanvänder tidigare kontextgranskade LIFX-etiketter; sex menyvägs- och hjälptexter har granskats i sina respektive komponenter.

Kontroller: JSON och platshållare, l10n-lint, svlang, Hunspell-sv, diffkontroll och Gitleaks. `msgfmt` är inte tillämpligt för Lokalise JSON/API-batcher.

Samtliga poster sparades med Lokalise API, `is_unverified: false`, och återlästes efter varje sparning.
