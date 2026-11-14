# Session Desktop – svensk lokalisering, status 2026-11-14

## Projekt och kanal

- Projekt: [session-foundation/session-desktop](https://github.com/session-foundation/session-desktop)
- Senaste utgåva: `v1.18.4`, 2026-11-13.
- Projektets README och bidragsguide anger [Sessions Crowdin-projekt](https://crowdin.com/project/session-crossplatform-strings) som enda kanal för användarsträngar.

## Lokal granskning

Källträdet innehåller lokaliseringskod och genererade resurser men ingen svensk källresurs. Bidragsguiden förbjuder manuella ändringar i `ts/localization/generated/` och hänvisar rena översättningsändringar till plattformen. Någon lokal svensk fil ska därför inte skapas eller skickas som GitHub-pull request.

## Åtkomst och nästa steg

Den lokalt lagrade Crowdin-nyckeln ger API-svar för användarens tillgängliga projekt, men Sessions offentliga projekt finns inte i den listan. Försök att öppna projektet i webbläsaren ledde till Crowdins kontoauktorisering i en oinloggad session.

Ingen svensk resurs hämtades, ingen lokal ändring skapades och inget skickades upstream. Nästa steg är en autentiserad Session-Crowdin-session eller projektspecifik API-behörighet. Då ska aktuell svensk export hämtas och granskas före varje import.

## Kontrollstatus

- Releasefärskhet: godkänd, utgåva från 2026-11-13.
- Käll- och kanalgranskning: godkänd.
- `msgfmt`, l10n-lint, svlang och Hunspell-SV: ej tillämpliga utan aktuell svensk export.
- Gitleaks: körs före arkivering och eventuellt inskick.
