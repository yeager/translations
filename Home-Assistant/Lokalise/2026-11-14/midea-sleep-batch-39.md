# Midea: sömnläge

Datum: 2026-11-14

Midea-läget `Sleep` granskades i luftfuktarens lägeslista och sparades i
Lokalise som `Sömnläge`.

Källsträngen innehåller en Home Assistant-nyckelreferens. Referensen
bevarades i målsträngen så att Lokalises platshållarkontroll passerar; den
råa måltexten är:

```
[%key:component::humidifier::entity_component::_::state_attributes::mode::state::sleep%]Sömnläge
```

Sparningen återlästes efteråt med både måltext och nyckelreferens. Den
tidigare osparade feltexten `Manuell` korrigerades innan sparning.

JSON-underlaget passerade l10n-lint, svlang, Hunspell-sv, diffkontroll och
Gitleaks. `msgfmt` är inte tillämpligt på Lokalise-JSON.
