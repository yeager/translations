# Swell Foop — hjälp, main

Radgranskning av hela den svenska hjälpkatalogen mot aktuell POT.

- Damned Lies: https://l10n.gnome.org/vertimus/swell-foop/main/help/sv/
- Statistik före granskningen: 72 översatta, 0 fuzzy, 0 oöversatta.
- POT: `POT-Creation-Date: 2026-11-17 05:34+0000`; SHA-256 `a345ae34f11df4690bebce13cc8a106db12ff0e6c40de898508c064385d648fe`.
- Granskade poster: 72 av 72.
- Nya översättningar: 0.
- Befintliga översättningar rättade: 17.
- Slutstatus: 72 översatta, 0 fuzzy, 0 oöversatta.

## Granskning

Rättade grammatik och idiomatik i spelregler och instruktioner, bland annat beskrivningen av grupper, spelbrädets storlek, poängdialogen och strategitipsen. GNOME-etiketter kontrollerades mot aktuell svensk UI-katalog; `Setup` återges som `Konfiguration`. Licensnamnet behölls enligt GNOME:s befintliga TM-form. Produktnamnet Swell Foop och exempelvärden ändrades inte. `Last-Translator` uppdaterades till Daniel Nylander <gnome@danielnylander.se>.

## Validering

- `msgfmt --check --check-format`: godkänd.
- `msgcmp` mot aktuell POT: katalogerna matchar.
- `l10n-lint --language sv --reference <latest.pot>`: 0 fel, 0 varningar.
- Egen kontroll: 72 källposter matchar POT; 0 tomma och 0 fuzzy. Markup och platshållare bevarade. Ändrade poster saknar radbrytningar.
- `hunspell -d sv_SE` på ändrade texter: endast `namnlist` flaggades; ordet är etablerad GNOME-terminologi och finns i Swedish TM.

Damned Lies API efter granskning: HTTP 200, 72/0/0. Aktivitetssidan hämtades (HTTP 200). Ingen fil har skickats in och ingen kommentar har publicerats.

## Arkiverade filer

- [Original PO](swell-foop.main.help.original.po)
- [Senaste POT](swell-foop.main.help.latest.pot)
- [Granskad PO](swell-foop.main.help.reviewed.po)
- [Unified diff](swell-foop.main.help.review.diff)
- [API före](api-before.json) · [API efter](api-after.json)
- [Aktivitetssida](activity-after.html)
- [l10n-lint-resultat](l10n-lint.json)
