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

## Android Talk

Android Talk `v25.0.2` publicerades 2026-10-02 och uppfyller kravet på en
officiell release inom 48 månader. De 25 nya UI-raderna för ljuduppspelning,
samtal, certifikat och HTTP-reservläge granskades mot Talk-resursens befintliga
svenska terminologi. De arkiverades i
`nextcloud-android-talk-sv-20261030.json` och skickades via Transifex
REST-API med HTTP 200.

Efterkontrollen visar 883 av 883 strängar och 3 397 av 3 397 ord översatta,
med 0 oöversatta strängar kvar.

## Assistant

Assistant har den aktuella taggen `v4.1.0` från 2026-10-26 och uppfyller
kravet på en officiell version inom 48 månader. Sjutton UI-strängar för
assistentens svar, agentinstruktioner, åtgärdsomfång och aviseringar
granskades mot resursens befintliga svenska termer. De arkiverades i
`nextcloud-assistant-sv-20261030.json` och skickades via Transifex REST-API
med HTTP 200.

Efterkontrollen visar 552 av 552 strängar och 3 201 av 3 201 ord översatta,
med 0 oöversatta strängar kvar.

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

## Agora

Agora är en aktiv Nextcloud-app: App Store visar version `1.7.12`, uppdaterad
2026-09-21, och Transifex-resursen ändrades senast 2026-10-30. Den uppfyller
därmed kravet på en aktuell officiell release inom 48 månader. Första
UI-batchen med 74 strängar för grupper, förfrågningar, omröstningar och
administration granskades och arkiverades i
`nextcloud-agora-sv-20261030-batch01.json`. Den innehåller inte den separata
pluralposten för antal väljare; den hanteras med svenska singular- och
pluralformer i en egen API-batch.

`l10n-lint`, `svlang skrivregler`, platshållarjämförelsen och Gitleaks
passerar. Hunspell markerar enbart egennamn, metodnamn och tekniska
platshållare. Batchen skickades som vanliga, ogranskade översättningar via
Transifex REST-API med HTTP 200 och API:t returnerade 74 sparade måltexter.
Den separata pluralposten för `%n voter`/`%n voters` arkiverades i
`nextcloud-agora-sv-20261030-plural01.json` och skickades därefter med båda
svenska formerna. API:t bekräftade även den med HTTP 200. Efterkontrollen
visar 1 857 av 2 103 strängar översatta, alltså 246 kvar.

Den andra UI-batchen med 51 poster för grupptyper, fält och åtgärdsinställningar
arkiverades i `nextcloud-agora-sv-20261030-batch02.json`. Samma
kontrollkedja passerade och Transifex bekräftade samtliga poster med HTTP 200.
Måltexten för varje post återlästes via API innan statusen räknades som
skickad. Statistikändpunkten visar nu 1 908 av 2 103 strängar översatta,
alltså 195 kvar.

Tredje batchen med 30 poster för familjer och alternativtyper är arkiverad i
`nextcloud-agora-sv-20261030-batch03.json`. Kontrollkedjan passerade och
Transifex API bekräftade alla 30 med HTTP 200. Statistikändpunkten visar
1 938 av 2 103 strängar översatta, alltså 165 kvar.

Fjärde batchen med 20 poster för alternativtyper arkiverades i
`nextcloud-agora-sv-20261030-batch04.json`. Kontrollkedjan passerade och
Transifex API bekräftade alla med HTTP 200. Efterkontrollen visar 1 958 av
2 103 strängar översatta, alltså 145 kvar.

Femte batchen med 32 poster för svarstyper och förfrågningstyper finns i
`nextcloud-agora-sv-20261030-batch05.json`. Den passerade kontrollkedjan och
skickades med HTTP 200. Statistikändpunkten visar 1 990 av 2 103 strängar
översatta, alltså 113 kvar.

Sjätte batchen med 25 poster för förfrågningsinställningar och
omröstningsmetoder finns i `nextcloud-agora-sv-20261030-batch06.json`.
Den passerade kontrollkedjan och Transifex API bekräftade 25 sparade
måltexter. Statistikändpunkten visar 2 015 av 2 103 strängar översatta,
alltså 88 kvar.

Åttonde batchen med 30 poster för ytterligare röstningsmetoder och
debattfunktioner finns i `nextcloud-agora-sv-20261030-batch08.json`. Den
skickades efter en ny API-förkontroll och Transifex bekräftade alla 30 med
HTTP 200. Statistikändpunkten visar 2 037 av 2 103 strängar översatta,
alltså 66 kvar.

Nionde batchen finns i `nextcloud-agora-sv-20261030-batch09.json`. Den
förkontrollerades på nytt och 20 fortfarande aktuella poster skickades med
HTTP 200; övriga poster hade redan ändrats i den aktuella kön. Statistik visar
2 087 av 2 103 strängar översatta, alltså 16 kvar.

## Agora – slutkontroll

Den arkiverade tionde batchen
`nextcloud-agora-sv-20261030-batch10.json` innehåller de återstående 16
UI-strängarna. Den 30 oktober lästes varje sträng åter från Transifex med dess
unika resursöversättnings-id; samtliga 16 måltexter är identiska med den
arkiverade kandidaten. API-filtret `translated=false` för resursen `agora`
och svenska (`l:sv`) returnerar dessutom 0 poster. Batchen behöver därför
inte skickas igen, och Agora är komplett för den aktuella källan.
