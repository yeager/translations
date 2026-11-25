# Errands — gränssnitt (`main`)

- GNOME Damned Lies: [Errands, svensk UI](https://l10n.gnome.org/vertimus/errands/main/po/sv/)
- Senaste POT: `Errands.main.latest.pot` (SHA-256 `750fc1f713213dc35c2cf87bf040bc7fd103f4de91f670ed81a29b953b8f313e`)
- Granskad: 2026-11-25
- Last-Translator: Daniel Nylander <gnome@danielnylander.se>

## Statistik mot aktuell POT (179 poster)

| | Översatta | Fuzzy | Oöversatta |
|---|---:|---:|---:|
| Före granskning | 173 | 3 | 3 |
| Efter granskning | 179 | 0 | 0 |

Nya översättningar: 3. Fuzzy-översättningar som rättades och godkändes: 3. Alla 9 pluralposter och deras två former är bevarade och kontrollerade.

## Granskning och validering

Radgranskade de tre saknade posterna och de tre fuzzy-posterna. TM-stöd bekräftade `Description` → `Beskrivning`, `Level` → `Nivå` och `Color` → `Färg`. Övriga förslag är kontextanpassade: `Undo Changes` → `Ångra ändringar`, `Task Accent Color` → `Uppgiftens accentfärg` och reset-knappens `Clear Color` → `Rensa färg`.

- `msgfmt --check`: godkänd.
- `l10n-lint --language sv --reference Errands.main.latest.pot`: 0 fel och 0 varningar; två informationsnotiser utan blockerande problem.
- Pluralformer och `%d`/`%zu`-platshållare kontrollerade; inga avvikelser. Acceleratorer och markup bevarade.
- `hunspell-sv`: kontrollerad. Undantag är Errands och CalDAV, `.ics`-filändelsen, korta svenska veckodagsnamn, `F10`, `pN`, `%zu` och det bokstavliga intervallet `0..9`.

## Filer

- [Senaste POT](Errands.main.latest.pot)
- [Originalfil](errands.main.sv.original.po)
- [Granskad fil](errands.main.sv.reviewed.po)
- [Diff](errands.main.sv.review.diff)

Ändringarna är sparade lokalt och i GitHub-kopian. De har inte skickats till Damned Lies.
