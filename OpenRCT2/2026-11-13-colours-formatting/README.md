# OpenRCT2, svenska färger och formatmallar, 13 november 2026

Den här andra OpenRCT2-batchen fyller de återstående aktuella luckorna i svenska huvudresursen:

- 18 färgnamn i programmet
- sju formatmallar som med avsikt speglar källans token- och layoutmarkörer

Tillsammans med statusbatchen i OpenRCT2 PR #27415 täcker den lokala svenska resursen alla 3 809 aktiva engelska id:n vid revisionen f13dcbfa1a8c76367f7183ada58bb77cc5bafc30.

Kontroller:

- kontroll av källmarkörer i samtliga formatmallar
- Hunspell-sv för färgnamnen: godkänd
- diffkontroll: godkänd
- Gitleaks för deltan: godkänd
- l10n-lint och svlang: inte tillämpliga på OpenRCT2:s id-baserade textformat

Upstream: inskickat som [OpenRCT2 PR #27416](https://github.com/OpenRCT2/OpenRCT2/pull/27416) den 13 november 2026. PR:en är öppen och väntar på granskning.
