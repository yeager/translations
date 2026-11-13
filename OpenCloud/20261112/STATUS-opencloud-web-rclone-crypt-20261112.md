# OpenCloud web-rclone-crypt – svenska översättningar

Datum: 2026-11-12
Projekt och komponent: OpenCloud / `web-rclone-crypt`
Status: inskickat och verifierat i Transifex

## Omfattning

- 19 tidigare oöversatta strängar för klientkrypterade valv granskades och översattes.
- Säkerhetsinnebörden bevarades i information om lösenord, återställningsbegränsningar, krypteringsnycklar, säkerhetskopior och oåterkallelig dataförlust.
- Befintlig OpenCloud-terminologi följdes: `vault` → `valv`, `space` → `arbetsyta`.
- Produktnamnet `Rclone Crypt` behölls oöversatt.

## Kvalitetskontroller

- `l10n-lint --language sv --json-format entries`: godkänd.
- `svlang skrivregler --enable-interpunktion`: godkänd.
- Platshållarkontroll: godkänd.
- `hunspell -d sv_SE`: träffar endast på produktnamn och avsiktliga sammansatta säkerhetstermer.
- `git diff --no-index --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga läckor.
- `msgfmt`: ej tillämpligt för JSON-resursen; valideringen gjordes med l10n-lint, strukturkontroll och Transifex API.

## Upstream

En Transifex API-batch med 19 uppdateringar skickades 2026-11-12 och fick HTTP 200. Efterkontrollen med `translated=false` returnerade 0 oöversatta svenska strängar i komponenten.
