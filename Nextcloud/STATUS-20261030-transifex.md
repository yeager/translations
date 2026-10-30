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
`%s` är bevarade.

Den 30 oktober verifierades den aktuella Transifex-resursen `core` i
redigeraren. Resursen rapporterar 576 av 576 strängar översatta och 0
oöversatta ord. Den exakta pluralposten visas med de arkiverade måltexterna:

- `Signaturen för %s saknas eller är ogiltig och kan därför inte verifieras.`
- `De %n signaturerna för %s saknas eller är ogiltiga och kan därför inte verifieras.`

Det finns alltså ingen ny Core-översättning att spara externt. Statusen
`inte granskad` i Transifex gäller granskningsflödet i stort och är inte ett
bevis på att just den här texten saknas.

## Calendar

Calendar hade en oöversatt pluralpost (Transifex-ID `640052248`) med
utvecklarkontexten `CalendarList.vue:208`. Den granskades och arkiverades i
`nextcloud-calendar-sv-20261030.json` med formerna `Delad kalender` och
`Delade kalendrar`. Den 30 oktober sparades båda formerna i Transifex av
`yeager`; därefter visade filtret för oöversatta strängar 0 av 827.

## Android Notes

Android Notes `35.0.0` publicerades 2026-09-16 och uppfyller kravet på en
officiell release inom 48 månader. De nio nya synkroniseringsfelen i
`android-notes` granskades mot aktuell källkod och befintliga svenska
appnamnstermer. Kandidaterna arkiverades i
`nextcloud-android-notes-sv-20261030.json` och skickades som ogranskade
översättningar med Transifex REST-API.

API-svaret var HTTP 200 med nio poster. Efterkontrollen visar 403 av 403
strängar och 1 771 av 1 771 ord översatta samt 0 oöversatta strängar.

## Analytics

Analytics `7.2.0` publicerades 2026-10-29 och uppfyller kravet på en
officiell release inom 48 månader. Femton UI- och hjälprader granskades mot
den befintliga svenska Analytics-terminologin och arkiverades i
`nextcloud-analytics-sv-20261030.json`. Batchen skickades via Transifex
REST-API med HTTP 200.

Efterkontrollen visar 754 av 755 strängar översatta. Den återstående posten
är en 985-teckens Markdown-beskrivning av appen; den är dokumentation och
väntar därför enligt instruktionen att inte behandla dokumentation ännu.

## Contacts

Contacts har 31 oöversatta UI-strängar i importflödet. De har granskats mot
den aktuella källkoden i `nextcloud/contacts` och är arkiverade i
`nextcloud-contacts-sv-20261030.json`. Sex poster är pluraler och innehåller
var sin svensk singular- och pluralform; alla `%n`, `%1$s` och namnplacerare
är bevarade. `svlang skrivregler`, `l10n-lint`, Hunspell, en
platshållarjämförelse och Gitleaks passerar.

Batchen skickades den 30 oktober som vanliga, ogranskade översättningar genom
Transifex REST-API. API:t bekräftade samtliga 31 poster med HTTP 200. Därefter
visade både statistik- och översättningsändpunkten 0 oöversatta strängar.
Detaljerat sändningsbevis finns i `contacts-submission-20261030.md`.
