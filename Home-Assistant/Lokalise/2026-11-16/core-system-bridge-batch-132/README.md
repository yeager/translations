# System Bridge

111 svenska strängar för System Bridge har granskats och sparats i Lokalise. De täcker strömhantering, ljud och bildskärmar, grafikkort, anslutningsinställningar och systemaviseringar.

Översättningarna använder svenska gränssnittstermer, till exempel `viloläge`, `växlingsutrymme`, `ljudingång`, `sökväg` och `aviserings-ID`. Kod, URL:er, entitetsnamn och platshållare har lämnats orörda.

Kontroller som passerade:

- platshållarparitet
- `l10n-lint` för JSON
- `svlang` och Hunspell-sv med manuellt granskade tekniska ord, variabler och egennamn
- Git-diffkontroll
- Gitleaks
- Lokalise-sparning med exakt läsning tillbaka av samtliga 111 poster; varje post är verifierad (`is_unverified: false`)

`msgfmt` är inte tillämpligt eftersom katalogen hanteras som JSON via Lokalise API.
