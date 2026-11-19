# Foundation – saknade DLC, svensk QA-rättning 2026-11-19

Två befintliga svenska menu-översättningar har granskats via Crowdins QA-API. Förslagen är utkast och har inte sparats i Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 26162 | This save contains content from missing DLC(s), which are not currently installed. \nPlease complete their installation to be able to load this save. | Den här sparningen innehåller innehåll från DLC som saknas och inte är installerade. \nSlutför installationen för att kunna läsa in sparningen. | Den här sparningen innehåller innehåll från DLC (ett eller flera) som saknas och inte är installerade. \nSlutför installationen för att kunna läsa in sparningen. |
| 26164 | Missing Required DLC(s) | Obligatoriska DLC saknas | Obligatoriska DLC (ett eller flera) saknas |

## Kontroller

- Källans pluralmarkering `(s)` är återställd som ”(ett eller flera)”.
- `l10n-lint --language sv` passerade utan fel eller varningar.
- Hunspell markerar bara förkortningen DLC.
- Den svenska meningsgränskontrollen noterar den förväntade skillnaden mellan engelsk `DLC(s)` och svensk omformulering.
