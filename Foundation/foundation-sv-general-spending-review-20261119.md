# Foundation – allmänna utgifter, svensk QA-rättning 2026-11-19

En befintlig svensk översättning i `general.json` har granskats via Crowdins QA-API. Förslaget är ett utkast och har inte sparats i Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 129 | General Spending | Allmänna utgifter: | Allmänna utgifter |

## Kontroller

- Crowdins QA visar att källan saknar avslutande kolon; den svenska översättningens kolon tas därför bort.
- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` passerade utan anmärkningar.
