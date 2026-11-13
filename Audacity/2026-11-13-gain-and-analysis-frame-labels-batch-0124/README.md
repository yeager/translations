# Audacity: förstärkning och analysramar

- Datum: 2026-11-13
- Källcommit: `0fff536`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 4 svenska PO-poster i Phaser, Wahwah och MIDI-ljudsynkronisering.

Batchen skiljer **utgångsförstärkning** från enbart utgångsnivå i effektkontrollerna. `Frame Period` i den signalbaserade MIDI-anpassningen återges som **ramperiod**, inte som en bildruteperiod.

Kontroller: `msgfmt` (4 443 översatta poster), avgränsad Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. Inga av verktygen träffar någon ändrad post.
