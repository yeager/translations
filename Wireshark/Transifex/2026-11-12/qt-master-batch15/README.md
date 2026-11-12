# Wireshark Qt, svensk batch 15

Datum: 2026-11-12

Källa: Transifex-resursen `o:wireshark:p:wireshark:r:qt-master`.

21 granskade förklaringar av färgtoken i `ThemeTokenHandler`. Interna
tokenidentifierare, till exempel `palette.base`, `accent.error` och
`packets.selection`, har bevarats exakt. Den synliga beskrivningen är
översatt till svenska.

Kontroller före uppladdning:

- Färsk Transifex-export: alla ID:n och källsträngar jämförda.
- Kontroll av samtliga interna tokenidentifierare.
- `l10n-lint` och `svlang svengelska` utan träffar.
- Hunspell-svenska: enbart avsiktliga interna tokenidentifierare.
- `git diff --check` utan blankteckenfel.
- Gitleaks utan hemligheter.
- `msgfmt` är inte tillämpligt på denna Transifex JSON-deltafil för Qt TS.

Uppladdning: Transifex bulk-API uppdaterade 21 strängar utan fel. Färsk
uppföljning visade 140 oöversatta strängar, ned från 161, och inga strängar i
denna batch återstod som oöversatta. Uppladdningen är verifierad;
upstreamgranskning eller publicering är inte verifierad.

Filer:

- `candidates.json`: den granskade deltafilen.
- `transifex-bulk-receipt.json`: API-kvittot från uppladdningen.
- `untranslated-after.json`: oförändrad API-export efter uppladdningen.
