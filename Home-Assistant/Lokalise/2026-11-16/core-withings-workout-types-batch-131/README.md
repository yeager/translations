# Withings: återstående träningsformer

83 svenska Withings-strängar har granskats och sparats i Lokalise. Batchen slutför den aktuella Withings-katalogen och omfattar idrotter, motion, vardagsrörelser och hjälpmedelsrelaterade aktiviteter.

Svenska etablerade namn används där de finns, till exempel `spökboll`, `discgolf`, `skärmflygning`, `rullskidåkning` och `stavgång`. Internationella sportnamn som Padel, HIIT, Teqball och CrossFit behålls när de används som namn på aktiviteten.

Kontroller som passerade:

- platshållarparitet
- `l10n-lint` för JSON
- `svlang` och Hunspell-sv med manuellt granskade fack- och egennamn
- Git-diffkontroll
- Gitleaks
- Lokalise-sparning med exakt läsning tillbaka av samtliga 83 poster; varje post är verifierad (`is_unverified: false`)

`msgfmt` är inte tillämpligt eftersom katalogen hanteras som JSON via Lokalise API.
