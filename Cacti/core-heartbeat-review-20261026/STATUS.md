# Core: datainsamlarens status

Både `settings.php` och `lib/functions.php` jämför tiden sedan `last_status` med två insamlingsintervall innan varningen visas. Översättningen förtydligar att datainsamlaren inte rapporterat i tid. Den tidigare texten kontrollerades i Weblates editor innan filen skickades upp 2026-10-26. Weblate rapporterade en uppdaterad sträng, inga överhoppade och inga saknade.

`msgfmt --check --check-format` och l10n-lint passerade efter att metadata kompletterats. svlang rapporterade inga skrivregelfel och Hunspell flaggade inga ord i den svenska meningen. Terminologin jämfördes med Cactis gemensamma termlista. Gitleaks fann inga hemligheter i katalogen före kompletteringen av metadata.
