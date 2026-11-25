# Sysprof — master — svensk dokumentation

- Katalog: [Sysprof Help i Damned Lies](https://l10n.gnome.org/vertimus/sysprof/master/help/sv/)
- Senaste POT hämtad 2026-11-25: `https://l10n.gnome.org/POT/sysprof.master/docs/sysprof-help.master.pot`
- POT SHA-256: `e00d3e4a99113c59ea330f29a5d4c5fcdd2c32957ad8062acca7ed734aacca3a`
- Före granskning: 49/49 översatta, 0 fuzzy, 0 oöversatta.
- Efter granskning: 49/49 översatta, 0 fuzzy, 0 oöversatta.
- Ändringar: 31 befintliga översättningar rättade; inga nya översättningar.
- Last-Translator: Daniel Nylander <gnome@danielnylander.se>.

## Validering

- `msgfmt --check` och `msgcmp` mot senaste POT: godkända.
- `l10n-lint --language sv --reference sysprof-help.master.pot`: 0 fel och 0 varningar. En informationsnotis gäller den svenska förklaringen efter JIT-förkortningen.
- Egen kontroll av DocBook-taggar och radbrytningar: inga avvikelser.
- `hunspell-sv`: kontrollerad. Undantag är kommandoradsflaggor och filnamn, produkt-/projektnamn, JIT/GCC/GTK, koden `malloc`, pseudo-ramnamnet `Context Switch` samt tekniska termer som `heap`, `stackspår` och `spårningsprofilerare`.
- `swedish-tm` kontrollerad: `profiling` → `profilering`, `profiler` → `profilerare`, `stacktraces` → `stackspår` och `callgraph` → `anropsgraf`.

Ingen GNOME-inskickning har gjorts.

## Filer

- [Original PO](sysprof.master.help.sv.original.po)
- [Granskad PO](sysprof.master.help.sv.reviewed.po)
- [Diff](sysprof.master.help.sv.diff)
- [Senaste POT](sysprof-help.master.pot)
