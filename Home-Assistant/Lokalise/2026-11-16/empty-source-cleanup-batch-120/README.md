# Home Assistant Core – avsiktligt tomma källvärden, batch 120

Datum: 2026-11-16

Åtta svenska värden innehöll tidigare “Tom” trots att motsvarande engelska
källvärde är avsiktligt tomt. De återställs därför till tomma svenska värden.
Detta är inte samma sak som tillståndet *Empty* för exempelvis en behållare
eller vätskenivå, där *Tom* kan vara korrekt i svensk UI-kontext.

Status: alla åtta poster återställdes via Lokalise API och lästes tillbaka med
samma översättnings-ID:n. `is_untranslated: 1` är förväntat för dessa poster,
eftersom både källa och mål avsiktligt är tomma. `is_fuzzy: false` bekräftas
för samtliga. Arkivposten är pushad till vårt arkiv; detta är inte ett
upstream-godkännande eller en release.

Kontroller: JSON, källnycklar, kontroll av att källa och mål är tomma,
diffkontroll och Gitleaks. l10n-lint, svlang, Hunspell och msgfmt är inte
tillämpliga på avsiktligt tomma JSON-värden.
