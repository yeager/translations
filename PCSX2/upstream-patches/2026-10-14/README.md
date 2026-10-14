# PCSX2-uppdatering 2026-10-14

Den aktuella svenska TS-katalogen hämtades från PCSX2:s `master`.

Patchen ändrar endast översättningen för källsträngen `--` från `—` till `--`. Det är ett litteralt gränssnittsvärde och ska följa källsträngens syntax.

Kontroller:

- XML-katalogen är välformad enligt `xmllint`.
- `l10n-lint` hittar inga svenska tankstreck som saknar motsvarighet i källsträngen.
- Gitleaks hittar inga hemligheter.

PCSX2:s Crowdin-projekt går att läsa med den tillgängliga tokenen, men tokenen saknar behörighet att bygga export. PCSX2:s egna bidragsregler kräver dessutom mänsklig verifiering innan agentgenererade bidrag publiceras.
