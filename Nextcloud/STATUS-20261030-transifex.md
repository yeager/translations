# Nextcloud – svensk Transifex-status 2026-10-30

## Aktuell release

Nextcloud Server `v33.0.10` publicerades 2026-10-15 och uppfyller därmed
kravet på en officiell release inom 48 månader.

## Inventering

Den svenska Transifex-projektvyn innehåller ett stort antal fristående appar
och bibliotek. Vid kontrollen 2026-10-30 hade bland annat följande resurser
nya oöversatta strängar:

- `core`: 1
- `android-notes`: 9
- `android-talk`: 25
- `analytics`: 16
- `agora.pot`: 321
- `assistant.pot`: 17
- `calendar`: 1
- `contacts`: 31
- `deck`: 4

Fortsatt arbete ska ske komponentvis. Det gör ursprung, kontrollresultat och
uppladdningar spårbara och undviker att en stor, osammanhängande import döljer
fel.

## Core

`core` har den nya pluralsträngen med hash
`460e1f5b5fbae6f088af7a01760707f6`. Den arkiverade kandidaten
`nextcloud-core-sv-20261030.json` innehåller:

- singular: `Signaturen för %s saknas eller är ogiltig och kan därför inte verifieras.`
- plural: `De %n signaturerna för %s saknas eller är ogiltiga och kan därför inte verifieras.`

`svlang skrivregler`, `l10n-lint` och Gitleaks passerar. Den lokala
Hunspell-körningen ger inga okända ord. Platshållarna `%s` respektive `%n` och
`%s` är bevarade. Båda pluralformerna är förberedda i Transifex-redigeraren,
men har ännu inte sparats externt.
