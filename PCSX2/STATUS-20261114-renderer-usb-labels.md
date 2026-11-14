# PCSX2: renderarmotorer och USB-etikett, 14 november 2026

En rad-för-rad-kontroll av den aktuella CrowdIn-exporten visade sex klart
felmappade måltexter. Två väljare för grafikrenderare hade i stället fått ett
felmeddelande om Vulkan, API-namnet Metal hade försvenskats trots att det ska
bevaras, tidsformatet `{}s` hade fått ett orelaterat printf-fel och USB-
etiketten `B 1` hade fått en kontosträng.

Deltafilen återställer de korrekta, kontextberoende värdena. `Vulkan` och
`Metal` är synliga API-namn och lämnas därför oförändrade. `{} s` behåller
platshållaren och använder svenskt mellanrum före enheten.

## Kontroller före inskick

XML, l10n-lint, platshållarkontroll, Hunspell-sv med sänkt prioritet på bara
de svenska ord som berörs, svlang, diffkontroll och Gitleaks körs innan
arkivering och import. `msgfmt` gäller inte XLIFF.

## Upstream-status

Väntar på CrowdIn-import och direkt återläsning.
