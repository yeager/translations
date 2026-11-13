# Obtainium – import och export

Datum: 2026-11-14
Komponent: `assets/translations/sv.json`
Källversion: `v1.7.4`, publicerad 2026-11-01

## Granskning

Den här batchen översätter tio texter för import och export, bland annat
filnamn vid automatisk export, import från Hämtade filer och export av
certifikat. Klartextvarningen har granskats mot exportdialogens kod: den
informerar om att inställningar och potentiellt känsliga värden i den
exporterade filen kan läsas av alla som kommer åt filen.

## Kontroller

- JSON-syntax: godkänd
- `l10n-lint`: godkänd
- Hunspell-sv: böjningar och produktnamn granskade manuellt
- `svlang`: godkänd
- `git diff --check`: godkänd
- Gitleaks: godkänd
- `msgfmt`: inte tillämpligt på JSON

## Upstream

Ändringarna är inskickade som
[ImranR98/Obtainium#3520](https://github.com/ImranR98/Obtainium/pull/3520).
PR:en är öppen; upstreamgranskning och merge återstår.
