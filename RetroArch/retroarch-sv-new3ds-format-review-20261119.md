# RetroArch – New3DS-klockhastighet, svensk QA-rättning 2026-11-19

En befintlig svensk översättning i `msg_hash_us.json` har granskats via Crowdins QA-API. Förslaget är inte sparat eller skickat till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 3398118 | Enable New3DS clock speed (804MHz) and L2 cache. | Aktivera New3DS-klockhastighet på 804 MHz och L2-cache. | Aktivera New3DS-klockhastighet (804 MHz) och L2-cache. |

## Kontroller

- Källans parenteser runt `804MHz` är återställda.
- `l10n-lint --language sv` passerade utan anmärkningar.
- Hunspell och QA markerar New3DS-klockhastighet och L2-cache som tekniska sammansättningar. QA:s versalträff gäller svensk inledande versal, inte en översättningsbrist.
- QA rapporterar även att den föreslagna texten redan förekommer som en annan översättning; den är därför ett dokumenterat förslag och inte en Crowdinskrivning.
