# Wireshark Qt, svensk batch 19

Datum: 2026-11-12

Källa: Transifex-resursen `o:wireshark:p:wireshark:r:qt-master`.

24 granskade strängar från välkomstförhandsvisningen och temaskrivaren.
Palettidentifierare och HTML-markering har bevarats exakt.

Kontroller före uppladdning:

- Färsk Transifex-export: alla ID:n och källsträngar jämförda.
- Kontroll av HTML-markering, platshållare och palettidentifierare.
- `l10n-lint` utan träffar.
- `svlang svengelska`: en träff i den engelska källsträngen `item`; svensk
  måltext innehåller inte ordet.
- Hunspell-svenska: enbart avsiktliga interna namn och fackmässiga ord.
- `git diff --check` utan blankteckenfel.
- Gitleaks utan hemligheter.
- `msgfmt` är inte tillämpligt på denna Transifex JSON-deltafil för Qt TS.

Uppladdning: Transifex bulk-API uppdaterade 24 strängar utan fel. Färsk
uppföljning visade 58 oöversatta strängar, ned från 82, och inga strängar i
denna batch återstod som oöversatta. Uppladdningen är verifierad;
upstreamgranskning eller publicering är inte verifierad.

Filer:

- `candidates.json`: den granskade deltafilen.
- `transifex-bulk-receipt.json`: API-kvittot från uppladdningen.
- `untranslated-after.json`: oförändrad API-export efter uppladdningen.
