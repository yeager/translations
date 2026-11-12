# Wireshark Qt, svensk batch 17

Datum: 2026-11-12

Källa: Transifex-resursen `o:wireshark:p:wireshark:r:qt-master`.

17 granskade regler för färger, kontrast och kort i `ThemeTokenHandler`.
Interna identifierare för färgpalett, accent, kort och länk har bevarats
exakt. De läsbara beskrivningarna är översatta till svenska.

Kontroller före uppladdning:

- Färsk Transifex-export: alla ID:n och källsträngar jämförda.
- Kontroll av interna identifierare för färgpalett och accent.
- `l10n-lint` och `svlang svengelska` utan träffar.
- Hunspell-svenska: enbart avsiktliga interna namn och fackmässiga
  sammansättningar.
- `git diff --check` utan blankteckenfel.
- Gitleaks utan hemligheter.
- `msgfmt` är inte tillämpligt på denna Transifex JSON-deltafil för Qt TS.

Uppladdning: Transifex bulk-API uppdaterade 17 strängar utan fel. Färsk
uppföljning visade 105 oöversatta strängar, ned från 122, och inga strängar i
denna batch återstod som oöversatta. Uppladdningen är verifierad;
upstreamgranskning eller publicering är inte verifierad.

Filer:

- `candidates.json`: den granskade deltafilen.
- `transifex-bulk-receipt.json`: API-kvittot från uppladdningen.
- `untranslated-after.json`: oförändrad API-export efter uppladdningen.
