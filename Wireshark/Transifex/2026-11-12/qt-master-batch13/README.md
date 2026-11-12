# Wireshark Qt, svensk batch 13

Datum: 2026-11-12

Källa: Transifex-resursen `o:wireshark:p:wireshark:r:qt-master`.

Batchen innehåller 22 granskade strängar från `ThemeDesignerDialog`,
`ThemeImportErrorDialog` och `ThemeLuaCodePreview`. Termerna följer den
projektspecifika terminologin: *theme* = *tema*, *personal themes* =
*personliga teman* och *colors* = *färger*.

Kontroller före uppladdning:

- Källsträngar och Transifex-ID:n jämförda mot färsk API-export.
- Platshållare kontrollerade.
- `l10n-lint` utan träffar.
- `svlang svengelska` utan träffar.
- Hunspell-svenska: endast avsiktliga format- och enhetsnamn (`json`,
  `jsonc`, `MiB`).
- `git diff --check` utan blankteckenfel.
- Gitleaks utan hemligheter.
- `msgfmt` är inte tillämpligt på denna Transifex JSON-deltafil för Qt TS.

Uppladdning: Transifex bulk-API uppdaterade 22 strängar utan fel. En färsk
API-kontroll efter uppladdningen visade 184 oöversatta strängar, ned från 206,
och inga av denna batch återstod som oöversatta. Uppladdningen är verifierad;
upstreamgranskning eller publicering är inte verifierad.

Filer:

- `candidates.json`: den granskade deltafilen.
- `transifex-bulk-receipt.json`: API-kvittot från uppladdningen.
- `untranslated-after.json`: oförändrad API-export efter uppladdningen.
