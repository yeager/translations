# Wireshark Qt, svensk batch 20

Datum: 2026-11-12

Källa: Transifex-resursen `o:wireshark:p:wireshark:r:qt-master`.

30 granskade ThemeWriter-strängar för paket, visningsfilter, fångstfilter,
symboler och Lua-felsökaren.

Kontroller före uppladdning:

- Färsk Transifex-export: alla ID:n och källsträngar jämförda.
- `l10n-lint` utan träffar.
- `svlang svengelska`: träff i engelska källordet `items`, inte i måltexten.
- Hunspell-svenska: `Lua` och `self` är avsiktliga program- och
  kodidentifierare.
- `git diff --check` utan blankteckenfel.
- Gitleaks utan hemligheter.
- `msgfmt` är inte tillämpligt på denna Transifex JSON-deltafil för Qt TS.

Uppladdning: Transifex bulk-API uppdaterade 30 strängar utan fel. Färsk
uppföljning visade 28 oöversatta strängar, ned från 58, och inga strängar i
denna batch återstod som oöversatta. Uppladdningen är verifierad;
upstreamgranskning eller publicering är inte verifierad.

Filer:

- `candidates.json`: den granskade deltafilen.
- `transifex-bulk-receipt.json`: API-kvittot från uppladdningen.
- `untranslated-after.json`: oförändrad API-export efter uppladdningen.
