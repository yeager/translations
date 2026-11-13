# LocalSend, svensk UI-granskning, 13 november 2026

LocalSend är ett lokalt nätverksverktyg för att skicka filer och text mellan enheter. Den svenska resursen jämfördes med den aktuella engelska filen vid revisionen 2e7ef1972b0b4e210608ec77ef5fad334f798f7e.

Tre nya UI-strängar saknades i svenska:

- **Always on top** → **Alltid överst**
- **Not supported on Wayland** → **Stöds inte i Wayland**
- **Enter a whole number between 1 and 65535.** → **Ange ett heltal mellan 1 och 65 535.**

Ändringen ligger i projektets avsedda kompletteringsfil och kan tillämpas med dart run slang apply --locale=sv i en komplett utvecklingsmiljö.

Kontroller:

- JSON-syntax: godkänd
- l10n-lint: godkänd
- Hunspell-sv för den svenska deltan: godkänd
- svlang: den svenska texten godkänd; verktyget rapporterar engelska ord i projektets obligatoriska @@info-metadata
- diffkontroll: godkänd
- Gitleaks för deltan: godkänd

Projektspecifik generering med Slang kördes inte eftersom Dart saknas i arbetsmiljön. Gitleaks över projektets fulla git-historik fann en redan befintlig träff; den påverkar inte denna deltafil och behöver projektets egen bedömning.

Upstream: inskickat som [LocalSend PR #3706](https://github.com/localsend/localsend/pull/3706) den 13 november 2026. PR:en är öppen mot `main`. CodeRabbit har slutfört sin kontroll utan åtgärdskommentarer. Mänsklig upstreamgranskning och merge är ännu inte verifierade.
