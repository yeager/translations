# Home Assistant Core: mallmediespelare, batch 125

Den här batchen kompletterar 40 fält och hjälptexter för den mallbaserade mediespelaren.
Termerna `entitet`, `mediespelare`, `källa` och `källista` följer Home Assistants etablerade svenska gränssnittsterminologi.
Maskinläsbara tillståndsvärden som `off`, `on` och `buffering` har bevarats.

## Kontroller före inskick

- JSON-struktur och kodformaterade värden: godkända
- `l10n-lint`: godkänd
- `svlang`: granskat; varningarna är strukturella falska positiva för korta etiketter och tekniska tillståndsvärden
- `hunspell-sv`: endast bevarade tekniska värden och variabeln `source`
- `git diff --check`: godkänd
- Gitleaks: godkänd
- `msgfmt`: ej tillämpligt; Lokalise API-batchen använder JSON

## Upstreamresultat

Alla 40 poster sparades via Lokalise API med `is_unverified: false` och
återlästes omedelbart med respektive översättnings-ID. Det bekräftar sparat
innehåll, men inte extern granskning, sammanslagning eller utgivning.
