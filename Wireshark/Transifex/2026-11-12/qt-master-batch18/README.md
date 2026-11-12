# Wireshark Qt, svensk batch 18

Datum: 2026-11-12

Källa: Transifex-resursen `o:wireshark:p:wireshark:r:qt-master`.

23 granskade regler för färgtoken, filter och uppdateringsfält i
`ThemeTokenHandler`. Interna identifierare har bevarats exakt; den synliga
beskrivningen har översatts till svenska.

Kontroller före uppladdning:

- Färsk Transifex-export: alla ID:n och källsträngar jämförda.
- Kontroll av interna identifierare för palett, filter, accent och paket.
- `l10n-lint` och `svlang svengelska` utan träffar.
- Hunspell-svenska: enbart avsiktliga interna namn och fackmässiga
  sammansättningar.
- `git diff --check` utan blankteckenfel.
- Gitleaks utan hemligheter.
- `msgfmt` är inte tillämpligt på denna Transifex JSON-deltafil för Qt TS.

Uppladdning: Transifex bulk-API uppdaterade 23 strängar utan fel. Färsk
uppföljning visade 82 oöversatta strängar, ned från 105, och inga strängar i
denna batch återstod som oöversatta. Uppladdningen är verifierad;
upstreamgranskning eller publicering är inte verifierad.

Filer:

- `candidates.json`: den granskade deltafilen.
- `transifex-bulk-receipt.json`: API-kvittot från uppladdningen.
- `untranslated-after.json`: oförändrad API-export efter uppladdningen.
