# Midea: sömnläge

Datum: 2026-11-14

Midea-läget `Sleep` granskades i luftfuktarens lägeslista och sparades i
Lokalise som `Sömnläge`.

Källsträngen innehåller en Home Assistant-nyckelreferens. Referensen bevarades
i Midea-strängen och den delade humidifier-strängen rättades från `Sov` till
`Sömnläge`. Därmed blir den visade Midea-texten exakt `Sömnläge`, utan
dubblett. Den råa Midea-måltexten är:

```
[%key:component::humidifier::entity_component::_::state_attributes::mode::state::sleep%]
```

Sparningarna återlästes efteråt. Den tidigare osparade feltexten `Manuell`
korrigerades innan sparning.

JSON-underlaget passerade l10n-lint, svlang, Hunspell-sv, diffkontroll och
Gitleaks. `msgfmt` är inte tillämpligt på Lokalise-JSON.
