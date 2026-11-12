# ownCloud Client och Lib, svensk batch 1

Datum: 2026-11-12

Källa: Transifex-resurserna `o:owncloud-org:p:owncloud:r:client` och
`o:owncloud-org:p:owncloud:r:lib`.

Fem granskade strängar: en klientsträng och fyra valideringsmeddelanden för
apparkiv.

Kontroller före uppladdning:

- Färsk Transifex-export: alla ID:n och källsträngar jämförda.
- Platshållarkontroll.
- `l10n-lint` och `svlang svengelska` utan träffar.
- Hunspell-svenska: endast det avsiktliga filnamnet `info.xml-fil`.
- `git diff --check` utan blankteckenfel.
- Gitleaks utan hemligheter.
- `msgfmt` är inte tillämpligt på denna Transifex JSON-deltafil.

Uppladdning: Transifex bulk-API uppdaterade 1 sträng i `client` och 4 i
`lib`, utan fel. Färsk uppföljning visade 0 oöversatta strängar i båda
komponenterna. Uppladdningen är verifierad; upstreamgranskning eller
publicering är inte verifierad.

Filer:

- `candidates.json`: den granskade deltafilen.
- `transifex-*-bulk-receipt.json`: API-kvitton från uppladdningarna.
- `*-untranslated-after.json`: oförändrade API-exporter efter uppladdning.
