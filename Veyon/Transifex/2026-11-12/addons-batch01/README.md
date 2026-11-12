# Veyon Add-ons, svensk batch 1

Datum: 2026-11-12

Källa: Transifex-resursen `o:veyon-solutions:p:veyon:r:addons`.

Batchen innehåller 10 granskade dokumentationssträngar om Microsoft Intune,
API-behörigheter, MAC-adresser och internetåtkomst.

Kontroller före uppladdning:

- Färsk Transifex-export: alla ID:n och källsträngar jämförda.
- ReST-markering, kodidentifierare och länkar kontrollerade.
- `l10n-lint` utan träffar.
- `svlang svengelska`: träff i det engelska källordet `feature`, inte i
  måltexten.
- Hunspell-svenska: enbart avsiktliga produktnamn, API-behörigheter,
  ReST-markering och facktermer.
- `git diff --check` utan blankteckenfel.
- Gitleaks utan hemligheter.
- `msgfmt` är inte tillämpligt på denna Transifex JSON-deltafil.

Uppladdning: Transifex bulk-API uppdaterade 10 strängar utan fel. Färsk
uppföljning visade 0 oöversatta strängar i komponenten, ned från 10.
Uppladdningen är verifierad; upstreamgranskning eller publicering är inte
verifierad.

Filer:

- `candidates.json`: den granskade deltafilen.
- `transifex-bulk-receipt.json`: API-kvittot från uppladdningen.
- `untranslated-after.json`: oförändrad API-export efter uppladdningen.
