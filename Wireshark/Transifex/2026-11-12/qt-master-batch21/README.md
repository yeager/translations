# Wireshark Qt, svensk batch 21

Datum: 2026-11-12

Källa: Transifex-resursen `o:wireshark:p:wireshark:r:qt-master`.

28 granskade strängar från temaredigeraren, ThemeWriter, tidsdialogen och
Wiresharks huvudfönster. De sista oöversatta strängarna omfattar också en
menyetikett och två verktygstips där källkodens kontext verifierades.

Kontroller före uppladdning:

- Färsk Transifex-export: alla ID:n och källsträngar jämförda.
- Meny- och verktygstipskontext kontrollerad i Wiresharks Qt-källkod.
- Kontroll av HTML-markering, platshållare, Qt-namn, palettidentifierare och
  kortkommandomarkering.
- `l10n-lint` och `svlang svengelska` utan träffar.
- Hunspell-svenska: enbart avsiktliga format-, Qt- och kodnamn samt
  fackmässiga sammansättningar.
- `git diff --check` utan blankteckenfel.
- Gitleaks utan hemligheter.
- `msgfmt` är inte tillämpligt på denna Transifex JSON-deltafil för Qt TS.

Uppladdning: Transifex bulk-API uppdaterade 28 strängar utan fel. Färsk
uppföljning visade 0 oöversatta strängar, ned från 28. Uppladdningen är
verifierad; upstreamgranskning eller publicering är inte verifierad.

Filer:

- `candidates.json`: den granskade deltafilen.
- `transifex-bulk-receipt.json`: API-kvittot från uppladdningen.
- `untranslated-after.json`: oförändrad API-export efter uppladdningen.
