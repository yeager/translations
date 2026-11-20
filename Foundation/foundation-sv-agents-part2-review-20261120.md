# Foundation – agents.json, granskningsomgång 2

Datum: 2026-11-20  
Metod: Crowdin API; förslagen kontrollerades med `l10n-lint` och `hunspell-sv`.

| Nyckel | Engelsk källsträng | Tidigare svenska | Förslag | Resultat | Lint/stavning |
|---|---|---|---|---|---|
| BEHAVIOR_MESSAGES → PREPARING_TO_WORK | I am preparing to work | Jag förbereder mig för arbete. | Jag förbereder mig för att arbeta | Identisk översättning fanns redan i Crowdin; API:t rapporterade dubblett. | l10n-lint: inga fel. Hunspell: inga fel. |
| BEHAVIOR_MESSAGES → I_AM_WAITING_FOR_MY_WORKPLACE_TO_BE_BUILT | I am waiting for my workplace to be built | Jag väntar på att min arbetsplats ska bli byggd | Jag väntar på att min arbetsplats ska byggas | Sparad i Crowdin (HTTP 201). | l10n-lint: inga fel. Hunspell: inga fel. |

Gettext gav endast den generella UTF-8-portabilitetsvarningen för den temporära PO-filen.