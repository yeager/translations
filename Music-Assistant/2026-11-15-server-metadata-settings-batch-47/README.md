# Music Assistant Server – metadatainställningar, batch 47

Datum: 2026-11-15

Tolv lokalt granskade inställningstexter för nätmetadata, radioomslag,
språk, MusicBrainz-länkning, genremetadata och miniatyrbildscache.
Produktnamn och filformat har bevarats där de visas i gränssnittet.

Status: en tidigare snabbkontroll räckte inte för radvis verifiering. Åtta
strängar är sparade och återlästa i Lokalise, och en är verifierad oförändrad;
tre återstår.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken, diffkontroll och Gitleaks. `msgfmt` är inte tillämpligt på
JSON-kataloger. svlang-varningar för produktnamn och svenska nominalfraser har
granskats manuellt.
