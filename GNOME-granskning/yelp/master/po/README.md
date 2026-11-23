# Yelp — master/po (sv)

- GNOME-sida: <https://l10n.gnome.org/vertimus/yelp/master/po/sv/>
- POT-källa: `yelp.master.pot`
- Granskad: 2026-11-23

## Resultat

| Mått | Före | Efter |
| --- | ---: | ---: |
| Aktiva strängar | 83 | 83 |
| Oöversatta | 0 | 0 |
| Fuzzy | 0 | 0 |
| Ändrade befintliga översättningar | – | 4 |

Rättelserna omfattar bland annat konsekvent terminologi för komprimerade data,
XSLT-stilmall, `href`-attribut och en giltig accelerator för **Öppna länk**.

## Validering

- `msgfmt --check`: godkänd
- `msgcmp --use-fuzzy` mot aktuell POT: godkänd
- `l10n-lint`: 0 fel, 0 varningar
- `hunspell-sv`: manuellt kontrollerat; rimliga undantag är produkt- och
  formatnamnen `Yelp`, `Mallard`, `DocBook`, `PackageKit` och `XSLT`, samt
  tekniska sammansättningar/attributen `XSLT-stilmallen`, `href-attribut`,
  `yelp:document` och `URI:n`. Hunspell visar även acceleratormärkta
  restord som `opiera` och `ppna`; de är inte stavfel.

`l10n-lint` rapporterar två informationsnotiser för acceleratormarkeringar;
de är avsiktliga och formatet är korrekt.
