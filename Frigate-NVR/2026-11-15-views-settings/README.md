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

## Batch 005

Batchen omfattar formulärflikar, extra egenskaper, rollmappningar,
FFmpeg-argument, indataströmmar och konfigurationsavsnitt. Hosted Weblate
accepterade samtliga 54 strängar. Komponenten står därefter på 854 av 1 409
översatta strängar och 0 fuzzy.

Kontrollträffar i den här delen avser korrekta tekniska namn: `go2rtc`,
`FFmpeg`, `GenAI` och `Birdseye`. De är dokumenterade undantag; inga
översättningar ändrades för att dölja dem.

Kontroller: `jq empty`, `l10n-lint`, käll- och tokenjämförelse,
`git diff --check` och Gitleaks.

## Batch 014

Batchen omfattar kamerans driftstatus, live-strömmar och
detekteringsupplösning. Hosted Weblate accepterade samtliga 22 strängar.
Komponenten står därefter på 1 081 av 1 409 översatta strängar och 0 fuzzy,
utan nya kontrollträffar.

Kontroller: `jq empty`, `l10n-lint`, kontroll av platshållare, URL:er och
markup, `git diff --check` och Gitleaks.

## Batch 011

Batchen omfattar återstående HTTP-, RTSP- och inspelningsförinställningar,
granskningsetiketter och profilkolumner. Hosted Weblate accepterade samtliga
21 strängar. Komponenten står därefter på 1 017 av 1 409 översatta strängar
och 0 fuzzy.

Den nya kontrollträffen är produktnamnet `Blue Iris`, som ska vara oförändrat.
Kontroller: `jq empty`, `l10n-lint`, käll- och tokenjämförelse,
`git diff --check` och Gitleaks.

## Batch 012

Batchen omfattar konfigurationsvarningar för detektering, granskning,
ansiktsigenkänning, LPR och GenAI samt kameratyper. Hosted Weblate accepterade
18 aktuella källsträngar. Fyra äldre åsidosättningsnycklar saknas i Frigates
aktuella källfil och lämnades därför utanför.

Komponenten står därefter på 1 035 av 1 409 översatta strängar och 0 fuzzy,
utan nya kontrollträffar.

Kontroller: `jq empty`, `l10n-lint`, tokenjämförelse mot källfilen,
`git diff --check` och Gitleaks.

## Batch 013

Batchen omfattar bevarande- och förhandsvisningsval, ONVIF-autospårning,
detektorsidor, UI-status och Birdseye-kameraordning. Hosted Weblate accepterade
24 aktuella strängar. Tre äldre åsidosättnings- och toastnycklar som saknas i
den aktuella Frigate-källfilen lämnades utanför.

Komponenten står därefter på 1 059 av 1 409 översatta strängar och 0 fuzzy,
utan nya kontrollträffar.

Kontroller: `jq empty`, `l10n-lint`, käll- och tokenjämförelse,
`git diff --check` och Gitleaks.

## Batch 010

Batchen omfattar FFmpeg-förinställningar, synkroniseringsloggning,
ONVIF-profiler och tidsstämpelpositioner. Hosted Weblate accepterade samtliga
16 strängar. Komponenten står därefter på 996 av 1 409 översatta strängar och
0 fuzzy.

Åtta nya kontrollträffar är granskade och avsiktliga: Raspberry Pi, VAAPI,
Intel QuickSync, NVIDIA Jetson, Rockchip RKMPP och H.264/H.265 är tekniska
namn och format som ska behållas oförändrade.

Kontroller: `jq empty`, `l10n-lint`, käll- och tokenjämförelse,
`git diff --check` och Gitleaks.

## Batch 009

Batchen omfattar permanent kameraradering, återkoppling i bekräftelsedialoger,
profilåsidosättningar och gränssnittsinställningar. Hosted Weblate accepterade
samtliga 19 strängar. Komponenten står därefter på 980 av 1 409 översatta
strängar och 0 fuzzy, utan nya kontrollträffar.

Kontroller: `jq empty`, `l10n-lint`, käll- och tokenjämförelse,
`git diff --check` och Gitleaks.

## Batch 008

Batchen omfattar masker, zoner, MQTT-begränsningar och regionsrutnätets
underhållsåtgärder. Hosted Weblate accepterade samtliga 25 strängar.
Komponenten står därefter på 961 av 1 409 översatta strängar och 0 fuzzy,
utan nya kontrollträffar.

Kontroller: `jq empty`, `l10n-lint`, käll- och tokenjämförelse,
`git diff --check` och Gitleaks.

## Batch 007

Batchen omfattar go2rtc-strömmar, dess FFmpeg-kompatibilitetsalternativ och
inställningar för semantisk sökning. Hosted Weblate accepterade samtliga 44
strängar. Komponenten står därefter på 936 av 1 409 översatta strängar och 0
fuzzy, utan nya kontrollträffar.

Kontroller: `jq empty`, `l10n-lint`, käll- och tokenjämförelse,
`git diff --check` och Gitleaks.

## Batch 006

Batchen omfattar profilhantering och profilåsidosättningar. Hosted Weblate
accepterade 38 strängar. En äldre `cameraCount`-nyckel saknas i den aktuella
källfilen och lämnades därför utanför. Komponenten står därefter på 892 av
1 409 översatta strängar och 0 fuzzy.

Kontroller: `jq empty`, `l10n-lint`, käll- och tokenjämförelse,
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
