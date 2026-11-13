# Audacity: MP3-exportens dialogtexter

- Datum: 2026-11-13
- Källcommit: `87229de`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 5 svenska PO-poster för LAME-sökning och MP3-exportfel.

Batchen använder direkta svenska åtgärdstexter när användaren söker efter eller hämtar LAME. Den rättar också ett sakfel i felmeddelandet om MP3-kodningsbiblioteket: biblioteket kan vara ogiltigt **eller** sakna stöd. Produktnamnen `LAME` och `MP3` behålls oförändrade.

Kontroller: `msgfmt` (4 443 översatta poster), avgränsad Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. Hunspell-sv träffar inga ändrade ord. l10n-lint träffar ingen ändrad sträng. Svlang markerar ”MP3-exportbiblioteket hittades inte”, en korrekt svensk V2-sats, som falsk positiv.
