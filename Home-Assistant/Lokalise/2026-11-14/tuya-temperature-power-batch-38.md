# Tuya: temperatur, effekt och magnetisk störning

Datum: 2026-11-14

Tre Home Assistant Core-strängar i Tuya-komponenten granskades i sin
enhetsstatuskontext och sparades direkt i Lokalise. Varje sparning återlästes
i redigeraren.

- High temperature early warning → Tidigt varningsmeddelande om hög temperatur
- High power → Hög strömförbrukning
- Magnetic interference → Magnetisk störning

`Hög strömförbrukning` följer den etablerade svenska termen i den lokala
facktermresursen. Batchens JSON-underlag passerade l10n-lint och svlang;
Hunspell-sv gav inga träffar på måltexterna. Gitleaks och diffkontroll
passerade. `msgfmt` är inte tillämpligt eftersom Lokalise-underlaget är JSON,
inte en PO-fil.
