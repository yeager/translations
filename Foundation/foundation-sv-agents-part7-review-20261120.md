# Foundation – agents.json, granskningsomgång 7

Datum: 2026-11-20  
Metod: Crowdin API; förslagen kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Sparad svenska | Lint/stavning |
|---|---|---|---|---|
| BEHAVIOR_MESSAGES → PATROLLING | Patrolling | Patrullering | Patrullerar | l10n-lint: inga fel. Hunspell: inga fel. |
| STATUSES_DESC → TRADER_DESC | Traders visit our storage facilities to trade resources and coins according to the rules set in the Royal Book. | Handlare besöker våra lagerlokaler för att handla med resurser och mynt enligt de regler som anges i Kungaboken. | Handlare besöker våra lagerbyggnader för att handla med resurser och mynt enligt reglerna i den kungliga boken. | l10n-lint: inga fel. Hunspell: inga fel. |

Formen ”Patrullerar” följer övriga pågående aktivitetsmeddelanden. `Royal Book` normaliserades till den etablerade termen ”den kungliga boken”. Båda ändringarna skickades direkt till Crowdin via API (HTTP 201). Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.