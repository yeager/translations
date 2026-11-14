# Music Assistant Frontend – svensk onboarding, batch 1

Datum: 2026-11-14
Komponent: MA Frontend, `%LANG_ISO%.json`, svenska (Sverige)

## Sparade och återlästa måltexter

- `onboarding::continue` → `Fortsätt`
- `onboarding::explore_more` → `Utforska mer`
- `onboarding::listen_from_apps` → `Prova att spela från dina musikappar`
- `onboarding::steps::plugins::phone_apps_title` → `Anslut dina musikappar`
- `onboarding::steps::plugins::connect` → `Anslut en musikapp`
- `onboarding::steps::core_settings::network_details` → `Nätverksuppgifter`
- `onboarding::steps::finish::phone_apps_description` → idiomatisk sammanfattning av högtalare, appanslutningar och fortsatt konfiguration
- `onboarding::steps::plugins::phone_apps_description` → instruktion för Spotify Connect och AirPlay Receiver
- `onboarding::steps::intent::music_hub::preview` → svensk förhandsvisning av anslutning av musiktjänster och högtalare
- `onboarding::steps::intent::phone_apps::preview` → svensk förhandsvisning av anslutning av högtalare och musikappar

## Kontroller och status

- Varje måltext sparades direkt i Lokalise och återlästes i redigeraren.
- Kontext: första konfigureringen av Music Assistant Frontend för telefonappar och musikhubb.
- Produktnamnen Spotify Connect och AirPlay Receiver är oförändrade. I övrigt används svenska UI-termer, exempelvis `högtalare`, `musiktjänster` och `Nätverksuppgifter`.
- `msgfmt`, l10n-lint, svlang och Hunspell-sv är inte körbara för en direkt browserbatch utan lokal exportfil. Det är en begränsning för denna batch, inte ett godkänt lokalt testresultat.
- Git-diffkontroll och Gitleaks kördes för arkivändringen.

## Upstreamstatus

Sparad och återläst i Music Assistants Lokalise-projekt den 2026-11-14. Detta är ett verifierat inskick i översättningssystemet, men inte ett påstående om upstreamgranskning, synk till GitHub eller release.
