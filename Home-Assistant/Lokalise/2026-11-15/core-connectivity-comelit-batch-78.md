# Home Assistant Core – anslutningskategorier och Comelit

Datum: 2026-11-15

Femton kontextgranskade strängar sparades via Lokalise API. Batchen omfattar
Home Assistants anslutningskategorier för Matter, Modbus, MQTT, nätverk,
1-Wire, radiofrekvens och seriella enheter samt två Comelit-inställningar.

Tekniska standard- och produktnamn behålls. `MQTT-broker` följer etablerat
svenskt fackspråk. Samtliga poster återlästes med `is_unverified=false`.

Kontroller: JSON, l10n-lint, svlang, Hunspell, git-diff och Gitleaks.
`msgfmt` är inte tillämpligt eftersom batchen är JSON för Lokalise API.

Detta bekräftar lokal granskning, arkivering och sparning i Lokalise, men inte
upstream-granskning, merge eller release.
