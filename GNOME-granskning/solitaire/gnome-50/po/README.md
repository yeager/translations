# Solitaire — gnome-50/po (sv)

- GNOME-sida: <https://l10n.gnome.org/vertimus/solitaire/gnome-50/po/sv/>
- POT-källa: `solitaire.gnome-50.pot`
- Granskad: 2026-11-23

## Resultat

| Mått | Före | Efter |
| --- | ---: | ---: |
| Aktiva strängar | 140 | 140 |
| Oöversatta | 11 | 0 |
| Fuzzy | 1 | 0 |
| Ändrade befintliga översättningar | – | 12 |

Tio gemensamma strängar har jämförts med och återanvänts från `main`. De
återstående rättelserna omfattar bland annat **Oavslutat spel**, **Ge om** och
en giltig svensk accelerator i **S_pelfrö**.

## Validering

- `msgfmt --check`: godkänd
- `msgcmp --use-fuzzy` mot aktuell POT: godkänd
- `l10n-lint`: 0 fel, 0 varningar
- acceleratorkontroll: inga nordiska acceleratorer
- `hunspell-sv`: tekniska speltermer och produktnamn är dokumenterade
  undantag

## Extern blockerare

Damned Lies API svarade 2026-11-23 med `state: None` och en tom
åtgärdslista. Ingen reservation, kommentar eller uppladdning är därmed möjlig
utan extern ändring av katalogens DL-status.
