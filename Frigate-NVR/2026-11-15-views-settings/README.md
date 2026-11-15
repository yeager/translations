# Frigate NVR, views-settings — svensk granskningsbatch 001

- Datum: 2026-11-15
- Källa: Frigate `dev`, `web/public/locales/en/views/settings.json`
- Målkomponent: Hosted Weblate `frigate-nvr/views-settings`, svenska
- Omfattning: två fuzzy-strängar som granskats mot aktuell källtext
- Status: inskickad och mottagen i Hosted Weblate.

## Ändringar och verifiering

Kameraguidens beskrivning saknade översättningen av “features”. Meddelandet om
web push-aviseringar innehöll föråldrad markup som inte längre finns i
källsträngen. Båda korrigerades direkt i Weblate och lästes därefter tillbaka
via API:t: komponenten har 0 fuzzy-strängar.

Kontroller: JSON-validering, `l10n-lint`, tekniktokenjämförelse,
`git diff --check` och Gitleaks.

## Batch 002

Batchen omfattar underhåll och mediesynkronisering: säker testkörning,
rensning av överblivna filer, statusvärden och medietyper. Hosted Weblate
accepterade samtliga 40 strängar. Komponenten står därefter på 701 av 1 409
översatta strängar, 0 fuzzy och 14 återstående kontrollträffar som granskas
separat i sitt tekniska sammanhang.

Kontroller: `jq empty`, `l10n-lint`, tokenjämförelse mot aktuell källfil,
`git diff --check` och Gitleaks.

## Batch 004

Batchen omfattar formulärfält, globala inställningar, kamerainställningar och
statusmeddelanden. Hosted Weblate tog emot 37 aktuella källnycklar. Tre
föråldrade Weblate-nycklar, som saknas i Frigates aktuella källfil, lämnades
avsiktligt utanför batchen.

Åtta nya kontrollträffar från avslutande punkter i toast-meddelanden rättades
via enhets-API:t, eftersom importer inte skriver över befintliga översättningar.
Komponenten står därefter på 800 av 1 409 översatta strängar, 0 fuzzy och 18
kontrollträffar. De kvarvarande träffarna granskas separat; tekniska namn som
`FFmpeg` och `Birdseye` är dokumenterade avsiktliga undantag.

Kontroller: `jq empty`, `l10n-lint`, käll- och tokenjämförelse, API-läsning,
`git diff --check` och Gitleaks.

## Batch 003

Batchen omfattar sidtitlar, inställningsmenyer, sparade ändringar, Frigate+ och
grundläggande formulärtexter. Hosted Weblate accepterade samtliga 62 strängar.
Komponenten står därefter på 763 av 1 409 översatta strängar och 0 fuzzy.

Kontrollträffarna ökade från 14 till 17. De tre nya är avsiktliga och korrekta:
de tekniska produktnamnen `FFmpeg` (två gånger) och `Birdseye` i Frigates
navigering. De återstående 14 kontrollträffarna var befintliga och granskas
separat.

Kontroller: `jq empty`, `l10n-lint`, tokenjämförelse mot aktuell källfil,
`git diff --check` och Gitleaks.
