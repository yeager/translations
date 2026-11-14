# PCSX2: avstämning mot äldre export, 14 november 2026

Den lokala XLIFF-exporten har kontrollerats mot de senast arkiverade
CrowdIn-deltana. Den innehåller äldre aktiva måltexter för redan hanterade
fel: dubbelmellanrum i två sparfel, grafik-API:erna Vulkan och Metal,
tidsformatet `{} s` och USB-etiketten `B 1`.

En ny import skulle bara skapa dubblettkandidater. De korrekta texterna finns
redan i tidigare deltan och deras import/återläsning är dokumenterad i
`STATUS-20261113-xliff-integrity-repair.md` och respektive batchstatus. Ingen
ny deltafil eller ny CrowdIn-import skapades av denna avstämning.

## Kontroller

Den kompletta exporten är XML-validerad och körd genom l10n-lint. De aktuella
fynden jämfördes rad för rad med arkiverade deltafiler. svlang kördes för de
berörda svenska etiketterna; Hunspell-sv markerar bara produktnamnet `Metal`,
vilket är en avsiktlig falsk positiv. `msgfmt` gäller inte XLIFF.

Arkivdiff och Gitleaks passerade. Detta är endast en lokal och arkiverad
avstämning; den bekräftar inte att CrowdIn har valt eller godkänt kandidaterna
som aktiva översättningar.
