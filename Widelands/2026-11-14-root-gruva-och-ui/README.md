# Widelands Add-Ons: gruva och UI

Sju strängar i rotresursen har granskats lokalt och skickats till Transifex.

Projekt: Widelands Add-Ons
Resurs: rotresursen
Språk: svenska (`sv`)

## Strängar

- 612431475: gruvans utvinning på djupaste nivån
- 612431476: `Note:` → `Obs:`
- 612431477: arbetsområdets radie
- 612431478: läkning
- 612431479: garnisonerade soldaters läkning
- 612431480: erövringsräckvidd
- 612431482: synräckvidd

Platshållarna `%1%%%` och `%d` är bevarade. Termvalen följer Widelands
spelkontext: soldater kan stå i garnison, läkning sker per sekund och räckvidd
avser spelets avståndsmått.

## Verifiering

- `msgfmt --check --statistics`
- `l10n-lint --language sv --check`
- Hunspell-sv och svlang, med manuell kontextgranskning
- `git diff --check`
- Gitleaks
- Transifex: varje sträng sparad och återläst utan QA-varning
