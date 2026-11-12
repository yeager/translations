# Wireshark Qt, svensk batch 14

Datum: 2026-11-12

Källa: Transifex-resursen `o:wireshark:p:wireshark:r:qt-master`.

23 granskade strängar från hantering, import och förhandsvisning av teman.
Termerna följer projektets terminologilista, bland annat *tema*, *färger*,
*kantlinje* och *förhandsvisning*.

Kontroller före uppladdning:

- Färsk Transifex-export: alla ID:n och källsträngar jämförda.
- Platshållare kontrollerade.
- `l10n-lint` och `svlang svengelska` utan träffar.
- Hunspell-svenska: `png` och `PNG-bild` är avsiktliga formatnamn.
- `git diff --check` utan blankteckenfel.
- Gitleaks utan hemligheter.
- `msgfmt` är inte tillämpligt på denna Transifex JSON-deltafil för Qt TS.

Uppladdning: Transifex bulk-API uppdaterade 23 strängar utan fel. Färsk
uppföljning visade 161 oöversatta strängar, ned från 184, och inga strängar i
denna batch återstod som oöversatta. Uppladdningen är verifierad;
upstreamgranskning eller publicering är inte verifierad.

Filer:

- `candidates.json`: den granskade deltafilen.
- `transifex-bulk-receipt.json`: API-kvittot från uppladdningen.
- `untranslated-after.json`: oförändrad API-export efter uppladdningen.
