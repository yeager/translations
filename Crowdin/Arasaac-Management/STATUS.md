# Arasaac Management, svenska

Granskningen använder CrowdIn-projektet `arasaac-management` och språket `sv-SE`.

## Status 2026-10-19

CrowdIn rapporterar 100 % översatt och 85 % godkänt.

- `arasaac-management-sv-batch-01-20261019.*` innehåller de 44 tidigare tomma strängar som skickades in och blev aktiva.
- Filerna `arasaac-management-sv-review-batch-02-20261019.json` och `arasaac-management-sv-review-batch-03-20261019.json` innehåller tillsammans 45 språkgranskade rättningar som har skickats in som förslag. De är inte aktiva förrän en korrekturläsare godkänner dem i CrowdIn.
- `arasaac-management-sv-review-batch-02-20261019.po` är en granskningslista med 27 föreslagna rättningar. Två av dem, `Login.invalidEmail` och `app.components.CategoryForm.key`, fanns redan som identiska förslag och kunde därför inte skickas in en gång till. Batch 03 innehåller ytterligare 17 inskickade förslag. Batch 04 innehåller tre inskickade förslag; en fjärde formulering fanns redan som identiskt förslag.

En lokal export eller en filbyggnad via CrowdIn API kan inte skapas med den nuvarande tokenens behörigheter. Den här katalogen är därför en verifierbar arbetsbackup och inte en påstådd CrowdIn-export.

## Kvalitetskontroll

En full kontroll omfattade 846 strängpar med CrowdIns aktuella engelska källsträngar. Den svenska granskningskopian bestod av den lokala granskade filen samt de 16 nyare World Locations-strängarna från CrowdIn. `msgfmt --check`, `l10n-lint` och `svlang skrivregler` gav inga fel. Gitleaks hittade inga hemligheter.

Kontrollen är en språklig kvalitetskontroll av granskningskopian. Den är inte en export av de aktiva CrowdIn-översättningarna, eftersom tokenen inte får bygga en export och de 42 nya rättningarna fortfarande väntar på korrekturläsargodkännande.
