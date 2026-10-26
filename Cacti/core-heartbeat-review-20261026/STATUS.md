# Core: datainsamlarens status

Utkast, inte uppladdat. Både `settings.php` och `lib/functions.php` jämför tiden sedan `last_status` med två insamlingsintervall innan varningen visas. Förslaget förtydligar att datainsamlaren inte rapporterat i tid. Kontrollera aktuell text i Weblate innan eventuell inskickning.

`msgfmt --check --check-format` gav endast varningar om saknade metadatafält i utkastet; l10n-lint rapporterade inga fel och Hunspell flaggade inga ord i den svenska meningen. Gitleaks fann inga hemligheter i katalogen. Övriga granskningsverktyg återstår innan filen färdigställs.
