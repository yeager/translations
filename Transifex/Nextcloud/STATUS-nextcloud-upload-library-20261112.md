# Nextcloud Upload Library – svensk granskningsstatus 2026-11-12

Projekt: `o:nextcloud:p:nextcloud-upload-library`.

Deltafilen `nextcloud-upload-library-sv-delta-20261112.jsonl` innehåller den enda oöversatta svenska UI-strängen. Den beskriver att ett mappbyte skriver över alla filer i den befintliga mappen, även filer utan konflikt.

Kontroller: l10n-lint, svlang, Hunspell, `git diff --check` och Gitleaks godkända. `msgfmt` är inte tillämpligt eftersom Transifex-resursen är JSON-baserad.

Uppladdning: Transifex API returnerade HTTP 200 för 1 uppdatering. En separat API-läsning efter inskicket visade 0 oöversatta svenska strängar i resursen.

Status: lokalt granskat, arkiverat och uppladdat. Upstream-granskning eller publicering är inte verifierad.
