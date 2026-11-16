# Withings: hälsa och träningsformer

30 svenska Withings-strängar har granskats och sparats i Lokalise. Gruppen omfattar en konfigurationsvarning, två hälsomått och 27 träningsformer.

Terminologin har stämts av mot Home Assistants översättningsminne där det fanns träffar och annars mot etablerade svenska namn på idrotter och aktiviteter. Varumärken och etablerade aktivitetsnamn som CrossFit, Barre och Cornhole har behållits.

Kontroller som passerade:

- platshållarparitet
- `l10n-lint` för JSON
- `svlang` och Hunspell-sv med manuellt granskade fack- och egennamn
- Git-diffkontroll
- Gitleaks
- Lokalise-sparning med exakt läsning tillbaka av samtliga 30 poster; varje post är verifierad (`is_unverified: false`)

`msgfmt` är inte tillämpligt eftersom katalogen hanteras som JSON via Lokalise API.
