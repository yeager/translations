# Era — main/po (sv)

- GNOME-sida: <https://l10n.gnome.org/vertimus/era/main/po/sv/>
- POT-källa: `era.main.pot`
- Granskad: 2026-11-23

## Resultat

| Mått | Före | Efter |
| --- | ---: | ---: |
| Aktiva strängar | 151 | 151 |
| Oöversatta | 6 | 0 |
| Fuzzy | 3 | 0 |
| Ändrade befintliga översättningar | – | 9 |

De nya och korrigerade kalendersträngarna omfattar bland annat borttagning av
kalender, heldag samt dagräknare. Rust-platshållarna `{day_index}` och
`{day_count}` är oförändrade.

## Validering

- `msgfmt --check`: godkänd
- `msgcmp --use-fuzzy` mot aktuell POT: godkänd
- `l10n-lint`: 0 fel, 0 varningar
- Rust-platshållare: jämförda utan avvikelser
- `hunspell-sv`: rimliga undantag är produktnamnet `Calendar`, `caldav`,
  de tekniska variablerna och sammansättningen `Kalendervyn`

Filen skickades till Damned Lies med kommentaren **Granskad och klar**.
