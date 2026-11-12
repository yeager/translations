# Wireshark Qt, svensk batch 16

Datum: 2026-11-12

Källa: Transifex-resursen `o:wireshark:p:wireshark:r:qt-master`.

18 granskade beskrivningar av färg- och kontrastregler i
`ThemeTokenHandler`. Identifierare för palett, filter och rubriker har
bevarats exakt; endast den läsbara beskrivningen är översatt.

Kontroller före uppladdning:

- Färsk Transifex-export: alla ID:n och källsträngar jämförda.
- Kontroll av interna identifierare för palett och filter.
- `l10n-lint` och `svlang svengelska` utan träffar.
- Hunspell-svenska: enbart avsiktliga tokenidentifierare.
- `git diff --check` utan blankteckenfel.
- Gitleaks utan hemligheter.
- `msgfmt` är inte tillämpligt på denna Transifex JSON-deltafil för Qt TS.

Uppladdning: Transifex bulk-API uppdaterade 18 strängar utan fel. Färsk
uppföljning visade 122 oöversatta strängar, ned från 140, och inga strängar i
denna batch återstod som oöversatta. Uppladdningen är verifierad;
upstreamgranskning eller publicering är inte verifierad.

Filer:

- `candidates.json`: den granskade deltafilen.
- `transifex-bulk-receipt.json`: API-kvittot från uppladdningen.
- `untranslated-after.json`: oförändrad API-export efter uppladdningen.
