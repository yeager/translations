# Widelands Add-Ons: poängberäkning

Fyra etiketter i tilläggets beskrivning av poängberäkningen har granskats och
sparats i Transifex. Formuleringarna skiljer tydligt på slutpoäng, delpoäng,
ägd areal och soldatstatistik.

Projekt: Widelands Add-Ons
Resurs: rotresursen
Språk: svenska (sv)
Transifex-strängar: 628063220, 628063221, 628063223 och 628063224

## Verifiering

- msgfmt
- l10n-lint
- Hunspell-sv och svlang, med manuell kontextgranskning
- git diff --check
- Gitleaks
- Transifex: varje sträng sparad, sedan bekräftad genom full omladdning och
  minskat antal oöversatta strängar
